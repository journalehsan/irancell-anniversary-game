"""Builder pattern for constructing levels."""

from __future__ import annotations

import random

from core.factory import GameObjectFactory
from core.game_state import SingletonGameState
from utils.config_loader import GameSettings


class LevelBuilder:
    """Incrementally assemble a level using the builder pattern."""

    def __init__(self, settings: GameSettings, factory: GameObjectFactory | None = None):
        self._settings = settings
        self._state = SingletonGameState()
        self._factory = factory or GameObjectFactory(settings)

    def build_maze(self) -> "LevelBuilder":
        grid = self._settings.grid_size
        width = self._settings.width
        height = self._settings.height

        # Cleaner, more balanced maze with proper spacing
        walls_data = [
            # Border walls
            (0, 0, width, grid),
            (0, height - grid, width, grid),
            (0, 0, grid, height),
            (width - grid, 0, grid, height),
            
            # Left side chambers
            (grid, grid * 2, grid * 2, grid),
            (grid, grid * 4, grid * 2, grid),
            (grid * 3, grid * 3, grid, grid),
            (grid, grid * 7, grid * 2, grid),
            (grid * 3, grid * 8, grid, grid),
            (grid, grid * 10, grid * 2, grid),
            (grid * 3, grid * 11, grid, grid),
            
            # Center passages and dividers
            (grid * 4, grid * 2, grid * 2, grid),
            (grid * 5, grid * 5, grid, grid * 2),
            (grid * 6, grid * 7, grid * 2, grid),
            (grid * 7, grid * 10, grid, grid),
            (grid * 8, grid * 2, grid, grid),
            (grid * 8, grid * 12, grid, grid),
            (grid * 9, grid * 5, grid, grid),
            
            # Right side chambers
            (grid * 11, grid * 2, grid * 2, grid),
            (grid * 12, grid * 4, grid, grid),
            (grid * 11, grid * 7, grid * 2, grid),
            (grid * 13, grid * 10, grid, grid),
            (grid * 14, grid * 5, grid, grid * 2),
            (grid * 15, grid * 2, grid * 2, grid),
            (grid * 15, grid * 11, grid * 2, grid),
            (grid * 17, grid * 8, grid, grid),
        ]

        for x, y, w, h in walls_data:
            self._state.walls.append(self._factory.create_wall(x, y, w, h))
        return self

    def build_coins(self) -> "LevelBuilder":
        grid = self._settings.grid_size
        for row in range(1, self._settings.grid_height - 1):
            for col in range(1, self._settings.grid_width - 1):
                pos_x, pos_y = col * grid, row * grid
                if not self._has_wall(pos_x, pos_y) and random.random() > 0.7:
                    self._state.coins.append(self._factory.create_coin(pos_x, pos_y))
        return self

    def build_power_pellets(self) -> "LevelBuilder":
        grid = self._settings.grid_size
        positions = [
            (grid * 1, grid * 1),
            (grid * (self._settings.grid_width - 2), grid * 1),
            (grid * 1, grid * (self._settings.grid_height - 2)),
            (grid * (self._settings.grid_width - 2), grid * (self._settings.grid_height - 2)),
        ]
        for x, y in positions:
            self._state.power_pellets.append(self._factory.create_power_pellet(x, y))
        return self

    def build_enemies(self, count: int = 4) -> "LevelBuilder":
        grid = self._settings.grid_size
        colors = self._settings.enemy.colors
        positions = [
            (grid * 3, grid * 3),
            (grid * 4, grid * 4),
            (grid * 5, grid * 3),
            (grid * 4, grid * 5),
        ]
        for idx in range(min(count, len(positions))):
            x, y = positions[idx]
            self._state.enemies.append(self._factory.create_enemy(x, y, colors[idx % len(colors)]))
        return self

    def build(self) -> SingletonGameState:
        return self._state

    def _has_wall(self, x: int, y: int) -> bool:
        grid = self._settings.grid_size
        for wall in self._state.walls:
            if x < wall.x + wall.width and x + grid > wall.x and y < wall.y + wall.height and y + grid > wall.y:
                return True
        return False
