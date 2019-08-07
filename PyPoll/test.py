# to import the modules
import os
import csv
from collections import defaultdict, Counter

csvpath=os.path.join("..", "Resources", "election_data.csv") 

# to read the file and specify delimiter
with open(csvpath, newline='') as csvfile:
    csvdata = csv.reader(csvfile, delimiter=',') #read the file
    headerline = next(csvdata) # to skip the header
    candidates=[] # to set up a list for the candidats
    for row in csvdata:
        candidates.append(str(row[2])) # to append data from col C to a list
        #print(candidates) 
    khanVotes=candidates.count('Khan')
    print("Khan: ", khanVotes)
    correyVotes=candidates.count('Correy')
    print("Correy: ", correyVotes)


    

    #reader = csv.DictReader(csvfile) 
    #headerline = next(csvreader) # to skip the header
    #candidates=list(csvdata)
    #print("Khan: ", candidates.count('Khan'))
    #print("Correy: ", candidates.count('Correy'))
    #print("Li: ", candidates.count('Li'))
    #print("O'Tooley: ", candidates.count('O'Tooley')) - problem with the appostrophy in the name