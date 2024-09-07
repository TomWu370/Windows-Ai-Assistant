import time
import tkinter
from GifPlayer2 import AnimatedGifPlayer, ImagePosition

root = tkinter.Tk()
root.config(bg='#ffffff')
root.wm_attributes('-transparentcolor', 'white')

#root.wm_attributes('-toolwindow', True)
#root.withdraw()
root.title("hi")
root.overrideredirect(True)

gif = AnimatedGifPlayer("snoop.gif", root, ImagePosition(500, 100))

gif.initialise_player(500)
print("hi")

gif2 = AnimatedGifPlayer("patra.gif", root, ImagePosition(800, 100))
gif2.initialise_player(300)
#gif.change(400)
#gif2.stop_animation()
#gif.stop_animation()

root.mainloop()