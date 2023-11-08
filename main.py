import os
from functions.fetch_data import fetch_data
from functions.open_zip import extract_and_delete_zips

def main():
    print("Hello")
    y_n = input("Do you have any specific directory for storage? (Y/N): ")
    
    if y_n.upper() == "Y":
        folder_path = input("Please Enter The Path: ")
    else:
        print("Data Folder Created")
        folder_path = 'Data'  # Default folder name if not provided
        os.makedirs(folder_path, exist_ok=True)  # Create a Data folder if it doesn't exist

    csv_file_path = input("Please Enter The CSV File Path: ")
    
    

    # Fetch the data
    fetch_data(csv_file_path)
    
    # Extract the zip files
    extract_and_delete_zips(folder_path)

if __name__ == "__main__":
    main()
