"""
Reset the messy_folder to its original state for testing.
Run this after testing your organizer to get fresh test files.

Uses Faker to generate realistic file names.
Install: pip install faker
"""

import os
import shutil
import random
from faker import Faker

fake = Faker()
Faker.seed(42)  # Consistent names each run
random.seed(42)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MESSY_FOLDER = os.path.join(SCRIPT_DIR, "messy_folder")


def generate_test_files():
    """Generate a dictionary of all test files with realistic names."""
    files = {}

    # === IMAGES ===
    # Vacation/travel photos
    locations = ["beach", "mountain", "paris", "tokyo", "safari", "cruise", "camping", "roadtrip"]
    for loc in locations:
        for i in range(random.randint(2, 4)):
            files[f"{loc}_{fake.date_this_year().strftime('%Y%m%d')}_{i+1}.jpg"] = "vacation photo"

    # Phone camera photos
    for _ in range(15):
        date = fake.date_this_year()
        files[f"IMG_{date.strftime('%Y%m%d')}_{random.randint(1000,9999)}.jpg"] = "phone photo"

    # Screenshots
    apps = ["chrome", "vscode", "slack", "discord", "twitter", "settings", "terminal"]
    for app in apps:
        files[f"Screenshot_{app}_{fake.date_this_month()}.png"] = "screenshot"

    # WhatsApp images
    for _ in range(8):
        files[f"WhatsApp_Image_{fake.date_this_month()}_at_{random.randint(10,23)}.{random.randint(10,59)}.jpeg"] = "whatsapp"

    # Memes and random
    meme_names = ["funny_cat", "distracted_boyfriend", "drake_meme", "stonks", "surprised_pikachu", "doge"]
    for name in meme_names:
        files[f"{name}.gif"] = "meme"

    # Profile pics and avatars
    files["profile_pic_old.png"] = "old profile"
    files["profile_pic_new.jpg"] = "new profile"
    files["avatar_backup.png"] = "avatar"

    # === MUSIC ===
    # Songs with artist names
    artists = ["drake", "weeknd", "kendrick", "taylor", "beyonce", "adele", "ed_sheeran", "billie"]
    for artist in artists:
        song = fake.word()
        files[f"{artist}_{song}.mp3"] = "song"
        files[f"{artist}_{fake.word()}_remix.mp3"] = "remix"

    # Podcasts
    podcasts = ["joe_rogan", "lex_fridman", "tim_ferriss", "huberman_lab", "daily_stoic"]
    for pod in podcasts:
        files[f"{pod}_ep{random.randint(100,500)}.mp3"] = "podcast"

    # Voice memos
    for _ in range(6):
        files[f"voice_memo_{fake.date_this_month()}_{random.randint(1,5)}.m4a"] = "voice memo"

    # Sound effects and ringtones
    sounds = ["notification", "alarm", "ringtone_old", "ringtone_new", "alert", "doorbell"]
    for sound in sounds:
        files[f"{sound}.wav"] = "sound"

    # FLAC albums
    albums = ["dark_side_of_moon", "thriller", "abbey_road", "rumours"]
    for album in albums:
        for i in range(1, 4):
            files[f"{album}_track{i:02d}.flac"] = "lossless audio"

    # === VIDEOS ===
    # Movies
    movies = ["inception_2010", "interstellar_2014", "parasite_2019", "dune_2021", "oppenheimer_2023"]
    for movie in movies:
        files[f"{movie}.mp4"] = "movie"

    # YouTube downloads
    yt_titles = ["how_to_code_python", "guitar_tutorial_beginner", "workout_routine_30min",
                 "cooking_pasta_easy", "math_explained_simply", "history_documentary"]
    for title in yt_titles:
        files[f"{title}_720p.mp4"] = "youtube download"

    # Screen recordings
    for _ in range(5):
        files[f"screen_rec_{fake.date_this_month()}_{fake.word()}.mov"] = "screen recording"

    # Clips
    games = ["minecraft", "fortnite", "valorant", "gta5", "eldenring"]
    for game in games:
        files[f"{game}_clip_{random.randint(1,99)}.webm"] = "game clip"

    files["funny_fail_compilation.avi"] = "compilation"
    files["wedding_ceremony_full.mkv"] = "wedding video"
    files["graduation_2023.mp4"] = "graduation"

    # === DOCUMENTS ===
    # Work documents
    for _ in range(5):
        files[f"report_{fake.month_name()}_{fake.year()}.pdf"] = "report"

    for _ in range(4):
        files[f"invoice_{fake.company().replace(' ', '_').replace(',', '')}_{random.randint(1000,9999)}.pdf"] = "invoice"

    for _ in range(3):
        files[f"receipt_{fake.company().replace(' ', '_').replace(',', '')}_{fake.date_this_year()}.pdf"] = "receipt"

    # Personal docs
    files["resume_latest.pdf"] = "resume"
    files["resume_old_version.doc"] = "old resume"
    files["cover_letter_google.docx"] = "cover letter"
    files["cover_letter_amazon.docx"] = "cover letter"
    files["passport_scan.pdf"] = "passport"
    files["drivers_license.jpg"] = "id"
    files["tax_return_2023.pdf"] = "tax"
    files["lease_agreement.pdf"] = "lease"
    files["car_insurance_policy.pdf"] = "insurance"

    # Notes
    subjects = ["meeting", "ideas", "todo", "shopping", "goals", "journal", "brainstorm", "reading_list"]
    for subj in subjects:
        files[f"{subj}_notes_{fake.date_this_month()}.txt"] = "notes"

    # School/learning
    files["assignment_calculus_final.pdf"] = "assignment"
    files["lecture_notes_physics.txt"] = "lecture notes"
    files["essay_draft_v2.docx"] = "essay"
    files["study_guide_biology.pdf"] = "study guide"

    # === CODE ===
    # Python scripts
    py_names = ["scraper", "analyzer", "bot", "automation", "backup_script", "data_cleaner",
                "api_client", "test_stuff", "untitled", "new_project"]
    for name in py_names:
        files[f"{name}.py"] = "python script"

    # Web files
    web_pages = ["index", "about", "contact", "dashboard", "login", "profile"]
    for page in web_pages:
        files[f"{page}.html"] = "html page"

    css_files = ["styles", "main", "responsive", "dark_theme", "animations"]
    for css in css_files:
        files[f"{css}.css"] = "stylesheet"

    js_files = ["app", "main", "utils", "api", "components", "handlers", "config"]
    for js in js_files:
        files[f"{js}.js"] = "javascript"

    # React/TypeScript
    components = ["Button", "Modal", "Navbar", "Card", "Form", "Table"]
    for comp in components:
        files[f"{comp}.tsx"] = "react component"

    # === ARCHIVES ===
    # Backups
    for _ in range(4):
        files[f"backup_{fake.date_this_year()}.zip"] = "backup"

    files["photos_2023_backup.zip"] = "photo backup"
    files["documents_archive.zip"] = "doc archive"
    files["old_projects.tar.gz"] = "project archive"
    files["website_backup_full.tar.gz"] = "site backup"
    files["music_collection.rar"] = "music archive"
    files["downloads_cleanup.zip"] = "downloads"

    # === DATA FILES ===
    # CSV
    csv_names = ["contacts", "expenses", "sales_data", "user_list", "inventory", "survey_results"]
    for name in csv_names:
        files[f"{name}.csv"] = "csv data"

    # Excel
    excel_names = ["budget_2024", "project_timeline", "employee_roster", "grades", "expenses_tracker"]
    for name in excel_names:
        files[f"{name}.xlsx"] = "spreadsheet"

    # JSON configs
    json_names = ["settings", "config", "package", "data", "preferences", "secrets"]
    for name in json_names:
        files[f"{name}.json"] = "json"

    # XML
    files["sitemap.xml"] = "sitemap"
    files["config.xml"] = "xml config"
    files["data_export.xml"] = "xml data"

    # === MISC FILES ===
    # Installers
    files["chrome_installer.exe"] = "installer"
    files["vscode_setup.exe"] = "installer"
    files["zoom_latest.msi"] = "installer"
    files["slack_desktop.dmg"] = "mac installer"
    files["spotify.deb"] = "linux package"

    # Media related
    files["movie_name.torrent"] = "torrent"
    files["movie_english.srt"] = "subtitles"
    files["movie_spanish.srt"] = "subtitles"
    files["documentary_subtitles.vtt"] = "subtitles"

    # Fonts
    fonts = ["roboto", "opensans", "montserrat", "lato"]
    for font in fonts:
        files[f"{font}_regular.ttf"] = "font"
    files["custom_font.otf"] = "font"

    # Ebooks
    books = ["atomic_habits", "deep_work", "thinking_fast_slow", "sapiens", "python_crash_course"]
    for book in books:
        ext = random.choice(["epub", "mobi", "pdf"])
        files[f"{book}.{ext}"] = "ebook"

    # Temp/logs/misc
    files["debug.log"] = "log"
    files["error.log"] = "log"
    files["access.log"] = "log"
    files["tempfile.tmp"] = "temp"
    files["~document.tmp"] = "temp"
    files["backup.bak"] = "backup"
    files["old_version.bak"] = "backup"
    files["mystery_file"] = "unknown"
    files["whatisthis.xyz"] = "unknown"
    files["random_download"] = "unknown"
    files["untitled"] = "unknown"

    # Hidden files
    files[".DS_Store"] = "mac system"
    files[".Thumbs.db"] = "windows cache"
    files[".gitignore"] = "git config"
    files[".env"] = "environment vars"
    files[".bashrc_backup"] = "shell backup"

    return files


def reset():
    """Reset the messy folder to original state."""
    test_files = generate_test_files()

    if os.path.exists(MESSY_FOLDER):
        shutil.rmtree(MESSY_FOLDER)

    os.makedirs(MESSY_FOLDER)

    for filename, content in test_files.items():
        filepath = os.path.join(MESSY_FOLDER, filename)
        with open(filepath, "w") as f:
            f.write(content + "\n")

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
