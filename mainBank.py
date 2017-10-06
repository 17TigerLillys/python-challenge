import os
import csv

monthCounter=0
revCounter=0
greatestIncrease=0
smallestIncrease=0
greatestIncreaseMonth=" "
smallestDecreaseMonth=" "
last_month_revenue=0
current_month_revenue=0
change_in_revenue=0
averageRevenueChange=0
changeInt=0
dataList=[]
changeList=[]

csvpath=os.path.join('Resources', "budget_data_1.csv")
with open(csvpath) as csvfile:
	csvreader=csv.reader(csvfile, delimiter=",")
	next (csvfile)		#skips the header row
	for row in csvreader:
		monthCounter=monthCounter+1
		revCounter=revCounter+int(row[1])
		dataList.append(row)
		current_month_revenue=int(row[1])
		change_in_revenue=current_month_revenue-int(last_month_revenue)
		#changeList.append(change_in_revenue)
		changeInt=changeInt+change_in_revenue
		last_month_revenue=int(row[1])
		if change_in_revenue>greatestIncrease:
			greatestIncrease=change_in_revenue
			greatestIncreaseMonth=row[0]
		if change_in_revenue<smallestIncrease:
			smallestIncrease=change_in_revenue
			greatestDecreaseMonth=row[0]
	
	averageRevenueChange=changeInt/float(monthCounter)

print("""Financial Analysis
--------------------------
Total Months: """+str(monthCounter)+"""
Total Revenue: $"""+str(revCounter)+"""
Greatest Increase In Revenue: """+greatestIncreaseMonth+" ($"+str(greatestIncrease)+")")
print("Greatest Decrease in Revenue: "+greatestDecreaseMonth +" ($"+str(smallestIncrease)+")")
print("Average Revenue Change: "+str(averageRevenueChange))
