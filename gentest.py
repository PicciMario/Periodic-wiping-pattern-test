import os
import random

fileName = "test.dat";
seq = "abcdeFG";
numRip = 10000;

error_prob = 10;

out_file = open(fileName,"w")
for i in range(numRip):
	if (random.uniform(1,100) <= error_prob):
		string = os.urandom(len(seq))
	else:
		string = seq
	out_file.write(string)
out_file.close()

print("Generato file \""+fileName+"\" con "+str(numRip)+" ripetizioni della sequenza ["+seq+"] (rumore:"+str(error_prob)+"%).");