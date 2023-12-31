import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def unpack_gif(src):
    # Load Gif
    image = Image.open(src)
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
            raise ValueError('Disposal Methods other than 2:Restore to Background, 1:Do Not Dispose, and 0:No Disposal are supported at this time')
        # Update lastFrame
        lastFrame = loadedFrame
    return output

class AnimatedGifPlayer:
    def __init__(self, root, gif_path):
        self.root = root
        self.gif_path = gif_path
        self.frames = unpack_gif(gif_path)
        self.current_frame_index = 0

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.frames[0].width, height=self.frames[0].height)
        self.canvas.pack()

        self.play_animation()

    def play_animation(self):
        frame = self.frames[self.current_frame_index]
        self.photo = ImageTk.PhotoImage(frame)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)

        # Repeat the animation by calling the play_animation method after a delay
        self.root.after(30, self.play_animation)

# Example usage
root = tk.Tk()
root.title("Animated GIF Player")

# Replace 'path/to/your/animated.gif' with the actual path to your GIF file
gif_path = r"..\..\WindowUI\framework.gif"

player = AnimatedGifPlayer(root, gif_path)
root.config(bg = '#f0f0f0')

#Create a transparent window
root.wm_attributes('-transparentcolor','#f0f0f0')
root.mainloop()
