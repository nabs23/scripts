from PIL import Image
import os

# Define the current folder path and the output folder for jpg images
folder_path = os.getcwd()
output_folder = os.path.join(folder_path, 'jpg')

# Create the 'jpg' folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the folder
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
