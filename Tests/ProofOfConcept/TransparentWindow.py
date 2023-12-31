#Import the Tkinter Library
from tkinter import *

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry of window
win.geometry("700x350")

#Add a background color to the Main Window
win.config(bg = '#ffffff')

#Create a transparent window
win.wm_attributes('-transparentcolor','#ffffff')

frameCnt = 169
frames = [PhotoImage(file=r"..\..\WindowUI\022Fl.gif",format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    win.after(169, update, ind)
label = Label(win, bg='#ffffff')
label.pack()
win.after(0, update, 0)
win.mainloop()