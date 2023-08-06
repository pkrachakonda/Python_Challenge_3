import os, csv

date = []
values = []

with open(os.path.join("Resources", "budget_data.csv"), newline="") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        date.append(row["Date"])
        values.append(float(row["Profit/Losses"]))

    total = 0
    change = 0
    count = 0
    diff = []
    for i in range(0, len(values)):
        total = total + values[i]
        if i >= 1:
            diff.append(values[i] - values[i - 1])
            change = change + float(diff[i - 1])
        count += 1
    average_change = change / (count - 1)

    lower_profit = 0
    higher_profit = 0
    for i in range(1, len(values) - 1):
        if float(diff[i]) < 0:
            if float(diff[i]) < lower_profit:
                lower_profit = float(diff[i])
                day_low = date[i + 1]
        elif float(diff[i]) > higher_profit:
            higher_profit = float(diff[i])
            day_high = date[i + 1]

print("Financial Analysis \n")

print("----------------------------------------------")

print(f"Total Months: {count}")

print(f"Total: ${int(total)}")

print(f"Average Change: ${round(average_change,2)}")

print(f"Greatest Increase in Profits: {day_high}  (${int(higher_profit)})")

print(f"Greatest Decrease in Profits: {day_low}  (${int(lower_profit)})")

with (open(os.path.join("Analysis", "PyBank_Analysis.txt"), 'w', newline = '') as csv_write):
    writer = csv.writer(csv_write, delimiter = ',', quoting = csv.QUOTE_MINIMAL)

    writer.writerow(['Financial Analysis'])
    writer.writerow(['                      '])
    writer.writerow(['----------------------------------------------'])
    writer.writerow(['                      '])
    writer.writerow(['Total Months: ' + str(count)])
    writer.writerow(['                      '])
    writer.writerow(['Total: $'+str(int(total))])
    writer.writerow(['                      '])
    writer.writerow(['Average Change: $'+ str(round(average_change, 2))])
    writer.writerow(['                      '])
    writer.writerow(['Greatest Increase in Profits: ' + day_high +'  '+'($'+str(int(higher_profit)) +')'])
    writer.writerow(['                      '])
    writer.writerow(['Greatest Decrease in Profits: ' + day_low +'  '+'($'+str(int(lower_profit)) +')'])
