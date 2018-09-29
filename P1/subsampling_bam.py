import pysam
from random import choice
import os
import sys
import uuid
sample_ratio = int(sys.argv[1])
# pysam.sort('-o','liyc.bam',"SRR1658652.bam")
# pysam.index("liyc.bam")

bam = pysam.AlignmentFile("liyc.bam",'rb')


out_bigger_bam = str(uuid.uuid1())+"."+str(sample_ratio)+".bam"
bigger_bam = pysam.AlignmentFile(out_bigger_bam, "wb", template=bam)
# my_lines = bam.fetch()
# for read in [choice(my_lines) for _ in range(int(sample_ratio*len(my_lines)))]:
    # bigger_bam.write(read)
for read in bam:
    map(lambda x:bigger_bam.write(read),range(sample_ratio))


bigger_bam.close()

print out_bigger_bam," generation Done"

command  = '/usr/bin/time -f "mem: %M kilobytes" -o ' + str(sample_ratio) + ".size " + "./bam2pairs " + out_bigger_bam + " " +str(sample_ratio) + ""

os.system(command)
# os.system("rm " + out_bigger_bam)

print "finished",sample_ratio,out_bigger_bam