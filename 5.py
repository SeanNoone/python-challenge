import os
import csv
polldata1_csv = os.path.join("election_data_1.csv")
    
votes_cast = []
candidates = []
new_candidates = []
winner = []
county = []
win = []
percentage = []
individual = []
    
with open(polldata1_csv, newline="") as csvfile1: 
    csvreader1= csv.reader(csvfile1, delimiter=",")
    next(csvreader1)
    for row in csvreader1:
#float
        votes_cast.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    
    
    for x in candidates:
        if x not in new_candidates:
            new_candidates.append(x)
    
    #print(new_candiates)
    
    for z in range(len(new_candidates)):
    	individual.append(candidates.count(new_candidates[z]))
    	percentage.append(individual[z]/len(votes_cast)*100)

    win = int(individual.index(max(individual)))
    	
    print("Election Results")
    print("---------------------------")
    print("Total Votes :", len(votes_cast))
    print("----------------------------")
   
    for r in range(len(new_candidates)):
    	print(str(new_candidates[r]) + ":" + str(percentage[r]) + "%" + " " + str(individual[r]))
   
    print("----------------------------")
    print("Winner:" + str(new_candidates[win]))




