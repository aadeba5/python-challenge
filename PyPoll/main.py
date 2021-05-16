import os
import csv
import math
import statistics
import numpy as np
import scipy.stats

import os
import csv
import math
# from posix import ST_NOATIME
import statistics
import numpy as np
import scipy.stats

# PyBank/Resources/budget_data.csv

csvpath= os.path.join("../budget_data.csv")
print(csvpath)

# open("u.item", encoding="utf-8") with open('u.item', encoding = "ISO-8859-1")

# PyPoll/Resources/election_data.csv

csvpath = os.path.join("Resources", "election_data.csv")
csvpath = os.path.join("Resources", "election_data.csv")

# State = []
# Population = []
# Pct = []
# open('u.item', encoding = "ISO-8859-1")

# open the file in the write mode
DataFile = open('newPopulation.csv', 'w')
writer = csv.writer(DataFile)

#The total number of votes cast
with open(csvpath,encoding = "ISO-8859-1") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        newstuff = row[0][1:]
        State.append(newstuff)
        Population.append(row[1])
        Pct.append(row[2])
        writer.writerow ([
            newstuff, row[1], row[2]

        ])

    print(State)
    print(Population)
    print(Pct)



# write a row to the csv file
# writer.writerow("Nick")


# close the file
DataFile.close()
csvpath= os.path.join("PyBank", "Resources", "budget_data.csv")

#PyPoll/Resources/election_data.csv

# csvpath = os.path.join("Resources", "election_data.csv")
csvpath = os.path.join("Resources", "election_data.csv")

Voter_ID = []
County = []
Candidates = []

#The total number of votes cast
with open(csvpath) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidates.append(row[2])

    print(Voter_ID)
    print(County)
    print(Candidates)

#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.