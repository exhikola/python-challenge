import csv

# Initialization of variables to store the data and statistics
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Step to read the CSV file
with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skipping the header row that has no data
    header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Output file path
output_file = 'election_results.txt'

# Write the results to a text file
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    # Calculate and write the results for each candidate
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        # Determine the winner
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

# Print a message indicating that the results have been exported
print("Election results exported to 'election_results.txt'")

