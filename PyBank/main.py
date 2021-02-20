import os
import csv

# create path variables for read and write functions
filepath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Analysis', 'financial_report.txt')

# read in information from budget_data.csv
with open(filepath) as file_object:
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
month_change = []

# loop through revenue list to find total revenue
for value in revenue:
    net_total = net_total + value

# loop to calculate difference from month to month
# and to store difference and corresponding month in lists above
for i in range(0,(tot_month-1)):
    # the range for loop is from index 0 to 85, which will allow calculations for 86 months
    # in diff(erence) and month_change
    
    diff = revenue[i+1] - revenue[i]
    
    # ave_change is appending the diff(erence) calculated to new list
    
    ave_change.append(diff)
    
    # month_change is appending months starting with Feb 2010 to correspond with diff(erence)
    # calculated above 
    
    month_change.append(month[i+1])


# loop to calculate the precentage change using ave_change list calculated above
for j in ave_change:
    # first calculate the sum of all ave_change in list
    tot_change = tot_change + j
    # find average and store it in variable mean
    mean = tot_change/len(ave_change)



# Zip ave_change list and new_month list together
zip_list = zip(month_change,ave_change)
zipper = list(zip_list)

# Loop through zipper list to find greatest increase and decrease in profit and corresponding dates
for x in zipper:
    if x[1] == max(ave_change):
        profit_date = x[0]       
        profit = x[1]
    elif x[1] == min(ave_change):
        loss_date = x[0]
        loss = x[1]

print("\nFinancial Analysis Report")
print("___________________________")
print(f'\nTotal Months:                 {tot_month}')
print(f'Total:                        ${net_total}')
print(f'Average Change:               ${round(mean,3)}')
print(f'Greatest Increase in Profit:  {profit_date} : ${profit}')
print(f'Greatest Decrease in Profit:  {loss_date} : ${loss}')
print('\n')

with open(output_path, 'w') as output_file:
    csvwriter = csv.writer(output_file)
    
    csvwriter.writerow(["Financial Analysis Report"])
    csvwriter.writerow(["___________________________"])
    csvwriter.writerow([f'Total Months:                 {tot_month}'])
    csvwriter.writerow([f'Total:                        ${net_total}'])
    csvwriter.writerow([f'Average Change:               ${round(mean,3)}'])
    csvwriter.writerow([f'Greatest Increase in Profit:  {profit_date} : ${profit}'])
    csvwriter.writerow([f'Greatest Decrease in Profit:  {loss_date} : ${loss}'])
