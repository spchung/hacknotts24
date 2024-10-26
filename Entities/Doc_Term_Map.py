class DocTermMap:
  def __init__(self, doc_id, term, term_freq):
    self.doc_id = doc_id
    self.term = term
    self.term_freq = term_freq
  
  def to_json(self):
    return {
      "doc_id": self.doc_id,
      "term": self.term,
      "term_freq": self.term_freq
    }