import os
import csv

voteCounter=0
candidateList=[]
candidate_count=0
candidate_name=""
winner_count=0
winner=""


csvpath=os.path.join('Resources', "election_data_2.csv")
vpath=os.path.join('Resources', "budget_data_1.csv")
with open(csvpath) as csvfile:
	csvreader=csv.reader(csvfile, delimiter=",")
	next (csvfile)		#skips the header row
	for row in csvreader:
		voteCounter=voteCounter+1
		if row[2] not in candidateList:
			candidateList.append(row[2])

def count(name):		
	with open(csvpath) as csvfile:
		csvreader=csv.reader(csvfile, delimiter=",")
		candidate_count=0
		global winner_count
		global winner 
		for row in csvreader:
			if row[2]==name:
				candidate_count=candidate_count+1
	candidate_per=0.0
	candidate_per=round((candidate_count/voteCounter)*100)
	if candidate_per>winner_count:
		winner_count=candidate_per
		winner=name
	print(str(name)+": " +str(candidate_per)+"% (" +str(candidate_count)+")")

print("Election Results")
print("-----------------------------")
print("Total Votes: "+str(voteCounter))
print("-----------------------------")
for i in range(len(candidateList)):
	count(candidateList[i])
print("-----------------------------")
print("Winner: "+str(winner))
print("-----------------------------")


