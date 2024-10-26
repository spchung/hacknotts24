from collections import defaultdict
from typing import List
from CommonUtils import CommonUtils
from DatabaseUtils import DatabaseUtils


class Graph:
    def __init__(self):
        self.topic_doc_dict = defaultdict(defaultdict)
        self.doc_topic_dict = defaultdict(defaultdict)

    def add_doc_2_graph(self, doc_name: str, topic_freq: List[tuple]):
        for topic, freq in topic_freq:
            DatabaseUtils.insert_doc_term_relationship(doc_name, topic, freq)

    def search_topics(self, query):
        return CommonUtils.fuzzy_search(query, DatabaseUtils.get_all_topics_from_db())


def test_graph():
    g = Graph()
    g.add_doc_2_graph("test", [('NLP', 104), ('SVM', 3), ('idk what to fill', 100)])
    g.add_doc_2_graph('file2', [('NLP', 1), ('idk what to fill', 1), ('ABCD', 134)])
    g.add_doc_2_graph('file3', [('NLP', 1), ('idk what to fill', 1), ('ABCD', 130),
                                ('brain cell killing while writing test case', 12)])
    g.add_doc_2_graph('filehaha', [('idk what to fill', 1), ('ABCD', 130), ('haha', 30)])
    assert (g.find_docs_by_topic('NLP')) == [('test', 104), ('file2', 1), ('file3', 1)]
    assert (g.find_docs_by_topic('ABCD')) == [('file2', 134), ('file3', 130), ('filehaha', 130)]
    assert (g.find_topic_by_doc('test')) == [('NLP', 104), ('idk what to fill', 100), ('SVM', 3)]
