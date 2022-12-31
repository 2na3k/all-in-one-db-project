from sqlalchemy import create_engine

def main():
    try:
        engine = create_engine('postgresql://user:user_password@{}:5432/database'.format('service_name_of_postgres'))
    except: 
        return "Homie there was something"    

if __name__ == "__main__":
    main()