import os
import csv

# Create variable for file path and output path
csvpath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("Analysis", "election_analysis.txt")

# Convert CSV file into date to interpret with python
with open(csvpath) as file_object:
    csvreader = csv.reader(file_object, delimiter=",")
    csvheader = next(csvreader)
    
    # list to store individual voter information
    voter_id = []
    county = []
    voted_for = []

    # for loop to append information into list above
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        voted_for.append(row[2])

# total votes
tot_votes = len(voter_id)

# For loop to find number and name of candidates running for office
candidates = []
for y in voted_for:
    if y in candidates:
        continue
    else:
        candidates.append(y)

# Zip 3 lists from csv file into 1 list
zipper = zip(voter_id, county, voted_for)
zip_list = list(zipper)

# list to add number of votes per candidate (Khan, Correy, Li, O'Tooley)
votes = [0,0,0,0]

# for loop to add votes per candidate
for x in zip_list:
    if x[2] == "Khan":
        votes[0] += 1
    elif x[2] == "Correy":
        votes[1] += 1
    elif x[2] == "Li":
        votes[2] += 1
    else:
        votes[3] += 1

# percentage of votes for each candidate
khan = (votes[0]/tot_votes) * 100
correy = (votes[1]/tot_votes) * 100
li = (votes[2]/tot_votes) * 100
tool = (votes[3]/tot_votes) * 100

# Zip list together to find out winner of election
zip_list2 = zip(candidates,votes)
zipper2 = list(zip_list2)

# Winner of election
for z in zipper2:
    if z[1] == max(votes):
        winner = z[0]


print("\nElection Results")
print("_______________________________")
print(f'\nTotal Votes:  {tot_votes}')
print("_______________________________")
print(f'\n{candidates[0]}:          {round(khan,4)}% ({votes[0]})')
print(f'{candidates[1]}:        {round(correy,4)}% ({votes[1]})')
print(f'{candidates[2]}:            {round(li,4)}% ({votes[2]})')
print(f"{candidates[3]}:      {round(tool,4)}%  ({votes[3]})")
print("_______________________________")
print(f"\nWinner:        {winner}")
print("\n")


with open(output_path, 'w') as results:
    csvwriter = csv.writer(results)
    
    csvwriter.writerow(["\nElection Results"])
    csvwriter.writerow(["_______________________________"])
    csvwriter.writerow([f'\nTotal Votes:  {tot_votes}'])
    csvwriter.writerow(["_______________________________"])
    csvwriter.writerow([f'\n{candidates[0]}:          {round(khan,4)}% ({votes[0]})'])
    csvwriter.writerow([f'{candidates[1]}:        {round(correy,4)}% ({votes[1]})'])
    csvwriter.writerow([f'{candidates[2]}:            {round(li,4)}% ({votes[2]})'])
    csvwriter.writerow([f"{candidates[3]}:      {round(tool,4)}%  ({votes[3]})"])
    csvwriter.writerow(["_______________________________"])
    csvwriter.writerow([f"\nWinner:        {winner}"])
    
