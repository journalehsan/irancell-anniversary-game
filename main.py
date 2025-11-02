import pygame
import random
import math
import sys
import json
from datetime import datetime
from abc import ABC, abstractmethod
from enum import Enum

# Initialize Pygame
pygame.init()

# Load configuration from config.json
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    config = {
        "game_title": "Irancell Anniversary Pac-Man",
        "window_width": 800,
        "window_height": 600,
        "grid_size": 40,
        "colors": {
            "primary": [255, 204, 0],
            "background": [0, 0, 0],
            "wall": [0, 0, 255],
            "text": [255, 255, 255]
        },
        "player_settings": {
            "speed": 20,
            "initial_lives": 3,
            "score_per_coin": 10,
            "score_per_power_pellet": 50,
            "score_per_enemy": 200
        },
        "enemy_settings": {
            "speed": 15,
            "colors": [
                [255, 0, 0],
                [255, 192, 203],
                [0, 255, 255],
                [255, 165, 0]
            ]
        },
        "game_speed": {
            "fps": 60,
            "movement_update_rate": 2
        },
        "power_mode": {
            "duration": 300,
            "enabled": True
        },
        "branding": {
            "company_name": "Irancell",
            "slogan": "Celebrating Years of Connection",
            "anniversary_text": "Irancell Anniversary Edition",
            "years_of_service": 20
        },
    }

# Ensure 'game_speed' exists, providing defaults if missing
if "game_speed" not in config:
    config["game_speed"] = {
        "fps": 60,
        "movement_update_rate": 2
    }

# Screen Dimensions
WIDTH = config["window_width"]
HEIGHT = config["window_height"]
GRID_SIZE = config["grid_size"]
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
YELLOW = tuple(config["colors"]["primary"])
BLACK = tuple(config["colors"]["background"])
WHITE = tuple(config["colors"]["text"])
BLUE = tuple(config["colors"]["wall"])
RED = tuple(config["enemy_settings"]["colors"][0])
PINK = tuple(config["enemy_settings"]["colors"][1])
CYAN = tuple(config["enemy_settings"]["colors"][2])
ORANGE = tuple(config["enemy_settings"]["colors"][3])
PURPLE = (128, 0, 128)
LIGHT_BLUE = (173, 216, 230)
GOLD = (255, 215, 0)

# Game settings
PLAYER_SPEED = config["player_settings"]["speed"]
ENEMY_SPEED = config["enemy_settings"]["speed"]
INITIAL_LIVES = config["player_settings"]["initial_lives"]
SCORE_PER_COIN = config["player_settings"]["score_per_coin"]
SCORE_PER_POWER_PELLET = config["player_settings"]["score_per_power_pellet"]
SCORE_PER_ENEMY = config["player_settings"]["score_per_enemy"]
POWER_MODE_DURATION = config["power_mode"]["duration"]
GAME_FPS = config["game_speed"]["fps"]
MOVEMENT_UPDATE_RATE = config["game_speed"]["movement_update_rate"]

# Create screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(config["game_title"])
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 72)
medium_font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 24)


# ===================== DESIGN PATTERNS =====================

class Direction(Enum):
    """Enum for directions"""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Drawable(ABC):
    """Abstract base class for drawable objects - Strategy Pattern"""
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self):
        pass


class Collidable(ABC):
    """Abstract base class for collidable objects"""
    @abstractmethod
    def check_collision(self, x, y):
        pass


class GameObjectFactory:
    """Factory Pattern for creating game objects"""
    @staticmethod
    def create_coin(x, y):
        return Coin(x, y)

    @staticmethod
    def create_power_pellet(x, y):
        return PowerPellet(x, y)

    @staticmethod
    def create_enemy(x, y, color, speed=ENEMY_SPEED):
        return Enemy(x, y, color, speed)

    @staticmethod
    def create_wall(x, y, width, height):
        return Wall(x, y, width, height)


