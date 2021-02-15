import os
import csv

py_bank = os.path.join('Resources', 'budget_data.csv')


month = []
revenue = []

with open(py_bank) as file_object:
    csvreader = csv.reader(file_object, delimiter=",")
    #print(csvreader)

    header = next(csvreader)
    
    for row in csvreader:
        
        month.append(row[0])
        revenue.append(int(row[1]))
        #print(f' {month} : {revenue}')
        
tot_month = len(month)



net_total = 0
ave_change = []
tot_change = 0

for value in revenue:
    net_total = net_total + value

for i in range(0,(tot_month-1)):
    diff = revenue[i+1] - revenue[i]
    ave_change.append(diff)

for j in ave_change:
    tot_change = tot_change + j
    working = tot_change/len(ave_change)

zip_list = zip(month,ave_change)
clan = list(zip_list)
print (clan)



print(f'\nTotal Months:  {tot_month}')
print(f'Total:  {net_total}')
print(f'Average Change: ${round(working,2)}')
print(f'Greatest Increase:  {max(ave_change)}')
print(f'Greatest Decrease:  {min(ave_change)}')



print('\n')