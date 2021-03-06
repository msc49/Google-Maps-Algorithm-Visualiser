
from queue import PriorityQueue
import pygame
import math
from node import Node, ORANGE, BLUE, TURQUOISE, BLACK, WHITE
from collections import deque


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

  row = y // node_size
  column = x // node_size

  return row, column


def reconstruct_path(came_from, current, draw):
  while current in came_from:
    current = came_from[current]
    current.make_path()
    draw()

def dijkstras_algo(draw, grid, start, end):
  came_from = {}
  visited = []
  queue = deque()   #deque is a container datatype that allows you to append and pop from both sides of the list.
  # we are using this over a standard list because of its swiftness 

  queue.append(start)
  visited.append(start)

  while len(queue) > 0:
    current = queue.popleft()
    if current == end:
      reconstruct_path(came_from,end,draw)
      end.make_end_node()
      return True

    for neighbor in current.neighbors:
      if neighbor not in visited:
          visited.append(neighbor)
          came_from[neighbor] = current
          queue.append(neighbor)
          neighbor.make_open_node()
    draw()
    if current != start:
     current.make_closed_node()

  return False



def main(window, width):
  ROWS = 50
  grid = make_the_grid(ROWS,width)

  start = None
  end = None

  run = True

  while run:
    draw(window, grid, ROWS, width)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

      
      if pygame.mouse.get_pressed()[0]: #LEFT CLICK
        position = pygame.mouse.get_pos()
        row, column = clicked_position(position, ROWS, width)
        node = grid[row][column]
        if not start and node != end:
          start = node
          start.make_start_node()

        elif not end and node != start:
          end = node
          end.make_end_node()

        elif node != end and node != start:
          node.make_wall()

      elif pygame.mouse.get_pressed()[2]: # RIGHT CLICK
        position = pygame.mouse.get_pos()
        row, col = clicked_position(position, ROWS, width)
        node = grid[row][col]
        node.reset()
        if node == start:
          start = None
        elif node == end:
          end = None
      

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and start and end:
          for row in grid:
            for node in row:
              node.updating_neighbors(grid)

          dijkstras_algo(lambda: draw(window, grid, ROWS, width), grid, start, end)

        if event.key == pygame.K_c:
          start = None
          end = None
          grid = make_the_grid(ROWS, width)

  pygame.quit()




main(WINDOW, WIDTH)


