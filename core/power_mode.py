"""Power mode state management."""

from __future__ import annotations

from utils.config_loader import GameSettings


class PowerMode:
    """Handle temporary empowered state for the player."""

    def __init__(self, settings: GameSettings):
        self._settings = settings
        self.active = False
        self.timer = 0
        self.freeze_active = False
        self.freeze_timer = 0

    def activate(self) -> None:
        if not self._settings.power_mode.enabled:
            return
        self.active = True
        self.timer = self._settings.power_mode.duration

    def activate_freeze(self) -> None:
        """Freeze all enemies temporarily."""
        if not self._settings.power_mode.enabled:
            return
        self.freeze_active = True
        self.freeze_timer = self._settings.power_mode.duration

    def update(self) -> None:
        if self.active:
            self.timer -= 1
            if self.timer <= 0:
                self.active = False
        
        if self.freeze_active:
            self.freeze_timer -= 1
            if self.freeze_timer <= 0:
                self.freeze_active = False
