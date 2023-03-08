import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'budget_data.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    #define variables
    months = set()
    changes_profit_losses = []
    total_profit_losses = 0 
    previous_profit_losses = None
    max_difference_date = None
    min_difference_date = None
    max_difference = None
    min_difference = None

    # read each row of data after the header
    for row in csvreader:
        #print(row) 
        month=row[0]
        profit_losses=int(row[1])
            
        months.add(month)

        #adds the profit losses together through each iteration
        total_profit_losses += profit_losses

        #calculates the difference between the previous row and the current row
        if previous_profit_losses != None:
            difference = profit_losses - previous_profit_losses 
            #each time difference is calculated it will be added to the changes_profit_loss list
            changes_profit_losses.append(difference)
            #find max_difference
            if max_difference == None or difference > max_difference:
                max_difference = difference
                max_difference_date = month
            #find min_difference
            if min_difference == None or difference < min_difference:
                min_difference = difference
                min_difference_date = month
        # saves the previous row value to start with that on next row iteration
        previous_profit_losses = profit_losses 
    
    def average (list_of_numbers):
        length = len(list_of_numbers)
        total = 0
        for number in list_of_numbers:
            total += number
        return total / length
    

    print("Financial Analysis\n")

    print("----------------------------------------------\n")
    
    #total number of months included in the dataset- create a set to count months
    print(f"Total Months: {len(months)}\n")

    #The net total amount of "Profit/Losses" over the entire period
    print(f"Total: ${total_profit_losses}\n")

    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    print(f"Average Change: ${round(average(changes_profit_losses),2)}\n")
          
    #The greatest increase in profits (date and amount) over the entire period
    print(f"Greatest Increase in Profits: {max_difference_date} (${max_difference})\n")
    
    #The greatest decrease in profits (date and amount) over the entire period
    print(f"Greatest Decrease in Profits: {min_difference_date} (${min_difference})")

    #In addition, your final script should both print the analysis to the terminal and export a text file with the results
