from sqlalchemy import create_engine
import pandas as pd

def get_and_load(cnn):
    # Create database
    cnn\
        .execution_options(isolation_level="AUTOCOMMIT")\
        .execute("CREATE database sales_db")

    # Load .csv files onto database
    names = ["accounts", "orders", "region", "sales_reps", "web_events"]
    for name in names:
        try:    
            n = pd.read_csv(f"../data/{name}.csv")
            n.to_sql(f"{name}", cnn, if_exists="append")
            print(f"Completed loading {name}.csv to sales_db")
        except Exception as error:
            print(f"Just got error in adding {name} to the database. Error: {error}")

    # Create connection: Alter tables
def main():
    '''
    Logging in the case of having no other user so imma put the things right her 
    '''
    try:
        engine = create_engine(f'postgresql://root:root@localhost:5432/')
        get_and_load(engine)
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        engine.dispose()

if __name__ == "__main__":
    main()