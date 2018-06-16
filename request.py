import hashlib
import http.client, json
import time


class DevRequest:
    conn = http.client.HTTPSConnection("devhw.bianla.cn")
    headers = {"User-Agent": "okhttp/2.7.5", "Content-Type": "application/json;charset=utf-8"}

    def md5(self, data):
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

    def login(self, phone, pwd):
        t = int(time.time())
        sign = self.md5(self, 'user_id=null&timestamp='+str(t)+'&token=null')
        print(sign)
        userinfo = {"phone_number": phone, "password":  pwd, "local_language": "zh", "phone_number_prefix": "+86"}
        body = json.dumps(userinfo)
        path = "/api/users/login.action?user_id=null&timestamp="+str(t)+"&sign="+str(sign)+"&local_language=zh)"
        self.conn.request("POST", path, body.encode('utf-8'), self.headers)
        return self.conn.getresponse()

    def get_action(self, user_id, token):

        t = int(time.time())
        sign = self.md5(self,'user_id='+user_id+'&timestamp='+str(t)+'&token='+token)
        path = "/api/health_logs/get.action?user_id="+user_id+"&timestamp="+str(t)+"&sign="+sign+"" \
               "&local_language=zh"
        self.conn.request('GET', path, '', self.headers)
        return self.conn.getresponse()

    def add_action(self, user_id, token):
        t = int(time.time())
        sign = self.md5('user_id=' + user_id + '&timestamp=' + str(t) + '&token=' + token)
        path = "/api/health_logs/day_healthlogs.action?user_id="+user_id+"&timestamp="+str(t)+"&sign="+sign
        badydata = ""
        body = json.dumps(badydata)
        self.conn.request('POST', path, body.encode('utf-8'), self.headers)
        return self.conn.getresponse()


if __name__ == '__main__':
    test = DevRequest()
    user_login = test.login('13281549858', '123456')
    user_info = json.loads(user_login.read().decode('utf-8 '))
    user_id = user_info['User']['id']
    token = user_info['User']['token']
    print(user_id, token)
    user_action = test.get_action(user_id, token)
    print(user_action.read().decode('utf-8'))
    bodydata = test.add_action(user_id, token)
    print(bodydata.read().decode('utf-8'))
