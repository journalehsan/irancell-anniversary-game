"""Factory helpers for constructing core game objects."""

from __future__ import annotations

from core.entities import Coin, Enemy, Player, PowerPellet, Wall
from utils.config_loader import GameSettings


class GameObjectFactory:
    """Centralised creation logic implementing the factory pattern."""

    def __init__(self, settings: GameSettings):
        self._settings = settings

    def create_player(self) -> Player:
        return Player(self._settings)

    def create_coin(self, x: int, y: int) -> Coin:
        return Coin(self._settings, x, y)

    def create_power_pellet(self, x: int, y: int) -> PowerPellet:
        return PowerPellet(self._settings, x, y)

    def create_enemy(self, x: int, y: int, color) -> Enemy:
        return Enemy(self._settings, x, y, color)

    def create_wall(self, x: int, y: int, width: int, height: int) -> Wall:
        return Wall(self._settings, x, y, width, height)
