import json
import requests

url = 'https://restapi.amap.com/v3/geocode/geo'
para = {
    'address' : '',
    'key' : "25411e0758eb9f7b742cfa331a2a75c6",
} #可通过设定参数方式避免报错，参考https://blog.csdn.net/m0_67575344/article/details/127662148

with open('./985_name.txt', 'r') as f:
    for name in f.readlines():
        name = name.strip() #去除可能存在的空格和换行符
        para['address'] = name
        response = requests.get(url, params = para) # 向url发送请求
        data = response.json() #获取url对应的json文件，参考https://www.jiyik.com/tm/xwzj/prolan_4664.html和https://www.volcengine.com/theme/6505311-R-7-1
        location = data['geocodes'][0]['location']
        with open ('./985_location.txt', 'a') as fl:
            fl.write('{1}{0}{2}\n'.format('|', name , location))

# 进一步参考：https://blog.csdn.net/qq_42370313/article/details/121869032