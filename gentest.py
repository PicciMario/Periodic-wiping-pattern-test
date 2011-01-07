import os
import random
import getopt, sys

fileName = "test.dat";
seq = "abcdeFG";
numRip = 10000;

error_prob = 10;

#  usage

def usage():
	print "Periodic file generator (with noise)." 
	print " -h (--help)                    : this help";
	print " -s <seq> (--sequence <seq>)    : the base sequence";
	print " -o <file> (--output <file>)    : output file (default: test.dat)";
	print " -r <number> (--rip <number>)   : number of base sequences to write";
	print " -n <number> (--noise <number>) : noise probability in output file (0-100)";

# parsing command line arguments

try:
	opts, args = getopt.getopt(sys.argv[1:], "hs:o:r:n:", ["help", "sequence", "output", "rip", "noise"])
except getopt.GetoptError, err:
	print str(err)
	sys.exit(2)

for o, a in opts:
	if o in ("-h", "--help"):
		usage()
		sys.exit(0)
	
	if o in ("-s", "--sequence"):
		seq = a;
	
	if o in ("-o", "--output"):
		fileName = a;
	
	if o in ("-r", "--rip"):
		numRip = int(a);
	
	if o in ("-n", "--noise"):
		error_prob = a;

# creating the file

out_file = open(fileName,"w")
for i in range(numRip):
	if (random.uniform(1,100) <= error_prob):
		string = os.urandom(len(seq))
	else:
		string = seq
	out_file.write(string)
out_file.close()

# confirm

print("Generated file \""+fileName+"\" with "+str(numRip)+" elements of the sequence ["+seq+"] (noise probability:"+str(error_prob)+"%).");