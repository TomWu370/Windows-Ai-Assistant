import tkinter as tk
from PIL import Image, ImageTk, ImageSequence


class AnimatedGifPlayer:
    def __init__(self, root, gif_path):
        self.root = root
        self.gif_path = gif_path
        self.frames = self.load_gif(gif_path)
        self.current_frame_index = 0

        self.create_widgets()
        self.play = True

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.frames[0].width, height=self.frames[0].height, background='white',
                                borderwidth=0, highlightthickness=0)
        self.canvas.pack()

        self.play_animation()

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
        # 1 time, create widget window and canvas
        # if played again then location should just change
        if self.play:
            frame = self.frames[self.current_frame_index]
            self.photo = ImageTk.PhotoImage(frame)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

            self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)

            # Repeat the animation by calling the play_animation method after a delay
            self.root.after(15, self.play_animation)  # 15 is the same as the normal playing speed

    def pause_animation(self):
        self.play = False

    def resume_animation(self):
        self.play = True

    def stop_animation(self):
        self.play = True
        self.current_frame_index = 0
        # destroy window
