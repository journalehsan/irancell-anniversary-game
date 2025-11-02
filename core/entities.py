"""Game entity implementations."""

from __future__ import annotations

import math
import random
from typing import Tuple

import pygame

from core.direction import Direction
from core.game_state import SingletonGameState
from core.interfaces import Collidable, Drawable
from utils.config_loader import GameSettings


class Wall(Drawable):
    """Axis-aligned wall segment."""

    def __init__(self, settings: GameSettings, x: int, y: int, width: int, height: int):
        self._settings = settings
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface) -> None:  # type: ignore[override]
        pygame.draw.rect(surface, self._settings.colors.wall, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, (0, 0, 100), (self.x, self.y, self.width, self.height), 2)


class Coin(Drawable):
    """Collectible coin with pulsing animation."""

    def __init__(self, settings: GameSettings, x: int, y: int):
        self._settings = settings
        self.x = x
        self.y = y
        self.collected = False
        self._grid_size = settings.grid_size
        self.radius = self._grid_size // 4
        self.animation_counter = 0

    def update(self) -> None:
        self.animation_counter = (self.animation_counter + 1) % 20

    def draw(self, surface) -> None:  # type: ignore[override]
        if self.collected:
            return
        center_x = self.x + self._grid_size // 2
        center_y = self.y + self._grid_size // 2
        pulse_radius = self.radius - 1 + (self.animation_counter % 4) // 2
        pygame.draw.circle(surface, self._settings.colors.primary, (center_x, center_y), pulse_radius)
        pygame.draw.circle(surface, (255, 255, 100), (center_x, center_y), pulse_radius, 1)


class PowerPellet(Drawable):
    """Larger collectible that activates power mode."""

    def __init__(self, settings: GameSettings, x: int, y: int):
        self._settings = settings
        self.x = x
        self.y = y
        self.collected = False
        self._grid_size = settings.grid_size
        self.radius = self._grid_size // 2 - 4
        self.animation_counter = 0

    def update(self) -> None:
        self.animation_counter = (self.animation_counter + 1) % 30

    def draw(self, surface) -> None:  # type: ignore[override]
        if self.collected:
            return
        center_x = self.x + self._grid_size // 2
        center_y = self.y + self._grid_size // 2
        pulse_radius = self.radius - 2 + (self.animation_counter % 5) // 2
        pygame.draw.circle(surface, (255, 255, 0), (center_x, center_y), pulse_radius)
        pygame.draw.circle(surface, (255, 200, 0), (center_x, center_y), pulse_radius, 1)


