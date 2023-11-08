import zipfile
import os

def extract_and_delete_zips(folder_path):
    # Check if the folder path exists
    if not os.path.exists(folder_path): # Check if the folder path exists:
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Get a list of files in the folder
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        # Check if the file is a zip archive
        if file.endswith('.zip'):
            print(f"Extracting {file}...")
            
            # Open the zip file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Extract all the contents to the same folder
                zip_ref.extractall(folder_path)
            
            # Remove the zip file
            os.remove(file_path)
            print(f"{file} has been extracted and deleted.")

if __name__ == "__main__":
    folder_path = "your_folder_path_here"  # Replace with the path to your specific folder
    extract_and_delete_zips(folder_path)
