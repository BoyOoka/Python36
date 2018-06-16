from request import*

r = DevRequest
user_info = json.loads(r.login(r, '13100000001','123456').read().decode('utf-8'))
#print(user_info)
user_id = user_info['User']['id']
token = user_info['User']['token']
user_action = json.loads(r.get_action(r, user_id, token).read().decode('utf-8'))
age = user_action['HealthData']['age']
print(user_id,age)
