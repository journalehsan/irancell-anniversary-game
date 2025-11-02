"""Anniversary themed decorative rendering."""

from __future__ import annotations

import random
from datetime import datetime
from pathlib import Path

import pygame

from utils.config_loader import GameSettings
from views.fonts import FontBundle


class AnniversaryView:
    """Render anniversary specific UI elements."""

    def __init__(self, settings: GameSettings, fonts: FontBundle):
        self._settings = settings
        self._fonts = fonts
        self._logo = None
        self._load_logo()

    def _load_logo(self) -> None:
        """Load the anniversary logo image."""
        logo_paths = [
            Path("assets/start-logo.png"),
            Path("assets/logo.png"),
            Path("assets/irancell-pacman.png"),
        ]
        for path in logo_paths:
            if path.exists():
                try:
                    self._logo = pygame.image.load(str(path))
                    # Scale logo to fit nicely on screen (max 600px wide, 400px tall)
                    logo_rect = self._logo.get_rect()
                    max_width = min(600, self._settings.width - 100)
                    max_height = 400
                    
                    scale_factor = min(max_width / logo_rect.width, max_height / logo_rect.height)
                    new_width = int(logo_rect.width * scale_factor)
                    new_height = int(logo_rect.height * scale_factor)
                    
                    self._logo = pygame.transform.scale(self._logo, (new_width, new_height))
                    break
                except Exception:
                    continue

    def draw_decorations(self, surface: pygame.Surface) -> None:
        year_text = self._fonts.small.render(f"{datetime.now().year}", True, self._settings.colors.primary)
        surface.blit(year_text, (20, 20))
        surface.blit(year_text, (self._settings.width - 40, 20))
        pygame.draw.circle(surface, self._settings.colors.primary, (25, self._settings.height - 25), 15, 2)
        pygame.draw.circle(surface, self._settings.colors.primary, (self._settings.width - 25, self._settings.height - 25), 15, 2)

    def draw_start_screen(self, surface: pygame.Surface) -> None:
        surface.fill(self._settings.colors.background)
        
        # Draw subtle background decorations
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

        # Draw logo if available
        if self._logo:
            logo_rect = self._logo.get_rect(center=(self._settings.width // 2, self._settings.height // 2 - 80))
            surface.blit(self._logo, logo_rect)
            
            # Position text below logo
            start_text = self._fonts.large.render("Press any key to start", True, self._settings.colors.text)
            start_rect = start_text.get_rect(center=(self._settings.width // 2, self._settings.height // 2 + 180))
            surface.blit(start_text, start_rect)
            
            # Optional: Add slogan below
            branding_text = self._fonts.medium.render(
                self._settings.branding.slogan, 
                True, 
                (173, 216, 230)
            )
            branding_rect = branding_text.get_rect(center=(self._settings.width // 2, self._settings.height // 2 + 230))
            surface.blit(branding_text, branding_rect)
        else:
            # Fallback to text-only if logo not found
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

