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
        _learn_key(bigram[0], bigram[1])


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
with open('nonself1.csv', 'r') as csvfile:

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


chunks = [ll[x:x+2] for x in range(0, len(ll), 2)]

counter = {}
for el in chunks:
    el = str(el)
    if el in counter:
        counter[el]+=1
    else:
        counter[el]=1



coll = ([(v,k) for (k,v) in counter.items()])
tokens = call
bigrams = [(tokens[i],tokens[i+1]) for i in range(0,len(tokens)-1)]

#print(bigrams)




###
m = learn(bigrams)
from collections import Counter


new = {}
for k,v in memory.items():
    c=Counter()
    #print(k,v)
    #print("\n")
    for letter in v:
        c[letter] += 1
    v = [(i, c[i] / len(v)) for i in c]
    new[k] = v



royal_probability = 0
flag = 0
flog = 0
for i in bigrams:
    for k,v in new.items():

         if(i[0] in k):
             #print("match")
             nucor = new[k]
             test = dict(nucor) 
             print(test)


             if i[1] in test:
                  flag = 1 + flag

print(flag/leng)

#print(new)
##########################################################################
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

leng = i
for i in tensor1:
    time1.append(i[0])
    call1.append(i[1])




tokens1 = call1
bigrams1 = [(tokens1[i],tokens1[i+1]) for i in range(0,len(tokens1)-1)]


royal_probability = 0
flag = 0
flog = 0
for i in bigrams1:
    for k,v in new.items():

         if(i[0] in k):
             #print("match")
             nucor = new[k]
             test = dict(nucor) 



             if i[1] in test:
                  flag = 1 + flag

print(flag/leng)

