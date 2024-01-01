import threading
import time
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence


class AnimatedGifPlayer:
    def __init__(self, gif_path):
        self.photo = None
        self.canvas = None
        self.root = None
        self.frames = self.load_gif(gif_path)
        self.oddColour = None
        self.current_frame_index = 0
        self.play_state = True
        # self.create_widgets()

    def create_widgets(self, position):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        # self.root.geometry("+500+500")

        # Create a transparent window
        # root.wm_attributes('-transparentcolor','#00ff00')
        self.root.attributes('-topmost', True)

        self.root.lift()

        self.root.wm_attributes('-transparentcolor', 'white')
        self.root.config(bg='#ffffff')

        self.canvas = tk.Canvas(self.root, width=self.frames[0].width, height=self.frames[0].height, background='white',
                                borderwidth=0, highlightthickness=0)
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
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

            self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)

            # Repeat the animation by calling the play_animation method after a delay
            self.root.after(15, self.play_animation)  # 15 is the same as the normal playing speed


    def initialise_player(self, position):
        self.create_widgets(position)
        self.play_animation()
        self.root.mainloop()
    def play(self, position):
        # 1 time, create widget window and canvas
        # if played again then location should just change
        threading.Thread(target=self.initialise_player, args=(position,)).start()
    def pause_animation(self):
        self.play_state = False

    def resume_animation(self):
        self.play_state = True

    def stop_animation(self):
        self.play_state = True
        self.current_frame_index = 0
        self.root.quit()


if __name__ == '__main__':
    gif = AnimatedGifPlayer(r'022Fl.gif')
    print(gif)
    gif.play("hi")
    gif.stop_animation()
    time.sleep(5)
    gif.pause_animation()
    print(gif.play)
