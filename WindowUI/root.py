import time
import tkinter
import tkinter.ttk
import tkinterDnD
from GifPlayer2 import AnimatedGifPlayer, ImagePosition

root = tkinterDnD.Tk()
root.config(bg='#ffffff')
root.wm_attributes('-transparentcolor', 'white')

#root.wm_attributes('-toolwindow', True)
#root.withdraw()
root.title("hi")
#root.overrideredirect(True)

gif = AnimatedGifPlayer("snoop.gif", root, ImagePosition(500, 100))

gif.initialise_player(500)
print("hi")

gif2 = AnimatedGifPlayer("cat.gif", root, ImagePosition(800, 100))
gif2.initialise_player(300)
#gif.change(400)
#gif2.stop_animation()
#gif.stop_animation()

def drop(event):
    # This function is called, when stuff is dropped into a widget
    gif3 = AnimatedGifPlayer(event.data, root, ImagePosition(1000, 100))
    gif3.initialise_player(100)

def drag_command(event):
    # This function is called at the start of the drag,
    # it returns the drag type, the content type, and the actual content
    return (tkinterDnD.COPY, "DND_Text", "Some nice dropped text!")

label_1 = tkinter.Label(root, textvar="s", relief="solid")
label_1.pack(fill="both", expand=True, padx=10, pady=10)

label_1.register_drop_target("*")
label_1.bind("<<Drop>>", drop)

label_1.register_drag_source("*")
label_1.bind("<<DragInitCmd>>", drag_command)


root.mainloop()