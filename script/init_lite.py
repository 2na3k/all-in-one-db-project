'''
Initiative script for the SQLite database, cuz it's lightweight as hell
'''

import pandas as pd 
import sqlite3

# Main function
def main():
    # Create connection 
    cnn = sqlite3.connect('../sales.db')

    # Load the .csv files into SQLite database
    names = ["accounts", "orders", "region", "sales_reps", "web_events"]
    for name in names:
        n = pd.read_csv(f"../data/{name}.csv")
        n.to_sql(f"{name}", cnn)
        print(f"Completed loading {name}.csv to sales.db")

    # Relationship creation

# Usual things: main program
if __name__ == "__main__":
    main()