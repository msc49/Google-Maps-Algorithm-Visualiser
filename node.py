from queue import PriorityQueue
import pygame
import math



# lets add some constants which will represent the colours for our nodes using RGB colours
ORANGE = (255, 165 ,0) # starting node
BLUE = (0, 255, 0) # ending node
BLACK = (0, 0, 0) # wall node
TURQUOISE = (64, 224, 208) # path finder
WHITE = (255, 255, 255) # default nodes


LIGHT_GREEN = (36, 255, 72) # if the node is open
RED = (255,0,0) # node closed

class Node:


  def __init__(self, row, column, width, total_rows):
    self.width = width
    self.total_rows = total_rows
    self.row = row
    self.column = column
    # we now need an x co-ordinate and y co-ordinate
    # this is because wont know how big each node is if we just used the row and column
    self.x = row * width
    self.y = column * width
    self.neighbors = [] #here we will add other nodes that will be above/down/left/right to our node
    self.colour = WHITE

  
  def reset(self):
    self.colour = WHITE

  def make_wall(self):
    self.colour = BLACK
  
  def make_start_node(self):
    self.colour = ORANGE

  def make_end_node(self):
    self.colour = BLUE

  def make_open_node(self):
    self.colour = LIGHT_GREEN

  def make_closed_node(self):
    self.colour = RED

  def make_path(self):
    self.colour = TURQUOISE

  def is_wall(self):
    return self.colour == BLACK

  def is_start_node(self):
    return self.colour == ORANGE

  def is_end_node(self):
    return self.colour == BLUE

  def is_open_node(self):
    return self.colour == LIGHT_GREEN

  def is_closed_node(self):
    return self.colour == RED

  def get_node_position(self):
    return self.row, self.column

  def draw_node(self, window):
    pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.width))

  def updating_neighbors(self,grid):
    self.neighbors  = []

    if self.row < self.total_rows - 1 and not grid[self.row + 1][self.column].is_wall(): #checks neighbor below
      self.neighbors.append(grid[self.row + 1][self.column])

    if self.row > 0 and not grid[self.row - 1][self.column].is_wall():  #checks neighbor above
      self.neighbors.append(grid[self.row + 1][self.column])

    if self.column < self.total_rows - 1 and not grid[self.row][self.column + 1].is_wall(): # neighbor to right
      self.neighbors.append(grid[self.row][self.column + 1])

    if self.column > 0 and not grid[self.row][self.column - 1].is_wall(): # left neighbor 
      self.neighbors.append(grid[self.row][self.column - 1])





