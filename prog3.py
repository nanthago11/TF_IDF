import os
import re 
import sys 
import collections 
import math 

#python prog3.py out2.txt out3.txt 
def main():
	inputfile_str=sys.argv[1]
	outputfile_str=sys.argv[2]
	OutFilename1 = open( os.path.join(os.getcwd() ,outputfile_str ), "w")
	InFilename1 = open( os.path.join(os.getcwd() ,inputfile_str ), "r") 
	BigFullHlist=[]
	FinalStringValue=""
	UniqueBigFullHlist=[]

	for line in InFilename1:
		WholeLine=line.replace('\n', '')
		LineSplit = list(WholeLine.split("\t")) 
		fString=list(LineSplit[0].split(" "))
		remList=list(set(LineSplit) - set(fString))
		BigFullHlist=BigFullHlist+remList
	##Only extract Uniqe values from list
	for x in BigFullHlist: 
			if x not in UniqueBigFullHlist: 
				UniqueBigFullHlist.append(x) 
	TempListSort=list(set(UniqueBigFullHlist) - set([' ','','\t']))
	TempListSort.sort()
	FinalStringValue=FinalStringValue+"\t\t\t"+"\t".join(TempListSort)+"\n"
	InFilename1 = open( os.path.join(os.getcwd() ,inputfile_str ), "r") 
	for line in InFilename1:
		WholeLine=line.replace('\n', '')
		LineSplit = list(WholeLine.split("\t")) 
		fString=list(LineSplit[0].split(" "))
		remList=list((set(LineSplit) - set(fString))-set([' ','','\t']))
		FinalStringValue=FinalStringValue+LineSplit[0]+"\t\t"
		for each in TempListSort:
			if each in remList:
				FinalStringValue=FinalStringValue+"{0:.3f}".format(float(math.log10(float(len(TempListSort))/float(len(remList)))))+"\t"
			else : 
				FinalStringValue=FinalStringValue+"0"+"\t"
		FinalStringValue=FinalStringValue+"\n"
	OutFilename1.write(FinalStringValue)

	OutFilename1.close()
	InFilename1.close()

main()