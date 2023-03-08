import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    #define variables
    months = set()
    total_profit_losses = 0 
    # read each row of data after the header
    for row in csvreader:
        #print(row) 
        month=row[0]
        profit_losses=int(row[1])
            
        months.add(month)
        total_profit_losses += profit_losses
    #total number of months included in the dataset- create a set to count months
    print("Financial Analysis\n")

    print("----------------------------------------------\n")
    
    #total number of months included in the dataset- create a set to count months
    print(f"Total Months: {len(months)}\n")

    #The net total amount of "Profit/Losses" over the entire period
    print(f"Total: ${total_profit_losses}\n")
    
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in profits (date and amount) over the entire period

    #In addition, your final script should both print the analysis to the terminal and export a text file with the results