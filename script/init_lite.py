'''
Initiative script for the SQLite database, cuz it's lightweight as hell
'''

import pandas as pd 
import sqlite3

# Main function
def main():
    # Create connection and cursor
    cnn = sqlite3.connect('../sales.db')
    # cursor = cnn.cursor()

    # Load the .csv files into SQLite database
    # Later please try use try/except/finally to deal with errors
    names = ["accounts", "orders", "region", "sales_reps", "web_events"]
    for name in names:
        try:    
            n = pd.read_csv(f"../data/{name}.csv")
            n.to_sql(f"{name}", cnn)
            print(f"Completed loading {name}.csv to sales.db")
        except sqlite3.Error as error:
            print(f"Just got error in adding {name} to the database. Error: {error}")
    # Oops I've just realized that SQLite does not support adding constraint by alter table so ye, next time


# Usual things: main program
if __name__ == "__main__":
    main()