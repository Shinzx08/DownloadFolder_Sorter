import os
import shutil

def organize_files(source_dir, destination_base):
  extension_mappings = {
      ".txt": "TextFiles",
      ".docx": "WordFiles",
      ".pptx": "PowerPointFiles",
      ".pdf": "PDFs",
      ".zip": "ZIPs",
      ".jpg": "Pictures",
      ".png": "Pictures",
      ".gif": "Pictures",
      ".mp4": "Vid",
  }
  other_folder = "Other"

  for filename in os.listdir(source_dir):
    source_path = os.path.join(source_dir, filename)

    if os.path.isfile(source_path):
      _, file_extension = os.path.splitext(filename)
      destination_folder = extension_mappings.get(file_extension.lower(), other_folder)
      destination_path = os.path.join(destination_base, destination_folder)
      os.makedirs(destination_path, exist_ok=True)

      shutil.move(source_path, os.path.join(destination_path, filename))

  print("Tapulan")

source_dir = input("Enter the source directory path: ")
destination_base = input("Enter the destination directory path: ")
organize_files(source_dir, destination_base)
