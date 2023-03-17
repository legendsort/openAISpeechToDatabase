from celery import Celery

app = Celery('tasks', broker='redis://127.0.0.1:6379/0')

@app.task
def long_running_api():

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
    return "SDF"
