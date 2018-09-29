import os
# import joblib
from joblib import Parallel, delayed
# for i in [1,5,10,20,40,60,120,200,300]:
	# print i
	# os.system("python subsampling_bam.py " + str(i))
def run(i):
	print i
	os.system("python subsampling_bam.py " + str(i))
	
Parallel(n_jobs=16)(delayed(run)(i) for i in range(1,60,5))