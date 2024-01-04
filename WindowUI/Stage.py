# this script is used for setting the same for different GifPlayer objects
# these GifPlayer objects are also objects inside a tkinter canvas
# and stage refers to that canvas, it will house all the given GifPlayer objects
# there may be different stages at the same time, but logic for 1 stage will only apply to that stage
# for example you could have a stage with meowrio game playing, and another with a gif of a cat idling
# essentially never use GifPlayer alone, always use it inside a stage

class Stage:
    # you may inherit this class to create your own stage, ie another class called meowrio
    def __init__(self, player, objects, gravity, stage_effects):
        self.player = player # limitation, only 1 player per stage
        self.objects = objects
        self.gravity = gravity
        self.stage_effects = stage_effects

        # for each object, apply gravity, when apply gravity, check if grounded
        # when wasd or arrow key is pressed depending on bindings
        # apply coordinate shifting to all objects in the stage, side scroll
        # but implement dragging, i.e. unless you're at a certain length to the side, camera will not move
        # when this is the case, only move character, and not the stage
        # when you reach the edge of the stage, then move the stage, see 2d game tutorials for this

        # GifPlayer object will have an hitbox associated with it, therefore it won't be canvas.move, but rather
        # stage.move, which will invoke canvas.move inside GifPlayer which will move both object and hitbox
        # i guess also add bodies with hitbox, without hitbox, and bodies with hitbox but not affected by stage_effects
        # the whole stage, as the name indicates, once object are out of view, they are not processed
        # camera system
        # collision detection
        # 3 main object types
        # stage effects, gravity, etc
        # persistence of world out of view, can be heavily borrowed from pygame maps
        # try a list of objects, with their coordinates, x,y, at which they start or end
        # when at start coordinate for atleast 1, spawn in object
        # may use quadmap for enironment that are not interactable objects, only for footings