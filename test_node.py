import pytest
from node import Node, ORANGE, BLUE, TURQUOISE, BLACK, WHITE


def test_default_node_colour():
  node = Node(1, 1, 14, 50)
  assert node.colour == WHITE

def test_initialised_with_no_neighbours():
    node = Node(1, 1, 14, 50)
    assert node.neighbors == []


def test_wall_can_be_made():
  node = Node(1, 1, 14, 50)
  node.make_wall()
  assert node.colour == BLACK

def test_get_node_position():
    node = Node(1, 1, 14, 50)
    assert node.get_node_position() == (1,1)
