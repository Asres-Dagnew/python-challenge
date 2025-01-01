# python-challenge
Python-challenge has two parts: PyBank and PyPoll.
## PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
Your task is to create a Python script that analyzes the records to calculate each of the following values:
1. The total number of months included in the dataset
2. The net total amount of "Profit/Losses" over the entire period
3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
4. The greatest increase in profits (date and amount) over the entire period
5.  The greatest decrease in profits (date and amount) over the entire period
In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# PyPoll Instructions
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
1. The total number of votes cast
2. A complete list of candidates who received votes
3.  The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote
In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#Budget Data Analysis
This section performs analysis of the budget data using a CSV file. The script processes the budget data to calculate the total number of months, the total net amount of profits/loss, the average net changes over the months and the months with the greatest increase and decrease in profits.
The analysis has the following parts:
1. Analysis: This is the output text file containing the results of the budget data analysis.
2. Resources: This is the input CSV file containing the budget data.
3. Main.py: This is the main python script used to perform the analysis.
#Budget Data Analysis Result
The analysis results the following output:
Financial Analysis
--------------------
1. Total Months = 86
2. Total: $22564198
3. Average Change: $-8311.11
4. Greatest Increase in Profits: Aug-16 ($1862002)
5. Greatest Decrease in Profits: Feb-14 ($-1825558)
#Election Data Analysis
This part performs an election data analysis using a CSV file of the voting data. The script processes the voting data to calculate the total number of votes cast, the list of candidates who received votes, the percentage of votes each candidate won, and the winner of the election based on the popular votes.
The analysis has the following parts:
1. Analysis: This is the output text file containing the results of the election data analysis.
2. Resources: This part contains the input CSV file containing the election data.
3. Main.py: This is the main python script used to perform the analysis.

#Election Data Analysis Result
The analysis results the following output:

             Election Results
             -----------------------------------------
1. Total Votes:369711
            ------------------------------------------------------
2. Charles Casper Stockham: 23.049% (85213)
3. Diana DeGette: 73.812% (272892)
4. Raymon Anthony Doane: 3.139% (11606)
            ----------------------------------------------
5. Winner: Diana DeGette
            --------------------------------
