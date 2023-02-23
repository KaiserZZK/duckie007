# comment out import for test mode
from rrt import rrt

XDIM = 640
YDIM = 480
w = 100
w2 = 25
h = 150
h2 = 60
X0 = XDIM/5
Y0 = YDIM/3
X1 = 4*XDIM/5
Y1 = 2*YDIM/3

CENTER_SIZE = 20
Obs = {}
# Obs[0] = [(XDIM/2, YDIM/7),(XDIM/2, 6*YDIM/7)]
# Obs[0] = [(XDIM/6, YDIM/2),(5*XDIM/6, YDIM/2)]
# Obs[0] = [(50,50), (200,100)]


Obs[0] = [(XDIM/2, YDIM/7),(XDIM/2, YDIM/3)]
Obs[1] = [(XDIM/2, 6*YDIM/7),(XDIM/2, 2*YDIM/3)]
Obs[2] = [(XDIM/2 - CENTER_SIZE, YDIM/2 - CENTER_SIZE),(XDIM/2 + CENTER_SIZE, YDIM/2 + CENTER_SIZE)]
Obs[3] = [(XDIM/6, YDIM/2),(XDIM/3, YDIM/2)]
Obs[4] = [(5*XDIM/6, YDIM/2),(2*XDIM/3, YDIM/2)]

# """

weight = 5.0
print(Obs.values())
point0 = (325, 160) # supposed to collide with Obs[0]
# point = (500, 238) # supposed to collide with Obs[4]
# point1 =
xCoord, yCoord = point0[0], point0[1]

for obstacle in Obs.values():
    pointX1, pointX2 = obstacle[1][0], obstacle[0][0]
    pointY1, pointY2 = obstacle[1][1], obstacle[0][1]
    xSlope = pointX1 - pointX2
    ySlope = pointY1 - pointY2
    print(obstacle, xSlope, ySlope)
    if abs(xSlope) > abs(ySlope):
        print(obstacle, xSlope, ySlope)
        print('horizontal type')
        if min(pointX1, pointX2) <= xCoord <= max(pointX1, pointX2):
            yOnLine = pointY1 + (xCoord - pointX1) * (ySlope / xSlope)
            if yOnLine - weight < yCoord < yOnLine + weight:
                collideFree = False
                print('collision!')
                continue
    else:
        print(obstacle, xSlope, ySlope)
        print('vertical type')
        if min(pointY1, pointY2) <= yCoord <= max(pointY1, pointY2):
            xOnLine = pointX1 + (yCoord - pointY1) * (xSlope / ySlope)
            if xOnLine - weight < xCoord < xOnLine + weight:
                collideFree = False
                print('collision!')
                continue
# """

XY_START = (X0+w/2,Y0+3*h/4) # Start in the trap
# XY_START = (1,1)
XY_GOAL = (4*XDIM/5,5*YDIM/6)


XY_GOAL = (X1-w/2,Y1-3*h/4)
print(XY_START, XY_GOAL)

game = rrt(Obs, XY_START, XY_GOAL, XDIM, YDIM)
game.runGame()