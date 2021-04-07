import sys
import os
import csv
if len(sys.argv) != 2:
    print("Exiting - not enough arguments" + str(len(sys.argv)))
    os._exit(1)

webversion="v1.0"
printversion="v1.0"

print("Starting")
csvFiles = sys.argv[1] 
with open(csvFiles, newline='') as csvFile:
    csvData = csv.DictReader(csvFile)
    rowNum = 0
    for row in csvData:
        prefix = str(rowNum)
        if rowNum < 10:
            prefix = "0" + prefix
        ymlFile = prefix + '_chapter.markdown'
        ymlData = open(ymlFile, 'w')
        ymlData.write('---' + "\n")
        ymlData.write('layout: default' + "\n")
        ymlData.write('category: case-study' + "\n")
        # create content:
        # Title,Author(s) ,Presenter(s) if different,Presenter 1 bio,Presenter 2 bio,Presenter 3 bio,Presenter 4 bio,Abstract,Webinar link,Webinar date 
        print(row['Title'])
        ymlData.write('title: "' + row['Title'] + '"\n')
        ymlData.write('authors: ' + row['Authors'] + "\n")
        ymlData.write('printfile: ' + row['PDF'] + "\n")
        ymlData.write('printversion: ' + printversion + "\n")
        ymlData.write('onlinefile: ' + row['Online'] + "\n")
        ymlData.write('onlineversion: ' + printversion + "\n")
        if row['Webinar link'] != "":
            ymlData.write('webinarurl: ' + row['Webinar link'] + "\n")
            ymlData.write('webinardate: ' + row['Webinar date'] + "\n")
        ymlData.write('---' + "\n")
        ymlData.write('' + "\n")
        ymlData.write(row['Abstract'] + "\n")
        
        # wrap up
        ymlData.close()
        rowNum +=1
