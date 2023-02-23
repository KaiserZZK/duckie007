# COMS BC 3997 - F22
# Grid and Random Search Algorithms

In this project, you will implement the random search algorithm RRT to help Pacman find paths in a maze.


## RRT Algorithm (8 points + 1 bonus)

<img src="https://upload.wikimedia.org/wikipedia/en/thumb/f/f5/RRT_graph1.png/300px-RRT_graph1.png">

**Files you'll edit (and thus submit to Gradescope for Autograding):**

`util.py` 	Where all of your RRT helper functions will go.

In this section, you'll be implementing the RRT robotic planning algorithm. All code can be found in the `rrt` folder. Your goal will be to implement several functions in `util.py` to successfully find a path from a source point to the goal using RRT. This path should avoid collisions with obstacles.

**NOTE: You need to install pygame for this to run: `pip3 install pygame`**

Functions that should be filled in for full credit are:
* `winCondition`    - 1 point
* `nearestNode`     - 1 point
* `getNewPoint`     - 1 point
* `extend`          - 2 points
* `isCollisionFree` - 3 points

To test your implementation, there are three maps that increase in difficulty:
* `python3 runNoObs.py` -- no obstacles (you can test your other functions with this before implementing `isCollisionFree` -- just make sure `isCollisionFree` returns True always -- should take 500ish iterations)
* `python3 runBasicObs.py` -- some basic obstacles that you can test with that will still finish quickly (again around 500ish iterations)
* `python3 runBugtrap.py` -- start in a bugtrap (should take a couple thousand iterations)
* `python3 runDoubleBugtrap.py` -- start and end in a bugtrap (a very hard problem for RRT, this could take some time)

Note: Sometimes the graphics will make it appear that a vaild solution is just barely crossing the tip of a diagonal line and that is ok!

Note2: By construction our tests will never take a step that is bigger than an obstacle so you do not need to worry about collisions in the middle of your extensions. [You're welcome :-)](https://www.youtube.com/watch?v=79DijItQXMM)
