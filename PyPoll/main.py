#Modules
import os
import csv
from pathlib import Path 
#Esteblishing path to the CSV file (relative path doesn't work in VSCode, so I used absolute path on my Mac, but submitted as relative)
csvpath = Path('election_data.csv')
# Declaring arrays to iterate through csv columns of data
votes = []
cadidates = []
unique_candidates = []
number_unique_candidates = []
#declaring variables for for-loop iterations
number=0
max_votes=0
candidate_name=""
precentage=0
# Open file with CSV module
with open(csvpath, newline='') as csvfile:
#Specifing delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#Skipping the header of the CSV file
    csv_header = next(csvreader)
#Appending the total number of votes (since the number of voter IDs in column[0]is the same as the number of Candidates in row[2], we can use row[2] to calculate the total number of votes)
    for row in csvreader: 
        cadidates.append(row[2])
#Using len function to calculate the total number of votes
    total_votes = len(cadidates)
#Printing the Header and the total number of votes 
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " +str(total_votes))
    print("-------------------------")
#Appending names of condidates into a new arrey
    for i in cadidates:
        if i not in unique_candidates:
            unique_candidates.append(i)

#loop through all unique candidates
    for i in range(len(unique_candidates)):
        number=0
#Using the data (names) from the "unique_candidates" arrey to iterate through the "candidates" colummn and calculate their number of votes 
        for x in range(len(cadidates)):
            if unique_candidates[i]==cadidates[x]:
                number=number+1
 #Iterating to find  a condidate with the max number of votes and puling the name of this candidate      
        if max_votes<number:
             max_votes=number
             candidate_name=unique_candidates[i]
#Calculating percentage of total votes each candidate received 
        precentage=precentage+number/total_votes*100
#Printing the list of candidates with their percentage of votes along with the number of votes in specified formate 
        print(str(unique_candidates[i])+ ": " + str("%.3f%%" % round(number/total_votes*100)) + " (" + str(number) + ")")

#Printing the name of the candidete who won the election
    print("-------------------------")
    print("Winner: " + str(candidate_name))
    print("-------------------------")

with open('election_results.txt', 'w') as text:
    text.write("Election Results"+ "\n")
    text.write("-------------------------\n")
    text.write("Total Votes: " + str(total_votes) + "\n")
    text.write("-------------------------\n")
    for i in range(len(unique_candidates)):
        text.write(str(unique_candidates[i])+ ": " + str("%.3f%%" % round(number/total_votes*100)) + " (" + str(number) + ")" +"\n")
    text.write("-------------------------\n")
    text.write("Winner: " + str(candidate_name) + "\n")
    text.write("-------------------------\n")