class Player(Drawable, Collidable):
    """Player controlled Pac-man style entity."""

    def __init__(self, settings: GameSettings):
        self._settings = settings
        self.x = settings.grid_size
        self.y = settings.grid_size
        self.speed = settings.player.speed
        self.score = 0
        self.lives = settings.player.initial_lives
        self.radius = settings.grid_size // 2 - 2
        self.animation_counter = 0
        self.mouth_angle = 45
        self.direction = Direction.RIGHT

    def move(self, direction: Direction) -> None:
        dx, dy = direction.delta
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed

        if 0 <= new_x < self._settings.width and 0 <= new_y < self._settings.height and not self.check_collision(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.direction = direction

    def check_collision(self, x: float, y: float) -> bool:
        game_state = SingletonGameState()
        grid_size = self._settings.grid_size
        for wall in game_state.walls:
            if x < wall.x + wall.width and x + grid_size > wall.x and y < wall.y + wall.height and y + grid_size > wall.y:
                return True
        return False

    def update(self) -> None:
        self.animation_counter = (self.animation_counter + 1) % 20
        self.mouth_angle = 45 if self.animation_counter < 10 else 20

    def draw(self, surface) -> None:  # type: ignore[override]
        center_x = self.x + self._settings.grid_size // 2
        center_y = self.y + self._settings.grid_size // 2

        pygame.draw.circle(surface, self._settings.colors.primary, (center_x, center_y), self.radius)

        direction_angles = {
            Direction.RIGHT: (360 - self.mouth_angle, self.mouth_angle),
            Direction.LEFT: (180 - self.mouth_angle, 180 + self.mouth_angle),
            Direction.UP: (270 - self.mouth_angle, 270 + self.mouth_angle),
            Direction.DOWN: (90 - self.mouth_angle, 90 + self.mouth_angle),
        }
        start_angle, end_angle = direction_angles.get(self.direction, (self.mouth_angle, 360 - self.mouth_angle))

        points: list[Tuple[float, float]] = [(center_x, center_y)]
        
        # Handle angle wrapping for proper arc drawing
        if start_angle <= end_angle:
            angles = range(int(start_angle), int(end_angle) + 1)
        else:
            # Wrap around 360
            angles = list(range(int(start_angle), 360)) + list(range(0, int(end_angle) + 1))
        
        for angle in angles:
            radians = math.radians(angle)
            px = center_x + self.radius * math.cos(radians)
            py = center_y + self.radius * math.sin(radians)
            points.append((px, py))
        points.append((center_x, center_y))

        pygame.draw.polygon(surface, self._settings.colors.background, points)


class Enemy(Drawable, Collidable):
    """Ghost enemy with light-weight AI movement."""

    def __init__(self, settings: GameSettings, x: int, y: int, color: Tuple[int, int, int]):
        self._settings = settings
        self.x = x
        self.y = y
        self.color = color
        self.speed = settings.enemy.speed
        self.direction = random.choice(list(Direction))
        self.radius = settings.grid_size // 2 - 2
        self.animation_counter = 0
        self.frightened = False
        self.move_counter = 0
        self.frozen = False
        self.freeze_counter = 0

    def update(self, power_mode_active: bool = False, freeze_active: bool = False) -> None:
        self.frightened = power_mode_active
        
        # Handle freeze state
        if freeze_active and not self.frozen:
            self.frozen = True
            self.freeze_counter = 60  # Freeze for 60 frames
        
        if self.frozen:
            self.freeze_counter -= 1
            if self.freeze_counter <= 0:
                self.frozen = False
            self.animation_counter = (self.animation_counter + 1) % 20
            return
        
        self.move_counter += 1
        if self.move_counter < self._settings.speed.movement_update_rate:
            self.animation_counter = (self.animation_counter + 1) % 20
            return

        self.move_counter = 0
        
        # Smart AI: Chase player 40% of the time, random 60% of the time
        if random.random() < 0.4:
            new_x, new_y = self._get_smart_position()
        else:
            new_x, new_y = self._get_new_position()

        if self.check_collision(new_x, new_y):
            for _ in range(10):
                self.direction = random.choice(list(Direction))
                new_x, new_y = self._get_new_position()
                if not self.check_collision(new_x, new_y):
                    break

        if not self.check_collision(new_x, new_y):
            self.x = new_x
            self.y = new_y

        self.animation_counter = (self.animation_counter + 1) % 20

    def _get_smart_position(self) -> Tuple[float, float]:
        """Move towards the player with some logic."""
        game_state = SingletonGameState()
        player = game_state.player
        
        # Calculate direction to player
        dx = player.x - self.x
        dy = player.y - self.y
        
        # Choose the direction that brings us closer
        directions = [
            (Direction.RIGHT, abs(dx + self._settings.enemy.speed - dy)),
            (Direction.LEFT, abs(dx - self._settings.enemy.speed - dy)),
            (Direction.DOWN, abs(dx - (dy + self._settings.enemy.speed))),
            (Direction.UP, abs(dx - (dy - self._settings.enemy.speed))),
        ]
        
        best_direction = min(directions, key=lambda x: x[1])[0]
        self.direction = best_direction
        
        return self._get_new_position()

    def _get_new_position(self) -> Tuple[float, float]:
        dx, dy = self.direction.delta
        return self.x + dx * self.speed, self.y + dy * self.speed

    def check_collision(self, x: float, y: float) -> bool:
        grid_size = self._settings.grid_size
        game_state = SingletonGameState()
        for wall in game_state.walls:
            if x < wall.x + wall.width and x + grid_size > wall.x and y < wall.y + wall.height and y + grid_size > wall.y:
                return True
        return False

    def draw(self, surface) -> None:  # type: ignore[override]
        center_x = self.x + self._settings.grid_size // 2
        center_y = self.y + self._settings.grid_size // 2

        # Determine color based on state
        if self.frozen:
            color = (100, 200, 255)  # Light blue for frozen
        elif self.frightened:
            color = (173, 216, 230)  # Light blue when frightened
        else:
            color = self.color  # Normal color
            
        pygame.draw.circle(surface, color, (center_x, center_y), self.radius)
        pygame.draw.rect(surface, color, (center_x - self.radius, center_y, self.radius * 2, self.radius))

        eye_radius = self.radius // 3
        left_eye_x = center_x - self.radius // 2
        right_eye_x = center_x + self.radius // 3
        eye_y = center_y - self.radius // 4

        if self.frozen:
            # Frozen enemies have X eyes
            pygame.draw.circle(surface, self._settings.colors.background, (left_eye_x, eye_y), eye_radius)
            pygame.draw.circle(surface, self._settings.colors.background, (right_eye_x, eye_y), eye_radius)
            pygame.draw.line(surface, self._settings.colors.text, (left_eye_x - eye_radius // 2, eye_y - eye_radius // 2), (left_eye_x + eye_radius // 2, eye_y + eye_radius // 2), 2)
            pygame.draw.line(surface, self._settings.colors.text, (left_eye_x - eye_radius // 2, eye_y + eye_radius // 2), (left_eye_x + eye_radius // 2, eye_y - eye_radius // 2), 2)
            pygame.draw.line(surface, self._settings.colors.text, (right_eye_x - eye_radius // 2, eye_y - eye_radius // 2), (right_eye_x + eye_radius // 2, eye_y + eye_radius // 2), 2)
            pygame.draw.line(surface, self._settings.colors.text, (right_eye_x - eye_radius // 2, eye_y + eye_radius // 2), (right_eye_x + eye_radius // 2, eye_y - eye_radius // 2), 2)
        elif self.frightened:
            pygame.draw.circle(surface, self._settings.colors.text, (left_eye_x, eye_y), eye_radius)
            pygame.draw.circle(surface, self._settings.colors.text, (right_eye_x, eye_y), eye_radius)
            pygame.draw.line(surface, self._settings.colors.background, (left_eye_x - eye_radius // 2, eye_y), (left_eye_x + eye_radius // 2, eye_y), 2)
            pygame.draw.line(surface, self._settings.colors.background, (right_eye_x - eye_radius // 2, eye_y), (right_eye_x + eye_radius // 2, eye_y), 2)
        else:
            pygame.draw.circle(surface, self._settings.colors.text, (left_eye_x, eye_y), eye_radius)
            pygame.draw.circle(surface, self._settings.colors.text, (right_eye_x, eye_y), eye_radius)
            pygame.draw.circle(surface, self._settings.colors.background, (left_eye_x, eye_y), eye_radius // 2)
            pygame.draw.circle(surface, self._settings.colors.background, (right_eye_x, eye_y), eye_radius // 2)
