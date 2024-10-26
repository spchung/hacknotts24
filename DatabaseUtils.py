import sqlite3


class DatabaseUtils:
    @staticmethod
    def execute_query(query, args=None):
        try:
            # Connect to the database
            connection = sqlite3.connect('hacknoooooootts.db')

            # Create a cursor to execute the query
            cursor = connection.cursor()
            if args is not None:
                cursor.execute(query, args)
            else:
                cursor.execute(query)

            # If it’s a SELECT query, fetch the results
            if query.strip().lower().startswith("select"):
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
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
                                    'FOREIGN KEY(TERM_ID) REFERENCES TERMS(TERM_ID));')

    @staticmethod
    def insert_doc(doc_name, doc_CONTENT):
        id = DatabaseUtils.query_doc_id(doc_name)
        if id is not None:
            DatabaseUtils.execute_query(
                "UPDATE DOCS SET DOC_CONTENT = '{}' WHERE DOC_NAME = '{}'".format(doc_CONTENT, doc_name))
            return id
        else:
            DatabaseUtils.execute_query("INSERT INTO DOCS (DOC_NAME, DOC_CONTENT) VALUES (?, ?)",
                                        (doc_name, doc_CONTENT))
            return DatabaseUtils.query_doc_id(doc_name)

    @staticmethod
    def query_doc_id(doc_name):
        try:
            return DatabaseUtils.execute_query("SELECT DOC_ID FROM DOCS WHERE DOC_NAME = '{}';".format(doc_name))
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
            DatabaseUtils.execute_query("INSERT INTO TERMS (TERM) VALUES (?)", (term_name,))
            return DatabaseUtils.query_term_id(term_name)

    @staticmethod
    def query_term_id(term_name):
        try:
            return DatabaseUtils.execute_query("SELECT TERM_ID FROM TERMS WHERE TERM = '{}';".format(term_name))
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def insert_doc_term_relationship(doc_name, term, freq):
        try:
            doc_id = DatabaseUtils.query_doc_id(doc_name)
            if doc_id is None:
                return
            term_id = DatabaseUtils.query_term_id(term)
            if term_id is None:
                return
            DatabaseUtils.execute_query("INSERT INTO DOC_TERM_MAP (DOC_ID, TERM_ID, FREQ) VALUES (?, ?, ?)",
                                        (doc_id, term, freq))
        except Exception as e:
            print(e)

    @staticmethod
    def get_all_terms_from_db():
        return DatabaseUtils.execute_query('SELECT TERM FROM TERMS')

    @staticmethod
    def get_raw_text_from_db():
        return ''.join(DatabaseUtils.execute_query('SELECT DOC_CONTENT FROM DOCS'))
