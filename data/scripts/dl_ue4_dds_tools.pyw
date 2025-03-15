import urllib.request
import zipfile
import os

url = "https://github.com/matyalatte/UE4-DDS-Tools/releases/download/v0.6.1/UE4-DDS-Tools-v0.6.1-Batch.zip"
destination_folder = "data/tools/UE4 DDS Tools v0.6.1 Batch"

os.makedirs(destination_folder, exist_ok=True)

zip_path = os.path.join(destination_folder, 'UE4-DDS-Tools-v0.6.1-Batch.zip')
with urllib.request.urlopen(url) as response:
    with open(zip_path, 'wb') as f:
        f.write(response.read())

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(destination_folder)

os.remove(zip_path)
