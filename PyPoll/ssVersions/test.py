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
    khanprct= 50 #(khanVotes/row_count)*100
    print("Khan: ", khanVotes)
    correyVotes=candidates.count('Correy')
    print("Correy: ", correyVotes)

# to specify the file to write to
output_path=os.path.join("..", "output", "test_resultsPP.txt")
totalcount=3521001
#open the file using "write" mode and specify variable to hold hte content
with open(output_path, 'w', newline='') as textfile:
    #initialize csv.writer
    #csvwriter=csv.writer(csvfile, delimiter=',')
    # write the first row (header)
    #csvwriter.writerow(['Election Results'])
    #write the second row (seperator)
    #csvwriter.writerow(['___________________________________'])
    #write rest of the rows
    x=(f"Khan:  {khanprct:.3f}% ({khanVotes})\n"
    f""
    f"Total Votes : {totalcount}\n")

    
    textfile.write(x)
    

    #reader = csv.DictReader(csvfile) 
    #headerline = next(csvreader) # to skip the header
    #candidates=list(csvdata)
    #print("Khan: ", candidates.count('Khan'))
    #print("Correy: ", candidates.count('Correy'))
    #print("Li: ", candidates.count('Li'))
    #print("O'Tooley: ", candidates.count('O'Tooley')) - problem with the appostrophy in the name