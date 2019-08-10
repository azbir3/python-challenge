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
    khanprct=(khanVotes/row_count)*100
    print(f"Khan:  {khanprct:.3f}% ({khanVotes})\n")

    correyVotes=candidates.count('Correy')
    correyprct=(correyVotes/row_count)*100
    print(f"Correy:  {correyprct:.3f}% ({correyVotes})\n")

    liVotes=candidates.count('Li')
    liprct=(liVotes/row_count)*100
    print(f"Li:  {liprct:.3f}% ({liVotes}\n")

    tooleyVotes=candidates.count("O'Tooley")
    tooleyprct=(liVotes/row_count)*100
    print(f"O'Tooley:  {tooleyprct:.3f}% ({tooleyVotes})\n")

    print('___________________________________')

 #Step - 3 - to determine and print out the winner
    winnerList=[khanVotes, correyVotes, liVotes, tooleyVotes]
    winner=max(winnerList) # to determine a winner vote
        #print(winnerList) # to ck printing of the list - ok
        #print(winner) # to ck if winner is calcualted correctly - ok
    winnerName=["Khan", "Correy", "Li", "O'Tolley"] #to create a list of candidate names
    winnerPosition=winnerList.index(max(winnerList))
    #print(winnerPosition)
    winnerN=winnerName[winnerPosition]
    print('')
    print(f"Winner: {winnerN}")
    print('___________________________________') 

# Step 4 - to write Election Results to a text file
# specify the file to write to
output_path = os.path.join("..", "output", "Election_Results.txt")
with open(output_path, 'w') as textfile:
    textfile.write("Election Results \n") # to write the headder
    L = ["---------------------------- \n", # to write separate lines row 66 - 76
    f"Total Votes : {row_count} \n",
    "---------------------------- \n",
    f"Khan:  {khanprct:.3f}% ({khanVotes}) \n",
    f"Correy : {correyprct:.3f}% ({correyVotes}) \n",
    f"Li : {liprct:.3f}% ({liVotes}) \n",
    f"O'Tooley : {tooleyprct:.3f}% ({tooleyVotes}) \n",
    "---------------------------- \n",
    f"Winner : {winnerN} \n",
    "---------------------------- \n"]
    textfile.writelines(L)
    textfile.close()