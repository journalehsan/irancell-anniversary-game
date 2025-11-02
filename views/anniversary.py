"""Anniversary themed decorative rendering."""

from __future__ import annotations

import random
from datetime import datetime

import pygame

from utils.config_loader import GameSettings
from views.fonts import FontBundle


class AnniversaryView:
    """Render anniversary specific UI elements."""

    def __init__(self, settings: GameSettings, fonts: FontBundle):
        self._settings = settings
        self._fonts = fonts

    def draw_decorations(self, surface: pygame.Surface) -> None:
        year_text = self._fonts.small.render(f"{datetime.now().year}", True, self._settings.colors.primary)
        surface.blit(year_text, (20, 20))
        surface.blit(year_text, (self._settings.width - 40, 20))
        pygame.draw.circle(surface, self._settings.colors.primary, (25, self._settings.height - 25), 15, 2)
        pygame.draw.circle(surface, self._settings.colors.primary, (self._settings.width - 25, self._settings.height - 25), 15, 2)

    def draw_start_screen(self, surface: pygame.Surface) -> None:
        surface.fill(self._settings.colors.background)
        for _ in range(30):
            x = random.randint(0, self._settings.width)
            y = random.randint(0, self._settings.height)
            size = random.randint(1, 3)
            pygame.draw.circle(surface, self._settings.colors.primary, (x, y), size)

        for _ in range(10):
            start_pos = (
                random.randint(0, self._settings.width),
                random.randint(0, self._settings.height),
            )
            end_pos = (
                random.randint(0, self._settings.width),
                random.randint(0, self._settings.height),
            )
            pygame.draw.line(surface, (50, 50, 100), start_pos, end_pos, 1)

        title_text = self._fonts.large.render("PAC-IRANCELL", True, self._settings.colors.primary)
        title_rect = title_text.get_rect(center=(self._settings.width // 2, self._settings.height // 2 - 100))
        surface.blit(title_text, title_rect)

        subtitle = self._fonts.medium.render(
            f"Anniversary Edition - {self._settings.branding.years_of_service} Years of Service",
            True,
            (255, 215, 0),
        )
        subtitle_rect = subtitle.get_rect(center=(self._settings.width // 2, self._settings.height // 2 - 30))
        surface.blit(subtitle, subtitle_rect)

        branding_text = self._fonts.default.render(self._settings.branding.slogan, True, (173, 216, 230))
        branding_rect = branding_text.get_rect(center=(self._settings.width // 2, self._settings.height // 2 + 30))
        surface.blit(branding_text, branding_rect)

        start_text = self._fonts.default.render("Press any key to start", True, self._settings.colors.text)
        start_rect = start_text.get_rect(center=(self._settings.width // 2, self._settings.height // 2 + 80))
        surface.blit(start_text, start_rect)

        anniversary_msg = self._fonts.small.render(
            "Celebrating connectivity, innovation, and service", True, self._settings.colors.primary
        )
        anniversary_rect = anniversary_msg.get_rect(center=(self._settings.width // 2, self._settings.height // 2 + 120))
        surface.blit(anniversary_msg, anniversary_rect)

