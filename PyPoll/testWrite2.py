# to import the modules
import os
import csv
from collections import defaultdict, Counter

csvpath=os.path.join("..", "Resources", "election_data.csv") 

# to read the file and specify delimiter
with open(csvpath, newline='') as csvfile:
    csvdata = csv.reader(csvfile, delimiter=',') # to initialize csv reader
    headerline = next(csvdata) # to skip the header
    candidates=[] # to set up a list for the candidats
    for row in csvdata:
        candidates.append(str(row[2])) # to append data from col C to a list
        #print(candidates) 
    khanVotes=candidates.count('Khan')
    print("Khan: ", khanVotes)
    correyVotes=candidates.count('Correy')
    print("Correy: ", correyVotes)

# to specify the file to write to
output_path=os.path.join("..", "output", "test_results2.txt")
reader=txt.reader(csvdata)
lines=list(reader)
#open the file using "write" mode and specify variable to hold hte content
with open(output_path, 'w', newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(lines)

readFile.close()
writeFile.close()   
