from DatabaseUtils import DatabaseUtils
from Entities.Doc import Doc


def test_insert_doc():
    DatabaseUtils.insert_doc(Doc('test_doc1', '''77944-fbaab
    b4a70-9d6f1
    9e0fb-456ff
    a361d-3b9b5
    26ab0-edd4c
    876c2-63600
    eac47-630b5
    23e3b-632a1
    ab4e0-f5d9d
    be467-cc634
    ee613-3bdf9
    1fe92-37b9c
    b0c9b-467bf
    6284a-2b819
    2f929-79efc
    4a6f0-0aaed''', 'taetsataestas'))


def test_insert_term():
    DatabaseUtils.insert_term('SVM')
    DatabaseUtils.insert_term('NLP')
    DatabaseUtils.insert_term('IDK')


def test_insert_doc_term_relationship():
    DatabaseUtils.insert_doc_term_relationship('test_doc1', 'NLP', 10)
    DatabaseUtils.insert_doc_term_relationship('test_doc1', 'SVM', 1)
