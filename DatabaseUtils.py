import sqlite3

from Entities.Doc import Doc
from Entities.Doc_Term_Map import DocTermMap


class DatabaseUtils:
    @staticmethod
    def execute_query(query):
        try:
            # Connect to the database
            connection = sqlite3.connect('hacknoooooootts.db')

            # Create a cursor to execute the query
            cursor = connection.cursor()
            cursor.execute(query)

            # If it’s a SELECT query, fetch the results
            if query.strip().lower().startswith("select"):
                rows = cursor.fetchall()
                return rows
            else:
                connection.commit()  # Commit for non-SELECT queries (e.g., INSERT, UPDATE)
                print("Query executed successfully.")

            # Close cursor and connection
            cursor.close()
            connection.close()
            print("Connection closed.")

        except Exception as e:
            print("Error connecting to Supabase:", e)

    @staticmethod
    def create_tables():
        DatabaseUtils.execute_query('CREATE TABLE IF NOT EXISTS DOCS ('
                                    'DOC_ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                                    'UUID TEXT NOT NULL,'
                                    'DOC_NAME TEXT NOT NULL UNIQUE,'
                                    'DOC_CONTENT TEXT);')
        DatabaseUtils.execute_query('CREATE TABLE IF NOT EXISTS TERMS ('
                                    'TERM_ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                                    'TERM TEXT NOT NULL);')
        DatabaseUtils.execute_query('CREATE TABLE IF NOT EXISTS DOC_TERM_MAP ('
                                    'DOC_ID INTEGER,'
                                    'TERM_ID INTEGER,'
                                    'FREQ INTEGER,'
                                    'FOREIGN KEY(DOC_ID) REFERENCES DOCS(DOC_ID),'
                                    'FOREIGN KEY(TERM_ID) REFERENCES TERMS(TERM_ID),'
                                    'UNIQUE (DOC_ID, TERM_ID));')

    @staticmethod
    def insert_doc(doc: Doc):
        id = DatabaseUtils.query_doc_id(doc.doc_name)
        if id:
            DatabaseUtils.execute_query(
                "UPDATE DOCS SET DOC_CONTENT = '{}' WHERE DOC_NAME = '{}'".format(doc.doc_content, doc.doc_name))
            DatabaseUtils.execute_query(
                "UPDATE DOCS SET UUID = '{}' WHERE DOC_NAME = '{}'".format(doc.uuid, doc.doc_name))
            return id
        else:
            DatabaseUtils.execute_query(
                "INSERT INTO DOCS (DOC_NAME, DOC_CONTENT, UUID) VALUES ('{}', '{}', '{}')"
                .format(doc.doc_name, doc.doc_content, doc.uuid))
            return DatabaseUtils.query_doc_id(doc.doc_name)

    @staticmethod
    def query_doc_id(doc_name):
        try:
            return DatabaseUtils.execute_query("SELECT DOC_ID FROM DOCS WHERE DOC_NAME = '{}';".format(doc_name))[0][0]
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def insert_term(term_name):
        id = DatabaseUtils.query_term_id(term_name)
        if id is not None:
            DatabaseUtils.execute_query("UPDATE TERMS SET TERM = '{}' WHERE TERM_ID = '{}';".format(term_name, id))
            return id
        else:
            DatabaseUtils.execute_query("INSERT INTO TERMS (TERM) VALUES ('{}')".format(term_name, ))
            return DatabaseUtils.query_term_id(term_name)

    @staticmethod
    def query_term_id(term_name):
        try:
            return DatabaseUtils.execute_query("SELECT TERM_ID FROM TERMS WHERE TERM = '{}';".format(term_name))[0][0]
        except Exception as e:
            print(e)
            return None

    @DeprecationWarning
    @staticmethod
    def insert_doc_term_relationship(doc_name, term, freq):
        try:
            doc_id = DatabaseUtils.query_doc_id(doc_name)
            if doc_id is None:
                return
            term_id = DatabaseUtils.query_term_id(term)
            if term_id is None:
                return
            # val = DatabaseUtils.execute_query("SELECT FREQ FROM DOC_TERM_MAP "
            #                                   "WHERE DOC_ID = '{}' AND TERM_ID = '{}';".format(doc_id, term_id))
            # if val:
            #     freq += val[0][0]
            #     DatabaseUtils.execute_query("UPDATE DOC_TERM_MAP set FREQ = '{}' WHERE DOC_ID = '{}' AND TERM_ID = '{}'"
            #                                 .format(freq, doc_id, term_id))
            # else:
            DatabaseUtils.execute_query("INSERT INTO DOC_TERM_MAP (DOC_ID, TERM_ID, FREQ) VALUES ('{}', '{}', '{}')"
                                        .format(doc_id, term_id, freq))
        except Exception as e:
            print(e)

    @staticmethod
    def get_all_terms_from_db():
        return [i[0] for i in DatabaseUtils.execute_query('SELECT TERM FROM TERMS')]

    @staticmethod
    def get_raw_text_from_db():
        docs = DatabaseUtils.execute_query('SELECT DOC_CONTENT FROM DOCS')
        return [doc[0] for doc in docs]
    
    @staticmethod
    def list_docs():
        docs = DatabaseUtils.execute_query('SELECT * FROM DOCS')
        res = []
        for doc in docs:
            id, uuid, name, content,  = doc
            res.append(
                Doc(doc_name=name, doc_content=content, uuid=uuid)
            )
        return res
    
    @staticmethod
    def insert_doc_term_map(docTermMap: DocTermMap):
        doc_id = docTermMap.doc_id
        term = docTermMap.term
        freq = docTermMap.term_freq
        val = DatabaseUtils.execute_query("SELECT FREQ FROM DOC_TERM_MAP "
                                              "WHERE DOC_ID = '{}' AND TERM_ID = '{}';".format(doc_id, term))
        if val:
            DatabaseUtils.execute_query("UPDATE DOC_TERM_MAP set FREQ = '{}' WHERE DOC_ID = '{}' AND TERM_ID = '{}'".format(freq, doc_id, term))
        else:
            DatabaseUtils.execute_query("INSERT INTO DOC_TERM_MAP (DOC_ID, TERM_ID, FREQ) VALUES ('{}', '{}', '{}')"
                                        .format(doc_id, term, freq))

        return True
    
