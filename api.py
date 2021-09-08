import requests
import time

url = 'https://catfront.dianping.com'     #这里url末尾不能有'/'
with open("api字典.txt", 'r') as web:
    webs = web.readlines()
w = open('easyresult1.txt', 'w+')
for web in webs:
    web = web.strip()
    u = url + web
    response = requests.get(u)
    
    #print("url为:"+u)
    print("url为:" + u + ' ' + "状态为:%d"%response.status_code + ' ' + "content-length为:" + str(len(response.content)))
    time.sleep(2)       #想睡多久看自己~
    w.write("url为:" + u + ' ' + "状态为:%d"%response.status_code + ' ' + "content-length为:" + str(len(response.content)) + '\n')