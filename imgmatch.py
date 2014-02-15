import sys, re, os, shutil, commands, imp


if len(sys.argv) > 1:
    gInputDir = sys.argv[1]
    print "Location of files to compare and csv of output is %s" % gInputDir
else:
    print ("Please pass target directory")

if len(sys.argv) == 3:
	print "Compiling regex for group A"
	patA = re.compile(sys.argv[2])
if len(sys.argv) == 4:
	print "Compiling regex for group A and B"
	patA = re.compile(sys.argv[2])
	patB = re.compile(sys.argv[3])



def list2csv(mylist,fn,header=[]): #ported from my utilities
	import csv

	with open(fn+".csv", 'wb') as f:
		spamWriter = csv.writer(f)
		if len(header) > 0:
			spamWriter.writerow(header)
		for x in mylist:
			spamWriter.writerow(x)

	return fn+".csv"

Alist= []
Blist = []
matched = []

for dirname, dirnames, filenames in os.walk(gInputDir):
    for filename in filenames:
        matA = re.match(patA,filename)
        if matA:					#if the filename matches pattern A:
        	Alist.append(filename)	#put it on the A list
        	continue
        else:
        	if patB:				#if there's a pattern B to consider,
				matB = re.match(patB,filename) #if the match is patB:
				if matB:
					Blist.append(filename)		#append to B list
        			continue
        	else:					#if there's no pattern B to consider,

sigtoAFile = {}					#make a hash table with the signatures of the images
for aFile in Alist:
	result = commands.getoutput("""identify -verbose %s | grep signature""" % os.path.join(gFolderLoc, aFile))
	resList = result.split()
	#print resList[1] 			#turn this on if you want to see the hashes fly by
	sigtoaFile[resList[1]] = aFile

for bFile in Blist:
	result = commands.getoutput("""identify -verbose %s | grep signature""" % os.path.join(gFolderLoc, bFile))
	resList = result.split()
	try:
		aFile = sigtoaFile[resList[1]]
		print "matched %s to %s" % (bFile,aFile) 	
		matched.append([bFile,aFile])
	except:
		print "couldnt match %s" % bFile
		matched.append([bFile,''])
	
list2csv(matched,os.path.join(gInputDir,'matchresults'))

