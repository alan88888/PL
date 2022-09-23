import csv
import pandas as pd
with open('pyhw105.csv','r',encoding='utf-8') as df1,open('pyhw106.csv','r',encoding='utf-8') as df2:
    reader1=csv.reader(df1)
    reader2=csv.reader(df2)
    p1=pd.Series(reader1)
    p2=pd.Series(reader2)
    for i in p1:
        ps1=set(i)
        for j in p2:
            ps2=set(j)
            print(ps1|ps2)
            print(ps1&ps2)
            print(ps1-ps2)
            print(ps1^ps2)
   

