"""High level controller orchestrating gameplay."""

from __future__ import annotations

import random
import pygame

from core.direction import Direction
from core.factory import GameObjectFactory
from core.game_state import SingletonGameState
from core.level_builder import LevelBuilder
from core.power_mode import PowerMode
from utils.config_loader import GameSettings


class GameController:
    """Coordinate player input, state updates, and level progression."""

    def __init__(self, settings: GameSettings):
        self._settings = settings
        self.factory = GameObjectFactory(settings)
        self.game_state = SingletonGameState()
        self.player = self.factory.create_player()
        self.power_mode = PowerMode(settings)
        self.game_over = False
        self.level_complete = False

    def setup_level(self) -> None:
        self.game_state.reset()
        builder = LevelBuilder(self._settings, self.factory)
        builder.build_maze().build_coins().build_power_pellets().build_enemies().build()
        self.level_complete = False

    def handle_input(self, pressed_keys: pygame.key.ScancodeWrapper) -> None:
        if self.game_over or self.level_complete:
            return
        if pressed_keys[pygame.K_LEFT]:
            self.player.move(Direction.LEFT)
        elif pressed_keys[pygame.K_RIGHT]:
            self.player.move(Direction.RIGHT)
        elif pressed_keys[pygame.K_UP]:
            self.player.move(Direction.UP)
        elif pressed_keys[pygame.K_DOWN]:
            self.player.move(Direction.DOWN)

    def update(self) -> None:
        if self.game_over or self.level_complete:
            return

        self.player.update()
        self.power_mode.update()

        for coin in self.game_state.coins:
            coin.update()

        for pellet in self.game_state.power_pellets:
            pellet.update()

        for enemy in self.game_state.enemies:
            enemy.update(self.power_mode.active, self.power_mode.freeze_active)

        self._check_coin_collection()
        self._check_power_pellet_collection()
        self._check_enemy_collision()
        self._check_win_condition()

    def restart(self) -> None:
        self.player = self.factory.create_player()
        self.power_mode = PowerMode(self._settings)
        self.game_over = False
        self.level_complete = False
        self.setup_level()

    def next_level(self) -> None:
        self.player.lives += 1
        self.player.x = self._settings.grid_size
        self.player.y = self._settings.grid_size
        self.power_mode = PowerMode(self._settings)
        self.setup_level()
        if len(self.game_state.enemies) < 5 and self._settings.enemy.colors:
            color = (128, 0, 128)
            self.game_state.enemies.append(
                self.factory.create_enemy(self._settings.grid_size * 2, self._settings.grid_size * 7, color)
            )

    def _check_coin_collection(self) -> None:
        grid = self._settings.grid_size
        for coin in self.game_state.coins:
            if coin.collected:
                continue
            if self.player.x < coin.x + grid and self.player.x + grid > coin.x and self.player.y < coin.y + grid and self.player.y + grid > coin.y:
                coin.collected = True
                self.player.score += self._settings.player.score_per_coin
                # 15% chance to freeze enemies when collecting a coin
                if random.random() < 0.15:
                    self.power_mode.activate_freeze()

    def _check_power_pellet_collection(self) -> None:
        grid = self._settings.grid_size
        for pellet in self.game_state.power_pellets:
            if pellet.collected:
                continue
            if self.player.x < pellet.x + grid and self.player.x + grid > pellet.x and self.player.y < pellet.y + grid and self.player.y + grid > pellet.y:
                pellet.collected = True
                self.player.score += self._settings.player.score_per_power_pellet
                self.power_mode.activate()

    def _check_enemy_collision(self) -> None:
        grid = self._settings.grid_size
        enemies_snapshot = list(self.game_state.enemies)
        for enemy in enemies_snapshot:
            if self.player.x < enemy.x + grid and self.player.x + grid > enemy.x and self.player.y < enemy.y + grid and self.player.y + grid > enemy.y:
                if self.power_mode.active:
                    self.game_state.enemies.remove(enemy)
                    self.player.score += self._settings.player.score_per_enemy
                    spawn_x = self._settings.grid_size * random.randint(1, self._settings.grid_width - 2)
                    spawn_y = self._settings.grid_size * random.randint(1, self._settings.grid_height - 2)
                    if self._settings.enemy.colors:
                        color = random.choice(self._settings.enemy.colors)
                    else:
                        color = (255, 0, 0)
                    self.game_state.enemies.append(self.factory.create_enemy(spawn_x, spawn_y, color))
                else:
                    self.player.lives -= 1
                    if self.player.lives <= 0:
                        self.game_over = True
                    else:
                        self.player.x = self._settings.grid_size
                        self.player.y = self._settings.grid_size

    def _check_win_condition(self) -> None:
        if all(coin.collected for coin in self.game_state.coins) and all(pellet.collected for pellet in self.game_state.power_pellets):
            self.level_complete = True
