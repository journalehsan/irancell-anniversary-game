"""Rendering logic for the main gameplay view."""

from __future__ import annotations

import pygame

from core.game_controller import GameController
from utils.config_loader import GameSettings
from views.anniversary import AnniversaryView
from views.fonts import FontBundle


class GameRenderer:
    """Render the gameplay scene and heads-up display."""

    def __init__(self, settings: GameSettings, fonts: FontBundle):
        self._settings = settings
        self._fonts = fonts
        self._anniversary_view = AnniversaryView(settings, fonts)

    def draw_scene(self, surface: pygame.Surface, controller: GameController) -> None:
        surface.fill(self._settings.colors.background)
        self._anniversary_view.draw_decorations(surface)

        for wall in controller.game_state.walls:
            wall.draw(surface)

        for coin in controller.game_state.coins:
            coin.draw(surface)

        for pellet in controller.game_state.power_pellets:
            pellet.draw(surface)

        for enemy in controller.game_state.enemies:
            enemy.draw(surface)

        controller.player.draw(surface)
        self._draw_ui(surface, controller)

    def draw_start_screen(self, surface: pygame.Surface) -> None:
        self._anniversary_view.draw_start_screen(surface)

    def draw_game_over(self, surface: pygame.Surface) -> None:
        text = self._fonts.default.render("GAME OVER! Press R to restart", True, (255, 0, 0))
        rect = text.get_rect(center=(self._settings.width // 2, self._settings.height // 2))
        surface.blit(text, rect)

    def draw_level_complete(self, surface: pygame.Surface) -> None:
        text = self._fonts.default.render("LEVEL COMPLETE! Press N for next level", True, self._settings.colors.primary)
        rect = text.get_rect(center=(self._settings.width // 2, self._settings.height // 2))
        surface.blit(text, rect)

    def _draw_ui(self, surface: pygame.Surface, controller: GameController) -> None:
        score_text = self._fonts.default.render(f"Score: {controller.player.score}", True, self._settings.colors.text)
        surface.blit(score_text, (10, 10))

        lives_text = self._fonts.default.render(f"Lives: {controller.player.lives}", True, self._settings.colors.text)
        surface.blit(lives_text, (self._settings.width - 120, 10))

        if controller.power_mode.active:
            power_text = self._fonts.small.render(
                f"POWER MODE: {controller.power_mode.timer // 60}s",
                True,
                self._settings.colors.primary,
            )
            surface.blit(power_text, (self._settings.width // 2 - 80, self._settings.height - 70))

        title_text = self._fonts.large.render("PAC-IRANCELL", True, self._settings.colors.primary)
        title_rect = title_text.get_rect(center=(self._settings.width // 2, self._settings.height - 40))
        surface.blit(title_text, title_rect)
