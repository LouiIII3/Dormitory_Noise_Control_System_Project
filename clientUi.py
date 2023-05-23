import tkinter as tk
from tkinter import ttk
form tkinter import messagebox
import time
import socket

# 서버의 주소입니다. hostname 또는 ip address를 사용할 수 있습니다.
HOST = '192.168.0.*'  
# 서버에서 지정해 놓은 포트 번호입니다. 
PORT = 9999       

# 소켓 객체를 생성합니다. 
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.  
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 지정한 HOST와 PORT를 사용하여 서버에 접속합니다. 
client_socket.connect((HOST, PORT))

# 메시지를 전송합니다. 


# 메시지를 수신합니다.
copy ='0'


content = 0
firstCount = 0
Room = 0
class MyTableWidget(ttk.Treeview):
    def __init__(self, master, rows, cols):
        global content
        super().__init__(master, columns=("", "", ""), show="headings")
        self.initUI()
        self.bind('<ButtonRelease-1>', self.cell_was_clicked)
        self.heading("#1", text="호실")
        self.heading("#2", text="소리")
        self.heading("#3", text="경고")
        self.insert("", 0, values=["1호실", "0", "0"])
        self.insert("", 1, values=["2호실", "0", "0"])
        self.column("#1", anchor="center")
        self.column("#2", anchor="center")
        self.column("#3", anchor="center")
