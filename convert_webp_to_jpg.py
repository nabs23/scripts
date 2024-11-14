from PIL import Image
import os
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Convert all .webp images in a folder to .jpg format.")
parser.add_argument(
    "-f", "--folder",
    type=str,
    default=os.getcwd(),
    help="Specify the folder containing .webp images (default: current folder)"
)

args = parser.parse_args()
folder_path = args.folder

# Define the output folder for jpg images
output_folder = os.path.join(folder_path, 'jpg')

# Create the 'jpg' folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the specified folder
for filename in os.listdir(folder_path):
    if filename.endswith('.webp'):
        # Construct the full file path
        webp_path = os.path.join(folder_path, filename)
        
        # Open the .webp image
        with Image.open(webp_path) as img:
            # Convert to RGB mode for saving as .jpg
            img = img.convert('RGB')
            
            # Define the path for the converted .jpg file
            jpg_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")
            
            # Save the image as .jpg
            img.save(jpg_path, 'JPEG')
            
        print(f"Converted {filename} to JPG in the 'jpg' folder.")

print("Conversion completed.")
