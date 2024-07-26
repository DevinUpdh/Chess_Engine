import pygame as p
import Chess_engine

WIDTH =  HEIGHT = 512
DIMENSION = 8  # 8x8 chess board
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS=15 # for animation
IMAGES = {}

def loadImages():
    pieces = ["wp", "wR", "wB", "wQ", "wK", "wN", "bp", "bR", "bB", "bQ", "bK", "bN"]
    for piece in pieces:
        # scaled the images according to the board size
        IMAGES[piece] = p.transform.scale(p.image.load(f"images/+{piece}.png"), (SQ_SIZE, SQ_SIZE))

