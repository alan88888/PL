import jieba as jb
import networkx as nx
from collections import Counter
from matplotlib import pyplot as mt
from wordcloud import WordCloud
jb.set_dictionary('dict.txt.big')
with open ('stops.txt','r',encoding='utf-8') as st:
    stops=st.read().split('\n')
    stops.append('\n')  
    stops.append('\n\n')
    stops.append('羅斯')
    stops.append('克蘭')
    stops.append('已經')
    stops.append('赫爾')
    stops.append('克里')
    stops.append('里米')
with open('hw4.txt','r',encoding='utf-8') as text:
    teststr=text.read()
terms = [t for t in jb.cut(teststr, cut_all=True) if t not in stops]
sorted(Counter(terms).items(), key=lambda x:x[1], reverse=True)  
wordcloud = WordCloud(font_path="simsun.ttf")
wordcloud.generate_from_frequencies(frequencies=Counter(terms))
fig=mt.figure(figsize=(15,15))
mt.imshow(wordcloud,interpolation="nearest")
mt.axis("off")
#mt.show()
fig.savefig('hw4.png')
