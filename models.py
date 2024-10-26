from Entities.Doc import Doc 

class PageModel:
  def __init__(self, page_id, title, content):
    self.title = title
    self.content = content
    self.page_id = page_id
  
  def to_json(self):
    return {
      "title": self.title,
      "content": self.content,
      "page_id": self.page_id
    }

  def to_doc_model(self):
    return Doc(doc_name=self.title, doc_content=self.content, uuid=self.page_id)