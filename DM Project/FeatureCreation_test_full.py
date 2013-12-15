import csv
final =csv.writer(open('test_edit_full.csv','wb+'))
training= csv.reader(open("test.csv","rb"), delimiter=',')
###Set Column Names
for row in training:
	final.writerow(row+["DifAquiredAvg_CurAvgAuction"]+["DifAquiredAboveAvg_CurAboveAvgRetail"]+["DifAquiredAvg_CurAvgRetail"]+["DifAquiredAboveAvg_CurAboveAvgAuction"]+["AdjVehOd"])
	break


for row in training:
	row0=row[0]
	row4=row[4]
	row12=row[12]
	if row[22]=="0" or row[22]=="NULL":
		final.writerow(row)
		continue
	
	
### Difference in Price paid 31 and MMRCurrentAuctionAveragePrice 22


	avgCurAucPrice = (int(row[21])+int(row[22]))/2
	avgCurRetailPrice = (int(row[23])+int(row[24]))/2

### Difference in Aquired v. Current Average Auction Price
	if(int(row[4])>0):
		vehAge=int(row[4])
		dif1 = (int(row[17])-int(row[21]))/vehAge
	else:
		dif1 = (int(row[17])-int(row[21]))
### Difference in Aquired v. Current Above Average Retail Price
	if(int(row[4])>0):
		vehAge=int(row[4])
		dif2 = (int(row[20])-int(row[24]))/vehAge
	else:
		dif2 = (int(row[20])-int(row[24]))
### Difference in Aquired v. Current Average Retail Price
	if(int(row[4])>0):
		vehAge=int(row[4])
		dif3 = (int(row[19])-int(row[23]))/vehAge
	else:
		dif3 = (int(row[19])-int(row[23]))
### Difference in Aquired v. Current Above Average Auction Price	
	if(int(row[4])>0):
		vehAge=int(row[4])
		dif4 = (int(row[18])-int(row[22]))/vehAge
	else:
		dif4 = (int(row[18])-int(row[22]))

### Veh Miles divided by age
	if(int(row[4])>0 and int(row[13])>0):
		dif5 = int(int(row[13])/int(row[4]))
	else:
		dif5 = int(row[13])


	
	final.writerow(row+[dif1]+[dif2]+[dif3]+[dif4]+[dif5])

