#PyBank
import os
import csv
bank_csv = os.path.join('C:/Users/vijay/OneDrive/Documents/GitHub/Python-Challenge/PyBank/03-Python_Instructions_PyBank_Resources_budget_data.csv')
month_year = bank_csv[0]
profit_loss = bank_csv[1]
total_months = 0
total_profitloss = 0
avg_profitloss = 0
start_date = "Jan-2010"
end_date = "Feb-2017"
#first_value = 0
#last_value = 0
with open(bank_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvfile)
    for row in csvreader:
        total_months += int(len(month_year))
        total_profitloss += int(row[1])
        if row[0] == start_date:
            first_value = int(row[1])
        if row[0] == end_date:
            last_value = int(row[1])
avg_profitloss = ((last_value - first_value) / (total_months-1))
print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total : {total_profitloss}")
print(f"Average Change : {avg_profitloss}")

#Creating Output Text File

output_file = os.path.join('PyBank_output.txt')
with open(output_file, 'w') as output:
    writer = csv.writer(output)
    writer.writerow([f"Financial Analysis"])
    writer.writerow([f"--------------------------------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total : {total_profitloss}"])
    writer.writerow([f"Average Change : {avg_profitloss}"])