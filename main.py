# Import 
from functions.fetch_data import *
from functions.open_zip import *


def __main__():
    
    # Define the folder path
    folder_path = "your_folder_path_here"  # Replace with the path to your specific folder

    # Extract the zip files
    extract_and_delete_zips(folder_path)

    # Define the CSV file path
    csv_file_path = "csv_file_path_here"  # Replace with the path to your specific folder

    # Fetch the data
    fetch_data(csv_file_path)

