import numpy as np
from make_sentence import *
import sys

a = 0
literature = []
print(sys.argv[0])
input = str(sys.argv[1])
output1 = str(sys.argv[2])
output2 = str(sys.argv[3])
with open(input, "r") as f:
    f1 = f.readlines()
    #print(f1[4])
    for i in enumerate(f1):
        for j in enumerate(i[1]):
            if j[1] == "$":
                #print(i)

                literature.append(np.array((i[0],obtain_sentence(f1,i[1],i[0],j[0]))))

                a += 1

with open(output1, "+w") as f:
    for i in range(len(literature)):
        f.write(np.array(literature)[:,1][i][1])
with open(output2, "+w") as f:
    for i in range(len(literature)):
        f.write(np.array(literature)[:,1][i][0])
        f.write("\n")
