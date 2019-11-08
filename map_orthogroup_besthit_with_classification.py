#/usr/bin/env python
# Written by P.R. Timilsena 
# This file combines annotation files from blast2go with orthogroup cluster files from gene family classification using plnttribes
# The blast2go file is the first argument and the gene family classification the second argument. 


import os, sys, re

Usage = """Usage: map_orthogroup_besthit_with_classification.py blast2go_file genefamily_file combined_output_file
Please make sure your files are in proper order"""

if sys.argv[1] == "-h" or sys.argv[1] == "--h" or sys.argv[1] == "-help":
    print Usage
    sys.exit(1)

blast2gofile =	sys.argv[1]
genefamilyfile = sys.argv[2]
outputfile = sys.argv[3]



def open_file(filename):
	genes = {}
	with open(filename, "r") as fhi:
		for line in fhi:
			line = line.rstrip() 
			id = re.split(r'\t', line)[0]
			genes[id] = re.split(r'\t', line)[1:]		
	return genes
	

blast2goannot = open_file(blast2gofile)
genefamilyclass = open_file(genefamilyfile)
print(genefamilyclass)
#print(blast2goannot)

fho = open(outputfile, "w")
for gene_ids in blast2goannot.keys():
	fho.write("%s\t" %gene_ids)
	#print(genefamilyclass.get(gene_ids))
	#fho.write(genefamilyclass.get(gene_ids, "unsorted"))
	#print(blast2goannot.get(gene_ids))
	fho.write("%s\t" %genefamilyclass.get(rstrip(gene_ids), "unsorted"))
	fho.write("%s\n" %blast2goannot.get(gene_ids))

fho.close()