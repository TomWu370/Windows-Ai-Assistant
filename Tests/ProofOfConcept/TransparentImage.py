from tkinter import *
from PIL import Image


root = Tk()
root.title("Game")


frame = Frame(root)
frame.pack()


canvas = Canvas(frame, bg="black", width=700, height=400)
canvas.pack()
root.wm_attributes('-transparentcolor','black')
# could read all colours in image then set background to a colour not in the image

background = PhotoImage(file=r"..\..\WindowUI\framework.gif")
canvas.create_image(350,200,image=background)

character = PhotoImage(file="..\..\WindowUI\Leopard-Download-PNG.png")
canvas.create_image(30,30,image=character)

root.mainloop()