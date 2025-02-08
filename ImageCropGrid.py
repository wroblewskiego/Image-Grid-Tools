from PIL import Image
import os

# Parameters
IMAGE_PATH = r""
OUTPUT_PATH = r""
GRID_SIZE = 3  # Number of rows and columns in the grid

def crop_image_to_grid(image_path, output_folder, grid_size):
    try:
        img = Image.open(image_path)
        width, height = [dim // grid_size * grid_size for dim in img.size]
        img = img.crop((0, 0, width, height))
        cell_width, cell_height = width // grid_size, height // grid_size
        os.makedirs(output_folder, exist_ok=True)

        for row in range(grid_size):
            for col in range(grid_size):
                img.crop((col * cell_width, row * cell_height, (col + 1) * cell_width, (row + 1) * cell_height))\
                    .save(os.path.join(output_folder, f"grid_{row}_{col}.png"))

        print("Cropping completed. Images saved in the output path.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    crop_image_to_grid(IMAGE_PATH, OUTPUT_PATH, GRID_SIZE)
