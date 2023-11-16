import csv
import os

# Get the absolute path to the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the absolute path to the CSV file
csv_file_path = os.path.join(script_dir, 'budget_data.csv')

# Initialization of variables to store the data we need to get
total_months = 0
total = 0
profit_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Open the file using the absolute path
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # This function helps to skip the first row that is the header
    header = next(csvreader)
  
    # I have used the for loop to calculate the total months for all the rows.
    for row in csvreader:
        date = row[0]  # Calculation done on the first column
        profit_loss = int(row[1])  # Calculation done on the second column

        # Calculate total months and net total
        total_months += 1
        total += profit_loss

        # Calculation of profit changes and finding the greatest increase/decrease
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_changes.append(change)  # profit_changes is a list which stores the changes of the profit.
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]

        previous_profit_loss = profit_loss

# Calculation of the average profit changes
average_change = sum(profit_changes) / len(profit_changes)

# Print the results to the console
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Output file path
output_file = 'financial_analysis.txt'

# Write the results to a text file
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(f"Results exported to {output_file}")
