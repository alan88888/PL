import jieba as jb
import networkx as nx
from collections import Counter
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import scipy as sp
import pandas as pd
import jieba.posseg as pseg
import os
#os.system("pip install scipy")
#os.system("pip install networkx")
#os.system("pip install jieba")
#os.system("pip install matplotlib")
jb.set_dictionary('dict.txt.big')
with open ('stops.txt','r',encoding='utf-8') as st:
    stops=st.read().split('\n')
    stops.append('\n')  
    stops.append('\n\n')
    stops.append('。」')
    stops.append('羅斯')
    stops.append('克蘭')
    stops.append('已經')
    stops.append('赫爾')
    stops.append('克里')
    stops.append('里米')
    stops.append('米亞')
    stops.append('亞運')
with open('hw5.txt','r',encoding='utf-8') as text:
    teststr=text.read()
terms = [t for t in jb.cut(teststr, cut_all=True) if t not in stops]
counter=sorted(Counter(terms).items(), key=lambda x:x[1], reverse=True)
data = pd.DataFrame(counter)
print(data)
for i in range(len(data[0])):
  for j in list(jb.cut(data[0][i],cut_all=False)):
    if j not in stops:
      terms.append(j)
firstcolum = {}          
relationships = {}  
toprow = []  
for i in range(len(data[0])):
        poss = jb.cut(data[0][i], cut_all = False)
        toprow.append([])
        for w in poss:
            if w not in stops:
                toprow[-1].append(w)        
            if firstcolum.get(w) is None and w not in stops:
                relationships[w] = {}
term_dic = dict()
for sentence in toprow:
    for term in sentence:
        if term not in term_dic:
            term_dic[term] = {}
matrix = pd.DataFrame.from_dict(term_dic)
comatrix = matrix.T.dot(matrix)
print(comatrix)
