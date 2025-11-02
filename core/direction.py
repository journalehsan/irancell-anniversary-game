"""Direction related enums used in movement logic."""

from __future__ import annotations

from enum import Enum


class Direction(Enum):
    """Grid based movement directions."""

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @property
    def delta(self) -> tuple[int, int]:
        """Return directional delta for clarity."""
        return self.value
