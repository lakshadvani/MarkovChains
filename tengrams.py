from numpy import array
import csv
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

royal_probability = 0


memory = {}
def _learn_key(key, value):
    if key not in memory:
           memory[key] = []
    memory[key].append(value)

def learn(bigrams):


    for bigram in bigrams:
        for i in range(0,len(bigram)-1):

            _learn_key(bigram[i], bigram[i+1])
tensor = []


ll = []
troika = []
with open('mapping.txt', 'r') as map1:

    map1 = csv.reader(map1)
    for row in map1:
        troika.append(row)
troika = [item for sublist in troika for item in sublist]

#print(troika)

tensor = []
with open('exploit2.csv', 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    next(csvreader)
    i = 0
    for row in csvreader:
        i = i +1
        num = row[1]
        index = int(num)-1
        row[1] = troika[index]
        tensor.append([i,row[1]])
        ll.append(row[1])

time = []
call = []
leng = i
for i in tensor:
    time.append(i[0])
    call.append(i[1])

from collections import Counter
Q = Counter(call).items()



percentages = {x: (float(y) / len(call)) for x, y in Q}
q = {}
for name, pct in percentages.items():
    q[name] = pct



chunks = [ll[x:x+9] for x in range(0, len(ll), 10)]

counter = {}
for el in chunks:
    el = str(el)
    if el in counter:
        counter[el]+=1
    else:
        counter[el]=1



coll = ([(v,k) for (k,v) in counter.items()])
tokens = call
bigrams = [call[i:i+2] for i in range(0, len(call), 2)]
tengrams = [call[i:i+10] for i in range(0, len(call), 10)]
#print(tengrams)



###
m = learn(bigrams)
from collections import Counter


new = {}
for k,v in memory.items():
    c=Counter()
    for letter in v:
        c[letter] += 1
    v = [(i, c[i] / len(v)) for i in c]
    new[k] = v



royal_probability = 0
flag = 0
flog = 0
for i in bigrams:
  if(len(i)>1):
    for k,v in new.items():
         if(i[0] in k):
             nucor = new[k]
             test = dict(nucor) 
             if i[1] in test:
                  flag = 1 + flag
  else:
      pass
print(flag/leng)
#print(new)
#print(new)
#####################################################################################################################################################
ll1 = []
tensor1= []
time1 = []
call1 = []
with open('exploit2.csv', 'r') as csvfile1:
    csvreader1 = csv.reader(csvfile1)
    next(csvreader1)
    i = 0
    for row in csvreader1:
        i = i +1
        num1 = row[1]
        index1 = int(num1)-1
        row[1] = troika[index1]
        tensor1.append([i,row[1]])
        ll1.append(row[1])
for i in tensor1:
    time1.append(i[0])
    call1.append(i[1])
prob_seq = []
tokens1 = call1
tengrams1 = [call1[i:i+10] for i in range(0, len(call1), 10)]

leng = len(tengrams1)
royal_probability = 0
flag = 0
flog = 0

yankee_white = []
for i in tengrams1:
    seq = []
    probs = []
    z = 1
    if(i[0] in q):
         init = q[i[0]]
    else:
         init = 0
    if(i[0] in new):
       probs = dict(new[i[0]])
       for k in range(1,len(i)-1):
           if(i[k] in probs):
               seq.append(probs[i[k]])

           else:
               seq.append(0)
    for ii in seq:
         z = ii*z
    yankee = z*init
    #print(sum(seq))
    yankee_white.append(yankee)
print(sum(yankee_white)/leng)
