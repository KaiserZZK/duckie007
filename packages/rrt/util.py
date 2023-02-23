import random
from math import sqrt, cos, sin, atan2


class Util:
    ########################################
    #   Mandatory functions for the rrt    #
    ########################################

    # Tests if the new_node is close enough to the goal to consider it a goal
    def winCondition(self, new_node, goal_node, WIN_RADIUS):
        """
        new_node - newly generated node we are checking
        goal_node - goal node
        WIN_RADIUS - constant representing how close we have to be to the goal to
            consider the new_node a 'win'
        """
        won = False
        if self.getDist(new_node, goal_node) < WIN_RADIUS:
            won = True

        return won
        # Find the nearest node in our list of nodes that is closest to the new_node

    # Hint: If your solution appears to be drawing squiggles instead of the fractal like pattern
    #       of striaght lines you are probably extending from the last point not the closest point!
    def nearestNode(self, nodes, new_node):
        """
        nodes - a list of nodes in the RRT
        new_node - a node generated from getNewPoint
        """

        dist = -1
        minNode = None

        for node in nodes:
            currentDist = self.getDist(node, new_node)

            if dist == -1:
                dist = currentDist
                minNode = node
            elif currentDist < dist:
                dist = currentDist
                minNode = node

        return minNode

    # Find a new point in space to move towards uniformally randomly but with
    # probability 0.05, sample the goal. This promotes movement to the goal.
    # For the autograder to work you MUST use the already imported
    # random.random() as your random number generator.
    def getNewPoint(self, XDIM, YDIM, XY_GOAL):
        """
        XDIM - constant representing the width of the game aka grid of (0,XDIM)
        YDIM - constant representing the height of the game aka grid of (0,YDIM)
        XY_GOAL - node (tuple of integers) representing the location of the goal
        """

        if random.random() * 100 <= 5:
            return XY_GOAL
        else:
            newX, newY = random.random() * XDIM, random.random() * YDIM
            newNode = (newX, newY)
            return newNode

    # Extend (by at most distance delta) in the direction of the new_point and place
    # a new node there
    def extend(self, current_node, new_point, delta):
        """
        current_node - node from which we extend
        new_point - point in space which we are extending toward
        delta - maximum distance we extend by
        """

        # currentX, currentY = 0, 0
        #
        # if current_node != None:
        currentX, currentY = current_node[0], current_node[1]
        xDirection, yDirection = new_point[0] - currentX, new_point[1] - currentY
        dist = self.getDist(current_node, new_point)

        reach = delta if dist >= delta else dist

        '''
        Why this implementation:
        delta = 5.0 is usually too "insensitive" and most of the times it just "grazes" the goal 
        
        seems to be always working, but 2 issues:
        - usually takes more than 500 iterations (900-1200)
        - not recognized by Autograder... although in theory it should...
        '''

        xDelta, yDelta = xDirection * reach / dist, yDirection * reach / dist
        newX, newY = currentX + xDelta, currentY + yDelta

        extended = (newX, newY)

        return extended

    # iterate throught the obstacles and check that our point is not in any of them
    def isCollisionFree(self, obstacles, point, obs_line_width):
        """
        obstacles - a dictionary with multiple entries, where each entry is a list of
            points which define line segments of with obs_line_width
        point - the location in space that we are checking is not in the obstacles
        obs_line_width - the length of the line segments that define each obstacle's
            boundary
        """

        ''' understanding the architecture and data types
        # in rrt.py
        def __init__(self, obstacles, start_node, goal_node, XDIM = 640, YDIM = 480, DELTA = 5.0, MAX_ITER = 100000, WIN_RADIUS = 0.25, LINE_WIDTH = 10, TEST_MODE = 0):
        xy = u.getNewPoint(self.XDIM,self.YDIM,self.goal_node)
        u.isCollisionFree(self.obstacles,newnode,self.LINE_WIDTH):  # only checking whether a sampled new point is collision free
        LINE_WIDTH = 10
        newnode is a tuple of coordinates
        
        # in runBasicObs.py
        game = rrt(Obs, XY_START, XY_GOAL, XDIM, YDIM)
        Obs = {}    # a dictionary
        Obs[0] = [(XDIM/2, YDIM/7),(XDIM/2, YDIM/3)]    # a list of tuples of POINTS that constitute obstacle LINES
        '''

        # collideFree = True

        xCoord, yCoord = point[0], point[1]
        weight = obs_line_width / 2

        for obstacleItem in obstacles.values():
            for i in range(len(obstacleItem)-1):
                obstacle = (obstacleItem[i], obstacleItem[i+1])
                pointX1, pointX2 = obstacle[1][0], obstacle[0][0]
                pointY1, pointY2 = obstacle[1][1], obstacle[0][1]
                xSlope, ySlope = pointX1 - pointX2, pointY1 - pointY2
                print(obstacle, xSlope, ySlope)

                if abs(xSlope) > abs(ySlope):
                    # print('horizontal type')
                    if min(pointX1, pointX2) <= xCoord <= max(pointX1, pointX2):
                        yOnLine = pointY1 + (xCoord - pointX1) * (ySlope / xSlope)
                        if yOnLine - weight <= yCoord <= yOnLine + weight:
                            return False
                            # collideFree = False
                            # print('collision!')
                            # break
                else:
                    # print('vertical type')
                    if min(pointY1, pointY2) <= yCoord <= max(pointY1, pointY2):
                        xOnLine = pointX1 + (yCoord - pointY1) * (xSlope / ySlope)
                        if xOnLine - weight <= xCoord <= xOnLine + weight:
                            return False
                            # collideFree = False
                            # print('collision!')
                            # break

        return True

    ################################################
    #  Any other helper functions you need go here #
    ################################################

    def getDist(self, this_node, other_node):

        thisX, thisY = 0, 0

        if this_node != None:
            thisX, thisY = this_node[0], this_node[1]

        xDist, yDist = thisX - other_node[0], thisY - other_node[1]
        dist = sqrt(xDist ** 2 + yDist ** 2)

        return dist