import os
import csv

#import file to analyze
csvpath= os.path.join("..", "Resources", "election_data.csv" )

#create lists to store data
voter_id = []
county = []
candidate = []
unique = []
cand1 = []
perc = []
perc1 = []
final_perc = []

#open the csv file
with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader, None)
        for row in csvreader:
            #add informatio to preliminary lists
            voter_id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
#get the vote count
total_votes = len(voter_id)

#put unique names into new list 
#put assocated vote totals into new list
for x in candidate:
    if x not in unique:
            unique.append(x)
            cand1.append(candidate.count(x))

#using the unique vote count list, divide to get unique percentage totals
#create new percentage list to round to 2 decimel places
for x in cand1:
    perc.append((x / total_votes) * 100)
    perc_fin =  [round(x,2) for x in perc] 
   
#get the name of cnadidate with the max votes    
minpos = cand1.index(max(cand1))

#print all results to terminal
print("----------------------------Election Results-------------------------------")
print("---------------------Total Number of Votes: " + str(total_votes) + "------------------------")
print("")
print(str(unique[0]) + ": (" + str(cand1[0]) + ") " + str(float(perc_fin[0])) + "%")
print(str(unique[1]) + ": (" + str(cand1[1]) + ") " + str(float(perc_fin[1])) + "%")
print(str(unique[2]) + ": (" + str(cand1[2]) + ") " + str(float(perc_fin[2])) + "%")
print(str(unique[3]) + ": (" + str(cand1[3]) + ") " + str(float(perc_fin[3])) + "%")
print("")
print("---------------------------------------------------------------------------")
print("The Winner is " + str((unique[minpos])) + " with a whopping " + str(max(cand1)) + " votes!")
print("---------------------------------------------------------------------------")

#create the txt file to print results
output_file = os.path.join("vote_analysis.txt")

#open the txt file
with open(output_file, "w", newline="") as datafile:

#print the results to the text file    
    print(f"Election Results----", file=datafile)
    print(f"Total Number of Votes: {str(total_votes)} ----", file=datafile)
    print(f"{str(unique[0])}:({str(cand1[0])}) {str(float(perc_fin[0]))}% ", file=datafile)
    print(f"{str(unique[1])}:({str(cand1[1])}) {str(float(perc_fin[1]))}% ", file=datafile)
    print(f"{str(unique[2])}:({str(cand1[2])}) {str(float(perc_fin[2]))}% ", file=datafile)
    print(f"{str(unique[3])}:({str(cand1[3])}) {str(float(perc_fin[3]))}% ", file=datafile)
    print(f"----", file=datafile)
    print(f"The Winner is {str((unique[minpos]))} with a whopping {str(max(cand1))} votes!", file=datafile)
    print(f"----", file=datafile)