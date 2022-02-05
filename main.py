from queue import PriorityQueue
from turtle import onclick
from unittest import makeSuite
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

def draw_the_grid(window, rows, width):
  '''
  This essentially creates a grid where i represents rows and j will be columns
  note i = j because we number of rows = columns
  we then use the pygame draw.line function to make each individual square of the grid
  '''
  #this is different to make the grid because this physically draws the lines. The function make_the_grid is 'invisiable' and is purely there for us to make node instances
  node_size = width // rows
  for i in range(rows):
    pygame.draw.line(WINDOW, DARK_GREY, (0, i * node_size), (width, i * node_size) )
    for j in range(rows):
      pygame.draw.line(WINDOW, DARK_GREY, (j * node_size, 0), (j * node_size, width) )


def draw(window, grid, rows, width):
  window.fill(WHITE)
  for row in grid:
    for node in row:
      node.draw_node(window)

  draw_the_grid(window, rows, width)
  pygame.display.update()


def minimum_distance(x1,y1,x2,y2):
  return abs(x1-y2) + abs(y1-y2)

def clicked_position(position, rows, width):
  '''
  we will use this function to calculate where in the grid, the user clicked his mouse on
  '''
  node_size = width // rows
  y, x = position

  row = y // position
  column = x // position

  return row, column


