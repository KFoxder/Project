import csv
final =csv.writer(open('training_edit1.csv','wb+'))
training= csv.reader(open("training.csv","rb"), delimiter=',')
for row in training:
	## Tranform isBadBuy to Boolean
	if row[1]=="1":
		row[1]="TRUE"
	if row[1]=="0":
		row[1]="FALSE"
		## Transform Auction Attribute
		if row[3]=="ADESA":
			row[3]=1
		if row[3]=="MANHEIM":
			row[3]=2
		if row[3]=="OTHER":
			row[3]=3
		########################
		## Transform Color Attribute
		if row[10]=="BEIGE":
			row[10]=1
		if row[10]=="BLACK":
			row[10]=2
		if row[10]=="BLUE":
			row[10]=3
		if row[10]=="BROWN":
			row[10]=4
		if row[10]=="GOLD":
			row[10]=5
		if row[10]=="GREEN":
			row[10]=6
		if row[10]=="GREY":
			row[10]=7
		if row[10]=="MAROON":
			row[10]=8
		if row[10]=="NOT AVAIL":
			row[10]=9
		if row[10]=="NULL":
			row[10]=9
		if row[10]=="ORANGE":
			row[10]=10
		if row[10]=="OTHER":
			row[10]=11
		if row[10]=="PURPLE":
			row[10]=12
		if row[10]=="RED":
			row[10]=13
		if row[10]=="SILVER":
			row[10]=14
		if row[10]=="WHITE":
			row[10]=15
		if row[10]=="YELLOW":
			row[10]=4
		########################	

	
	final.writerow(row+ ["test_col"])

