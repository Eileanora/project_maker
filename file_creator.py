import os
from pathlib import Path

def make_files(repository="", directory="", files=[], base_dir="", soup=None):
    # if repo and dir are given valid
    if repository == "" or directory == "":
        print("No repo or dir given")
        exit()
    
    # create the paths to check
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
        if not Path(file_name).exists():
            open(file_name, 'w').close()

    # #create the readme file
    # with open('README.md', 'w') as f:
    #     f.write("### {directory}".format(directory=directory))
    make_readme(directory, soup)


def make_readme(directory="", soup=None):
    all_resources_elements = soup.find_all('div', {'class': 'panel-body'})

    for div in all_resources_elements:
        if div.find('h2', string='Requirements'):
            resources_element = div
            break
    try:
        read_or_watch_element = resources_element.find('h2', string='Resources').find_next_sibling('ul')
    except:
        read_or_watch_element = ""
    try:
        learning_objectives_element = resources_element.find('h2', string='Learning Objectives').find_next_sibling('ul')
    except:
        learning_objectives_element = ""

    # Extract Read or Watch
    if read_or_watch_element != "":
        resources = read_or_watch_element.find_all('li')

    if learning_objectives_element != "":
        learning_objectives = learning_objectives_element.find_all('li')


    # Write to README.md
    with open('README.md', 'w') as f:
        f.write("# {directory}\n".format(directory=directory))
        if learning_objectives_element != "":
            f.write("\n## Learning Objectives\n")
            for objective in learning_objectives:
                f.write(f"{objective}\n")
        if read_or_watch_element != "":
            f.write("\n## Resources\n")
            for resource in resources:
                f.write(f"{resource}\n")
