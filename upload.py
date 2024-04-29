import os
import time
from mega import Mega

def upload_to_mega(email, password, file_name):
    mega = Mega()
    
    try:
        # Login to MEGA
        print("Logging in to MEGA...")
        m = mega.login(email, password)
        print("Logged in successfully!")
        
        # Get the absolute path of the file
        file_path = os.path.abspath(file_name)
        print("File path:", file_path)
        
        # Check if file exists
        if not os.path.exists(file_path):
            print("Error: File not found.")
            return
        
        # Get file size for progress bar
        file_size = os.path.getsize(file_path)
        
        # Upload file
        print("Uploading file to MEGA...")
        file_handle = m.upload(file_path)
        
        # Simulate progress bar
        while m.get_upload_progress(file_handle) < 100:
            progress = m.get_upload_progress(file_handle)
            print(f"Uploading: {progress:.2f}% complete", end="\r")
            time.sleep(0.5)  # Adjust the sleep duration to control the refresh rate
        
        print("\nFile uploaded successfully to MEGA.")
        
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # MEGA account credentials
    email = input("Enter your MEGA email: ")
    password = input("Enter your MEGA password: ")
    
    # File name to upload
    file_name = input("Enter the name of the file to upload (in the current directory): ")
    
    upload_to_mega(email, password, file_name)
