import re
import requests
import time
import datetime

# def getYesterday():
#     yesterday = datetime.date.today() + datetime.timedelta(-1)
#     return yesterday
import datetime

def getday(day):
    today = datetime.date.today()
    oneday = datetime.timedelta(days=day)
    yesterday = today - oneday
    return yesterday.__str__()
# p=(str)(getYesterday())
# print(p)
mylist=[]
mylist_name=[]
url1="https://github.com/"
url2=""
headers = {'Cookie':'dotcom_user=; tz=Asia%2FShanghai'}
c={}
dic = []
for j in range(0,41):
    url2=mylist[j]
    URL = url1 + url2
    for i in re.findall('<rect .*? fill="(.*?)" data-count="(.*?)" data-date="(' + getday(1) + ')"/>',
                            requests.get(URL, headers=headers).text):
      #  print(i)
        c=((int)(i[1]),mylist_name[j])
        print(c)
        dic.append(c)
#print(dic)
re=sorted(dic)
#print(re)
print("易架构2019年 "+getday(0)+" GitHub贡献汇总如下：")
for q in re:
    print(q)
