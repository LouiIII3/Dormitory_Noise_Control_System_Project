import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# 날씨 정보 가져오기
weather_area = "아산시 신창면"
weather_html = requests.get(f"https://search.naver.com/search.naver?&query={weather_area}날씨")
weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

area_text = weather_soup.find('h2', {'class': 'title'}).text
print(area_text)

today_temper = weather_soup.find('div', {'class': 'temperature_text'}).text
today_temper = today_temper[6:10]
print(today_temper)

today_weather = weather_soup.find('span', {'class': 'weather before_slash'}).text
print(today_weather)

dust_info = weather_soup.select('ul.today_chart_list>li')
dust1_info = dust_info[0].find('span', {'class': 'txt'}).text
dust2_info = dust_info[1].find('span', {'class': 'txt'}).text
print("초미세먼지:" + dust2_info)


#윈도우를 생성하기
window = ctk.CTk()
window_width = 800
window_height = 480
window_x = 20
window_y = 5
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# 윈도우 크기 변경 불가능하도록 설정(고정)
window.resizable(False, False)

# 큰 레이블 생성
label_text = tk.StringVar()  # 방 호수를 업데이트할 문자열 변수 생성
label = tk.Label(window, textvariable=label_text, font=("Arial", 24), borderwidth=2, relief="solid", width=50, height=6)
label.place(relx=0.5, rely=0.3, anchor="center")

def left_button_click():
    print("Left button clicked")

def right_button_click():
    print("Right button clicked")

left_button = ctk.CTkButton(window, text="민원신고", command=left_button_click, width=200, height=100)
left_button.configure(border_color="#000080", fg_color="#000080", font=("Arial", 16, "bold"))
left_button.place(x=50, y=270)

right_button = ctk.CTkButton(window, text="경고확인", command=right_button_click, width=200, height=100)
right_button.configure(border_color="#000080", fg_color="#000080", font=("Arial", 16, "bold"))
right_button.place(x=550, y=270)

dust_label = ctk.CTkLabel(window, text="현재기온: " + today_temper + "°C  날씨: " + today_weather, fg_color="transparent",
                          width=30, height=5, font=("Arial", 14))
dust_label.place(x=520, y=0)

(호수)
room_number = "101"

time_label = tk.Label(window, text="시간: ", font=("Arial", 24))
time_label.place(x=320, rely=0.3, anchor="center")

day_label = tk.Label(window, text="요일: ", font=("Arial", 24))
day_label.place(x=640, rely=0.3, anchor="center")

def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 현재 시간을 원하는 형식으로 포맷팅
    day_of_week = datetime.now().strftime("%A")  # 현재 요일 가져오기

    label_text.set("{} 호".format(room_number))  # 호실 표시
    time_label.configure(text="시간: {}".format(current_time))  # 시간 업데이트
    day_label.configure(text="요일: {}".format(day_of_week))  # 요일 업데이트

    window.after(1000, update_time)  # 1초마다 update_time 함수 호출

update_time()
window.mainloop()
