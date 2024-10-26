# fast api
import json
from fastapi import FastAPI
from DatabaseUtils import DatabaseUtils
from get_data import get_all_pages_and_child_pages
from nlp.content_ngrams_freq import build_page_to_bigram_map, build_relationshiop

DatabaseUtils.create_tables()

app = FastAPI()

from dotenv import load_dotenv
load_dotenv()

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.post("/build_graph/{page_id}")
async def build_graph(page_id):
  pages = get_all_pages_and_child_pages(page_id)
  
  # insert pages into database
  for model in pages:
    doc_model = model.to_doc_model()
    DatabaseUtils.insert_doc(doc_model)

  # pipe nlp
  return {
    'status': 200,
    "message": f'inserted {len(pages)} pages'
  }

@app.post("/nlp/process_docs")
async def query_terms():
  pages_raw_text = DatabaseUtils.get_raw_text_from_db()
  docs = DatabaseUtils.list_docs()
  page_to_bigram_map = build_page_to_bigram_map(pages_raw_text, docs)
  doc_term_maps = build_relationshiop(page_to_bigram_map)

  for doc_term_map_entity in doc_term_maps:
    DatabaseUtils.insert_doc_term_map(doc_term_map_entity)

  return {
    'status': 200,
    'message': [map.to_json() for map in doc_term_maps]
  }