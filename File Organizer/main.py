import os
import shutil

source_directory = (r"C:\Users\USER\Downloads")
destination_base = (r"C:\Users\USER\Documents")

extension_to_folder = {
    ".txt": "TextFiles",
    ".docx": "WordFiles",
    ".pptx": "PowerPointFiles",
    ".jpg": "Images",
    ".png": "images",
    ".gif": "images",
    ".pdf": "PDFs",
}

for filename in os.listdir(source_directory):
    source_path = os.path.join(source_directory, filename)
    

    if os.path.isfile(source_path):
      
        _, file_extension = os.path.splitext(filename)
        
        destination_folder = extension_to_folder.get(file_extension, "Other")
        
        destination_path = os.path.join(destination_base, destination_folder)
        os.makedirs(destination_path, exist_ok=True)
        
        shutil.move(source_path, os.path.join(destination_path, filename))

print("File organization completed bossing.")
