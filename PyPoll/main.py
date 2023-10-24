import csv

# Initialize variables to store the data and statistics
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Print the total number of votes
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the results for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Determine the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
