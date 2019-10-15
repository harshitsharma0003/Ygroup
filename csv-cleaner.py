
#!/usr/bin/python

import csv

filename    = "merged_dataset.csv"
outputFile  = "clean-file.csv"
delimiterToReplaceWith = "_"        # For individual values that consists of ',' will be replaced  by this.  
checkingDelimiter = '"'
outputData = []


def replaceString ( substring ):
    x = substring.replace(",", delimiterToReplaceWith)
    #print ("[*] replaceString : " , substring , " : " ,x)
    return x

def cleanRow( oneRowOfData ):
    """
        Clean row i.e for comma seperated values in the row , where individual values also consists of ',' in them , it replaces those commans with the 'delimiterToReplaceWith'.
        Constraint : Those individual values which contains the commas must be inside '"'(double-quotes) , that's how it checks it.
        Also , this will replace the double quotes which were present in the original string, as not required now.

        Example : 
            Input  : 4,4,10816,"Grimb Blonde BOT 4X6X0,25 TraN","Grimb Blonde BOT 4X6X0,25 ",CH,G,"Grimb Blonde BOT 4X6X0,25 TraN",80,,"GLASS BTL, ONE WAY"
            Output : 4,4,10816,"Grimb Blonde BOT 4X6X0_25 TraN","Grimb Blonde BOT 4X6X0_25 ",CH,G,"Grimb Blonde BOT 4X6X0_25 TraN",80,,"GLASS BTL_ ONE WAY"
    """
    #print ("Input String  : " , oneRowOfData , " : " , len(oneRowOfData))
    newString = ""
    start = 0
    while (start != -1):
        start = oneRowOfData.find(checkingDelimiter)
        newString += oneRowOfData[:start]
        oneRowOfData = oneRowOfData[start+1:]
        end = oneRowOfData.find(checkingDelimiter)
        #print ("start : {} , end : {}".format(start,end)) 
        if (start == -1 or end == -1):
            break
        newString += replaceString(oneRowOfData[:end])
        oneRowOfData = oneRowOfData[end+1:]

    #print()
    #print ("Returning     : " , newString)
    return newString


def main():

    inputData  = None

    with open(filename,"r")as f:
        inputData = f.readlines()

    skipFirst = 1
    for row in inputData:
        if skipFirst != 1:
            x = cleanRow(str(row))
            x = ",".join(x.split(",")[1:])
        else:
            x = str(row)
        #print (x)
        outputData.append(x)
        skipFirst +=1

    with open(outputFile, "w") as csv_file:
        for line in outputData:
            csv_file.write(line)
            csv_file.write('\n')

if __name__ == "__main__":
    main()

