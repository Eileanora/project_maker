# project_maker

This is the first version of the project. It is a simple script that automates the process of creating intranet project files because i hate creating them one by one.

## Prerequisites

- Python 3
- BeautifulSoup package installed: `pip3 install bs4`
- Requests package installed: `pip3 install requests`

## How to Use

1. Open the `script.py` file.
2. Enter your email and password in the appropriate fields (line 8 and 9).
3. Enter the project link in it's field (line 10).
4. Enter the path of your ALX projects directory in it's field (line 11).
5. Run the script.


## How it Works

This script is designed to automate the process of completing tasks on a specific project management platform. 

The script uses the `requests` library to send HTTP requests to the project management platform's server. It then uses the `BeautifulSoup` library to parse the HTML response and extract the necessary information.

Once you have entered your email and password, as well as the project link, the script will log in to the platform and retrieve a list of tasks associated with the project. It will then loop through each task and mark it as complete by sending a POST request to the server with the appropriate parameters.

To use this script, you will need to manually enter your email and password in the appropriate fields in the script. You will also need to enter the project link. Once you have done this, simply run the script and it will take care of the rest. 

Please note that this script is just a basic script that was designed for a specific website and a specific task.

## Change Log
- if file exists, skip -> (doesn't replace it anymore)
- if one task contain multiple files, it will create them all -> (doesn't create only the first one anymore)
- Add learning objectives and resources and concepts if available to the README.md file
