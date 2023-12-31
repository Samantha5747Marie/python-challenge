import csv
import os

file = os.path.join("Resources", "election_data.csv")
outfile = os.path.join("analysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate options and vote counters
candidate_option = []
candidate_votes = {}

# Winning 
winning_cand = ""
winning_count = 0

# Read the csv and convert to a list of dictionaries
with open(file) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # Loop the rows
    for row in reader:
        # Add the total vote count
        total_votes = total_votes + 1

        # Get the candidate name
        name = row[2]

        # If candidate does not match any existing candidates
        if name not in candidate_option:
            candidate_option.append(name)

            candidate_votes[name] = 0

        # Then add a vote to that cand count
        candidate_votes[name] = candidate_votes[name] + 1

# Print the results and export
with open(outfile, "w") as txt_file:
    # save the final vote count to the text file
    # Create some election results print statement
    election_results = "Total Votes: " + str(total_votes)
    txt_file.write(election_results)

    for candidate in candidate_votes:
        # Get the vote count and percentage
        votes = candidate_votes[candidate]
        vote_perc = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_cand = candidate

        # Print each candidates voter count and percentage (to terminal) 
        output = f"{candidate}: {vote_perc}% ({votes})"
        # Save each candidatess voter count and percent 
        txt_file.write(output)

    summary = (
        f"------------\n"
        f"Winner: {winning_cand}\n"
        f"-------------\n")
    
    print(summary)
    txt_file.write(summary)

print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
print("Charles Casper Stockham: ${candidate_votes}")
print("Diana DeGetter: ${candidate_votes}")
print("Raymon Anthony Doane: ${candidate_votes}")
print("-------------------------")
print("Winner: Diana DeGette")
