#!/usr/bin/python
#splitBitext.py
#Weston Feely
#1/22/14
import sys, os, re, random, math

def main(args):
	#Check args
	if len(args) < 3:
		print "Usage: python splitBitext.py src.txt tgt.txt"
		return 1
	srcpath, src = os.path.split(args[1].rstrip('.txt'))
	tgtpath, tgt = os.path.split(args[2].rstrip('.txt'))
	srctext = open(args[1]).readlines()
	tgttext = open(args[2]).readlines()
	assert len(srctext) == len(tgttext)
	num_segments = len(srctext)
	#Set fraction of data to use for train, tune, test
	train_fraction = 0.98
	tune_fraction = 0.01
	test_fraction = 0.01
	assert (train_fraction + tune_fraction + test_fraction) == 1.0
	#Loop through data
	parallel = []
	for i in xrange(num_segments):
		parallel.append((srctext[i],tgttext[i]))
	#Shuffle segments
	random.shuffle(parallel)
	#Split shuffled sentences into training and test sets
	num_train = int(num_segments*train_fraction) # number of segments to be in train set
	num_tune = num_train + int(math.ceil(num_segments*tune_fraction)) # number of segments to be in tune set	
	train_set = [] # list of string 2-tuples, to write to file as training set
	tune_set = [] # list of string 2-tuples, to write to file as tune set
	test_set = [] # list of string 2-tuples, to write to file as test set
	#Loop through segments
	for i in xrange(num_segments):
		if i < num_train:
			#Put segment in training set
			train_set.append(parallel[i])
		elif i < num_tune:
			#Put segment in tune set
			tune_set.append(parallel[i])
		else:
			#Put segment in test set
			test_set.append(parallel[i])
	#Write sets to file
	src_set = os.path.join(srcpath, src+'-shuffled.txt')
	tgt_set = os.path.join(tgtpath, tgt+'-shuffled.txt')
	src_train_fn = os.path.join(srcpath, 'train-'+src+'.txt')
	tgt_train_fn = os.path.join(tgtpath, 'train-'+tgt+'.txt')
	src_tune_fn = os.path.join(srcpath, 'tune-'+src+'.txt')
	tgt_tune_fn = os.path.join(tgtpath, 'tune-'+tgt+'.txt')
	src_test_fn = os.path.join(srcpath, 'test-'+src+'.txt')
	tgt_test_fn = os.path.join(tgtpath, 'test-'+tgt+'.txt')
	#Write all data
	f = open(src_set,'w')
	g = open(tgt_set,'w')
	for pair in parallel:
		f.write(pair[0])
		g.write(pair[1])
	f.close()
	g.close()
	#Write training set
	f = open(src_train_fn,'w')
	g = open(tgt_train_fn,'w')
	for pair in train_set:
		f.write(pair[0])
		g.write(pair[1])
	f.close()
	g.close()
	#Write tune set
	f = open(src_tune_fn,'w')
	g = open(tgt_tune_fn,'w')
	for pair in tune_set:
		f.write(pair[0])
		g.write(pair[1])
	f.close()
	g.close()
	#Write test set
	f = open(src_test_fn,'w')
	g = open(tgt_test_fn,'w')
	for pair in test_set:
		f.write(pair[0])
		g.write(pair[1])
	f.close()
	g.close()
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
