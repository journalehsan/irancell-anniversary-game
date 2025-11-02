"""Common abstract interfaces for core game objects."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Drawable(ABC):
    """Strategy style interface for objects that render themselves."""

    @abstractmethod
    def draw(self, surface) -> None:  # type: ignore[override]
        """Draw the object to the provided surface."""


class Collidable(ABC):
    """Interface for objects that can participate in collision checks."""

    @abstractmethod
    def check_collision(self, x: float, y: float) -> bool:
        """Determine whether a future position collides with the object."""
