from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ["API_KEY"]

import requests, json

def get_page_info(page_id: str):
    url = "https://api.notion.com/v1/pages/" + page_id # + "123224ca-354c-80e5-aed9-d13d55592914"

    payload = {}
    headers = {
    'Notion-Version': '2022-06-28',
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)



def list_pages(): # arg = subject (parent folder name/id)
    url = "https://api.notion.com/v1/search"

    payload = json.dumps({
        "query": "",
        "filter": {
            "value": "page",
            "property": "object"
        },
        "sort": {
            "direction": "ascending",
            "timestamp": "last_edited_time"
        }})

    headers = {
        'Notion-Version': '2022-06-28',
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()["results"]



def process_page_metadata(pages:list):
    for page in pages:
        # Grab id, parent id, title
        title = page.get("properties", {}).get("title", {}).get("title", [{}])[0].get("text", {}).get("content", "")
        page_id = page.get("id", "")
        parent_id = page.get("parent", {}).get("page_id", "")
        print(title, page_id, parent_id)





pages_json = list_pages()

process_page_metadata(pages_json)