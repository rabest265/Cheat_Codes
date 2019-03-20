import os
import csv

#READING AND WRITING CSV FILES
# Name input and output paths
csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join("dummy.csv")
output_txt = os.path.join("dummy.txt")
totalmonth = 0
total = 0
month = []
pandl = []

# Reading a csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # Use this syntex to do things with each row of daga
    for row in csvreader:
        month.append(row[0])
        pandl.append(float(row[1]))
        total += float(row[1])
        totalmonth += 1
newrows = zip(month, pandl)

# Writing a CSV file
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the rows one by one (such as a header)
    csvwriter.writerow(csv_header)
    # write zipped arrays
    csvwriter.writerows(newrows)

#Writing an output text file
file = open(output_txt,"w")
file.write("-----------------------------\n") #\n gets you to another line
file.write("The total number of months is: " + str(totalmonth) + "\n")
file.write("The total profit and loss is: " + str(total) + "\n")
file.write("-----------------------------")
file.close()
    
#Print the file in terminal
file = open(output_txt,"r")
print (file.read())
file.close
