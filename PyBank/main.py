#Modules
import os
import csv
from pathlib import Path 
#Esteblishing path to the CSV file (relative path doesn't work in VSCode, so I used absolute path on my Mac, but submitted as relative)
csvpath = Path('budget_data.csv')
# Declaring arrays to iterate through csv columns of data
months = []
profit = []
change_profit = []
#Declaring variables for for-loop iterations
max_increase_value=0
max_decrease_value=0
# Open file with CSV module
with open(csvpath, newline='') as csvfile:
#Specifing delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#Skipping the header of the CSV file
    csv_header = next(csvreader)
#Printing the header of the report
    print("Financial Analysis")
    print("-------------------------")
#Filling arrays with month and profits columns
    for row in csvreader: 
        months.append(row[0])
        profit.append(int(row[1]))
#Printing the total number of months
    print("Total Months: " + str(len(months)))
#Calculating the sum of differences in profit/loss between adjacent periods
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
#Printing summery of profit/loss and the average of profit/loss between periods
    print("Total: $" + str (sum(profit)))
    print("Average Change: $" + str(round(sum(change_profit)/len(change_profit),2)))
#Iterating to find the greatest increase in profit over the entire period with the corresponding months
    for i in range(len(change_profit)):
        if change_profit[i]> max_increase_value:
            max_increase_value=change_profit[i]
            max_increase_month = months[i+1]
#Iterating to find the greatest decrease in profit over the entire period with the corresponding months
    for i in range(len(change_profit)):
        if change_profit[i]<max_decrease_value:
            max_decrease_value=change_profit[i]
            max_decrease_month = months[i+1]
#Printing the greatest increase and the greatest decrease in profit over the entire period
print("Greatest Increase in Profits: " + str(max_increase_month) + " ($" + str(max_increase_value) + ")")
print("Greatest Decrease in Profits: " + str(max_decrease_month) + " ($" + str(max_decrease_value) + ")")