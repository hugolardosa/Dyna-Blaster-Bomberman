import enum

class Direction(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    
class PowerUps(enum.Enum):
    NextLevel = 0
    Wallpass = 1
    FireUp = 2
    FireDown = 3
    SpeedUp = 4
    SpeedDown = 5
    
class PlayerState(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    IDLE = 5