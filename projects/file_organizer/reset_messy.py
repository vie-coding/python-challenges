"""
Reset the messy_folder to its original state for testing.
Run this after testing your organizer to get fresh test files.
"""

import os
import shutil

# Get the directory where this script lives
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MESSY_FOLDER = os.path.join(SCRIPT_DIR, "messy_folder")

# Test files to create
TEST_FILES = {
    # Images
    "vacation_2024.jpg": "vacation photo",
    "IMG_1234.png": "family pic",
    "funny_cat.gif": "meme",
    "Screenshot_2024-01-15.png": "screenshot",
    "photo_2023.jpg": "old photo",

    # Music
    "summer_vibes.mp3": "favorite song",
    "episode_42.mp3": "podcast",
    "notification.wav": "sound effect",
    "track_01.flac": "album track",

    # Videos
    "inception_2010.mp4": "movie",
    "python_basics.mkv": "tutorial",
    "funny_moment.avi": "clip",

    # Documents
    "quarterly_report.pdf": "report",
    "meeting_notes.txt": "notes",
    "my_resume.doc": "resume",
    "assignment_final.pdf": "essay",
    "README.txt": "readme",

    # Code
    "automation.py": "script",
    "index.html": "webpage",
    "styles.css": "styles",
    "app.js": "app code",

    # Archives
    "backup_2024.zip": "archive",
    "data.tar.gz": "compressed",

    # Other
    "contacts.csv": "data",
    "budget.xlsx": "spreadsheet",
    "something.xyz": "random",
    "settings.json": "config",
    "photo_2023.jpg.bak": "duplicate",

    # Hidden files
    ".hidden_file.txt": "hidden content",
    ".secret_notes": "another hidden",
}


def reset():
    # Remove the entire messy_folder and recreate it
    if os.path.exists(MESSY_FOLDER):
        shutil.rmtree(MESSY_FOLDER)

    os.makedirs(MESSY_FOLDER)

    # Create all test files
    for filename, content in TEST_FILES.items():
        filepath = os.path.join(MESSY_FOLDER, filename)
        with open(filepath, "w") as f:
            f.write(content + "\n")

    print(f"Reset complete! Created {len(TEST_FILES)} files in messy_folder/")
    print("\nFiles created:")
    for filename in sorted(TEST_FILES.keys()):
        if not filename.startswith("."):
            print(f"  {filename}")
    print(f"\n  + {sum(1 for f in TEST_FILES if f.startswith('.'))} hidden files")


if __name__ == "__main__":
    reset()
