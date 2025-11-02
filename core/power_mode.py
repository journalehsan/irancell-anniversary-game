"""Power mode state management."""

from __future__ import annotations

from utils.config_loader import GameSettings


class PowerMode:
    """Handle temporary empowered state for the player."""

    def __init__(self, settings: GameSettings):
        self._settings = settings
        self.active = False
        self.timer = 0

    def activate(self) -> None:
        if not self._settings.power_mode.enabled:
            return
        self.active = True
        self.timer = self._settings.power_mode.duration

    def update(self) -> None:
        if not self.active:
            return
        self.timer -= 1
        if self.timer <= 0:
            self.active = False
