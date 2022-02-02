from queue import PriorityQueue
import pygame
import math

# In Queue, the oldest element is dequeued first. While, in Priority Queue, element based on highest priority is dequeued.
pygame.display.set_caption('Google Maps Algorithm Visualiser (Dijkstras Algorithm)')
WIDTH = 1000
LENGTH = WIDTH
WINDOW = pygame.display.set_mode((WIDTH,LENGTH))