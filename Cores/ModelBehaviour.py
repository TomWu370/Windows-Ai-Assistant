# play animation, and detect clicks or other events, then play other animations

class TextToModel:
    def __init__(self):
        self.animation = {} # read and load animations, then store in dictionary

    def play_animation(self, animation_name, copy=False):
        self.animation[animation_name].play_animation() # arg position
        # may play the same animation multiple times if copy is true

    def get_animation(self):
        pass  # return animation name