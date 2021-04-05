import math

xDistance = input("what is the X distance?\n")
yDistance = input("what is the Y distance?\n")
distanceToTarget = math.sqrt(int(xDistance) ** 2 + int(yDistance) ** 2)
print (distanceToTarget)
angleToTarget = (math.degrees(math.atan(int(yDistance) / int(xDistance)))
print (angleToTarget)