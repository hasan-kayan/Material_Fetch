import csv
import requests
import os
from tqdm.auto import tqdm

def total_rows(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return sum(1 for _ in reader)

def fetch_data(csv_file_path, save_path):
    # Open the CSV file
    total = total_rows(csv_file_path)
    
    with open(csv_file_path, 'r') as csvfile:
        
        reader = csv.DictReader(csvfile)

        # Loop through each row in the CSV file
        for row in tqdm(reader, desc='Downloading', total=total):
            # Extract the assetId, rawLink, and filetype    
            # downloadAttribute = row['downloadAttribute']
            # if not ('8K' in downloadAttribute):
            #     continue
            rawLink = row['rawLink']

            # Download the file
            # Extract the filename from the rawLink
            filename = rawLink.split('/')[-1]
            filepath = os.path.join(save_path, filename)

            if not os.path.exists(filepath):
                try:
                    response = requests.get(rawLink)

                    with open(filepath, 'wb') as f:
                        f.write(response.content)
                except Exception as e:
                    print(f"Failed to download {rawLink}. Reason: {e}")
