# importing csv module
import csv

# csv file name
filename = "data.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)
	
	# extracting field names through first row
	fields = next(csvreader)

	# extracting each data row one by one
	for row in csvreader:
		rows.append(row)
		


# printing data (just for debugging purpose, later we can change it to the desired format)
for row in rows:
	out = fields[0] + ":" + row[0] + ", " + fields[1] + ":" + row[1]
	print(out)
