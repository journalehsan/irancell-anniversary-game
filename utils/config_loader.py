"""Configuration loading helpers."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Tuple

_DEFAULT_CONFIG: Dict[str, Any] = {
    "game_title": "Irancell Anniversary Pac-Man",
    "window_width": 800,
    "window_height": 600,
    "grid_size": 40,
    "colors": {
        "primary": [255, 204, 0],
        "background": [0, 0, 0],
        "wall": [0, 0, 255],
        "text": [255, 255, 255],
    },
    "player_settings": {
        "speed": 20,
        "initial_lives": 3,
        "score_per_coin": 10,
        "score_per_power_pellet": 50,
        "score_per_enemy": 200,
    },
    "enemy_settings": {
        "speed": 15,
        "colors": [
            [255, 0, 0],
            [255, 192, 203],
            [0, 255, 255],
            [255, 165, 0],
        ],
    },
    "game_speed": {
        "fps": 60,
        "movement_update_rate": 2,
    },
    "power_mode": {
        "duration": 300,
        "enabled": True,
    },
    "branding": {
        "company_name": "Irancell",
        "slogan": "Celebrating Years of Connection",
        "anniversary_text": "Irancell Anniversary Edition",
        "years_of_service": 20,
    },
}


@dataclass(frozen=True)
class ColorPalette:
    primary: Tuple[int, int, int]
    background: Tuple[int, int, int]
    wall: Tuple[int, int, int]
    text: Tuple[int, int, int]


@dataclass(frozen=True)
class PlayerSettings:
    speed: int
    initial_lives: int
    score_per_coin: int
    score_per_power_pellet: int
    score_per_enemy: int


@dataclass(frozen=True)
class EnemySettings:
    speed: int
    colors: List[Tuple[int, int, int]]


@dataclass(frozen=True)
class GameSpeed:
    fps: int
    movement_update_rate: int


@dataclass(frozen=True)
class PowerModeSettings:
    duration: int
    enabled: bool


@dataclass(frozen=True)
class Branding:
    company_name: str
    slogan: str
    anniversary_text: str
    years_of_service: int


@dataclass(frozen=True)
class GameSettings:
    title: str
    width: int
    height: int
    grid_size: int
    grid_width: int
    grid_height: int
    colors: ColorPalette
    player: PlayerSettings
    enemy: EnemySettings
    speed: GameSpeed
    power_mode: PowerModeSettings
    branding: Branding


def _ensure_game_speed(config: Dict[str, Any]) -> None:
    if "game_speed" not in config:
        config["game_speed"] = _DEFAULT_CONFIG["game_speed"].copy()


def load_raw_config(path: str | Path = "config.json") -> Dict[str, Any]:
    """Load configuration JSON, falling back to defaults when missing."""
    config_path = Path(path)
    if not config_path.exists():
        return json.loads(json.dumps(_DEFAULT_CONFIG))

    with config_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_settings(path: str | Path = "config.json") -> GameSettings:
    """Load the configuration and convert it into strongly typed settings."""
    raw_config = load_raw_config(path)
    _ensure_game_speed(raw_config)

    colors = raw_config.get("colors", {})
    palette = ColorPalette(
        primary=tuple(colors.get("primary", _DEFAULT_CONFIG["colors"]["primary"])),
        background=tuple(colors.get("background", _DEFAULT_CONFIG["colors"]["background"])),
        wall=tuple(colors.get("wall", _DEFAULT_CONFIG["colors"]["wall"])),
        text=tuple(colors.get("text", _DEFAULT_CONFIG["colors"]["text"])),
    )

    player_config = raw_config.get("player_settings", {})
    player = PlayerSettings(
        speed=player_config.get("speed", _DEFAULT_CONFIG["player_settings"]["speed"]),
        initial_lives=player_config.get("initial_lives", _DEFAULT_CONFIG["player_settings"]["initial_lives"]),
        score_per_coin=player_config.get("score_per_coin", _DEFAULT_CONFIG["player_settings"]["score_per_coin"]),
        score_per_power_pellet=player_config.get("score_per_power_pellet", _DEFAULT_CONFIG["player_settings"]["score_per_power_pellet"]),
        score_per_enemy=player_config.get("score_per_enemy", _DEFAULT_CONFIG["player_settings"]["score_per_enemy"]),
    )

    enemy_config = raw_config.get("enemy_settings", {})
    enemy_colors = enemy_config.get("colors", _DEFAULT_CONFIG["enemy_settings"]["colors"])
    enemy = EnemySettings(
        speed=enemy_config.get("speed", _DEFAULT_CONFIG["enemy_settings"]["speed"]),
        colors=[tuple(color) for color in enemy_colors],
    )

    speed_config = raw_config.get("game_speed", {})
    speed = GameSpeed(
        fps=speed_config.get("fps", _DEFAULT_CONFIG["game_speed"]["fps"]),
        movement_update_rate=speed_config.get("movement_update_rate", _DEFAULT_CONFIG["game_speed"]["movement_update_rate"]),
    )

    power_config = raw_config.get("power_mode", {})
    power_mode = PowerModeSettings(
        duration=power_config.get("duration", _DEFAULT_CONFIG["power_mode"]["duration"]),
        enabled=power_config.get("enabled", _DEFAULT_CONFIG["power_mode"]["enabled"]),
    )

    branding_config = raw_config.get("branding", {})
    branding = Branding(
        company_name=branding_config.get("company_name", _DEFAULT_CONFIG["branding"]["company_name"]),
        slogan=branding_config.get("slogan", _DEFAULT_CONFIG["branding"]["slogan"]),
        anniversary_text=branding_config.get("anniversary_text", _DEFAULT_CONFIG["branding"]["anniversary_text"]),
        years_of_service=branding_config.get("years_of_service", _DEFAULT_CONFIG["branding"]["years_of_service"]),
    )

    width = raw_config.get("window_width", _DEFAULT_CONFIG["window_width"])
    height = raw_config.get("window_height", _DEFAULT_CONFIG["window_height"])
    grid_size = raw_config.get("grid_size", _DEFAULT_CONFIG["grid_size"])

    return GameSettings(
        title=raw_config.get("game_title", _DEFAULT_CONFIG["game_title"]),
        width=width,
        height=height,
        grid_size=grid_size,
        grid_width=width // grid_size,
        grid_height=height // grid_size,
        colors=palette,
        player=player,
        enemy=enemy,
        speed=speed,
        power_mode=power_mode,
        branding=branding,
    )
