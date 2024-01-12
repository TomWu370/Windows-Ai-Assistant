


class rectangleHitBox:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width  = width
        self.height = height

class circleHitBox:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

class capsuleHitBox:
    def __init__(self, x, y, radius, length):
        self.x = x
        self.y = y
        self.radius = radius
        self.length = length