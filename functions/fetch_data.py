import csv
import requests
import os

def fetch_data(csv_file_path):
    # Create a Data folder to keep files in it 
    os.makedirs('Data')

# Open the CSV file
    with open(csv_file_path, 'r') as csvfile:
        
        reader = csv.DictReader(csvfile)

        # Loop through each row in the CSV file
        for row in reader:
            # Extract the assetId, rawLink, and filetype    
            assetId = row['assetId']
            rawLink = row['rawLink']
            filetype = row['filetype']

            # Download the file
            filename = f'{assetId}_{filetype}.{filetype}'
            filepath = os.path.join('Data', filename)

            if not os.path.exists(filepath):
                response = requests.get(rawLink)

                with open(filepath, 'wb') as f:
                    f.write(response.content)

                print(f'Downloaded {filename}')

if __name__ == "__main__":
    csv_file_path = "csv_file_path_here"  # Replace with the path to your specific folder
    fetch_data(csv_file_path)
