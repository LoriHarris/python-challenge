import os
import csv


#import csv file
csvpath = os.path.join("..", "PyBank", "budget_data.csv")

#create lists to store data
months = []
profitloss = []
profitloss2 = []

#open csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
       #put info into lists using proper casting
       #create 2 profitloss lists so we can subtract one from the other
        months.append(str(row[0]))
        profitloss.append(int(row[1]))
        profitloss2.append(int(row[1]))
    #pop off the top value so that we can subract the new month from the previous month 
    profitloss.pop(0)
            
#get total number of months
totalm = (len(months))
#get total proft        
totalp = (sum(profitloss2))

#calculate the change month over month        
change = [x - y for x, y in zip(profitloss, profitloss2)]
aveChange = (sum(change)/(totalm - 1))
aveChange1 = (str(round(aveChange, 2)))

#get the min and max change
minpos = change.index(min(change))
maxpos = change.index(max(change))

#print results to terminal
print("")
print("--------------Financial Analysis")
print("--------------Total Months: " + str(totalm))
print("--------------Total Volume: $" + str(totalp))
print("--------------Average Change: $" + str(aveChange1))
print("--------------Greatest decrease in profits: " + str(months[minpos + 1]) + " ($" + str(max(change)) + ")")
print("--------------Greatest increase in profits: " + str(months[maxpos + 1]) + " ($" + str(min(change)) + ")")

#create txt file to print the results to
output_file = os.path.join("fin_analysis.txt")

#open the txt file
with open(output_file, "w", newline="") as datafile:
    
    #print the results to the txt file
    print(f"Financial Analysis -----------------------------", file=datafile)
    print(f"Total Months: {str(totalm)} ",  file=datafile) 
    print(f"Total Volume: ${str(totalp)} ", file=datafile) 
    print(f"Average Change: ${str(aveChange1)} ", file=datafile) 
    print(f"Greatest decrease in profits: {str(months[minpos + 1])} ($ {str(max(change))})", file=datafile) 
    print(f"Greatest increase in profits: {str(months[maxpos + 1])} ($ {str(min(change))})", file=datafile) 




    









































































        #if row[0] == months:
            #print(row[0] + "Is this the month you chose")

            #found = True
            
            #break

        #if found is False:
            #print(csvreader)
