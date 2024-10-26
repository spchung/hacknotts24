import sqlite3


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
                                    'DOC_NAME TEXT NOT NULL,'
                                    'DOC_CONTEXT TEXT);')
        DatabaseUtils.execute_query('CREATE TABLE IF NOT EXISTS TERMS ('
                                    'TERM_ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                                    'TERM TEXT NOT NULL);')
        DatabaseUtils.execute_query('CREATE TABLE IF NOT EXISTS DOC_TERM_MAP ('
                                    'DOC_ID INTEGER,'
                                    'TERM_ID INTEGER,'
                                    'FREQ INTEGER,'
                                    'FOREIGN KEY(DOC_ID) REFERENCES DOCS(DOC_ID),'
                                    'FOREIGN KEY(TERM_ID) REFERENCES TERMS(TERM_ID));')


# Example usage:
# Replace "your_table" with the actual table name in your Supabase database
DatabaseUtils.create_tables()
DatabaseUtils.execute_query("SELECT name FROM sqlite_master WHERE type='table';")
