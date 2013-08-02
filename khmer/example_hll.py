from pylab import *
import khmer
import random
from collections import defaultdict
from khmer_hll import KmerCardinality

TRIAL_N = 10000

def trial():

	k=22
	
	counter=KmerCardinality(10, k)
	
	given_string = ["A","C","G","T"]*(TRIAL_N/4)
	random.shuffle(given_string)
	given_string = "".join(given_string)
	
	counter.consume(given_string)
	#counter.consume_file('*.fa')
	
	d=defaultdict(int)
	
	for i in range(len(given_string)-k+1):
		d[given_string[i:i+k]] += 1

	real_num=len(d)
	estimated = counter.cardinality() 

	error_rate=abs(real_num - estimated )/real_num

	print real_num, estimated
	
	if error_rate < 1:
		print error_rate 
	else:
		print 'irrelevant'
	
for i in range(5):
	trial()
