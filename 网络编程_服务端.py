import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 获取本地主机名
host = socket.gethostname()
port = 9999
# 绑定端口号
s.bind((host, port))

# 设置最大连接数，超过后排队
s.listen(5)
print(host)
while True:
    # 建立客户端连接
    clientsocket,addr = s.accept()
    print("连接地址：%s" % str(addr))
    msg = "欢迎访问菜鸟教程！"+"\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()

