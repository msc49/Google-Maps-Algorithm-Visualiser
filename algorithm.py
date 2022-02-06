from collections import deque

from main import reconstruct_path

def dijkstras(draw, grid, start, end):
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
          neighbor.makeOpen()
    draw()
    if current != start:
     current.makeClosed()

  return False

