"""
Cleanup script: Deletes all files inside the organize/ subdirectories.
Keeps the folders, just empties them.
"""

from pathlib import Path
import os

organize_dir = Path(__file__).parent / "organize"

count = 0
for folder in organize_dir.iterdir():
    if folder.is_dir():
        for file in folder.iterdir():
            if file.is_file():
                os.remove(file)
                count += 1

print(f"Cleaned {count} files from {organize_dir}")
