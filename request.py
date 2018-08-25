import requests
import hashlib,gzip
import http.client,json
import time

class devRequest():
    conn = http.client.HTTPSConnection("devhw.bianla.cn")
    headers = {"User-Agent":"okhttp/2.7.5", "Content-Type":"application/json;charset=utf-8"}
    def MD5(self,data):
        hashobj = hashlib.md5()
        hashobj.update(data.encode('utf-8'))
        return hashobj.hexdigest()
    # t = int(time.time())
    # sign = MD5('user_id=null&timestamp='+str(t)+'&token=null')
    # data = {"device_imei":"990009263653019","mac_address":"02:00:00:00:00:00","channel_id":"","dealer_code":"","device_details":{"device_model":"OD103","os_version":"7.1.1","device_resolution":3000,"app_name":"变啦国际版","app_version_number":"1.1.1","local_language":"zh"}}
    # params = json.dumps(data)
    #
    # conn.request("POST", "/api/users/startup.action?user_id=null&timestamp="+str(t)+"&sign="+sign+"&local_language=zh",\
    #              params.encode('utf-8'), headers)
    # response = conn.getresponse()
    # back = response.readline()
    # a = '23421'
    # a1 = gzip.compress(a)
    # a2 = gzip.decompress(a1)
    # #b1 = gzip.decompress(back)
    #
    # one = response.headers
    # two = response.getcode()
    # three = response.info()
    # print(response.status)
    # print(one)
    # print(two)
    def login(self,phone, pwd):
        t = int(time.time())
        sign = self.MD5('user_id=null&timestamp='+str(t)+'&token=null')
        print(sign)
        userInfo = {"phone_number":phone,"password":pwd,"local_language":"zh","phone_number_prefix":"+86"}
        params = json.dumps(userInfo)
        path = "/api/users/login.action?user_id=null&timestamp="+str(t)+"&sign="+str(sign)+"&local_language=zh)"
        self.conn.request("POST",path,params.encode('utf-8'),self.headers)
        return self.conn.getresponse()
test = devRequest()
user_login=test.login('13281549858','123456')
user_info =user_login.read().decode('utf-8 ')
print(user_info)