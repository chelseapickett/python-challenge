import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # read each row of data after the header
    for row in csvreader:
        print(row) 
