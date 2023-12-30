# use tkintret to create a window, frameless
# use pyqt
# command to send to front or back, for use when command is realised
import tkinter as tk
from tkinter import LEFT, RIGHT, X

from PIL import Image

root = tk.Tk()
root.title("Displaing Gif")

file = "framework.gif"
info = Image.open(file)

frames = info.n_frames  # number of frames

photoimage_objects = []
for i in range(frames):
    obj = tk.PhotoImage(file=file, format=f"gif -index {i}")
    photoimage_objects.append(obj)


def animation(current_frame=0):
    global loop
    image = photoimage_objects[current_frame]

    gif_label.configure(image=image)
    current_frame = current_frame + 1

    if current_frame == frames:
        current_frame = 0

    loop = root.after(50, lambda: animation(current_frame))


def stop_animation():
    root.after_cancel(loop)
def move_app(e):
  root.geometry(f'+{e.x_root}+{e.y_root}')

def quitter(e):
  root.quit()
  #root.destroy()

# Create Fake Title Bar
title_bar = tk.Frame(root, bg="darkgreen", relief="raised", bd=0)
title_bar.pack(expand=1, fill=X)
# Bind the titlebar
title_bar.bind("<B1-Motion>", move_app)


# Create title text
title_label = tk.Label(title_bar, text="  My Awesome App!!", bg="darkgreen", fg="white")
title_label.pack(side=LEFT, pady=4)

# Create close button on titlebar
close_label = tk.Label(title_bar, text="  X  ", bg="darkgreen", fg="white", relief="sunken", bd=0)
close_label.pack(side=RIGHT, pady=4)
close_label.bind("<Button-1>", quitter)
root.overrideredirect(True)
root.geometry("+500+500")
root.wm_attributes('-transparentcolor', 'white')
root.config(bg='#f0f0f0')


gif_label = tk.Label(root, image="")
gif_label.pack()

start = tk.Button(root, text="Start", command=lambda: animation(current_frame=0))

animation(current_frame=0)
start.pack()

stop = tk.Button(root, text="Stop", command=stop_animation)
stop.pack()


root.mainloop()
