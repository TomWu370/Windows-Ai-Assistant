from CppSource import collision

def isCollide(obj1, obj2):
    if obj1.x < obj2.x + obj2.width and obj1.x + obj1.width > obj2.x \
            and obj1.y < obj2.y + obj2.height and obj1.y + obj1.height > obj2.y:
        return True
    else:
        return False

def isCollide2(obj1, obj2):
    pass
    # for capsule hitboxes, essentially check for collision between 2 circles and 1 rectangles
    # https://wickedengine.net/2020/04/26/capsule-collision-detection/
    # or more efficiently, find closest point then calculate distance between closest closest circle and other hitbox



if __name__ == "__main__":
    class Box:
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
    obj1 = Box(0, 0, 10, 10)
    obj2 = Box(10, 10, 10, 10)
    print(collision.collide(obj1, obj2))