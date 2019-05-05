from enum import Enum
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

for item in Direction:
    print(item)

print(Direction[0])