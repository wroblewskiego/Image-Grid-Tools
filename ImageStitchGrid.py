from PIL import Image
import os

# Parameters
INPUT_FOLDER = r""
OUTPUT_PATH = r"stitched_image.png"
GRID_SIZE = 3  # Change this value to adjust grid dimensions

def restitch_images(input_folder, output_path, grid_size):
    try:
        images = [[Image.open(os.path.join(input_folder, f"grid_{r}_{c}.png")) 
                   for c in range(grid_size)] for r in range(grid_size)]
        cell_width, cell_height = images[0][0].size
        stitched_img = Image.new('RGB', (cell_width * grid_size, cell_height * grid_size))
        
        for r, row in enumerate(images):
            for c, img in enumerate(row):
                stitched_img.paste(img, (c * cell_width, r * cell_height))
        
        stitched_img.save(output_path)
        print(f"Restitching completed. Image saved to {output_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    restitch_images(INPUT_FOLDER, OUTPUT_PATH, GRID_SIZE)
