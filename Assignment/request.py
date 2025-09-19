import os
import requests
from urllib.parse import urlparse
from pathlib import Path

def fetch_image():
    url = input("Enter the image URL: Assignment/Fetched_Images/3B0B3060-0309-47DE-82C9-08D4369A710F.webp").strip()
    
    if not url.lower().startswith(("http://", "https://")):
        print("Invalid URL. Please provide a valid http/https link.")
        return

    
    folder = "Fetched_Images"
    
    os.makedirs(folder, exist_ok=True) 

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  

        
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        
        if not filename:
            filename = "downloaded_image.jpg"

        
        if "." not in filename:
            filename += ".jpg"

        
        filepath = os.path.join(folder, filename)

    
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image saved successfully at: {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch image. Error: {e}")

if __name__ == "__main__":
    fetch_image()
