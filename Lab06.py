import requests
import hashlib
import subprocess
import os

def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
    # we will get the expected value of the installer
    link = 'https://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
    # code for getting the response 
    response = requests.get(link)
    hash_value =  response.text.split()[0]
    return hash_value

def download_installer():
    # now download the installer 
    link = 'https://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
    response = requests.get(link)
    return

def installer_ok(installer_data, expected_sha256):
   #check the integrity of the installer
   expected_sha256 == hashlib.sha256(installer_data).hexdigest()
   if expected_sha256 == hashlib.sha256(installer_data).hexdigest(): 
    return True
   else: 
    raise ValueError('Hash mismatch, possible malware')
    

def save_installer(installer_data):
    #now we will save the installer to temp folder
    file_path = '"C:\temp\"'
    with open(file_path, 'wb') as f:
      f.write(installer_data)
    return

def run_installer(installer_path):
    # Now run the installer silently 
    subprocess.run([installer_path, '/S'], check=True)

    return installer_path
    
def delete_installer(installer_path):
    # Now delete the installer file 
    os.remove(installer_path)
    return

if __name__ == '__main__':
    main()