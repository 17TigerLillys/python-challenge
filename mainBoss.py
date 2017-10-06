####################################################################
#This program mostly works but I'm still overwriting the original 
#file instead of writing to a .txt file!!!
####################################################################

import os
import csv
import datetime 

ssnList=[]
newName=" "
row3=[]
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

csvpath=os.path.join('Resources', "employee_data1.csv")
with open(csvpath) as csvfile:
	csvreader=csv.reader(csvfile, delimiter=",")
	next (csvfile)
	for row in csvreader:
		row[1]=row[1].split(" ") #splits the names
		#changes the format of the dates
		row[2]=datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%y')
		row3=list(row[3])
		#replaces the first social security numbers with "*"
		for i in range(3):
			row3[i]="*"
		for i in range(4,6):
			row3[i]="*"
		row3string=''.join(row3)
		row4=row[4]
		row4_2='row4'
		#switches to the state abbreviations
		row[4]=us_state_abbrev[row4]

		#this is the part I couldn't get to work!!!
		file=open("main_boss.txt",'w')
		file.write(row3string)
		"""
		output_file = os.path.join("main_Boss.csv")
		with open(output_file, "w", newline="") as datafile:
			writer=csv.writer(datafile)
			writer.writerows(row[:])
		"""
