import numpy as np

tf=open("f.txt")
ls=[]
i=1
for line in tf:
    line = line.replace("\n",'')
    ls=line.split('\t')
    a=np.array(i,ls)
    i = i+1
 #   print(ls)
#   ls.append(line.split(","))
#print(ls)

print(a)
#tf.writelines('abcdef')
tf.close()
