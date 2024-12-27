import os
import shutil

def organize_files(source_dir):
    """
    Organizes files in a directory into subfolders based on their extensions.

    Args:
        source_dir (str): Path to the directory to be organized.
    """
    # Check if the directory exists
    if not os.path.exists(source_dir):
        print("Source directory does not exist. Exiting...")
        return
    
    # Dictionary to group file extensions into categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".java", ".cpp"],
    }

    # Create folders if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(source_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Organize files based on their extensions
    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)
        if os.path.isfile(file_path):  # Only process files
            file_ext = os.path.splitext(file)[1]  # Get file extension
            
            moved = False
            for folder, extensions in file_types.items():
                if file_ext.lower() in extensions:
                    shutil.move(file_path, os.path.join(source_dir, folder, file))
                    print(f"Moved: {file} → {folder}")
                    moved = True
                    break
            
            # If the file does not match any category, move it to 'Others'
            if not moved:
                other_folder = os.path.join(source_dir, "Others")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, file))
                print(f"Moved: {file} → Others")

if __name__ == "__main__":
    # Replace with the path of the directory to be organized
    source_directory = input("Enter the path to the folder to organize: ")
    organize_files(source_directory)
