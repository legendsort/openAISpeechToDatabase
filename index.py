import requests
import json

# apiKey = XXX
# notionAPI = XXX
# notionDB = XXX
formatPrompt = "Reformat my verbal thoughts into grammatically correct sentences while preserving my unique communication style as much as possible. "
titlePrompt = "create a title and one-liner based on the content. Output JSON string with only title and oneLiner "


def speechToText(fileUrl):
    # Replace with your audio file URL
    fileUrl = fileUrl[:-1] + "1"
    response = requests.get(fileUrl)
    audio_data = response.content
    response = requests.post(
        "https://api.openai.com/v1/audio/transcriptions",
        headers={"Authorization": f"Bearer {apiKey}"},
        files={"file": ("audio.mp3", audio_data)},
        data={"model": "whisper-1"}
    )

    transcription = ""
    if response.status_code != 200:
        transcription = response.json()['error']
    else:
        transcription = response.json()["text"]

    return transcription


def formatText(transcription):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {apiKey}'
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': f'{transcription} + \n ${formatPrompt}'}]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    formatted = response.json()['choices'][0]['message']['content']
    return formatted


def createTitle(formatted):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {apiKey}'
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': f'{formatted} + \n ${titlePrompt}'}]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    title = response.json()['choices'][0]['message']['content']
    return title


def getTitleNOneLiner(str):
    return json.loads(str)['title'], json.loads(str)['oneLiner']


transcription = speechToText(fileUrl)
print(transcription)

formatted = formatText(transcription)
print(formatted)

response = createTitle(formatted)
print(response)

title, oneLiner = getTitleNOneLiner(response)
print(title, oneLiner)

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
                        'content': title
                    }
                }
            ]
        },
        'Category': {
            'rich_text': [
                {
                    'text': {
                        'content': oneLiner
                    }
                }
            ]
        },
        'Content': {
            'rich_text': [
                {
                    'text': {
                        'content': formatted
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
