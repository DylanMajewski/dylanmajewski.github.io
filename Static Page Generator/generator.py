from app import port
import requests
import shutil
import os

def get_files(folder=""):
    # Construct an absolute path to the 'templates/routes' directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(base_dir, 'templates', 'routes', folder.strip("/"))

    files = []

    if not os.path.exists(target_dir):
        print(f"Directory does not exist: {target_dir}")
        return files

    for file in os.listdir(target_dir):
        if file.endswith('.j2'):
            files.append(f'{folder}/{file[:-3]}')

    for folder in os.listdir(target_dir):
        folder_path = os.path.join(target_dir, folder)
        if os.path.isdir(folder_path):
            nested_folder = folder if folder.startswith("/") else f"/{folder}"
            files += get_files(nested_folder)

    return files

def create_folders(files):
    #create a folder for each directory in the files list
    # ie /index -> ../, ../projects/project1 -> ../projects/
    for file in files:
        if '/' in file:
            try:
                os.makedirs(f'./{file[:file.rfind("/")+1]}')
            except FileExistsError:
                pass

def get_routes(files):

    for file in files:
        # request the route from the app, save the response html to a file in the directory above generator.py
        print(f'http://localhost:{port}{file}')
        response = requests.get(f'http://localhost:{port}{file}')
        with open(f'.{file}.html', 'w') as f:
            f.write(response.text)

def copy_static_files():
    # path of static folder in same directory
    src = './Static Page Generator/static'  # Relative path to the source folder
    dst = './static'  # Relative path to the destination folder

    # Check if the destination folder exists, and remove it if it does
    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    # Copy the entire folder from src to dst
    shutil.copytree(src, dst)

    print("Static files copied successfully.")


if __name__ == "__main__":
    files = get_files()     # get all files in /templates/routes
    # create_folders(files)   # create folders for each directory in the files list
    # get_routes(files)       # request the route from the app, 
    copy_static_files()     # copy the static files to the static folder