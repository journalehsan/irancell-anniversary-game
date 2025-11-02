"""Font factory helpers."""

from __future__ import annotations

from dataclasses import dataclass

import pygame


@dataclass
class FontBundle:
    """Grouped pygame fonts for consistent styling."""

    default: pygame.font.Font
    large: pygame.font.Font
    medium: pygame.font.Font
    small: pygame.font.Font


def create_font_bundle() -> FontBundle:
    """Instantiate the default font bundle used across the UI."""
    return FontBundle(
        default=pygame.font.SysFont(None, 36),
        large=pygame.font.SysFont(None, 72),
        medium=pygame.font.SysFont(None, 48),
        small=pygame.font.SysFont(None, 24),
    )
