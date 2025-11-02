# Irancell Anniversary Game - Development Notes

## Project Structure
```
irancell-anniversary-game/
├── main.py              # Main game file with all game logic
├── sounds.py            # Sound management module
├── config.json          # Configuration settings
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
├── LOGO.md              # Logo and branding elements
├── launch.py            # Launcher script
├── assets/              # Game assets (images, sounds)
└── docs/                # Additional documentation
```

## Key Features Implemented

### 1. Core Game Mechanics
- Classic Pac-Man gameplay with maze navigation
- Coin collection system
- Power pellet mechanics
- Enemy AI with chase/frightened behavior
- Lives and scoring system

### 2. Enhanced Visuals
- Animated player character (Pacman with opening/closing mouth)
- Animated coins and power pellets
- Frightened enemy state (blue when power mode active)
- Smooth 60 FPS gameplay
- Grid-based movement system

### 3. Irancell Branding
- Primary color: Irancell yellow (#FFCC00)
- Anniversary-themed start screen
- Network connection motifs
- "PAC-IRANCELL" title
- "Celebrating Years of Connection" messaging
- Special anniversary decorations

### 4. Configurable Settings
- JSON-based configuration system
- Customizable colors, speeds, and game parameters
- Easy to modify gameplay elements
- Branding configuration

### 5. Game States
- Start screen with anniversary theme
- Main gameplay loop
- Game over screen
- Level completion screen
- Restart and next level functionality

## Technical Details

### Dependencies
- pygame: Game engine and rendering
- json: Configuration management
- random: For enemy AI and maze generation
- math: For drawing calculations
- sys: For application exit

### Classes
- `Player`: Manages player position, movement, and rendering
- `Wall`: Represents maze barriers
- `Coin`: Collectible items
- `PowerPellet`: Special items that enable power mode
- `Enemy`: Ghost characters with AI
- `PowerMode`: Manages power mode state
- `SoundManager`: Handles game audio (placeholder)

## Customization Options

The game can be customized by modifying:
1. `config.json` - Change colors, speeds, scores, and branding
2. `main.py` - Adjust game mechanics and visuals
3. Adding new sound files to enhance audio
4. Creating new maze layouts by modifying the walls array

## Future Enhancements

Potential improvements could include:
- Actual sound effects and music
- High score tracking
- Multiple maze layouts
- Special power-ups
- Mobile-friendly controls
- Additional difficulty levels
- Online leaderboards

## Development Process

This game was developed by starting with a basic Pac-Man concept and progressively enhancing it with:
1. More complex game mechanics
2. Better visual effects and animations
3. Strong Irancell branding and anniversary theme
4. Configurable settings
5. Improved user interface

The final result is a complete, polished game that celebrates Irancell's anniversary while providing engaging retro-style gameplay.