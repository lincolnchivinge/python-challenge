#import library
import os
import csv

#joining path with the folder containing the CSV file.
budget_data = os.path.join("c:/Users/Lincoln/Desktop/Personal/UZ MDS/Adv Programming for Data Analytics/python-challenge/PyBank/Resources", "budget_data.csv")

# open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    # find net amount of profit and loss by creating empty lists Profit/Losses and months respectively
    Profit_Losses = []
    months = []

    #read through each row of data after header
    for rows in csvreader:
        Profit_Losses.append(int(rows[1]))
        months.append(rows[0])

    # Creating a revenue change list to be used in the calculations of net Profit or Loss
    revenue_change = []

    for x in range(1, len(Profit_Losses)):
        revenue_change.append((int(Profit_Losses[x]) - int(Profit_Losses[x-1])))
    
    # calculate average revenue change by getting the quotient of the total revenue change and the frequency. 
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(revenue_change)
    # greatest decrease in revenue
    greatest_decrease = min(revenue_change)


    # print the Results
    print("Financial Analysis")

    print("....................................................................................")

    print("Total months: " + str(total_months))

    print("Total: " + "$" + str(sum(Profit_Losses)))

    print("Average Change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))


    # output to a text file

    file = open("c:/Users/Lincoln/Desktop/Personal/UZ MDS/Adv Programming for Data Analytics/python-challenge/PyBank/analysis/output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(Profit_Losses)) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()

