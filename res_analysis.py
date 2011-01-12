import os, getopt, sys

filename = "prova";

bin = [0,0,0,0,0,0,0,0,0,0];
bin_perc = [0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00];
testFilter = "";

positives = 0;
threshold = 50;
lines = 0;

#  usage

def usage():
	print "Output file analyzer." 
	print " -h (--help)                    : this help";
	print " -f <file> (--file <file>)      : input file (default: " + prova + ")";
	print " -t <test> (--test <test>)      : test to retrieve data from"
	print " -v <th> (--threshold <th>)     : threshold in column 1 to achieve a positive line"

# parsing command line arguments

try:
	opts, args = getopt.getopt(sys.argv[1:], "hf:t:v:", ["help", "file", "test", "threshold"])
except getopt.GetoptError, err:
	print str(err)
	sys.exit(2)

for o, a in opts:
	if o in ("-h", "--help"):
		usage()
		sys.exit(0)
	
	if o in ("-f", "--file"):
		filename = a;
		
	if o in ("-t", "--test"):
		testFilter = a;
		
	if o in ("-v", "--threshold"):
		threshold = int(a);

# reading file

testDescr = " all tests.";
if (testFilter != ""):
	testDescr = testFilter + " test.";

print "\nAnalyzing file " + filename + " for results of " + testDescr;

in_file = open(filename,"r")

for line in in_file:
	elements = line.split();
	
	# estract elements from the read line
	c1 = int(elements[0]);
	c2 = int(elements[1]);	
	c3 = int(elements[2]);
	c4 = int(elements[3]);	
	c5 = int(elements[4]);	
	c6 = int(elements[5]);	
	c7 = int(elements[6]);
	c8 = int(elements[7]);	
	c9 = int(elements[8]);	
	c10 = int(elements[9]);
	perc = elements[10];
	esit = elements[11];
	test = elements[12];
	date = elements[13];
	hour = elements[14];
	file = elements[15];
	
	if ((testFilter == test) | (testFilter == "")):
	
		lines += 1;
	
		# inserts elements into bins
		bin[0] += c1;
		bin[1] += c2;
		bin[2] += c3;
		bin[3] += c4;
		bin[4] += c5;
		bin[5] += c6;
		bin[6] += c7;
		bin[7] += c8;
		bin[8] += c9;
		bin[9] += c10;	
		
		# test single positive lines		
		if (c1 >= threshold):
			positives = positives + 1;

tot = sum(bin);

if (tot != 0):
	for i in range(len(bin)):
		bin_perc[i] = float(bin[i]) / float(tot) * 100;
	
	for i in range(len(bin_perc)):
		print str(i) + " - " + ("%3.2f" % bin_perc[i]).zfill(5) + " %";
	
	print "    " + str(sum(bin_perc)) + " %";

	positivesPerc = float(positives) / float(lines) * 100;
	print "Positive tests (with " + str(threshold) + " threshold): " + str(positives) + "/" + str(lines) + " (%3.2f" % positivesPerc + " %)\n";

else:
	print "No result for selected test(s).\n";

in_file.close()