# Import necessary modules
import csv
import os

#Define file paths for both Input and Output
file_to_load = os.path.join("Resources","election_data.csv") # Input file path
file_to_ouput = os.path.join("analysis","election_analysis.txt") # Output file path
#Initialize variables to track the election data
total_votes = 0 #Tracks the total number of votes cast
candidate_options = [] #Lists candidate names
candidate_votes = {} #Dictionary to tack votes for each candidate

#Winning candidate and winning count tracker
winning_candidate = "" #Tracks the winning candidate
winning_count = 0 #Tracks the winning vote count
winning_percentage = 0 #Tracks the winning vote percentage

#Open the CSV file and process it
with open(file_to_load) as election_data:
    reader=csv.reader(election_data)

    #skip the header row
    header=next(reader)

    #Loop through each row of the dataset and process it
    for row in reader:
    #Print a loading indicator(for larage datasets)
        print(".",end="")

        #Increment the total vote count for each row
        total_votes += 1

        #Get the candidate's name from the row
        candidate_name = row[2]

        #If the candidate is not already in the candidate lit, add them

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        #Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

#Open a text file to save the output
with open(file_to_ouput,"w") as txt_file:
    
    #Print the total vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes:{total_votes}\n"
        f"-------------------------\n")
    print(election_results,end="")

    #write the total vote count to the text file

    txt_file.write(election_results)

    #loop through the candidates to determine vote percentages and identify the winner

    for candidate in candidate_votes:

    #Get the vote count and calculate the percentage

        votes = candidate_votes[candidate]

        vote_percentage = (votes / total_votes) * 100

        #Update the winning candidate if this one has more votes

        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

        #Print and save each candidate's vote count and percentage
        candidate_results = (f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
        print(candidate_results, end="")
        txt_file.write(candidate_results)

    #Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"------------------------\n")
    print(winning_candidate_summary)
    
    #Save the winning candidate summary to the text file
    txt_file.write(winning_candidate_summary)