from dotenv import load_dotenv
load_dotenv()

import requests, json, os
# import DatabaseUtils, GraphUtils

api_key = os.environ["API_KEY"]






def get_page_info(page_id: str):
    url = "https://api.notion.com/v1/pages/" + page_id

    payload = {}
    headers = {
    'Notion-Version': '2022-06-28',
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response_json = response.json()

    title = response_json.get("properties", {}).get("title", {}).get("title", [{}])[0].get("text", {}).get("content", "")
    page_id = response_json.get("id", "")
    parent_id = response_json.get("parent", {}).get("page_id", "")

    return (title, page_id, parent_id)



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


# NEED TO CREATE A PAGE DB FOR EACH SUBJECT

def fill_page_database(root_page_id:str):
    """
    Step 1: Call API https://api.notion.com/v1/blocks/:root_id/children?page_size=100 
        - Get all children ID's 
        - For each children page:
            - Call API <url> to get block IDs
            - For each block ID
                - If block type is text
                    - Append content to subject_db.children_ID.content 
    
    Step 2: 
    
    """
    url = f"https://api.notion.com/v1/blocks/{root_page_id}/children?page_size=100"

    headers = {
        'Notion-Version': '2022-06-28',
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.request("GET", url, headers=headers)

    for _ in response.json()["results"]:
        print(_)


# pages_json = list_pages()

# process_page_metadata(pages_json)

# print(get_page_info("12a224ca-354c-80b0-950e-fc16ac57c1d6"))

fill_page_database("111224ca-354c-8020-8ccd-f1d4e30914ac")