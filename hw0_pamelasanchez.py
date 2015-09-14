import csv
counter = 0
f = open('iowa-liquor-sample.csv')
csv_f = csv.reader(f)
for row in csv_f:
   for element in row:
        if element.lower().find("single malt scotch") > -1:
	    counter +=1
            break
print counter

