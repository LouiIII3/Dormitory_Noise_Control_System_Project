from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt
import json
import customtkinter as ctk
import threading
import matplotlib
matplotlib.use('TkAgg')


url = "ip주소/sagam"
url2 = "ip주소/sagam_chk"

root = tk.Tk()
event_id = ""
data = {
    'warning': '',
    'room': 0
}
sure_chk = {
    "sagam_check": "something"    
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

row = 0
# content = ""
# precontent = 0
##################################################################################################################
# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')
# plt.rcParams['font.family'] = 'Malgun Gothic'


##################################################################################################################
warned = [0,0]
class MyTableWidget(ttk.Treeview):
    # 주어진 숫자들
    global numbers

    def __init__(self, master, rows, cols):
        global warned
        super().__init__(master, columns=("", "", ""), show="headings")
        self.initUI()
        self.bind('<ButtonRelease-1>', self.cell_was_clicked)
        self.heading("#1", text="호실")
        self.heading("#2", text="소리")
        self.heading("#3", text="경고")
        
        self.insert("", 0, values=["1호실", warned[0], "0"])
        self.insert("", 1, values=["2호실", warned[1], "0"])
        self.column("#1", anchor="center")
        self.column("#2", anchor="center")
        self.column("#3", anchor="center")

        # self.pack(fill=tk.BOTH, expand=True)
        self.place(relx=0.5, rely=0.5, anchor='n')

        # 열 높이 변경하기
        s = ttk.Style()
        s.theme_use('clam')
        # Add the row height
        s.configure('Treeview', rowheight=40)
        
        button_frame = tk.Frame(master)
        button_frame.pack(side=tk.BOTTOM, padx=10, pady=10)
        
        # 하단 버튼
        btn_graph = ctk.CTkButton(button_frame, text="그래프 창 열기", height=40, width=3, command=self.sendWarning)
        btn_graph.pack(side=tk.LEFT, padx=10, pady=(0, 10))

        btn_another = ctk.CTkButton(button_frame, text="경고주기 버튼", height=40, width=3, command=self.send)
        btn_another.pack(side=tk.LEFT, padx=10, pady=(0, 10))
        
        

    def initUI(self):
        self.pack(padx=0, pady=0)
        # print("testing")
        
        print("처음으로 여기서 보냈다" + data["warning"])
        self.response2 = requests.post(url2, data=json.dumps(sure_chk), headers=headers)
        self.response = requests.post(url, data=json.dumps(data), headers=headers) # data = wornning
        data["warning"] = ""
        

        self.response_data = self.response.json()
        self.response2_data = self.response2.json()
        
        self.content1 = self.response_data['sound_101']
        self.content2 = self.response_data['sound_102']
        
        print(f"response2_data: {self.response2_data['room102']}" + f"{type(self.response2_data['room102'])}")

        print(self.response.text)
        
        if self.get_children():
            item_id = self.get_children()[0]
            new_values = ["1호실", self.content1, warned[0]]
            self.item(item_id, values=new_values)
            item_id = self.get_children()[1]
            new_values = ["2호실", self.content2, warned[1]]
            self.item(item_id, values=new_values)
            # print(f"response2_data: {response2_data['room102']}")
            if self.response2_data['room101'] == 1: # 확인버튼 눌렀다
                # item_id = self.get_children()[0]
                # new_values = ["1호실", content1, 0, ""]
                # self.item(item_id, values=new_values)
                messagebox.showinfo("101호","확인하였습니다")
                
                
            if self.response2_data['room102'] == 1:
                # item_id = self.get_children()[1]
                # new_values = ["2호실", content2, 0, ""]
                # self.item(item_id, values=new_values)
                messagebox.showinfo("102호","확인하였습니다")
                
                
        
        # # print("alert:", response2_data['alert102'])
        
            # if response2_data['alert101'] == 1:    
            #     message=tk.Message(root, text='101호실에서 경고메시지가 왔다', width=100, relief="solid")
            #     message.pack()
            # if response2_data['alert102'] == c1:
            #     print("실행되얻")
            #     message=tk.Message(root, text='102호실에서 경고메시지가 왔다', width=100, relief="solid")
            #     message.pack()
            if self.response2_data['alert101'] == 1:    
                # message = messagebox(root, text='101호실에서 경고메시지가 왔다', width=100, relief="solid")
                # messagebox.showinfo("경고", "민원이 들어왔습니다")
                messagebox.showwarning("101호실", "신고가 들어왔습니다")
                # messagebox.place(relx=0.5, rely=0.5, anchor="center")  # 중앙에 배치
            if self.response2_data['alert102'] == 1:
                print("실행되얻")
                # message = messagebox(root, text='102호실에서 경고메시지가 왔다', width=100, relief="solid")
                # messagebox.showinfo("경고", "민원이 들어왔습니다")
                messagebox.showwarning("102호실", "신고가 들어왔습니다")
                
        #         # messagebox.place(relx=0.5, rely=0.3,anchor="center")  # 중앙에 배치
                
        # print(f"response value: {response2_data['alert102']} + {type(response2_data['alert102'])}")
        ###################################################################################################
        # thread = threading.Thread(target=self.updateValue)
        # thread.start()
        # thread.join(1)
        self.after(1000, self.get_children)
        global event_id
        event_id = self.after(1000, self.initUI)  # 1000ms마다 업데이트한다
    
    def live_plotter(self,x_vec, y1_data, line1, identifier='', pause_time=0.5):
        if line1 == []:
            # this is the call to matplotlib that allows dynamic plotting
            plt.ion()
            fig = plt.figure(figsize=(3,1))
            ax = fig.add_subplot(111)#,projection='3d')
            # create a variable for the line so we can later update it
            line1, = ax.plot(x_vec, y1_data, '-o', alpha=0.5, animated=True)
            # update plot label/title
            plt.ylabel('소음')
            plt.title('Title: {}'.format(identifier))
            # plt.show()
            plt.pause(0.5)

        # after the figure, axis, and line are created, we only need to update the y-data
        line1.set_ydata(y1_data)
        # adjust limits if new data goes beyond bounds
        if np.min(y1_data) <= line1.axes.get_ylim()[0] or np.max(y1_data) >= line1.axes.get_ylim()[1]:
            plt.ylim([np.min(y1_data) - np.std(y1_data), np.max(y1_data) + np.std(y1_data)])
        # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
        plt.pause(pause_time)

        # return line so we can update it again in the next iteration
        return line1


    def updateValue(self):
        
        if self.get_children():
            item_id = self.get_children()[0]
            new_values = ["1호실", self.content1, warned[0]]
            self.item(item_id, values=new_values)
            item_id = self.get_children()[1]
            new_values = ["2호실", self.content2, warned[1]]
            self.item(item_id, values=new_values)
            # print(f"response2_data: {response2_data['room102']}")
            if self.response2_data['room101'] == 1: # 확인버튼 눌렀다
                # item_id = self.get_children()[0]
                # new_values = ["1호실", content1, 0, ""]
                # self.item(item_id, values=new_values)
                messagebox.showinfo("101호      ","  확인하였습니다       ")
            if self.response2_data['room102'] == 1:
                # item_id = self.get_children()[1]
                # new_values = ["2호실", content2, 0, ""]
                # self.item(item_id, values=new_values)
                messagebox.showinfo("102호      ","  확인하였습니다       ")
        

            if self.response2_data['alert101'] == 1:    
                # message = messagebox(root, text='101호실에서 경고메시지가 왔다', width=100, relief="solid")
                # messagebox.showinfo("경고", "민원이 들어왔습니다")
                messagebox.showwarning("101호실", "신고")
                # messagebox.place(relx=0.5, rely=0.5, anchor="center")  # 중앙에 배치
            if self.response2_data['alert102'] == 1:
                print("실행되얻")
                # message = messagebox(root, text='102호실에서 경고메시지가 왔다', width=100, relief="solid")
                # messagebox.showinfo("경고", "민원이 들어왔습니다")
                messagebox.showwarning("102호실", "신고가 들어왔습니다")
                
                # messagebox.place(relx=0.5, rely=0.3,anchor="center")  # 중앙에 배치
                
        print(f"response value: {self.response2_data['alert102']} + {type(self.response2_data['alert102'])}")
        
    def cell_was_clicked(self, event):  # 셀이 클릭됐을때
        global row
        row = self.focus()
        row = row[len(row) - 1]
        print(f"row의 값:{row}")

    def show_custom_message(self):
        messagebox.showinfo("메시지", "버튼 클릭")
        self.on_confirmation()

    def on_confirmation(self):
        print("확인 버튼이 클릭되었습니다.")


    def send(self):  # 호실의 값을 서버에 보낸다
        # send 함수의 로직을 여기에 추가
        # POST 요청을 보낼 데이터
        # response = requests.post(url, data=json.dumps(data), headers=headers)
        global row
        data["warning"] = ""
        data["warning"] = row
        self.response = requests.post(url, data=json.dumps(data), headers=headers)
        warned[int(row)-1] = warned[int(row)-1] + 1
        print("보냈다" + " " + row)
        data["warning"] = ""


    def sendWarning(self):

        # self.send(row)
        print("눌렀자나")
        ################################################################################################################################################
        # 그래프 값을 갱신할 때 사용할 numbers 리스트 초기화
        # global numbers
        
        # 그래프 만들기
        # create_graph_window()
        # use ggplot style for more sophisticated visuals

        # create initial data
        size = 100
        x_vec = np.linspace(0, 1, size + 1)[0:-1]
        y_vec = [i*0 for i in range(len(x_vec))]#np.random.randn(len(x_vec)) 
        # print(len(x_vec)+"fjkashdkfjashfkjasdhf")
        line1 = []

        # create plot and update in a loop
        plt.ion()  # enable interactive mode
        fig, ax = plt.subplots(figsize=(5, 3))
        line1, = ax.plot(x_vec, y_vec, '-o', alpha=0.8)
        plt.ylabel('db')
        plt.title('sound')
        
        # content = self.response_data['sound_101']
        # content = self.response_data['sound_102']
        
        
        # self.content1 = self.response_data['sound_101']
        # self.content2 = self.response_data['sound_102']
        # print(f"self.content1의 값은: {self.content1}")
        # print(f"self.content2의 값은: {self.content2}")
        while True:
            # self.response = requests.post(url, data=json.dumps(data), headers=headers) # data = wornning
            # self.response_data = self.response.json()
            temp = 0
            print(f"row의 값:{row} : {type(row)}")
            if int(row)==1:
                temp = int(self.content1)
            elif int(row)==2:
                temp = int(self.content2)

            
            # content = int(content)
            print(f"실행은 됐는데 이상한 경우{temp} : {type(temp)}")
            
            # if content == 0:
            #     rand_val = precontent
            #     precontent = content
            # else:
            
            rand_val = temp #np.random.randn(1) # 값을 추가하는 곳
            y_vec[-1] = rand_val
            line1 = self.live_plotter(x_vec, y_vec, line1)
            y_vec = np.append(y_vec[1:], 0.0)
    
    ################################################################################################################################################


# root.attributes('-fullscreen', False)
root.attributes('-fullscreen', True)
root.title("My Table Widget")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tableWidget = MyTableWidget(frame, 2, 3)
tableWidget.pack(fill=tk.BOTH, expand=True)
# tableWidget.place()


    
root.mainloop()
