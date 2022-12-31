'''Using for testing the relationships things, independently'''

from sqlalchemy import text, create_engine

cnn = create_engine(f'postgresql://root:root@localhost:5432/')

with open("relationships.sql") as file:
        try: 
            query = text(file.read())
            cnn.execute(query)
        except Exception as ex:
            print(f"You're done bois, error: {ex}")