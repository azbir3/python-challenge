# to print title
print(" Financial Analysis")
print('_____________________________')
print('') 

# to import the modules
import os
import csv

# path to the csv data file
csvpath=os.path.join("..", "Resources", "budget_data.csv") 

# to check ability to read the file - seccessful 
#with open(csvpath, 'r') as file_handler:
 #   lines = file_handler.read()
  #  print(lines)
   # print(type(lines))

# Step 1 - to count number on month included in the dataset
# to read the file and specify delimiter
with open(csvpath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
    #to use sum function to calculate number of month data shown in the csv file and print the total
     for row in csvreader:
         row_count = sum(1 for row in csvreader) 
         print(f'Total Month : {row_count}') 

# Step 2 - to calculate total amount of "Profit/Loss"
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headerline = next(csvreader) # to skip the header
    total = 0 #set total to zero

    #to loop through second column, sum up the values and print out total
    for row in csvreader:
        total += int(row[1])
    print (f'Total : ${total}')
        
# Step 3 - to calculate change in "Profit/Loss"
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') # read the file
    headerline = next(csvreader) # to skip the header
    profits=[] # to set up a list of the values of profits
    for row in csvreader:
        profits.append(int(row[1])) #to append data from col B to a list
        #print(profits) # to check if data is being received - ok
        # to calculate change in profits and append to a list
    change=[profits[i+1]-profits[i] for i in range(len(profits)-1)] 
    #print(change) #to check if change list is generated = successful 

    #to calculate and print requested output
    average=round(sum(change)/(row_count -1), 2) # to find average value
    max_increase = max(change) # to find max value
    min_increase = min(change) # to find min value
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits:(${max_increase})')
    print(f'Greatest Decrease in Profits:(${min_increase})')

# Step 4 - to write Financial analysis to a text file
# specify the file to write to
output_path = os.path.join("..", "output", "Financial_Analysis.txt")
with open(output_path, 'w', newline='') as textfile:
    x=(f"Financial Analysis\n"
    "---------------------\n"
    " \n"
    f"Total Month : {row_count}\n"
    f"Total : {total}\n"
    f"Average Change: {average}\n"
    f"Greatest Increase in Profits: {max_increase}\n"
    f"Greatest Decrease in Profits: {min_increase}\n")
    textfile.write(x)
