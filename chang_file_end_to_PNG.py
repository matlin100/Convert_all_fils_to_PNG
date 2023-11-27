import os
from PIL import Image

def convert_images(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.nef')):
            image_path = os.path.join(folder_path, filename)
            try:
                # Open the image file
                with Image.open(image_path) as img:
                    # Create a new file name with the .png extension
                    new_filename = os.path.splitext(filename)[0] + '.png'
                    new_image_path = os.path.join(folder_path, new_filename)

                    # Save the image in the new format
                    img.save(new_image_path, 'PNG')

                    print(f"Converted: {filename} to {new_filename}")

                    # Optionally, you can remove the original file
                    # os.remove(image_path)
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    folder_path = "/path/to/your/folder"  # Replace with the path to your folder
    convert_images(folder_path)
