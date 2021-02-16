import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as file_object:
    csvreader = csv.reader(file_object, delimiter=",")
    csvheader = next(csvreader)
    
    voter_id = []
    county = []
    voted_for = []

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        voted_for.append(row[2])

tot_votes = len(voter_id)
zipper = zip(voter_id, county, voted_for)
zip_list = list(zipper)

votes = [0,0,0,0]
candidate = []
for x in zip_list:
    if x[2] == "Khan":
        votes[0] += 1
    elif x[2] == "Correy":
        votes[1] += 1
    elif x[2] == "Li":
        votes[2] += 1
    else:
        votes[3] += 1

khan = (votes[0]/tot_votes) * 100
correy = (votes[1]/tot_votes) * 100
li = (votes[2]/tot_votes) * 100
tool = (votes[3]/tot_votes) * 100

winner = max(votes)

print(f'\nTotal Votes:  {tot_votes}')
print(f'\nKhan:          {round(khan,4)}% ({votes[0]})')
print(f'Correy:        {round(correy,4)}% ({votes[1]})')
print(f'Li:            {round(li,4)}% ({votes[2]})')
print(f"O'Tooley:      {round(tool,4)}%  ({votes[3]})")
print(f"Winner:    {winner}")
print("\n")
