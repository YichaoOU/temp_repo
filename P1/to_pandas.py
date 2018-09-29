

import pandas as pd
import os
import seaborn as sns
import glob
df = []

for i in range(1,60,5):
	mem = int(open(str(i)+".size").readlines()[0].split()[1]) 
	input_file = glob.glob("*."+str(i)+".bam")[0]
	input_size = os.path.getsize(input_file) /1024
	output_size = os.path.getsize(str(i)+".bsorted.pairs.gz") /1024
	df.append([input_size,mem,output_size])
df = pd.DataFrame(df,columns=['input_size','mem','output_size'])

df.to_csv("P1.csv",index=False)


sns.lmplot(x="input_size", y="output_size",data=df)

sns.lmplot(x="input_size", y="mem",data=df)