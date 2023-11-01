import os
import sys
from PIL import Image
from tqdm import tqdm

def scale_images(input_folder, scale_factor, output_folder):
    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: The input folder '{input_folder}' does not exist.")
        sys.exit(1)
    
    # Check if the scale factor is a valid float
    try:
        scale_factor = float(scale_factor)
    except ValueError:
        print("Error: The scale factor must be a valid float.")
        sys.exit(1)
    
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff'))]

    # Loop through all files in the input folder
    for filename in tqdm(image_files, desc="Scaling images", unit="file"):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff')):
            input_image_path = os.path.join(input_folder, filename)
            
            # Open the image
            with Image.open(input_image_path) as img:
                # Calculate new dimensions
                width, height = img.size
                new_width = int(width * scale_factor)
                new_height = int(height * scale_factor)
                
                # Scale the image
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Save the scaled image to the output folder
                output_image_path = os.path.join(output_folder, filename)
                img.save(output_image_path)

    print(f"All images have been scaled and saved to {output_folder}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python scale_images.py <input_folder> <scale_factor> <output_folder>")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    scale_factor = sys.argv[2]
    output_folder = sys.argv[3]

    scale_images(input_folder, scale_factor, output_folder)
