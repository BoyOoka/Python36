import requests
import hashlib
import http.client,json
import time

def MD5(data):
    hashobj = hashlib.md5()
    hashobj.update(data.encode('utf-8'))
    return hashobj.hexdigest()
t = int(time.time())
print(t)
sign = MD5('user_id=null&timestamp='+str(t)+'&token=null')
print(sign)
headers = {"User-Agent":"okhttp/2.7.5", "Content-Type":"application/json;charset=utf-8"}
data = {"device_imei":"990009263653019","mac_address":"02:00:00:00:00:00","channel_id":"","dealer_code":"","device_details":{"device_model":"OD103","os_version":"7.1.1","device_resolution":3000,"app_name":"变啦国际版","app_version_number":"1.1.1","local_language":"zh"}}
params = json.dumps(data)
conn = http.client.HTTPSConnection("devhw.bianla.cn")
conn.request("POST", "/api/users/startup.action?user_id=null&timestamp="+str(t)+"&sign="+sign+"&local_language=zh",\
             params.encode('utf-8'), headers)
response = conn.getresponse()
back = response.readline()
one = response.headers
two = response.getcode()
three = response.info()
print(response.status)
print(back.decode('utf-8'))
print(one)
print(two)

name = 'laogaoyang'
nameBytes = name.encode('utf-8')   # 字节
nameStr = nameBytes.decode('utf-8')# 字符串
print(name)
print(nameBytes)
print(nameStr)
#conn.set_tunnel("www.python.org")
#conn.request("HEAD","/index.html")
'''
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.headers)
r = requests.get('http://chaoao.iteye.com/')
#rs = requests.get('https://www.baidu.com', cafile='')
herder = r.headers
print(herder)
print(type(herder))
'''