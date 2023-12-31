import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
class AnimatedGif:
    def __init__(self, root, src=''):
        self.root = root
        # Load Frames
        self.image = Image.open(src)
        self.frames = []
        self.duration = []
        for frame in ImageSequence.Iterator(self.image):
                self.duration.append(frame.info['duration'])
                self.frames.append(ImageTk.PhotoImage(frame))
        self.counter = 0
        self.image = self.frames[self.counter]
        # Create Label
        self.label = tk.Label(self.root, image=self.image)
        self.label.pack()
        # Start Animation
        self.__step_frame()
    def __step_frame(self):
        # Update Frame
        self.label.config(image=self.frames[self.counter])
        self.image = self.frames[self.counter]
        # Loop Counter
        self.counter += 1
        if self.counter >= len(self.frames):
            self.counter = 0
        # Queue Frame Update
        self.root.after(self.duration[self.counter], lambda: self.__step_frame())
    def pack(self, **kwargs):
        self.label.pack(**kwargs)
    def grid(self, **kwargs):
        self.label.grid(**kwargs)
    def getLabel(self):
        return self.label
if __name__ in '__main__':
    root = tk.Tk()
    gif = AnimatedGif(root, r'..\..\WindowUI\022Fl.gif')
    label = gif.getLabel()
    label.pack()
    root.mainloop()