from dotenv import load_dotenv
load_dotenv()

import requests, json, os
from DatabaseUtils import DatabaseUtils

api_key = os.environ["API_KEY"]

def get_page_json(page_id: str):
    url = "https://api.notion.com/v1/pages/" + page_id

    payload = {}
    headers = {
    'Notion-Version': '2022-06-28',
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response_json = response.json()
    
    return response_json



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


def get_page_contents(page_id:str):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100"

    headers = {
        'Notion-Version': '2022-06-28',
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.request("GET", url, headers=headers)

    print(response.json()["results"])
    return response.json()["results"]

def fill_page_database(root_page_id:str):
    """
    Step 1: Call API https://api.notion.com/v1/blocks/:root_id/children?page_size=100 
        - Get all children ID's 
        - For each children page:
            - Call API <url> to get block IDs
            - For each block ID
                - If block type is text
                    - Append content to subject_db.children_ID.content
    """
    url = f"https://api.notion.com/v1/blocks/{root_page_id}/children?page_size=100"

    headers = {
        'Notion-Version': '2022-06-28',
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.request("GET", url, headers=headers)

    page_contents = {} #empty dict to store page title keys and page content values


    textual_block_types = ["text", "paragraph", "headings1", "headings2", "headings3", "bullet_list_item"]
    
    for entity in response.json()["results"]:
        if entity["type"] == "child_page":
            print(entity["child_page"]["title"])
            page_contents[entity["child_page"]["title"]] = ""

            child_page_contents = get_page_contents(entity["id"])

            for block in child_page_contents:
                if block["type"] in textual_block_types:
                    print(type(block[block["type"]]["rich_text"]))
                    plain_text = block[block["type"]]["rich_text"][0]["plain_text"]
                    page_contents[entity["child_page"]["title"]] += plain_text

    print(page_contents)
    


# pages_json = list_pages()

# process_page_metadata(pages_json)

# print(get_page_info("12a224ca-354c-80b0-950e-fc16ac57c1d6"))

fill_page_database("111224ca-354c-8020-8ccd-f1d4e30914ac")

# get_page_contents("12a224ca-354c-80b0-950e-fc16ac57c1d6")




