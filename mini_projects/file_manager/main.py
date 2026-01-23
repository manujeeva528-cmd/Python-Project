import os
import shutil # used for copy and move, see what files are there in directory
folder_path = os.getcwd() # current working directory
# file types and their corresponding extensions
file_types={
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"], 
    "Scripts": [ ".js", ".html", ".css", ".sh"]   
}
# create folder if not exists

for file_name in file_types.keys():
    folder_name = os.path.join(folder_path, file_name) #python Program\project-file-manager\Audio  -join the path current working directory to folder
    # print(folder_name)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

 # organize files into respective folders

for file in os.listdir(folder_path):
    # print(file)
    file_path = os.path.join(folder_path, file)
    # print(file_path)
     #skip folders
    if os.path.isdir(file_path):
        continue
    #get file extension
    file_ext= os.path.splitext(file)[1].lower() #.splitext split the file name and extension
    for folder, extensions in file_types.items():
        if file_ext in extensions:
            dest_folder = os.path.join(folder_path, folder)
            print(dest_folder)
            shutil.move(file_path, dest_folder) #move file to destination folder
            break
    print(f"Organized files in {folder_path}")