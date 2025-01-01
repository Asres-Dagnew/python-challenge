import csv
import os

#Define file paths for both Input and Output
file_to_load=os.path.join("Resources","budget_data.csv") # Input file path
file_to_output=os.path.join("analysis","budget_analysis.txt")# Output file path

#Define Variables to track the financial data
total_months = 0 #Initial variable to count the total number of motnhs
total_net = 0 #Initial variable to sum the total net amount

#Add more variables to track other necessary financial data
change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""
changes = []
previous_row = None

#Open and read the budget data file
with open(file_to_load) as financial_data:
    reader=csv.reader(financial_data)

     #Skip the header row
    header = next(reader)

     #Extract the first row to avoid appending to net change_list
    first_row = next(reader)

    total_months+=1
    total_net+=int(first_row[1])
    previous_row =int(first_row[1])
     #Loop through the remaining rows in the CSV file and track the total, net change,greatest increase in profits,
     # greatest decrease in losses and average net changes across the months.
    for row in reader:
          total_months+=1
          total_net+=int(row[1])
          if previous_row is not None:
            #Track the net change
            change = int(row[1])- previous_row
            changes.append(change)

            #Calculate the greatest increase in profits(month and amount)
            if change > greatest_increase:
               greatest_increase = change
               greatest_increase_month = row[0]
    
             #Calculate the greatest decrease in losses(month and amount)
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]
      
  
            previous_row = int(row[1])

    #Calculate the average net changes across the months and round it
    average_change = round(sum(changes) / len(changes),2) if changes else 0
    
    #Generate the output summary
  
    output = (
          "Financial Analysis\n"
          "--------------------\n"
          f"Total months = {total_months}\n"
          f"Total : ${total_net}\n"
          f"Average Channge : ${average_change}\n"
          f"Greatest Increase in Profits : {greatest_increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits : {greatest_decrease_month} (${greatest_decrease})\n"
        )
    
     #Print the output
    print(output)

    #Write the Results to a text file
    with open(file_to_output,"w")as text_file:
     text_file.write(output)