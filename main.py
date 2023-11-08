import csv
import requests
import os

# Create a Data folder if it doesn't exist
if not os.path.exists('Data'):
    os.makedirs('Data')

# Open the CSV file
with open('ambientCG_downloads_csv.csv', 'r') as csvfile:
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