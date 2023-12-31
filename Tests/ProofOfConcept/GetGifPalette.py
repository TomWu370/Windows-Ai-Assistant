from PIL import Image, ImageSequence


def get_palette_from_gif(gif_path):
    # Open the GIF file
    gif = Image.open(gif_path)
    palettes = set()
    for frame_index in range(gif.n_frames):
        # Initialize a dictionary to store palettes for each frame
        # Iterate over frames
        # Go to the current frame
        gif.seek(frame_index)
        frame = gif.convert('RGB')
        pixels = list(frame.getdata())
        unique_colors = set(pixels)

        # Convert the RGB tuples to hexadecimal strings
        hex_colors = [f'#{r:02X}{g:02X}{b:02X}' for (r, g, b) in unique_colors]
        # Create a dictionary with color codes as keys and occurrences as values
        palettes.update(hex_colors)

    return palettes

# Example usage
gif_path = r'../../WindowUI/framework.gif'
palettes_dict = get_palette_from_gif(gif_path)
print(palettes_dict)
# Print the palettes for each frame
for palette in palettes_dict:
    print(f'colour: {palette}')