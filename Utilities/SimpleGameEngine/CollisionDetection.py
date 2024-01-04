

def isCollide(obj1, obj2):
    if obj1.x < obj2.x + obj2.width and obj1.x + obj1.width > obj2.x \
            and obj1.y < obj2.y + obj2.height and obj1.y + obj1.height > obj2.y:
        return True
    else:
        return False

def isCollide2(obj1, obj2):
    pass
    # for round hitboxes