class SingletonGameState:
    """Singleton Pattern for game state management"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.walls = []
            cls._instance.coins = []
            cls._instance.power_pellets = []
            cls._instance.enemies = []
        return cls._instance

    def reset(self):
        self.walls.clear()
        self.coins.clear()
        self.power_pellets.clear()
        self.enemies.clear()

# ===================== DRAWABLE OBJECTS =====================

class Player(Drawable, Collidable):
    """Player class with fixed C-shaped appearance"""
    
    def __init__(self):
        self.x = GRID_SIZE
        self.y = GRID_SIZE
        self.speed = PLAYER_SPEED
        self.score = 0
        self.lives = INITIAL_LIVES
        self.radius = GRID_SIZE // 2 - 2
        self.animation_counter = 0
        self.mouth_angle = 45
        self.direction = Direction.RIGHT

    def move(self, direction):
        """Move player in given direction"""
        dx, dy = direction.value
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed
        
        game_state = SingletonGameState()
        if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and \
           not self.check_collision(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.direction = direction

    def check_collision(self, x, y):
        """Check collision with walls"""
        game_state = SingletonGameState()
        for wall in game_state.walls:
            if x < wall.x + wall.width and \
               x + GRID_SIZE > wall.x and \
               y < wall.y + wall.height and \
               y + GRID_SIZE > wall.y:
                return True
        return False

    def update(self):
        """Update animation"""
        self.animation_counter = (self.animation_counter + 1) % 20
        self.mouth_angle = 45 if self.animation_counter < 10 else 20

    def draw(self):
        """Draw player as C shape (Pacman)"""
        center_x = self.x + GRID_SIZE // 2
        center_y = self.y + GRID_SIZE // 2
        
        # Draw circle
        pygame.draw.circle(screen, YELLOW, (center_x, center_y), self.radius)
        
        # Draw mouth based on direction
        direction_angles = {
            Direction.RIGHT: (self.mouth_angle, 360 - self.mouth_angle),
            Direction.LEFT: (180 - self.mouth_angle, 180 + self.mouth_angle),
            Direction.UP: (270 - self.mouth_angle, 270 + self.mouth_angle),
            Direction.DOWN: (90 - self.mouth_angle, 90 + self.mouth_angle)
        }
        
        start_angle, end_angle = direction_angles.get(self.direction, (self.mouth_angle, 360 - self.mouth_angle))
        
        # Draw mouth as pie slice
        points = [(center_x, center_y)]
        for angle in range(int(start_angle), int(end_angle) + 1):
            rad = math.radians(angle)
            px = center_x + self.radius * math.cos(rad)
            py = center_y + self.radius * math.sin(rad)
            points.append((px, py))
        points.append((center_x, center_y))
        
        pygame.draw.polygon(screen, BLACK, points)

class Wall(Drawable):
    """Wall class"""
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (0, 0, 100), (self.x, self.y, self.width, self.height), 2)

class Coin(Drawable):
    """Coin class with pulsing animation"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.collected = False
        self.radius = GRID_SIZE // 4
        self.animation_counter = 0

    def update(self):
        self.animation_counter = (self.animation_counter + 1) % 20

    def draw(self):
        if not self.collected:
            center_x = self.x + GRID_SIZE // 2
            center_y = self.y + GRID_SIZE // 2
            pulse_radius = self.radius - 1 + (self.animation_counter % 4) // 2
            pygame.draw.circle(screen, YELLOW, (center_x, center_y), pulse_radius)
            pygame.draw.circle(screen, (255, 255, 100), (center_x, center_y), pulse_radius, 1)

