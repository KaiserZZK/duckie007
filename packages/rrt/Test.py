import random
from math import sqrt, cos, sin, atan2

class Test:
    def extend(self, current_node, new_point, delta):

        currentX, currentY = 0, 0

        if current_node != None:
            currentX, currentY = current_node[0], current_node[1]

        xDirection, yDirection = new_point[0] - currentX, new_point[1] - currentY

        # reach = random.random() * delta
        print('reach is', delta)
        dist = self.getDist(current_node, new_point)

        xDelta = delta * xDirection / dist
        yDelta = delta * yDirection / dist

        newX = currentX + xDelta
        newY = currentY + yDelta

        extended = (newX, newY)

        print(self.getDist(current_node, extended) <= delta)
        print('distance is', self.getDist(current_node, extended))


        return extended

    def getDist(self, this_node, other_node):

        thisX, thisY = 0, 0

        if this_node != None:
            thisX, thisY = this_node[0], this_node[1]

        xDist, yDist = thisX - other_node[0], thisY - other_node[1]
        dist = sqrt(xDist ** 2 + yDist ** 2)

        return dist

from Test import Test
t = Test()
print(t.extend((1,1), (5,5), 5.0))

print(random.random()*5)