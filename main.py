from queue import PriorityQueue
import pygame
import math
from node import Node, ORANGE, BLUE, TURQUOISE, BLACK, WHITE


DARK_GREY = (159,159,159)


# In Queue, the oldest element is dequeued first. While, in Priority Queue, element based on highest priority is dequeued.
pygame.display.set_caption('Google Maps Algorithm Visualiser (Dijkstras Algorithm)')
WIDTH = 1000
HEIGHT = WIDTH
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))


def make_the_grid(rows,width):
  # this allows us to add a node to each square
  grid = []
  node_size = width // rows
  for i in range(rows):   
    grid.append([])   # in each row we want to add an empty array in the grid array
    for j in range(rows):
      node = Node(i, j, node_size, rows)
      grid[i].append(node) #in the empty array we just created we want to add our node instance

  return grid  #we return our grid that now has a node instance

def draw_the_grid(rows, width):
  #this is different to make the grid because this physically draws the lines. The function make_the_grid is 'invisiable' and is purely there for us to make node instances
  node_size = width // rows
  for i in range(rows):
    pygame.draw.line(WINDOW, DARK_GREY, (0, i * node_size), (width, i * node_size) )
    for j in range(rows):
      pygame.draw.line(WINDOW, DARK_GREY, (j * node_size, 0), (j * node_size, width) )


