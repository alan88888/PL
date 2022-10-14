import json
import os,time
file=r".\hw2.json"
test=open(file,encoding="utf8")
data=json.load(test)
dicname=data.get('cofopdlbyacadm')
usrinput=input("hw2查詢-請輸入你想要查詢的課程名稱或開課代碼:\n")
find=0
#print ("原始 JSON 數據：\n {0}".format ( dicname ) )

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
    print("查詢不到您輸入的課程\n")

print("hw2排序-正在利用開課代碼排序\n")
time.sleep(1)
sorted_json_data = json. dumps ( dicname , sort_keys = True , ensure_ascii=False)
print("base_the_key:\n{0}".format(sorted_json_data))
        
