import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # store/skip the header row
    csv_header = next(csvreader)
    
    #define variables
    candidates=set()
    counties=[]
    total_votes=0
    candidate_vote_counts = {}
    
    # read each row of data after the header
    for row in csvreader:
        county_id=int(row[0])
        county=row[1]
        candidate=row[2]
        #for each row add 1 to the total votes
        total_votes = total_votes +1
        #add unique candidates to set
        candidates.add(candidate) 
    
        if candidate in candidate_vote_counts: 
            candidate_vote_counts[candidate] +=1
        else: 
            candidate_vote_counts[candidate]=1



    print("Election Results\n")

    print("----------------------------------------------\n")
    
    # The total number of votes cast
    print(f"Total Votes: {total_votes}\n")

    print("----------------------------------------------\n")
    
    # A complete list of candidates who received votes
    print(candidates)
   
    # The total number of votes each candidate won
    print(candidate_vote_counts)
    
    
    # The percentage of votes each candidate won

    # The winner of the election based on popular vote

    # Final script should both print the analysis to the terminal and export a text file with the results