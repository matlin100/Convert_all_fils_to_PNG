import os

def convert_images(folder_path):
    converted_files = set()  # Use a set to keep track of converted files
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is a regular file (not a directory)
        if os.path.isfile(file_path) and filename.lower().endswith('.png'):
            photoname = os.path.splitext(filename.lower())[0]
            for filenameends in os.listdir(folder_path):
                fileends_path = os.path.join(folder_path, filenameends)
                # Check if the file is a regular file and matches the condition
                if (
                    os.path.isfile(fileends_path) and
                    filenameends.lower().startswith(photoname) and
                    not filenameends.lower().endswith('.png')
                ):
                    os.remove(fileends_path)
                    print("removed : " + filenameends)

if __name__ == "__main__":
    folder_path = "/path/to/your/folder"
    convert_images(folder_path)
