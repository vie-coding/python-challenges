"""
Reset the messy_folder to its original state for testing.
Run this after testing your organizer to get fresh test files.
"""

import os
import shutil

# Get the directory where this script lives
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MESSY_FOLDER = os.path.join(SCRIPT_DIR, "messy_folder")


def generate_test_files():
    """Generate a dictionary of all test files to create."""
    files = {}

    # === IMAGES ===
    # JPG photos
    for i in range(1, 21):
        files[f"IMG_{i:04d}.jpg"] = f"photo {i}"
    for i in range(1, 11):
        files[f"download_({i}).jpg"] = f"download {i}"
    files["vacation_2024.jpg"] = "vacation photo"
    files["photo_2023.jpg"] = "old photo"

    # PNG screenshots
    for i in range(1, 16):
        files[f"Screenshot_2024-0{(i % 9) + 1}-{i:02d}.png"] = f"screenshot {i}"
    files["IMG_1234.png"] = "family pic"

    # JPEG WhatsApp
    for i in range(1, 9):
        files[f"WhatsApp_Image_2024-01-{i:02d}.jpeg"] = f"whatsapp {i}"

    # GIF
    files["funny_cat.gif"] = "meme"

    # === MUSIC ===
    # MP3
    for i in range(1, 13):
        files[f"track_{i:02d}.mp3"] = f"song {i}"
    for i in range(1, 6):
        files[f"podcast_episode_{i}.mp3"] = f"podcast {i}"
    files["summer_vibes.mp3"] = "favorite song"
    files["episode_42.mp3"] = "podcast"

    # Other audio
    for i in range(1, 5):
        files[f"voice_note_{i}.m4a"] = f"voice {i}"
    for i in range(1, 4):
        files[f"ringtone_{i}.wav"] = f"ringtone {i}"
    files["notification.wav"] = "sound effect"
    files["track_01.flac"] = "album track"

    # === VIDEOS ===
    # MP4
    for i in range(1, 9):
        files[f"VID_2024010{i}.mp4"] = f"video {i}"
    files["inception_2010.mp4"] = "movie"

    # MOV
    for i in range(1, 5):
        files[f"screen_recording_{i}.mov"] = f"screen rec {i}"

    # Other video
    for i in range(1, 4):
        files[f"clip_{i}.webm"] = f"clip {i}"
    files["python_basics.mkv"] = "tutorial"
    files["funny_moment.avi"] = "clip"

    # === DOCUMENTS ===
    # PDF
    for i in range(1, 11):
        files[f"document_{i}.pdf"] = f"doc {i}"
    for i in range(1, 5):
        files[f"invoice_2024_{i}.pdf"] = f"invoice {i}"
    for i in range(1, 4):
        files[f"receipt_{i}.pdf"] = f"receipt {i}"
    files["quarterly_report.pdf"] = "report"
    files["assignment_final.pdf"] = "essay"

    # TXT
    for i in range(1, 7):
        files[f"notes_{i}.txt"] = f"notes {i}"
    files["meeting_notes.txt"] = "notes"
    files["README.txt"] = "readme"

    # DOCX
    for i in range(1, 6):
        files[f"report_{i}.docx"] = f"report {i}"
    files["my_resume.doc"] = "resume"

    # === CODE ===
    # Python
    for i in range(1, 9):
        files[f"script_{i}.py"] = f"code {i}"
    files["automation.py"] = "script"

    # Web
    for i in range(1, 6):
        files[f"page_{i}.html"] = f"web {i}"
    for i in range(1, 5):
        files[f"style_{i}.css"] = f"style {i}"
    for i in range(1, 7):
        files[f"app_{i}.js"] = f"js {i}"
    for i in range(1, 4):
        files[f"component_{i}.tsx"] = f"ts {i}"
    files["index.html"] = "webpage"
    files["styles.css"] = "styles"
    files["app.js"] = "app code"

    # === ARCHIVES ===
    for i in range(1, 7):
        files[f"backup_{i}.zip"] = f"archive {i}"
    for i in range(1, 5):
        files[f"archive_{i}.tar.gz"] = f"tar {i}"
    for i in range(1, 4):
        files[f"files_{i}.rar"] = f"rar {i}"
    files["backup_2024.zip"] = "archive"
    files["data.tar.gz"] = "compressed"

    # === DATA FILES ===
    for i in range(1, 9):
        files[f"data_{i}.csv"] = f"data {i}"
    for i in range(1, 6):
        files[f"spreadsheet_{i}.xlsx"] = f"excel {i}"
    for i in range(1, 5):
        files[f"config_{i}.json"] = f"json {i}"
    for i in range(1, 4):
        files[f"data_{i}.xml"] = f"xml {i}"
    files["contacts.csv"] = "data"
    files["budget.xlsx"] = "spreadsheet"
    files["settings.json"] = "config"

    # === MISC FILES ===
    # Installers
    files["setup.exe"] = "installer"
    files["installer.msi"] = "installer"
    files["program.dmg"] = "disk image"
    files["app.deb"] = "package"

    # Media related
    files["movie.torrent"] = "torrent"
    files["movie_eng.srt"] = "subtitle"
    files["movie_esp.vtt"] = "subtitle"

    # Fonts
    files["custom_font.ttf"] = "font"
    files["arial.otf"] = "font"

    # Ebooks
    files["book.epub"] = "ebook"
    files["manual.mobi"] = "ebook"

    # Temp/logs
    files["tempfile.tmp"] = "temp"
    files["debug.log"] = "log"
    files["error.log"] = "log"
    files["old_file.bak"] = "backup"
    files["photo_2023.jpg.bak"] = "duplicate"

    # Unknown
    files["mystery_file"] = "unknown"
    files["what_is_this.xyz"] = "unknown"
    files["random.abc"] = "unknown"
    files["something.xyz"] = "random"

    # Hidden files
    files[".hidden_file.txt"] = "hidden content"
    files[".secret_notes"] = "another hidden"
    files[".DS_Store"] = "mac junk"
    files[".thumbs.db"] = "windows junk"

    return files


def reset():
    """Reset the messy folder to original state."""
    test_files = generate_test_files()

    # Remove the entire messy_folder and recreate it
    if os.path.exists(MESSY_FOLDER):
        shutil.rmtree(MESSY_FOLDER)

    os.makedirs(MESSY_FOLDER)

    # Create all test files
    for filename, content in test_files.items():
        filepath = os.path.join(MESSY_FOLDER, filename)
        with open(filepath, "w") as f:
            f.write(content + "\n")

    # Count files
    visible = sum(1 for f in test_files if not f.startswith("."))
    hidden = sum(1 for f in test_files if f.startswith("."))

    print(f"Reset complete! Created {len(test_files)} files in messy_folder/")
    print(f"  - {visible} visible files")
    print(f"  - {hidden} hidden files")
    print("\nFile types included:")
    print("  Images: .jpg, .png, .gif, .jpeg")
    print("  Audio: .mp3, .wav, .flac, .m4a")
    print("  Video: .mp4, .mkv, .avi, .mov, .webm")
    print("  Documents: .pdf, .txt, .doc, .docx")
    print("  Code: .py, .js, .html, .css, .tsx")
    print("  Archives: .zip, .tar.gz, .rar")
    print("  Data: .csv, .xlsx, .json, .xml")
    print("  And more: .exe, .srt, .ttf, .epub, .log, etc.")


if __name__ == "__main__":
    reset()
