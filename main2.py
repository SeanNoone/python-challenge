import os
import csv


financialdata1_csv = os.path.join("../pybank","budget_data_1.csv")

with open(financialdata1_csv, newline="") as csvfile1: 
    csvreader1= csv.reader(csvfile1, delimiter=",")



    next(csvreader1) 
    revenue = []
    date = []
    rev_change = []

   
    for row in csvreader1:

        revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))


    
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print("Avereage Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

    output_path = os.path.join('output', 'new.csv')

    with open(output_path, 'w', newline='') as csvfile:

         csvwriter = csv.writer(csvfile, delimiter=',')
         csvwriter.writerow(["Total Months: " + str(len(date))])
         csvwriter.writerow(["Total Revenue: " + str(sum(revenue))])
         csvwriter.writerow(["Average Revenue Change: " + str(round(avg_rev_change))])
         csvwriter.writerow(["Greatest Increase in Revenue: " + max_rev_change_date,"($", max_rev_change,")"])
         csvwriter.writerow(["Greatest Decrease in Revenue: " + min_rev_change_date,"($", min_rev_change,")"])


