- This file is just meant to be used as a guide for myself to plan this project
- it will be left in my repository just in case others wanted to have a look as it :)

before even trying to implement the algorithm, we need a grid:
- This can be made using HTML/CSS or Pygame. To learn a new library and for a better user experience, i will use the latter
- since the algorithm is dependant on the grid, we leave that task to later



BREAKING DOWN PROBLEM (do each step first before moving onto other):
- make node class
- build grid
- allow grid to make start node
- allow grid to make end node 
- ensure start node and end node are different colours
- ensure start node != end node
- allow 'walls'
- Develop Dijikstra's Algorithm
- allow the nodes to find each other using the algorithm
- create error for no solution




To create a Node, we will make a node class so our model will follow OOP

NODE CLASS

INITIALISERS:
- white colour as default
- row
- column
- width
- total rows 
- x coordinate
- y coordinate



METHODS:
- start node colour
- end node colour
- wall node colour
- reset all the nodes to white default colour
- for all of the above make a method to set the colour but also one that returns the colour


QUESTIONS TO ASK MYSELF/RESEARCH:
- research whether feature tests can be implemented for Pygame







