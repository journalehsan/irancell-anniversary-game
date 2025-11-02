"""Entry point wiring together assets, controller, and rendering."""

from __future__ import annotations

import sys

import pygame

from core.game_controller import GameController
from utils.config_loader import load_settings
from views.fonts import create_font_bundle
from views.game_renderer import GameRenderer


def main() -> None:
    pygame.init()
    settings = load_settings()
    screen = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption(settings.title)
    clock = pygame.time.Clock()

    fonts = create_font_bundle()
    controller = GameController(settings)
    renderer = GameRenderer(settings, fonts)

    running = True
    show_start_screen = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if show_start_screen and event.type == pygame.KEYDOWN:
                show_start_screen = False
                controller.setup_level()

        if show_start_screen:
            renderer.draw_start_screen(screen)
            pygame.display.flip()
            clock.tick(settings.speed.fps)
            continue

        pressed_keys = pygame.key.get_pressed()
        controller.handle_input(pressed_keys)
        controller.update()
        renderer.draw_scene(screen, controller)

        if controller.game_over:
            renderer.draw_game_over(screen)
            if pressed_keys[pygame.K_r]:
                controller.restart()

        if controller.level_complete:
            renderer.draw_level_complete(screen)
            if pressed_keys[pygame.K_n]:
                controller.next_level()

        pygame.display.flip()
        clock.tick(settings.speed.fps)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
