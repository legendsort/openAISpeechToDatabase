
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import requests
import json
import threading

app = Flask(__name__)

def run():


    # Set the API endpoint URL and headers
    url = 'https://api.notion.com/v1/pages'
    headers = {
        'Authorization': 'Bearer ' + notionAPI,
        'Content-Type': 'application/json',
        'Notion-Version': '2021-08-16'
    }

    # Set the request data
    data = {
        'parent': {'database_id': notionDB},
        'properties': {
            'Title': {
                'title': [
                    {
                        'text': {
                            'content': "ASD"
                        }
                    }
                ]
            },
            'Category': {
                'rich_text': [
                    {
                        'text': {
                            'content': "SDF"
                        }
                    }
                ]
            },
            'Content': {
                'rich_text': [
                    {
                        'text': {
                            'content': "wer"
                        }
                    }
                ]
            }
        }
    }

    # Send the API request
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # Print the response status code and content
    print(response.status_code)
    print(response.content)

def hello_world():
    # Start a new thread for the API call
    thread = threading.Thread(target=run)
    thread.start()
    print("SDF")
    return "SDF"

hello_world()

