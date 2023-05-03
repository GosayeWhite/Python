#import file
from pathlib import Path
import csv
#open and read

csvpath=Path('Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:
    election_data=csv.reader(csvfile, delimiter=',')
    csv_header = next(election_data)

#set variables
    canditate_votes=[]
    total_votes=[]

#calculate total votes
    output= f'Election Results \n-----------------------------\n'
    for x in election_data:
        total_votes.append(x[2])
        total_count=len(total_votes)
    output= output + str(total_count)  + "\n----------------------------- \n"

#find votes per candidate
    candidates=list(set(total_votes))
    vote_percentage=[]
    votes_per_candidate=[]
    for candidate in candidates:
        votes_per_candidate.append(total_votes.count(candidate))

#find percentage of votes for each candidate
for i in range (len(candidates)):
    vote_percentage=round(votes_per_candidate[i]/total_count*100,3)

    output= output +f'{candidates[i]}: {vote_percentage}% ({votes_per_candidate[i]}) \n'

#find the winner 
winner=candidates[votes_per_candidate.index(max(votes_per_candidate))]
output= output+f'-----------------------------\n Winner: {winner} \n'
output=output + f'-----------------------------'

#export and save as a text file

csvpath=Path("Analysis", 'Final Analysis.txt')
with open(csvpath,"w") as textfile:
   textfile.write(output)



