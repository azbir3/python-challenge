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
        #print(candidates) # checked = ok
    #to calculate and print out results for all candidates
    khanVotes=candidates.count('Khan')
    khanprct=(khanVotes/row_count)*100
    print("Khan: {}%".format(round(khanprct, 5)), khanVotes)
    print(f"Khan:  {khanprct:.3f}% ({khanVotes})\n")
    correyVotes=candidates.count('Correy')
    correyprct=(correyVotes/row_count)*100
    print("Correy: {}%".format(round(correyprct, 3)), correyVotes)
    liVotes=candidates.count('Li')
    liprct=(liVotes/row_count)*100
    print("Li: {}%".format(round(liprct, 4)), liVotes)
    tooleyVotes=candidates.count("O'Tooley")
    tooleyprct=(tooleyVotes/row_count)*100
    print("O'Tooley: {}%".format(round(tooleyprct, 1)), tooleyVotes)
    print('___________________________________')

    # to determine and print out the winner
    winnerList=[khanVotes, correyVotes, liVotes, tooleyVotes]
    #print(winnerList) # to ck printing of the list
    print('')
    print("Winner: ", max(winnerList))
    print('___________________________________')

    #precision=2 
    #width=5
    #print(f'Khan: {khanprct:{width}.{precision}f}', khanVotes) 
    #print("Khan: " round(khanprct, 3), khanVotes)

# to specify the file to write to
output_path=os.path.join("..", "output", "election_results.csv")