class PowerPellet(Drawable):
    """Power pellet class"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.collected = False
        self.radius = GRID_SIZE // 2 - 4
        self.animation_counter = 0

    def update(self):
        self.animation_counter = (self.animation_counter + 1) % 30

    def draw(self):
        if not self.collected:
            center_x = self.x + GRID_SIZE // 2
            center_y = self.y + GRID_SIZE // 2
            pulse_radius = self.radius - 2 + (self.animation_counter % 5) // 2
            pygame.draw.circle(screen, (255, 255, 0), (center_x, center_y), pulse_radius)
            pygame.draw.circle(screen, (255, 200, 0), (center_x, center_y), pulse_radius, 1)

class Enemy(Drawable, Collidable):
    """Enemy/Ghost class with AI"""
    
    def __init__(self, x, y, color, speed=ENEMY_SPEED):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.direction = random.choice(list(Direction))
        self.radius = GRID_SIZE // 2 - 2
        self.animation_counter = 0
        self.frightened = False
        self.move_counter = 0

    def update(self, power_mode_active=False):
        """Update enemy with simple AI - move slower than original"""
        self.frightened = power_mode_active
        self.move_counter += 1
        
        if self.move_counter >= MOVEMENT_UPDATE_RATE:
            self.move_counter = 0
            new_x, new_y = self._get_new_position()
            
            if self.check_collision(new_x, new_y):
                for _ in range(10):
                    self.direction = random.choice(list(Direction))
                    new_x, new_y = self._get_new_position()
                    if not self.check_collision(new_x, new_y):
                        break
            
            if not self.check_collision(new_x, new_y):
                self.x = new_x
                self.y = new_y
        
        self.animation_counter = (self.animation_counter + 1) % 20

    def _get_new_position(self):
        """Get new position based on current direction"""
        dx, dy = self.direction.value
        return self.x + dx * self.speed, self.y + dy * self.speed

    def check_collision(self, x, y):
        """Check collision with walls"""
        game_state = SingletonGameState()
        for wall in game_state.walls:
            if x < wall.x + wall.width and \
               x + GRID_SIZE > wall.x and \
               y < wall.y + wall.height and \
               y + GRID_SIZE > wall.y:
                return True
        return False

    def draw(self):
        """Draw ghost"""
        center_x = self.x + GRID_SIZE // 2
        center_y = self.y + GRID_SIZE // 2
        
        color = LIGHT_BLUE if self.frightened else self.color
        pygame.draw.circle(screen, color, (center_x, center_y), self.radius)
        pygame.draw.rect(screen, color, 
                        (center_x - self.radius, center_y, 
                         self.radius * 2, self.radius))
        
        # Draw eyes
        eye_radius = self.radius // 3
        left_eye_x = center_x - self.radius // 2
        right_eye_x = center_x + self.radius // 3
        eye_y = center_y - self.radius // 4
        
        if self.frightened:
            pygame.draw.circle(screen, WHITE, (left_eye_x, eye_y), eye_radius)
            pygame.draw.circle(screen, WHITE, (right_eye_x, eye_y), eye_radius)
            pygame.draw.line(screen, BLACK, (left_eye_x - eye_radius//2, eye_y), 
                            (left_eye_x + eye_radius//2, eye_y), 2)
            pygame.draw.line(screen, BLACK, (right_eye_x - eye_radius//2, eye_y), 
                            (right_eye_x + eye_radius//2, eye_y), 2)
        else:
            pygame.draw.circle(screen, WHITE, (left_eye_x, eye_y), eye_radius)
            pygame.draw.circle(screen, WHITE, (right_eye_x, eye_y), eye_radius)
            pygame.draw.circle(screen, BLACK, (left_eye_x, eye_y), eye_radius // 2)
            pygame.draw.circle(screen, BLACK, (right_eye_x, eye_y), eye_radius // 2)

class PowerMode:
    def __init__(self):
        self.active = False
        self.duration = POWER_MODE_DURATION  # From config
        self.timer = 0

    def activate(self):
        self.active = True
        self.timer = self.duration

    def update(self):
        if self.active:
            self.timer -= 1
            if self.timer <= 0:
                self.active = False

def draw_anniversary_decorations():
    """Draw special anniversary decorations on the screen"""
    # Draw anniversary year in the corners
    year_text = small_font.render(f"{datetime.now().year}", True, YELLOW)
    screen.blit(year_text, (20, 20))
    screen.blit(year_text, (WIDTH - 40, 20))
    
    # Draw anniversary badges
    pygame.draw.circle(screen, YELLOW, (25, HEIGHT - 25), 15, 2)
    pygame.draw.circle(screen, YELLOW, (WIDTH - 25, HEIGHT - 25), 15, 2)
    
    # Draw connection lines (representing network)
    for i in range(20):
        start_pos = (random.randint(0, WIDTH), random.randint(0, 50))
        end_pos = (random.randint(0, WIDTH), random.randint(HEIGHT-50, HEIGHT))
        pygame.draw.line(screen, (50, 50, 100), start_pos, end_pos, 1)

def draw_anniversary_start_screen():
    """Draw special anniversary start screen"""
    screen.fill(BLACK)
    
    # Draw decorative elements
    for i in range(30):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.randint(1, 3)
        pygame.draw.circle(screen, YELLOW, (x, y), size)
    
    # Draw network connection lines
    for i in range(10):
        start_pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        end_pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        pygame.draw.line(screen, (50, 50, 100), start_pos, end_pos, 1)
    
    # Draw title with anniversary styling
    title_text = large_font.render("PAC-IRANCELL", True, YELLOW)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(title_text, title_rect)
    
    # Draw anniversary subtitle
    subtitle = medium_font.render(f"Anniversary Edition - {config['branding']['years_of_service']} Years of Service", True, GOLD)
    subtitle_rect = subtitle.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    screen.blit(subtitle, subtitle_rect)
    
    # Draw Irancell branding
    branding_text_start = font.render(config["branding"]["slogan"], True, LIGHT_BLUE)
    branding_rect_start = branding_text_start.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
    screen.blit(branding_text_start, branding_rect_start)
    
    # Draw instructions
    start_text = font.render("Press any key to start", True, WHITE)
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
    screen.blit(start_text, start_rect)
    
    # Draw anniversary message
    anniversary_msg = small_font.render("Celebrating connectivity, innovation, and service", True, YELLOW)
    anniversary_rect = anniversary_msg.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))
    screen.blit(anniversary_msg, anniversary_rect)
    
    pygame.display.flip()

# ===================== UI AND DECORATIONS =====================

class AnniversaryDecorator:
    """Decorator class for drawing anniversary elements"""
    
    @staticmethod
    def draw_decorations():
        year_text = small_font.render(f"{datetime.now().year}", True, YELLOW)
        screen.blit(year_text, (20, 20))
        screen.blit(year_text, (WIDTH - 40, 20))
        
        pygame.draw.circle(screen, YELLOW, (25, HEIGHT - 25), 15, 2)
        pygame.draw.circle(screen, YELLOW, (WIDTH - 25, HEIGHT - 25), 15, 2)

    @staticmethod
    def draw_start_screen():
        screen.fill(BLACK)
        
        for i in range(30):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            size = random.randint(1, 3)
            pygame.draw.circle(screen, YELLOW, (x, y), size)
        
        for i in range(10):
            start_pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
            end_pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
            pygame.draw.line(screen, (50, 50, 100), start_pos, end_pos, 1)
        
        title_text = large_font.render("PAC-IRANCELL", True, YELLOW)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(title_text, title_rect)
        
        subtitle = medium_font.render(f"Anniversary Edition - {config['branding']['years_of_service']} Years of Service", True, GOLD)
        subtitle_rect = subtitle.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        screen.blit(subtitle, subtitle_rect)
        
        branding_text = font.render(config["branding"]["slogan"], True, LIGHT_BLUE)
        branding_rect = branding_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
        screen.blit(branding_text, branding_rect)
        
        start_text = font.render("Press any key to start", True, WHITE)
        start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
        screen.blit(start_text, start_rect)
        
        pygame.display.flip()


# ===================== LEVEL BUILDER =====================

class LevelBuilder:
    """Builder Pattern for level construction"""
    
    def __init__(self):
        self.game_state = SingletonGameState()

    def build_maze(self):
        """Build maze walls"""
        factory = GameObjectFactory()
        
        walls_data = [
            (0, 0, WIDTH, GRID_SIZE),
            (0, HEIGHT - GRID_SIZE, WIDTH, GRID_SIZE),
            (0, 0, GRID_SIZE, HEIGHT),
            (WIDTH - GRID_SIZE, 0, GRID_SIZE, HEIGHT),
            (GRID_SIZE, GRID_SIZE * 2, GRID_SIZE * 3, GRID_SIZE),
            (GRID_SIZE * 5, GRID_SIZE * 2, GRID_SIZE * 3, GRID_SIZE),
            (GRID_SIZE, GRID_SIZE * 4, GRID_SIZE, GRID_SIZE * 2),
            (GRID_SIZE * 7, GRID_SIZE * 4, GRID_SIZE, GRID_SIZE * 2),
            (GRID_SIZE * 2, GRID_SIZE * 6, GRID_SIZE * 2, GRID_SIZE),
            (GRID_SIZE * 5, GRID_SIZE * 6, GRID_SIZE * 2, GRID_SIZE),
            (GRID_SIZE * 3, GRID_SIZE * 8, GRID_SIZE, GRID_SIZE * 2),
            (GRID_SIZE * 6, GRID_SIZE * 8, GRID_SIZE, GRID_SIZE * 2),
            (GRID_SIZE, GRID_SIZE * 10, GRID_SIZE * 3, GRID_SIZE),
            (GRID_SIZE * 5, GRID_SIZE * 10, GRID_SIZE * 3, GRID_SIZE),
            (GRID_SIZE * 4, GRID_SIZE * 3, GRID_SIZE, GRID_SIZE),
            (GRID_SIZE * 4, GRID_SIZE * 9, GRID_SIZE, GRID_SIZE),
        ]
        
        for x, y, w, h in walls_data:
            self.game_state.walls.append(factory.create_wall(x, y, w, h))
        
        return self

    def build_coins(self):
        """Build coin collectibles"""
        factory = GameObjectFactory()
        
        for row in range(1, GRID_HEIGHT - 1):
            for col in range(1, GRID_WIDTH - 1):
                pos_x, pos_y = col * GRID_SIZE, row * GRID_SIZE
                
                if not self._has_wall(pos_x, pos_y) and random.random() > 0.7:
                    self.game_state.coins.append(factory.create_coin(pos_x, pos_y))
        
        return self

    def build_power_pellets(self):
        """Build power pellets"""
        factory = GameObjectFactory()
        
        positions = [
            (GRID_SIZE * 1, GRID_SIZE * 1),
            (GRID_SIZE * (GRID_WIDTH - 2), GRID_SIZE * 1),
            (GRID_SIZE * 1, GRID_SIZE * (GRID_HEIGHT - 2)),
            (GRID_SIZE * (GRID_WIDTH - 2), GRID_SIZE * (GRID_HEIGHT - 2))
        ]
        
        for x, y in positions:
            self.game_state.power_pellets.append(factory.create_power_pellet(x, y))
        
        return self

    def build_enemies(self, count=4):
        """Build enemies"""
        factory = GameObjectFactory()
        colors = [RED, PINK, CYAN, ORANGE]
        
        positions = [
            (GRID_SIZE * 3, GRID_SIZE * 3),
            (GRID_SIZE * 4, GRID_SIZE * 4),
            (GRID_SIZE * 5, GRID_SIZE * 3),
            (GRID_SIZE * 4, GRID_SIZE * 5)
        ]
        
        for i in range(min(count, len(positions))):
            x, y = positions[i]
            self.game_state.enemies.append(factory.create_enemy(x, y, colors[i]))
        
        return self

    def _has_wall(self, x, y):
        """Check if position has wall"""
        for wall in self.game_state.walls:
            if x < wall.x + wall.width and \
               x + GRID_SIZE > wall.x and \
               y < wall.y + wall.height and \
               y + GRID_SIZE > wall.y:
                return True
        return False

    def build(self):
        """Get built level"""
        return self.game_state


# ===================== GAME CONTROLLER =====================

class GameController:
    """Controller for game logic"""
    
    def __init__(self):
        self.player = Player()
        self.power_mode = PowerMode()
        self.game_state = SingletonGameState()
        self.game_over = False
        self.level_complete = False

    def setup_level(self):
        """Setup a new level"""
        self.game_state.reset()
        builder = LevelBuilder()
        builder.build_maze().build_coins().build_power_pellets().build_enemies()
        self.level_complete = False

    def handle_input(self, keys):
        """Handle player input"""
        if keys[pygame.K_LEFT]:
            self.player.move(Direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            self.player.move(Direction.RIGHT)
        elif keys[pygame.K_UP]:
            self.player.move(Direction.UP)
        elif keys[pygame.K_DOWN]:
            self.player.move(Direction.DOWN)

    def update(self):
        """Update game state"""
        if self.game_over or self.level_complete:
            return
        
        self.player.update()
        self.power_mode.update()
        
        for coin in self.game_state.coins:
            coin.update()
        
        for pellet in self.game_state.power_pellets:
            pellet.update()
        
        for enemy in self.game_state.enemies:
            enemy.update(self.power_mode.active)
        
        self._check_coin_collection()
        self._check_power_pellet_collection()
        self._check_enemy_collision()
        self._check_win_condition()

    def _check_coin_collection(self):
        """Check and handle coin collection"""
        for coin in self.game_state.coins:
            if not coin.collected and \
               self.player.x < coin.x + GRID_SIZE and \
               self.player.x + GRID_SIZE > coin.x and \
               self.player.y < coin.y + GRID_SIZE and \
               self.player.y + GRID_SIZE > coin.y:
                coin.collected = True
                self.player.score += SCORE_PER_COIN

    def _check_power_pellet_collection(self):
        """Check and handle power pellet collection"""
        for pellet in self.game_state.power_pellets:
            if not pellet.collected and \
               self.player.x < pellet.x + GRID_SIZE and \
               self.player.x + GRID_SIZE > pellet.x and \
               self.player.y < pellet.y + GRID_SIZE and \
               self.player.y + GRID_SIZE > pellet.y:
                pellet.collected = True
                self.player.score += SCORE_PER_POWER_PELLET
                self.power_mode.activate()

    def _check_enemy_collision(self):
        """Check and handle enemy collision"""
        for enemy in self.game_state.enemies[:]:
            if self.player.x < enemy.x + GRID_SIZE and \
               self.player.x + GRID_SIZE > enemy.x and \
               self.player.y < enemy.y + GRID_SIZE and \
               self.player.y + GRID_SIZE > enemy.y:
                
                if self.power_mode.active:
                    self.game_state.enemies.remove(enemy)
                    self.player.score += SCORE_PER_ENEMY
                    factory = GameObjectFactory()
                    self.game_state.enemies.append(
                        factory.create_enemy(
                            GRID_SIZE * random.randint(1, GRID_WIDTH - 2),
                            GRID_SIZE * random.randint(1, GRID_HEIGHT - 2),
                            random.choice([RED, PINK, CYAN, ORANGE])
                        )
                    )
                else:
                    self.player.lives -= 1
                    if self.player.lives <= 0:
                        self.game_over = True
                    else:
                        self.player.x = GRID_SIZE
                        self.player.y = GRID_SIZE

    def _check_win_condition(self):
        """Check if level is complete"""
        if all(coin.collected for coin in self.game_state.coins) and \
           all(pellet.collected for pellet in self.game_state.power_pellets):
            self.level_complete = True

    def draw(self):
        """Draw all game objects"""
        screen.fill(BLACK)
        
        AnniversaryDecorator.draw_decorations()
        
        for wall in self.game_state.walls:
            wall.draw()
        
        for coin in self.game_state.coins:
            coin.draw()
        
        for pellet in self.game_state.power_pellets:
            pellet.draw()
        
        for enemy in self.game_state.enemies:
            enemy.draw()
        
        self.player.draw()
        
        self._draw_ui()

    def _draw_ui(self):
        """Draw UI elements"""
        score_text = font.render(f"Score: {self.player.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        lives_text = font.render(f"Lives: {self.player.lives}", True, WHITE)
        screen.blit(lives_text, (WIDTH - 120, 10))
        
        if self.power_mode.active:
            power_text = small_font.render(f"POWER MODE: {self.power_mode.timer // 60}s", True, YELLOW)
            screen.blit(power_text, (WIDTH // 2 - 80, HEIGHT - 70))
        
        title_text = large_font.render("PAC-IRANCELL", True, YELLOW)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT - 40))
        screen.blit(title_text, title_rect)

    def restart(self):
        """Restart the game"""
        self.player = Player()
        self.power_mode = PowerMode()
        self.game_over = False
        self.level_complete = False
        self.setup_level()

    def next_level(self):
        """Go to next level with increased difficulty"""
        self.player.lives += 1
        self.player.x = GRID_SIZE
        self.player.y = GRID_SIZE
        self.power_mode = PowerMode()
        self.setup_level()
        
        if len(self.game_state.enemies) < 5:
            factory = GameObjectFactory()
            self.game_state.enemies.append(
                factory.create_enemy(
                    GRID_SIZE * 2, GRID_SIZE * 7, PURPLE
                )
            )


# ===================== MAIN GAME LOOP =====================

def main():
    running = True
    show_start_screen = True
    game_controller = GameController()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if show_start_screen:
                if event.type == pygame.KEYDOWN:
                    show_start_screen = False
                    game_controller.setup_level()
        
        if show_start_screen:
            AnniversaryDecorator.draw_start_screen()
            clock.tick(GAME_FPS)
            continue
        
        keys = pygame.key.get_pressed()
        game_controller.handle_input(keys)
        
        game_controller.update()
        game_controller.draw()
        
        if game_controller.game_over:
            game_over_text = font.render("GAME OVER! Press R to restart", True, RED)
            screen.blit(game_over_text, (WIDTH // 2 - 180, HEIGHT // 2))
            
            if keys[pygame.K_r]:
                game_controller.restart()
        
        if game_controller.level_complete:
            win_text = font.render("LEVEL COMPLETE! Press N for next level", True, YELLOW)
            screen.blit(win_text, (WIDTH // 2 - 200, HEIGHT // 2))
            
            if keys[pygame.K_n]:
                game_controller.next_level()
        
        pygame.display.flip()
        clock.tick(GAME_FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
