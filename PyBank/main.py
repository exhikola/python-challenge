import csv

# First step is to declear the variables to store the data we need to get
total_months = 0
total = 0
profit_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# The function above helps to open dhe file and read it

with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # This function helps to skip the first row that is the header
  
    header = next(csvreader)
  
    #I have used the for loop to calculate the total months for all the rows.
  
    for row in csvreader:
        date = row[0] #Calculation done on the first column
        profit_loss = int(row[1]) #Calculation done on the second column
        
     # Calculate total months and net total
      
        total_months += 1
        total += profit_loss
        
     # Calculation of profit changes and finding the greatest increase/decrease
      
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_changes.append(change) #profit_changes is a list which stores the changes of the profit.
          
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]
        
        previous_profit_loss = profit_loss

# Calculation of the average profit changes

average_change = sum(profit_changes) / len(profit_changes)

# Print the results

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
