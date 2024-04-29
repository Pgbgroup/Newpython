import requests
import os
from tqdm import tqdm
from urllib.parse import unquote

def download_file(url):
    # Send a HEAD request to get the filename from the URL
    response = requests.head(url)
    # Get the filename from the URL or set a default name
    filename = unquote(url.split('/')[-1]) if 'Content-Disposition' not in response.headers else response.headers['Content-Disposition'].split('filename=')[1]
    # Set the path to save the file in the current directory
    save_path = os.path.join(os.getcwd(), filename)
    # Send a GET request to the URL
    response = requests.get(url, stream=True)
    # Check if the request was successful
    if response.status_code == 200:
        # Get the total file size in bytes
        total_size = int(response.headers.get('content-length', 0))
        # Open the file and write the content in chunks to display progress
        with open(save_path, 'wb') as f, tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024, disable=False) as pbar:
            for data in response.iter_content(chunk_size=1024):
                f.write(data)
                pbar.update(len(data))
        print("Download successful. File saved at:", save_path)
    else:
        print("Failed to download file.")

# Get URL input from the user
file_url = input("Enter the URL of the file to download: ")

# Call the function to download the file
download_file(file_url)
