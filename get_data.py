from models import PageModel

from dotenv import load_dotenv
load_dotenv()

import requests, json, os

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
    if response.status_code != 200:
        raise Exception(response.json())

    TYPE_TO_KEY = {
        "paragraph":"rich_text",
        "text": "plain_text",
        "heading_1": "rich_text",
        "heading_2":"rich_text",
        "heading_3":"rich_text",
        "bulleted_list_item":"rich_text",
        "numbered_list_item":"rich_text",
        "rich_text":"plain_text"
    }

    more_pages_id = []
    # if we see rich text - value is list of entity
    block_entities = response.json()["results"]

    entity_plain_texts = []
    for entity in block_entities:
        entity_type = entity["type"]
        try:
            if entity_type in TYPE_TO_KEY:
                rich_text_to_plain = []
                for text in entity[entity_type]["rich_text"]:
                    rich_text_to_plain.append(text['plain_text'])

                plain_text = ' '.join(rich_text_to_plain)
                entity_plain_texts.append(plain_text)
            
            # if linking to child page, call get_page_info
            elif entity_type == 'child_page':
                child_page_id = entity["id"]
                more_pages_id.append(child_page_id)
        except Exception as e:
            continue
    
    title, page, parent_id = get_page_info(root_page_id)                  
    model = PageModel(
        root_page_id,
        title,
        " ".join(entity_plain_texts)
    )
    # print(len(more_pages_id))
    return model, more_pages_id

def get_all_pages_and_child_pages(page_id:str):
    all_pages_id = [page_id]

    page_content_lis = [] 
    while all_pages_id:
        page_id = all_pages_id.pop()
        page_model, children_page_ids = fill_page_database(page_id)
        page_content_lis.append(page_model)
        all_pages_id.extend(children_page_ids)
    
    return page_content_lis
    

sample_page_id = "120224ca-354c-8017-bdf0-c9978dbbc5fa"
root_id = "111224ca-354c-8020-8ccd-f1d4e30914ac"
page_models = get_all_pages_and_child_pages(root_id)

from pprint import pprint
pprint([ent.to_json()['title'] for ent in page_models])