#PyBank code to calculate the values
import os
import csv
bank_csv = os.path.join('C:/Users/vijay/OneDrive/Documents/GitHub/Python-Challenge/PyBank/03-Python_Instructions_PyBank_Resources_budget_data.csv')
total_months = 0
total_profitloss = 0
avg_profitloss = 0
with open(bank_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvfile)
    month_year = []
    profit_loss = []
    value_change = []
    for row in csvreader:
        profit_loss.append(int(row[1]))
        month_year.append(row[0])
    total_months = len(month_year)
    total_profitloss = sum(profit_loss)
    for r in range(1,len(profit_loss)):
        value_change.append(profit_loss[r] - profit_loss[r-1])
        avg_profitloss = sum(value_change)/(len(profit_loss)-1)
        max_profit = max(value_change)
        min_profit = min(value_change)
        max_profit_time = str(month_year[value_change.index(max(value_change))+1])
        min_profit_time = str(month_year[value_change.index(min(value_change))+1])

print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total : ${total_profitloss}")
print(f"Average Change : ${avg_profitloss}")
print(f"Greatest increase in Profits : {max_profit_time} (${max_profit})")
print(f"Greatest decrease in Profits : {min_profit_time} (${min_profit})")

#Creating Output Text File

output_file = os.path.join('PyBank_output.txt')
with open(output_file, 'w') as output:
    writer = csv.writer(output)
    writer.writerow([f"Financial Analysis"])
    writer.writerow([f"--------------------------------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total : {total_profitloss}"])
    writer.writerow([f"Average Change : {avg_profitloss}"])
    writer.writerow([f"Greatest increase in Profits : {max_profit_time} (${max_profit})"])
    writer.writerow([f"Greatest decrease in Profits : {min_profit_time} (${min_profit})"])