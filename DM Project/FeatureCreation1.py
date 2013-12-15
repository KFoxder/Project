import csv
final =csv.writer(open('training_edit2.csv','wb+'))
training= csv.reader(open("training.csv","rb"), delimiter=',')
###Set Column Names
for row in training:
	final.writerow(row+["DifAquiredAvg_CurAvgAuction"]+["DifAquiredAboveAvg_CurAboveAvgRetail"]+["DifAquiredAvg_CurAvgRetail"]+["DifAquiredAboveAvg_CurAboveAvgAuction"]+["AdjVehOd"])
	break


for row in training:
	if row[22]=="0" or row[22]=="NULL":
		continue
	if row[1]=="1":
		row[1]="TRUE"		##BAD
	if row[1]=="0":
		row[1]="FALSE" 	##GOOD
	
	
### Difference in Price paid 31 and MMRCurrentAuctionAveragePrice 22

	avgCurAucPrice = (int(row[22])+int(row[23]))/2
	avgCurRetailPrice = (int(row[24])+int(row[25]))/2

### Difference in Aquired v. Current Average Auction Price
	if(int(row[5])>0):
		vehAge=int(row[5])
		dif1 = (int(row[18])-int(row[22]))/vehAge
	else:
		dif1 = (int(row[18])-int(row[22]))
### Difference in Aquired v. Current Above Average Retail Price
	if(int(row[5])>0):
		vehAge=int(row[5])
		dif2 = (int(row[21])-int(row[25]))/vehAge
	else:
		dif2 = (int(row[21])-int(row[25]))
### Difference in Aquired v. Current Average Retail Price
	if(int(row[5])>0):
		vehAge=int(row[5])
		dif3 = (int(row[20])-int(row[24]))/vehAge
	else:
		dif3 = (int(row[20])-int(row[24]))
### Difference in Aquired v. Current Above Average Auction Price	
	if(int(row[5])>0):
		vehAge=int(row[5])
		dif4 = (int(row[19])-int(row[23]))/vehAge
	else:
		dif4 = (int(row[19])-int(row[23]))
### Veh Miles divided by age
	if(int(row[5])>0 and int(row[14])>0):
		dif5 = int(int(row[14])/int(row[5]))
	else:
		dif5 = int(row[14])

	
	final.writerow(row+[dif1]+[dif2]+[dif3]+[dif4]+[dif5])

