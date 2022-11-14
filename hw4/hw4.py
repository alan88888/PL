import jieba as jb
from collections import Counter
from matplotlib import pyplot as mt
from wordcloud import WordCloud
jb.set_dictionary('dict.txt.big')
with open ('stops.txt','r',encoding='utf-8') as st:
    stops=st.read().split('\n')
    stops.append('\n')  
    stops.append('\n\n')
#teststr='''中文自然語言處理，與英文最大的差別就在斷詞，但是說實話，這個部分至今仍然沒有一個套件可以做好很好。目前而言，繁體中文有兩個套件可以使用，一個是中研院開發的斷詞系統，但是經過多方打聽，使用上並不是特別方便。因此我個人打選擇使用第二套系統jieba，中文叫做結巴，很幸運地這個套件有python的介面，使用上非常容易，只是這是大陸人開發的系統，必須自行輸入繁體字典，這篇文章的繁體字典出處在這邊。順帶一提，這篇文章寫得很好，對於jieba如果有想要有更深的認識，可以好好拜讀。'''
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
