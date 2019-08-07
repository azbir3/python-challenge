# to print title
print(" Election Results")
print('___________________________________')
print('') 

# to import the modules
import os
import csv

csvpath=os.path.join("..", "Resources", "election_data.csv") 

# to check ability to read the file - seccessful 
#with open(csvpath, 'r') as file_handler:
#    lines = file_handler.read()
#    print(lines)

# Step 1 - to use sum function to count number votes in the csv file and print the total
# to read the file and specify delimiter
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
         row_count = sum(1 for row in csvreader) 
         print(f'Total Votes : {row_count}') 
         print('___________________________________')
         print('')
# Step 2 - to count votes and % per candidate
# to read the file and specify delimiter
with open(csvpath, newline='') as csvfile:
    csvdata = csv.reader(csvfile, delimiter=',') #read the file
    headerline = next(csvdata) # to skip the header
    candidates=[] # to set up a list for the candidats
    for row in csvdata:
        candidates.append(str(row[2])) # to append data from col C to a list
        #print(candidates) 
    #to calculate and print out results for all candidates
    khanVotes=candidates.count('Khan')
    khanprct=khanVotes/row_count
    print("Khan: ", khanprct, khanVotes)
    correyVotes=candidates.count('Correy')
    correyprct=correyVotes/row_count
    print("Correy: ", correyprct, correyVotes)
    liVotes=candidates.count('Li')
    liprct=liVotes/row_count
    print("Li: ", liprct, liVotes)
    tooleyVotes=candidates.count("O'Tooley")
    tooleyprct=liVotes/row_count
    print("O'Tooley: ", tooleyprct, tooleyVotes)
    print('___________________________________')

    # to determine and print out the winner
    winnerList=[khanVotes, correyVotes, liVotes, tooleyVotes]
    #print(winnerList) # to ck printing of the list
    print('')
    print("Winner: ", max(winnerList))
    print('___________________________________') 
    