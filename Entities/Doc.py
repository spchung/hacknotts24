import json


class Doc:
    def __init__(self, doc_name='', doc_content='', uuid=''):
        self.doc_name = doc_name
        self.doc_content = doc_content
        self.uuid = uuid

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)
    
    def to_json(self):
        return {
            "doc_name": self.doc_name,
            "doc_content": self.doc_content,
            "uuid": self.uuid
        }
