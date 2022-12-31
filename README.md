# All-in-one project: Visualization, SQL and Python for Sales database
I create this for applying for Data Analyst role, which would cover a lot of knowlege fields. And it's fun to do since I can choose the techstack.

### ERD
![ERD for the thing](erd.png)

### Techstack
Overall I use:
- Docker for creating PostgreSQL container, in the port `localhost:5432`.
- DuckDB: For SQL interface to query from both SQLite and PostgreSQL.
- SQLAlchemy for creating ingestion pipeline to the database.
- PowerBI: Porting directly from Postgres containter for data visualization.



### How it works
- For SQLite: Check the `script/init_lite.py` for the ingestion pipeline and `notebook/queries.ipynb` for SQL queries and visualization with Seaborns. Data will be saved in `sales.db` file.
- For PostgreSQL: From the root of the directory, run `docker compose up`, and run the `script/init_postgres.py` to load the whole database.
- For visualization: Check the `sales_dashboard.pbix` file (using PowerBI).

To install the dependencies, run 'pip install -r requirements.txt' in the root folder.

### What I did
I don't have much time so I will explain my work here:
- Using Python script to initiate the database, and load the `.csv` files as tables.
- Using PowerBI to do the dashboard.
- Extracting information from the database to Jupyter notebook, and querying directly from the SQL database for the result. 
- (If okay) Using some kinds of method to do the ML.
- (If okay) Using Docker to create the container for the PostgreSQL database, and use the script for doing other extractions.