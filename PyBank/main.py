#Evgeniia Kozodeeva
#step first
import os, csv

# File path
PyBank_file = os.path.join("Resources", "budget_data.csv")

# Set variables
months_count = 0
total_net = 0
change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ("")
greatest_decrease_month = ("")
data = []

# open the budget data file
with open(PyBank_file, "r",newline="") as csvfile:
    PyBank = csv.reader(csvfile,delimiter = ",")
    file_header = next(PyBank)

    for row in PyBank:
        #the total number of months + the datase
        months_count = months_count + 1
        
        total_net = int(total_net) + int(row[1])

        #Put data  - calcualte month change
        data.append(row)

        #Loop through the whole list and get the monthly change (next month - current month)
        #len -1 is for the avoiding issue calculation for the last data
        for i in range(len(data)-1):
            monthly_change = int((data)[i + 1][1]) - int((data)[i][1])

            #The greatest increase
            if greatest_increase < monthly_change:
                greatest_increase = monthly_change
                greatest_increase_month = data[i + 1][0]                

            #The greatest decrease
            if  greatest_decrease > monthly_change:
                    greatest_decrease = monthly_change
                    greatest_decrease_month = data[i + 1][0]

            #The average change in losses
            average_change = round((int((data)[-1][1]) - int((data)[0][1])) / (len(data)-1),2)    



 # Create an results file
results = os.path.join("analysis","pybank_ result.txt")
with open(results,"w",newline="") as datafile:
    writer = csv.writer(datafile)

    # Write results to the file
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f'Total Months: {months_count}'])
    writer.writerow([f'Total: ${total_net}'])    
    writer.writerow([f'Average Change : ${average_change}'])
    writer.writerow([f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})'])
    writer.writerow([f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})']) 

# The result
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {months_count}')
print(f'Total: ${total_net}')
print(f'Average Change : ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')