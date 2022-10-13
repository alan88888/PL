import json

file=r".\hw2.json"
test=open(file,encoding="utf8")
data=json.load(test)
dicname=data.get('cofopdlbyacadm')
usrinput=input("請輸入你想要查詢的課程名稱或開課代碼:\n")
find=0
for i in dicname:
    if usrinput == i.get("中文課程名稱"):
        for key,value in i.items():
            print(key,value)
            find=1
    elif usrinput == i.get("開課代碼"):
        for key,value in i.items():
            print(key,value)
            find=1
if find == 0:
    print("查詢不到您輸入的課程")
        
