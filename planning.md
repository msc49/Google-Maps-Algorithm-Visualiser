- This file is just meant to be used as a guide for myself to plan this project
- it will be left in my repository just in case others wanted to have a look as it :)

before even trying to implement the algorithm, we need a grid:
- This can be made using HTML/CSS or Pygame. Although Pygame would be a better user experience, i will do it in the former to brush up on my HTML/CSS skills

The grid dimensions are irrelevant for now. The grid must be able to:
- Create a starting node
- Create an ending node
- (we will also add walls where the algorithm is not allowed to touch. These will also be nodes but for now we ignore this)

To create a Node, we will make a node class so our model will follow OOP

NODE CLASS

INITIALISERS:



METHODS:
- shortest_path (this is where we apply Dijikstra's Algorithm)
- speed (this will decide how fast we want our algorithm to visualise i.e. slow, medium or fast)





BREAKING DOWN PROBLEM (do each step first before moving onto other):
- build grid
- allow grid to make node instances whenever clicked
- expand upon above task by differentiating the starting node
- allow nodes to 'find' each other, using Dijikstra's Algorithm
- once that is completed, create wall nodes where the algorithm is not allowed to use as a route


Once all of those are completed:
- make it more visually pleasing

