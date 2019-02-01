#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:11:27 2018

@author: rld1996
"""

import time
startToken=time.time()
import re
cont=""

import glob

p = raw_input("Enter the path of your file: ")
if p=="":
    p="/people/cs/s/sanda/cs6322/Cranfield"
cnt=0
c=0
a=[]
b=[]
tot=[]
freq={}
average=[]
path=p+"/*"
#path = '/Users/rld1996/Desktop/IR/Assignment 1/*.txt'
unique=[]
files=glob.glob(path)
for file in files:
    f=open(file, 'r')
    for cont in f:
        clean=re.compile('<.*?>')
        cont=re.sub(clean,"",cont)
        cont=re.sub(r'[,-]'," ",cont)
        cont=re.sub(r'[^\w\s]', '', cont)
        tokens=re.sub(r'[0-9]+', ' ', cont)
        tokens=tokens.strip("\n")
        
        b=tokens.split()
        if b!= []:
            for x in b:
             
                x=x.lower()
                tot.append(x)
                if x not in a:
                    a.append(x)
                else:
                    if x not in freq:
                        freq[x]=2
                    else:
                        cntr=freq.get(x)+1
                        freq[x]=cntr
              
for x in a:
    if x not in freq:
        unique.append(x)
#print a
import operator

sorted_x = sorted(freq.items(), key=operator.itemgetter(1))
freq30=sorted_x[len(sorted_x)-30:]
endToken=time.time()-startToken
print "Tokens:"
#print tot
print "No of tokens"
print len(tot)
print "No of distinct tokens"
print len(a)
print "frequent 30"
print freq30
print "average tokens per doc"
print float(len(tot))/float(1400)
print "average unique tokens per doc"
print float(len(a))/float(1400)
print "no of tokens that occur only once"
print len(unique)
print "Time taken for the program to get all tokens and lists"
print endToken

startStem=time.time()
from nltk.stem import PorterStemmer
stemm=[]
stemOnce=[]
fstems={}
savg=[]
sc=0
ps=PorterStemmer()
stemNew=[]
for x in tot:
    
    
    s=ps.stem(x)
    s=s.encode("utf-8")
    stemm.append(s)
    if s not in stemOnce:
        stemOnce.append(s)
    else:
        if s not in fstems:
            fstems[s]=2
        else:
            cntr=fstems.get(s)+1
            fstems[s]=cntr

for x in stemm:
    if x not in fstems:
        stemNew.append(x)
endStem=time.time() -startStem 
print "No. of total stems  "
print len(stemm)  
print "no of distinct stems"
print len(stemOnce)
sorted_fstems = sorted(fstems.items(), key=operator.itemgetter(1))
freqStems30=sorted_fstems[len(sorted_fstems)-30:]
print "Most frequent 30 stems"
print freqStems30
print "Number of stems that occur only once"
print len(stemNew)
print "Average Number of unique stems per document"
print float(len(stemOnce))/float(1400)
print "Average Number of stems per document"
print float(len(stemm))/float(1400)
print "time taken for getting stems and stem lists"
print endStem