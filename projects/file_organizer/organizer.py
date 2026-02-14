"""
File Organizer CLI Tool
Usage: python organizer.py /path/to/folder

Your task: Complete this script to organize files by extension.
"""

import os
import argparse
import shutil


# Define which extensions go to which folder
CATEGORIES = {
    "Images": [".jpg", ".png", ".gif", ".jpeg", ".bmp"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt"],
    # Add more categories as needed
}


def get_category(filename):
    """
    Given a filename, return the category it belongs to.
    Returns "Other" if no category matches.
    """
    ext = os.path.splitext(filename)[1].lower() 
    for category, extensions in CATEGORIES.items(): 
        if ext in extensions:
            return category
    return "Other"

def organize_folder(folder_path):
    """
    Organize all files in the given folder into subfolders.
    """
    # List all files in folder_path
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for filename in files:
        category = get_category(filename)
        category_path = os.path.join(folder_path, category)

        # Create the category subfolder if it doesn't exist
        if not os.path.exists(category_path):
            os.makedirs(category_path)

        # Move the file to the subfolder
        src = os.path.join(folder_path, filename)
        dst = os.path.join(category_path, filename)
        
        # Handle duplicate filenames in destination
        if os.path.exists(dst):
            base, extension = os.path.splitext(filename)
            counter = 1
            while os.path.exists(os.path.join(category_path, f"{base}_{counter}{extension}")):
                counter += 1
            dst = os.path.join(category_path, f"{base}_{counter}{extension}")

        shutil.move(src, dst)
        print(f"Moved: {filename} -> {category}/")


def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory by extension.")
    parser.add_argument("folder", help="Path to the folder to organize")
    args = parser.parse_args()

    folder = args.folder

    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a valid directory")
        return

    organize_folder(folder)


if __name__ == "__main__":
    main()
