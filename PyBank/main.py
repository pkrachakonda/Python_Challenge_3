import os, csv # Importing OS and CSV modules required for the analysis

# Defining lists for storing data
date = []
values = []

# Reading csv file located in the resource folder with csv module and saving the column data to lists
with open(os.path.join("Resources", "budget_data.csv"), newline="") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        date.append(row["Date"])
        values.append(float(row["Profit/Losses"]))

# Defining variables and a empty list
    total = 0
    change = 0
    count = 0
    diff = []

# Procedure for calculating total months, total and average change in profit/losses for the entire duration

    for i in range(0, len(values)):
        total = total + values[i]                       # Calculating the final sum of profit and losses
        if i >= 1:
            diff.append(values[i] - values[i - 1])      # estimating difference in value between two rows and adding that value to Diff list
            change = change + float(diff[i - 1])        # estimating the total change in profit/losses at the current row
        count += 1                                      # counting total months in the csv file
    average_change = round((change / (count - 1)),2)    # estimating the average change and rounding the decimals to two places

# Procedure for estimating Greatest and lowest increase in profit for the entire duration

    lower_profit = 0                            # Declaration of variable
    higher_profit = 0                           # Declaration of variable
    for i in range(0, len(values) - 1):
        if float(diff[i]) < 0:
            if float(diff[i]) < lower_profit:   # checking to see if increase value is the lowest values
                lower_profit = float(diff[i])   # assigning the lowest increase to "lowest_profit" variable, if "if" condition is true
                day_low = date[i + 1]           # assigning the month value to "day_low" variable, if "if" condition is true
        elif float(diff[i]) > higher_profit:    # checking to see if increase value is the highest values
            higher_profit = float(diff[i])      # assigning the value to "highest_profit" variable, if "if" condition is true
            day_high = date[i + 1]              # assigning the month value to "day_high" variable, if "if" condition is true

csvfile.close() # Closing the csv file
# Procedure/commands for printing the results to screen/terminal

print("Financial Analysis \n")

print("----------------------------------------------")

print(f"Total Months: {count}")

print(f"Total: ${int(total)}")

print(f"Average Change: ${average_change}")

print(f"Greatest Increase in Profits: {day_high}  (${int(higher_profit)})")

print(f"Greatest Decrease in Profits: {day_low}  (${int(lower_profit)})")

#  Writing the analysis results to a txt file and saving it to Analysis folder

with (open(os.path.join("Analysis", "PyBank_Analysis.txt"), 'w', newline = '') as csv_write):  # Defining the path for saving the analysis results as txt file to a folder i.e. path to Analysis folder
    writer = csv.writer(csv_write, delimiter = ',', quoting = csv.QUOTE_MINIMAL)

    writer.writerow(['Financial Analysis'])
    writer.writerow(['                      '])
    writer.writerow(['----------------------------------------------'])
    writer.writerow(['                      '])
    writer.writerow(['Total Months: ' + str(count)])
    writer.writerow(['                      '])
    writer.writerow(['Total: $'+str(int(total))])
    writer.writerow(['                      '])
    writer.writerow(['Average Change: $'+ str(average_change)])
    writer.writerow(['                      '])
    writer.writerow(['Greatest Increase in Profits: ' + day_high +'  '+'($'+str(int(higher_profit)) +')'])
    writer.writerow(['                      '])
    writer.writerow(['Greatest Decrease in Profits: ' + day_low +'  '+'($'+str(int(lower_profit)) +')'])

csv_write.close()      #  Closing the  text file after writing all the information