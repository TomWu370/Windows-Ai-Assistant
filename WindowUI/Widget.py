# use tkintret to create a window, frameless
# use pyqt
# command to send to front or back, for use when command is realised
import tkinter as tk
from datetime import time
from time import sleep
from tkinter import LEFT, RIGHT, X

from PIL import Image, ImageTk, ImageSequence

root = tk.Tk()
root.title("Displaing Gif")

file = "framework.gif"
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
        self.label = tk.Label(self.root, image=self.image, border=0, highlightthickness=0)
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
def move_app(e):
  root.geometry(f'+{e.x_root}+{e.y_root}')

def quitter(e):
  root.quit() # destroys all children, destroy only kills current widget
  #root.destroy()

# Create Fake Title Bar
# title_bar = tk.Frame(root, bg="darkgreen", relief="raised", bd=0)
# title_bar.pack(expand=1, fill=X)
# # Bind the titlebar
# title_bar.bind("<B1-Motion>", move_app)


# Create title text
# title_label = tk.Label(title_bar, text="  My Awesome App!!", bg="darkgreen", fg="white")
# title_label.pack(side=LEFT, pady=4)

# Create close button on titlebar
# close_label = tk.Label(title_bar, text="  X  ", bg="darkgreen", fg="white", relief="sunken", bd=0)
# close_label.pack(side=RIGHT, pady=4)
# close_label.bind("<Button-1>", quitter)
#root.overrideredirect(True)
root.geometry("+500+500")
root.config(bg = '#00ff00')

#Create a transparent window
#root.wm_attributes('-transparentcolor','#00ff00')
root.attributes('-topmost', True)

root.lift()

#root.wm_attributes('-transparentcolor', 'white')
#root.config(bg='#ffffff')
AnimatedGif(root, file)

# gif_label = tk.Label(root, image='', bg='#3a4e4a')
# gif_label.pack()
# canvas = tk.Canvas(root, width=300, height=200, bg='#ffffff')
# canvas.pack()
# canvas.create_image(0, 0, anchor=tk.NW, image=gif)
# canvas.photo = gif
# animation(current_frame=0)



root.mainloop()
