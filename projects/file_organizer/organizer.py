"""
File Organizer CLI Tool
Usage: python organizer.py /path/to/folder

Your task: Complete this script to organize files by extension.
"""

import os
import argparse


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
    # TODO: Get the file extension and find its category
    pass


def organize_folder(folder_path):
    """
    Organize all files in the given folder into subfolders.
    """
    # TODO:
    # 1. List all files in folder_path
    # 2. For each file, determine its category
    # 3. Create the category subfolder if it doesn't exist
    # 4. Move the file to the subfolder
    # 5. Print what you moved
    pass


def main():
    # TODO: Use argparse to get the folder path from command line
    # For now, you can hardcode a test path:

    folder = input("Enter folder path to organize: ")

    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a valid directory")
        return

    organize_folder(folder)


if __name__ == "__main__":
    main()
