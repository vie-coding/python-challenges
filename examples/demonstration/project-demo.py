from pathlib import Path
import shutil





def main():


    messy_dir_path = "/mnt/c/Users/ZamokuhleMthimkhulu/CascadeProjects/vie/challanges/projects/file_organizer/messy_folder/"
    messy_dir =  Path(messy_dir_path)
    messy_files = []
    for item in messy_dir.iterdir():
        messy_files.append(item.name)

    dir_categories = ["music", "video", "documents", "download"]
    sections = { "music" : [], "video" : [], "documents" : [], "pictures" : []}
    for item in messy_files:
        ext = item.split(".")
        if ext[-1] == "mp4" :
            sections["video"].append(item) 

        if ext[-1] == "mp3" :
            sections["music"].append(item)

        if ext[-1] == "pdf" :
            sections["documents"].append(item)

        if ext[-1] == "jpg" :
            sections["pictures"].append(item)


    print("Music \n*******************")

    for item in sections["music"]:
        print(item)

    print("\n\nVideo \n*******************")

    for item in sections["video"]:
        print(item)

    print("\n\nDocuments \n*******************")

    for item in sections["documents"]:
        print(item)

    print("\n\nPictures \n*******************")

    for item in sections["pictures"]:
        print(item)

    Path("organize/Music").mkdir(parents=True, exist_ok=True) 
    Path("organize/Video").mkdir(parents=True, exist_ok=True) 
    Path("organize/Documents").mkdir(parents=True, exist_ok=True) 
    Path("organize/Pictures").mkdir(parents=True, exist_ok=True) 


    for item in sections["music"]:
        shutil.copy2(messy_dir_path + item, "organize/Music/" + item)

    for item in sections["video"]:
        shutil.copy2(messy_dir_path + item, "organize/Video/" + item)

    for item in sections["documents"]:
        shutil.copy2(messy_dir_path + item, "organize/Documents/" + item)

    for item in sections["pictures"]:
        shutil.copy2(messy_dir_path + item, "organize/Pictures/" + item)


   

 
main()
