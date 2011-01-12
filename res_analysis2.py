import os, getopt, sys

filename = "prova";
threshold = "1";
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
	opts, args = getopt.getopt(sys.argv[1:], "hf:v:", ["help", "file", "threshold"])
except getopt.GetoptError, err:
	print str(err)
	sys.exit(2)

for o, a in opts:
	if o in ("-h", "--help"):
		usage()
		sys.exit(0)
	
	if o in ("-f", "--file"):
		filename = a;
		
	if o in ("-v", "--threshold"):
		threshold = int(a);

# reading file

print "\nAnalyzing file " + filename;

print "\nDistribution of the percentage of FFT values over 95% in each run (should be around 5 for random data, and around 0 for periodic data).";

in_file = open(filename,"r")

for line in in_file:
	
	value = float(line);
	index = int(value);
	
	if (index > len(bin)):
		index = len(bin);
	
	bin[index] += 1;

tot = sum(bin);

if (tot != 0):

	print "\nFound " + str(tot) + " runs in file.";
	
	for i in range(len(bin)):
		bin_perc[i] = float(bin[i]) / float(tot) * 100;
		
	if ((bin_perc[0]+bin_perc[1]) > 50):
		print "\nFile seems PERIODICAL (over 50% of tests with less than 2% peaks in the FFT higher than 95% of expected value)"
	else:
		print "\nFile doesn't seem periodical";
	
	print "";
	
	for i in range(len(bin_perc)):
		string = str(i).zfill(2) + " - " + ("%3.2f" % bin_perc[i]).zfill(5) + "%  ";
		for rep in range(int(bin_perc[i])):
			string = string + "*";
		print string;
	
	print "\nWhere the column 0 contains results from 0.00 to 0.9999 and so on."
	
else:
	print "No results.\n";

in_file.close()