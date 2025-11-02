# Irancell Anniversary Pac-Man Game

A retro-style Pac-Man-inspired game created to celebrate Irancell's anniversary! This game features classic arcade gameplay with Irancell's signature yellow color (#FFCC00).

## Features

- Classic Pac-Man style gameplay with maze navigation
- Collect coins to increase your score
- Power pellets that let you eat ghosts
- Multiple enemies with simple AI
- Lives system and score tracking
- Irancell branding and anniversary theme

## Requirements

- Python 3.6 or higher
- Pygame library

## Installation

```bash
# Clone this repository
git clone https://github.com/your-username/irancell-anniversary-game.git
cd irancell-anniversary-game

# Install required packages
pip install -r requirements.txt

# Or if you're using Arch Linux:
sudo pacman -S python-pygame
```

## How to Play

1. Run the game:
```bash
python main.py
```

2. Use arrow keys to navigate the maze:
   - UP: Move up
   - DOWN: Move down
   - LEFT: Move left
   - RIGHT: Move right

3. Collect all coins to complete the level
4. Avoid enemies unless you've eaten a power pellet
5. Press 'R' to restart after game over
6. Press 'N' to go to the next level after completing

## Controls

- Arrow keys: Move the player
- R: Restart game (after game over)
- N: Next level (after level complete)

## Game Elements

- **Player (Yellow)**: The main character that collects coins
- **Coins (White)**: Collect these for points
- **Power Pellets (Yellow)**: Eat these to temporarily eat ghosts
- **Enemies (Red, Pink, Cyan, Orange)**: Avoid these or eat them during power mode
- **Walls (Blue)**: Impassable barriers

## Customization

The game can be customized by modifying:
- Wall positions in the `walls` array
- Enemy behavior in the `Enemy` class
- Game speed in the `clock.tick()` call
- Score values in the collision detection code

## About

This game was created to celebrate Irancell's anniversary with a fun, retro-style experience that brings back classic arcade memories while incorporating Irancell's brand colors and identity.

## License

This project is open source and available under the [Apache License 2.0](LICENSE).

Copyright © 2025 MTN Irancell ICI and Ehsan Tork.

Contact: ehsna.tor@mtnirancell.ir · https://journalehsan.github.io

This celebratory project is created independently by an MTN Irancell staff member to cheer for the MTN Irancell anniversary. MTN Irancell is not responsible for the project.