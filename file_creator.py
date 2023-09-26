import os
from pathlib import Path

def make_files(repository="", directory="", files=[]):
    # if repo and dir are given valid
    if repository == "" or directory == "":
        print("No repo or dir given")
        exit()
    
    # create the paths to check
    base_dir = "/home/yasmeen/Documents/vs-folders/ALX" # <=================== change this to your base directory
    repo_dir = Path(base_dir) / repository
    task_dir = Path(repo_dir) / directory

    # create missing repo/folders
    if not repo_dir.exists():
        os.makedirs(repo_dir)
    if not task_dir.exists():
        os.makedirs(task_dir)

    # change directory to the current project directory
    os.chdir(task_dir)

    # create tasks files
    for file_name in files:
        open(file_name, 'w').close()

    #create the readme file
    with open('README.md', 'w') as f:
        f.write("### {directory}".format(directory=directory))
