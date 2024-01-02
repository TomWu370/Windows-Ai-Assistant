import copy
import multiprocessing
import threading
#from joblib import Parallel, delayed
import time
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from multiprocessing import Process


class AnimatedGifPlayer:
    def __init__(self, gif_path, root, position):
        self.thread = None
        self.photo = None
        self.canvas = None
        self.root = tk.Toplevel(root)
        #self.root.overrideredirect(True)
        self.root.transient(root)
        # self.root.wm_attributes('-fullscreen', 'True')
        #self.root.wm_attributes('-type', 'splash')
        self.root.grab_set() # prevents dragging
        self.gif_path = gif_path
        self.frames = self.load_gif(gif_path)
        self.oddColour = None
        self.current_frame_index = 0
        self.play_state = True
        self.quit_state = False
        self.position = position

    def create_widgets(self, position):

        print("made root")
        # self.root = tk.Tk()
        # self.root.overrideredirect(True)
        # self.root.geometry("+500+500")

        # Create a transparent window
        # root.wm_attributes('-transparentcolor','#00ff00')
        self.root.attributes('-topmost', True)

        self.root.lift()
        self.root.config(bg='#ffffff')
        self.root.wm_attributes('-transparentcolor', 'white')
        self.root.geometry("+0+-100")

        self.canvas = tk.Canvas(self.root, width=1920, height=1080,
                                background='white', borderwidth=0, highlightthickness=0, bd=0)
        print("declared root")
        print(self.canvas.cget("background"))
        self.canvas.pack()


    def load_gif(self, gif_path):
        image = Image.open(gif_path)
        # Get frames and disposal method for each frame
        frames = []
        disposal = []
        for gifFrame in ImageSequence.Iterator(image):
            disposal.append(gifFrame.disposal_method)
            frames.append(gifFrame.convert('P'))
        # Loop through frames, and edit them based on their disposal method
        output = []
        lastFrame = None
        thisFrame = None
        for i, loadedFrame in enumerate(frames):
            # Update thisFrame
            thisFrame = loadedFrame
            # If the disposal method is 2
            if disposal[i] == 2:
                # Check that this is not the first frame
                if i != 0:
                    # Pastes thisFrames opaque pixels over lastFrame and appends lastFrame to output
                    lastFrame.paste(thisFrame, mask=thisFrame.convert('RGBA'))
                    output.append(lastFrame)
                else:
                    output.append(thisFrame)
            # If the disposal method is 1 or 0
            elif disposal[i] == 1 or disposal[i] == 0:
                # Appends thisFrame to output
                output.append(thisFrame)
            # If disposal method if anything other than 2, 1, or 0
            else:
                raise ValueError(
                    'Disposal Methods other than 2:Restore to Background, 1:Do Not Dispose, and 0:No Disposal are supported at this time')
            # Update lastFrame
            lastFrame = loadedFrame
        return output

    def play_animation(self):

        if self.play_state:
            frame = self.frames[self.current_frame_index]
            self.photo = ImageTk.PhotoImage(frame)
            self.canvas.create_image(self.position, 100, anchor=tk.NE, image=self.photo)
            # self.canvas.configure(background='white')
            self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)

            #self.root.update()
            #self.root.update_idletasks()
            #time.sleep(0.015)
            # key is this root, and the canvas to draw on
            # Repeat the animation by calling the play_animation method after a delay
            self.root.after(15, self.play_animation)  # 15 is the same as the normal playing speed

        if self.quit_state:
            self.current_frame_index = 0

            self.play_state = True
            self.quit_state = False
            print("exiting")
            self.root.destroy()
            # self.root = None

    def initialise_player(self, position):
        print("at init")
        self.create_widgets(position)
        print(self.canvas.cget("background"))
        print("finished create")
        self.play_animation()
        print("exited")

        #self.root.mainloop()
        print("after loop")

    def play(self, position):
        # 1 time, create widget window and canvas
        # if played again then location should just change
        self.position = position
        self.initialise_player(position)
        #self.thread = Process(target=self.initialise_player, args=(position,))
        # print("starting")
        #self.thread.start()

    def change(self, position):
        self.position = position


    def pause_animation(self):
        self.play_state = False

    def resume_animation(self):
        self.play_state = True

    def stop_animation(self):
        self.quit_state = True



if __name__ == '__main__':
    # multiprocessing.freeze_support()
    gif = AnimatedGifPlayer(r'bg-transparent.gif')
    gif2 = AnimatedGifPlayer(r'bg-transparent.gif')
    test = [gif, gif2]
    #Parallel(n_jobs=2)(delayed(AnimatedGifPlayer.play)(gif, "playing") for gif in test)
    for gif in test:
        Process(target=gif.play, args=("playing",)).start()
        print("hi")
    while True:
        pass
    # gif.play("playing")
    # time.sleep(3)
    # gif2 = gif.stop_animation()
    # time.sleep(2)
    # #gif2.play("playing")
    # # gif.thread.join() # the destroy or mainloop ends the thread before the thread is joined
    # # del gif.root deletes the async handler, therefore it can't handle mainloop
    # use multi process to achieve multi player, since multi process doesn't share the same memory
    #
    #
    # gif = AnimatedGifPlayer(r'022Fl.gif')
    # gif.play("playing")
    # time.sleep(3)
    # gif.stop_animation()
    # del gif
