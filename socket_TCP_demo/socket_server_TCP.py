import socket

#服务器
def send_file2_client(new_client_socket,client_addr):
    # 接收客户端发过来的请求
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端（%s）需要下载的文件是：%s" % (str(client_addr), file_name))
    #打开这个文件，读取数据
    file_content =None
    try:
        f =open(file_name,"rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件！")
    #3.发送文件的数据的客户端
    if file_content:

    # 发送数据
        new_client_socket.send(str(file_name).encode("utf-8"))



def main():
    # 1.买个手机（创建套接字 socket）
    # 这个套接字用来初始化响应，最终需要最后新定义的套接字进行真正的实现通信
    tcp_server_scoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.插入手机卡（绑定本地信息 bind）
    tcp_server_scoket.bind(("", 7890))
    # 3.将手机设为正常的响铃模式（让默认的套接字有主动变为被动 listen）
    tcp_server_scoket.listen(128)
    while True:
        # 4.等待别人电话到来（等待客户端的链接 accpet）
        new_client_socket, client_addr = tcp_server_scoket.accept()
        #调用发送文件函数，完成为客户段服务
        send_file2_client(new_client_socket,client_addr)
        #关闭套接字
        new_client_socket.close()
    tcp_server_scoket.close()

if __name__ == '__main__':
    main()