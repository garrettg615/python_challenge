import os
import csv

# create path variable for read and write files
py_bank = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Analysis', 'financial_report.txt')

# read in information from budget_data.csv
with open(py_bank) as file_object:
    csvreader = csv.reader(file_object, delimiter=",")
    
    # remove header from csv file
    header = next(csvreader)
    
    # create empty lists to store values from csv file
    month = []
    revenue = []

    # loop through data and store them in lists above
    for row in csvreader:
        month.append(row[0])
        revenue.append(int(row[1]))
        
# find total months in budget data       
tot_month = len(month)

# initalize variables for loops below
net_total = 0
tot_change = 0

# create lists to store loop variable below
ave_change = []
new_month = []

# loop through revenue list to find total revenue
for value in revenue:
    net_total = net_total + value

# loop to calculate difference from month to month
# and to store difference and corresponding month in lists above
for i in range(0,(tot_month-1)):
    diff = revenue[i+1] - revenue[i]
    ave_change.append(diff)
    new_month.append(month[i+1])

# loop to calculate the precentage change
for j in ave_change:
    tot_change = tot_change + j
    working = tot_change/len(ave_change)

# Zip ave_change list and new_month list together
zip_list = zip(new_month,ave_change)
clan = list(zip_list)

# Loop to find greatest increase and decrease in profit
for x in clan:
    if x[1] == max(ave_change):
        g = x[0]       
        h = x[1]
    elif x[1] == min(ave_change):
        m = x[0]
        n = x[1]

print("\nFinancial Analysis Report")
print("___________________________")
print(f'\nTotal Months:                 {tot_month}')
print(f'Total:                        ${net_total}')
print(f'Average Change:               ${round(working,2)}')
print(f'Greatest Increase in Profit:  {g} : ${h}')
print(f'Greatest Decrease in Profit:  {m} : ${n}')
print('\n')

with open(output_path, 'w') as output_file:
    csvwriter = csv.writer(output_file)
    
    csvwriter.writerow(["Financial Analysis Report"])
    csvwriter.writerow(["___________________________"])
    csvwriter.writerow([f'Total Months:                 {tot_month}'])
    csvwriter.writerow([f'Total:                        ${net_total}'])
    csvwriter.writerow([f'Average Change:               ${round(working,2)}'])
    csvwriter.writerow([f'Greatest Increase in Profit:  {g} : ${h}'])
    csvwriter.writerow([f'Greatest Decrease in Profit:  {m} : ${n}'])
