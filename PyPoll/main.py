# Evgeniia Kozodeeva
import os, csv
#File path
PyPoll_file = os.path.join("Resources","election_data.csv")

# Set veriables
total_number_votes = 0
candidate_votes = {}
candidate_list = []
votes_count = []
percentage_voted = []
winner = ""
winner_votes_count = 0
cleaned_output = []

# Read the file
with open(PyPoll_file,"r",newline="") as csvfile:
    pypoll = csv.reader(csvfile,delimiter= ",")
    file_header = next(pypoll)

    # Check each row in this file
    for row in pypoll:
        # Count total number of votes
        total_number_votes += 1

        # Set row[2] as candidate name (no need Header)
        candidate_name = row[2]

        # If name is in the list, then get the vote count
        if candidate_name in candidate_list:
            candidate_votes[candidate_name] += 1   
        # If name is not in the list, put the name in the list 
        else:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 1     


        # Get the percentage of votes each candidate won
    for win, value in candidate_votes.items():
        votes_count.append(value)
        votes = candidate_votes[candidate_name]
        percentage_v = round((int(value)/ total_number_votes * 100),3)
        percentage_voted.append(percentage_v)

        # Determine the winner by comparing votes count for each candidate
        if (value > winner_votes_count):
            winner_votes_count = value
            winner= win
    # Combine 3 lists as 1 list to print
    cleaned_output = zip(candidate_list,percentage_voted, votes_count)
    cleaned_output = list(cleaned_output)  

# Export the result
result = os.path.join("analysis", "PyPoll_result1.txt")
with open(result,"w",newline="") as datafile:
    csvresult = csv.writer(datafile)

    csvresult.writerow(["Election Results"])
    csvresult.writerow(["-------------------------"])
    csvresult.writerow([f'Total Votes :  {total_number_votes}'])
    csvresult.writerow(["-------------------------"])
    for item in cleaned_output:
        csvresult.writerow([f'{item[0]} : {item[1]}% ({item[2]})'])
    csvresult.writerow(["-------------------------"])
    csvresult.writerow([f'Winner : {winner}'])
    csvresult.writerow(["-------------------------"])


 # the result in csv
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes :  {total_number_votes}')
    print("-------------------------")
    for item in cleaned_output:
        print(f'{item[0]} : {item[1]}% ({item[2]})')
    print("-------------------------")
    print(f'Winner : {winner}')
    print("-------------------------")