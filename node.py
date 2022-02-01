from queue import PriorityQueue
import pygame
import math


# lets add some constants which will represent the colours for our nodes using RGB colours
ORANGE = (255, 165 ,0) # starting node
BLUE = (0, 255, 0) # ending node
BLACK = (0, 0, 0) # wall node
TURQUOISE = (64, 224, 208) # path finder
WHITE = (255, 255, 255) # default nodes

class Node:


  def __init__(self, row, column, width, total_rows):
    self.width = width
    self.total_rows = total_rows
    self.row = row
    self.column = column
    # we now need an x co-ordinate and y co-ordinate
    self.x = row * width
    self.y = column * width
    self.neighbors = [] #here we will add other nodes that will be above/down/left/right to our node
    self.colour = WHITE




