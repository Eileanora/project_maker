import requests
from bs4 import BeautifulSoup
from file_creator import make_files

def scrapping():

    # Get nessaary data from user
    email = "your intranet email" # <===================
    password = "your password" # <===================
    tasks_url = 'task link' # <===================
    base_dir = "/home/yasmeen/Documents/vs-folders/ALX" # change this to your base directory

    login_url = 'https://intranet.alxswe.com/auth/sign_in'

    # Create a session
    session = requests.Session()

    # Send a GET request to retrieve the login page
    response = session.get(login_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the authenticity token from the form
    authenticity_token = soup.find('input', {'name': 'authenticity_token'}).get('value')

    data = {
        'authenticity_token': authenticity_token,
        'user[email]': email,
        'user[password]': password
    }

    # Send a POST request to the login action URL
    response = session.post(login_url, data=data)

    # Check if the login was successful
    if response.url == login_url:
        print('Login failed')
        exit()

    # if login successful, go on with the script
    print('Login successful')

    # Send a GET request to retrieve the tasks page
    response = session.get(tasks_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the task elements
    task_elements = soup.find_all('div', class_='list-group-item')

    # Loop through each task element
    repository = ""
    directory = ""
    files = []
    for task in task_elements:
        # Extract GitHub repository, directory, and file names
        info_elements = task.find_all('li')

    # Check if the elements exist and extract their text
    repo_name = info_elements[0].find('code').text if info_elements else 'N/A'
    dir_name = info_elements[1].find('code').text if info_elements else 'N/A'
    file_names = info_elements[2].find('code').text if info_elements else 'N/A'

    if repository == "" and repo_name != "N/A":
        repository = repo_name
    if directory == "" and dir_name != "N/A":
        directory = dir_name
    if file_names != 'N/A':
        for file_name in file_names.split(', '):
            files.append(file_name.strip())

        # Print the extracted information for the current task (just to check it's valid)
        print(f"Repository: {repo_name}")
        print(f"Directory: {dir_name}")
        print(f"File: {file_name}")
        print()

    make_files(repository, directory, files, base_dir, soup)
    session.close()

if __name__ == "__main__":
    scrapping()
