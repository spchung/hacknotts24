from typing import List

from CommonUtils import CommonUtils
from DatabaseUtils import DatabaseUtils
from Entities.Doc import Doc


class Graph:
    def __init__(self):
        pass

    @staticmethod
    def add_doc_2_graph(doc_name: str, term_freq: List[tuple]):
        for term, freq in term_freq:
            DatabaseUtils.insert_doc_term_relationship(doc_name, term, freq)

    @staticmethod
    def search_terms(query):
        return CommonUtils.fuzzy_search(query, DatabaseUtils.get_all_terms_from_db())

    @staticmethod
    def get_terms_by_doc_simple(doc):
        query = "SELECT term_id FROM DOC_TERM_MAP WHERE doc_id like '%{}%' ORDER BY FREQ DESC".format(doc)
        return DatabaseUtils.execute_query(query)

    @staticmethod
    def get_doc_by_term_simple(term):
        query = "SELECT doc_id FROM DOC_TERM_MAP WHERE term_id = '{}' ORDER BY FREQ DESC".format(term)
        return [i[0] for i in DatabaseUtils.execute_query(query)]

    @staticmethod
    def get_terms_by_doc(doc_name):
        doc_id = DatabaseUtils.query_doc_id(doc_name)
        if doc_id is None:
            print('doc not found!')
            return []
        query = "SELECT term_id FROM DOC_TERM_MAP WHERE doc_id = '{}' ORDER BY FREQ DESC".format(doc_id)
        term_ids = DatabaseUtils.execute_query(query)
        ans = []
        for term_id in term_ids:
            q = "SELECT TERM FROM TERMS WHERE term_id = '{}'".format(term_id)
            ans.append(DatabaseUtils.execute_query(q))
        return ans

    @staticmethod
    def get_docs_by_term(term):
        term_id = DatabaseUtils.query_term_id(term)
        if term_id is None:
            print('term not found!')
            return []
        query = "SELECT doc_id FROM DOC_TERM_MAP WHERE term_id = '{}' ORDER BY FREQ DESC".format(term_id)
        doc_ids = [i[0] for i in DatabaseUtils.execute_query(query)]
        ans = []
        for doc_id in doc_ids:
            q = "SELECT * FROM DOCS WHERE doc_id = '{}'".format(doc_id)
            row = DatabaseUtils.execute_query(q)[0]
            ans.append(Doc(row[2], row[3], row[1]))
        return ans
