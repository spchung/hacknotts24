from collections import defaultdict
from typing import List

from scipy.stats import ansari

from CommonUtils import CommonUtils
from DatabaseUtils import DatabaseUtils


class Graph:
    def __init__(self):
        pass

    def add_doc_2_graph(self, doc_name: str, term_freq: List[tuple]):
        for term, freq in term_freq:
            DatabaseUtils.insert_doc_term_relationship(doc_name, term, freq)

    def search_terms(self, query):
        return CommonUtils.fuzzy_search(query, DatabaseUtils.get_all_terms_from_db())

    def get_terms_by_doc(self, doc_name):
        doc_id = DatabaseUtils.query_doc_id(doc_name)
        if doc_id is None:
            print('doc not found!')
            return []
        query = 'SELECT term_id FROM DOC_TERM_MAP WHERE doc_id = ? ORDER BY FREQ DESC'
        term_ids = DatabaseUtils.execute_query(query, (doc_id,))
        ans = []
        for term_id in term_ids:
            q = 'SELECT TERM FROM TERMS WHERE term_id = ?'
            ans.append(DatabaseUtils.execute_query(q, term_id))
        return ans

    def get_docs_by_term(self, term):
        term_id = DatabaseUtils.query_term_id(term)
        if term_id is None:
            print('term not found!')
            return []
        query = 'SELECT doc_id FROM DOC_TERM_MAP WHERE term_id = ? ORDER BY FREQ DESC'
        doc_ids = DatabaseUtils.execute_query(query, (term_id,))
        ans = []
        for doc_id in doc_ids:
            q = 'SELECT doc_ FROM DOC_TERM_MAP WHERE doc_id = ?'
            ans.append(DatabaseUtils.execute_query(q, doc_id))
        return ans
