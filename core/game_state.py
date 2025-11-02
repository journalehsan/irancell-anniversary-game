"""Singleton game state container."""

from __future__ import annotations

class SingletonGameState:
    """Centralised state shared across systems via the singleton pattern."""

    _instance: "SingletonGameState" | None = None

    def __new__(cls) -> "SingletonGameState":  # type: ignore[override]
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.walls = []
            cls._instance.coins = []
            cls._instance.power_pellets = []
            cls._instance.enemies = []
        return cls._instance

    def reset(self) -> None:
        """Clear all stateful collections to prepare for a new level."""
        self.walls.clear()
        self.coins.clear()
        self.power_pellets.clear()
        self.enemies.clear()
