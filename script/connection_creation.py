from sqlalchemy import text, create_engine

cnn = create_engine(f'postgresql://root:root@localhost:5432/')

with open("connections.sql") as file:
        try: 
            query = text(file.read())
            cnn.execute(query)
        except Exception as ex:
            print(f"You're done bois, error: {ex}")