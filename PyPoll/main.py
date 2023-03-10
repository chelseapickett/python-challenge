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
    winning_counts = 0
    winning_candidate=""
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

    for candidate in candidates:
        #print(candidate)
        votes = candidate_vote_counts.get(candidate)
        percentage_of_votes = (votes/total_votes) *100 
        # A complete list of candidates who received votes, percentage of votes each candidate won, total number of votes each candidate won
        print(f"{candidate}: {round(percentage_of_votes,3)}% ({votes})\n")

        if votes > winning_counts:
            winning_counts = votes
            winning_candidate = candidate
    
    print("----------------------------------------------\n")
    # The winner of the election based on popular vote
    print(f"Winner: {winning_candidate}\n")     
    
    print("----------------------------------------------\n")
    
# Final script should both print the analysis to the terminal and export a text file with the results

poll_analysis = os.path.join(dirname, 'Analysis', 'election_results.csv')

with open(poll_analysis, 'w') as csvfile:
    
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Total Votes:", "Winner:"])
    
    csvwriter.writerow([total_votes, winning_candidate])

    csvwriter.writerow([f"{candidate}: {round(percentage_of_votes,3)}% ({votes})\n"])

    


