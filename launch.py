#!/usr/bin/env python3

"""
Irancell Anniversary Pac-Man Game Launcher
"""

import pygame
import sys
import os

def main():
    print("Starting Irancell Anniversary Pac-Man Game...")
    print("Loading game assets...")
    
    # Change to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Import and run the main game
    try:
        import main
    except ImportError as e:
        print(f"Error importing main game module: {e}")
        print("Make sure main.py exists in this directory.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()