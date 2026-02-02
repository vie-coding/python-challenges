# CLI File Organizer Challenge

**Goal:** Build a command-line tool that organizes messy folders by sorting files into subfolders.

---

## Level 1: Basic

```bash
python organizer.py /path/to/folder
```

**Requirements:**
- Scan folder for files (not subfolders)
- Move files into subfolders by extension:
  - `.jpg`, `.png`, `.gif` → `Images/`
  - `.mp3`, `.wav`, `.flac` → `Music/`
  - `.mp4`, `.mkv`, `.avi` → `Videos/`
  - `.pdf`, `.doc`, `.txt` → `Documents/`
  - Everything else → `Other/`
- Create subfolders if they don't exist
- Print what was moved: `Moved report.pdf → Documents/`

---

## Level 2: Safety Features

```bash
python organizer.py /path/to/folder --dry-run
```

**Add:**
- `--dry-run` - show what WOULD happen without moving anything
- Handle duplicates: if `Images/photo.jpg` exists, rename to `photo_1.jpg`
- Skip hidden files (starting with `.`)
- Confirmation prompt: `Move 15 files? [y/n]`
- Summary at end: `Moved 12 files, skipped 3`

---

## Level 3: Flexibility

```bash
python organizer.py /path --by-date --recursive
```

**Add:**
- `--by-date` - organize by year/month: `2024/01/`, `2024/02/`
- `--recursive` - also process files in subfolders
- `--config rules.json` - custom rules from JSON file:

```json
{
  "Code": [".py", ".js", ".html", ".css"],
  "Archives": [".zip", ".tar", ".gz"]
}
```

---

## Level 4: Bonus Features

Pick any:
- `--undo` - reverse the last organize operation (save moves to log)
- `--min-size 1MB` - only move files larger than X
- `--older-than 30` - only move files older than N days
- Interactive mode: ask for each file
- Color output with categories

---

## Technical Skills Practiced

- `os` and `os.path` / `pathlib`
- `shutil.move()`
- `argparse` for CLI arguments
- File system operations
- JSON config files
- Error handling (permissions, missing paths)

---

## Starter Hints

```python
import os
import argparse

# Get file extension
name, ext = os.path.splitext("photo.jpg")  # ("photo", ".jpg")

# List files in folder
for item in os.listdir(folder):
    full_path = os.path.join(folder, item)
    if os.path.isfile(full_path):
        # process it
```

---

## Test Folder

Use the `messy_folder/` directory to test your organizer. It contains a mix of file types.

To reset the messy folder after testing:
```bash
python reset_messy.py
```
