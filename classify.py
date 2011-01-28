import os, getopt, sys

filename = "";
bin = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bin_perc = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

#  usage

def usage():
	print "Output file analyzer."
	print "Analyzes a file with a single numeric column."; 
	print " -h (--help)                    : this help";
	print " -f <file> (--file <file>)      : input file (default: " + prova + ")";
	print " -v <th> (--threshold <th>)     : threshold in column 1 to achieve a positive line"

# parsing command line arguments

try:
	opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file"])
except getopt.GetoptError, err:
	print str(err)
	sys.exit(2)

for o, a in opts:
	if o in ("-h", "--help"):
		usage()
		sys.exit(0)
	
	if o in ("-f", "--file"):
		filename = a;

# reading file

in_file = open(filename,"r")

for line in in_file:
	
	value = float(line);
	index = int(value);
	
	if (index > len(bin)):
		index = len(bin);
	
	bin[index] += 1;

tot = sum(bin);

if (tot != 0):
	
	for i in range(len(bin)):
		bin_perc[i] = float(bin[i]) / float(tot) * 100;
	
	# condition
	
	if ((bin_perc[0]+bin_perc[1]) > 90):
		print "1"
	else:
		print "0";
	
else:
	print "0";

in_file.close()