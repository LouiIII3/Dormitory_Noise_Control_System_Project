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

        
         self.place(x=0,width=400, height=400)

        btn = ttk.Button(master, text="경고주기", command=self.buttonClicked)
        btn.pack(pady=10,side="bottom")
        print("그래")
        
    def initUI(self):
        # 여기서 소켓 통신을 하는 것이다
        data = client_socket.recv(1024)
        copy='0'
        if copy == data:
            print()
        else:
            received_data = data.decode().replace("'", "")  # 따옴표 제거
            print('서버로부터 받은 메모장의 내용:', received_data)
        
        copy = received_data

        f = open('sound_average.txt', 'w')
        f.write(data.decode())
        f.close()
        
        global content
        '''file_path = '/Users/taewonyoon/Desktop/text.txt'  # 가져올 텍스트 파일의 경로를 지정합니다.
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")'''
        self.pack(padx=20, pady=20)
        # newcopy = ""
        # for i in range(len(copy)):
        #     if i != 0 and i != len(copy)-1:
        #         newcopy += copy[i]
        
            
        # content = int(newcopy)
        global firstCount
        global Room
        if firstCount == 0:
            firstCount = 1
        else:
            content = float(received_data)
            
        if content > 110:
            Room += 1
            
        if self.get_children():
            item_id = self.get_children()[0]
            new_values = ["1호실", content, Room]
            self.item(item_id, values=new_values)
        

        self.after(10, self.initUI)

    def cell_was_clicked(self, event):
        row = self.focus()
        if row:
            item = self.item(row)
            print(f"Clicked on {row} with value {item['values'][event.column]}")

    def show_custom_message(self):
        messagebox.showinfo("메시지", "버튼 클릭")
        self.on_confirmation()

    def on_confirmation(self):
        print("확인 버튼이 클릭되었습니다.")

    def buttonClicked(self):
        print("Button Clicked")
        self.show_custom_message()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("My Table Widget")

frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH, padx=100, pady=100)

tableWidget = MyTableWidget(frame, 2, 3)
tableWidget.pack(expand=True, fill=tk.BOTH)

root.mainloop()
