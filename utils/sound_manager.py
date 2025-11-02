"""Sound effect scaffolding for future expansion."""

from __future__ import annotations

import pygame


class SoundManager:
    """Centralised sound loader and playback helper."""

    def __init__(self) -> None:
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        self.sounds: dict[str, pygame.mixer.Sound | None] = {}

    def load_sound(self, name: str, file_path: str) -> None:
        try:
            self.sounds[name] = pygame.mixer.Sound(file_path)
        except pygame.error:
            print(f"Warning: Could not load sound {file_path}")
            self.sounds[name] = None

    def play_sound(self, name: str) -> None:
        sound = self.sounds.get(name)
        if sound:
            sound.play()

    def play_coin_collect(self) -> None:
        pygame.mixer.Sound.play(pygame.mixer.Sound(buffer=bytearray([128] * 44)))

    def play_power_mode(self) -> None:
        pygame.mixer.Sound.play(pygame.mixer.Sound(buffer=bytearray([128] * 44)))

    def play_enemy_eaten(self) -> None:
        pygame.mixer.Sound.play(pygame.mixer.Sound(buffer=bytearray([128] * 44)))

    def play_game_over(self) -> None:
        pygame.mixer.Sound.play(pygame.mixer.Sound(buffer=bytearray([128] * 44)))
