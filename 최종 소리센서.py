import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
import time
import RPi.GPIO as GPIO
import threading

buzzer_pin = 18

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

stop_event = threading.Event()  # 종료 이벤트 객체 생성

# 부저 소리 생성 함수
def buzz(pitch, duration):
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)
    for _ in range(cycles):
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(delay)

def play_buzzer():
    buzz(329, 1)  # 미

def cleanup_gpio():
    GPIO.cleanup()
        
# 윈도우 생성
window = ctk.CTk()
window_width = 800
window_height = 480
window_x = 20
window_y = 5
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

url = "http://ip 주소/hosil2"

#경고 문구 나왔을때
def blink_background():
    # global blink_job  # 전역 변수로 접근

    buzz(329, 5)  # 미, 5초 동안 소리 재생

    current_color = label.cget("background")  # 현재 배경 색상 가져오기
    label.configure(background="red", fg="white")  # 배경 색상을 빨강, 글씨 색상을 흰색으로 설정

    blink_job = label.after(500, blink_background)
    
    
def left_button_click():
    # 배경 색상 변경
    label.configure(bg="blue")
    # 2초 후에 원래 메시지와 배경으로 복원
    # window.after(2000, restore_background)
    # restore_background()
    global thread
    thread.join() # 스레드 종료 대기 -> 스레드 다 처리될떄까지
    print("스레드 종료11")
    request_thread = threading.Thread(target=alert)
    request_thread.start()
    request_thread.join(0.1)
    
    thread = threading.Thread(target=response_background)
    print("스레드 종료4")
    thread.start()
    print("스레드 종료5")

def alert():
    print("스레드 종료3")
    # urlchk = "ip /hosil2chk"
    data1 = {"hosil2_alert" : 1}
    requests.post(url, data=json.dumps(data1), headers=headers)


    
def right_button_click():
    '''right_check = {
        "check2" : "hosil2_right_Button"
    }
    response = requests.post(urlchk, data=json.dumps(right_check), headers=headers)'''
    # global blink_job  # 전역 변수로 접근
    # if blink_job is not None:
    #     label.after_cancel(blink_job)  # blink_background 함수 실행을 취소
    cleanup_gpio()
    label.configure(background="white", fg="black")  # 배경 색상을 흰색, 글씨 색상을 검정색으로 설정
    print("Right button clicked")
    
    global thread
    thread.join() # 스레드 종료 대기 -> 스레드 다 처리될떄까지
    print("스레드 종료")
    print("스레드 종료2")
    # urlchk = "http://1.228.201.87:8010/hosil2chk"
    # data1 = {"check2" : "No data"}
    # requests.post(urlchk, data=json.dumps(data1), headers=headers)

    request_thread = threading.Thread(target=send_ok)
    request_thread.start()
    request_thread.join(0.1)
    print("마무리")
    
    thread = threading.Thread(target=response_background)
    print("스레드 종료4")
    thread.start()
    print("스레드 종료5")

def send_ok():
    print("스레드 종료3")
    urlchk = "http://ip주소/hosil2chk"
    data1 = {"check2" : 1}
    requests.post(urlchk, data=json.dumps(data1), headers=headers)
    

def update_time():
    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S")  # 현재 시간을 원하는 형식으로 포맷팅
    label_text.set("시간: {}\n \n \n {}호".format(
        current_time, room_number))  # 레이블 텍스트 업데이트
    window.after(1000, update_time)  # 1초마다 update_time 함수 호출

# def restore_background():
#     label.configure(bg="white")  # 배경 색상 원래대로 변경
#     update_time()  # 원래 메시지로 복원
    
    

data = {"warning_check" : " "}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

blink_job = None

# 경고 문구 나왔을 때 blink_background 함수 실행
def response_background():
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response.text)
    i_data = json.loads(response.text)
    notion = i_data["notion"]
    alert = i_data["alert"]
    if(alert == "O"):
        blink_background()
    window.after(500, response_background)
    
    
# 날씨 정보 가져오기
# weather_area = "아산시 신창면"
# weather_html = requests.get(
#     f"https://search.naver.com/search.naver?&query={weather_area}날씨")
# weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

# area_text = weather_soup.find('h2', {'class': 'title'}).text
# print(area_text)

# today_temper = weather_soup.find('div', {'class': 'temperature_text'}).text
# today_temper = today_temper[6:10]
# print(today_temper)

# today_weather = weather_soup.find(
#     'span', {'class': 'weather before_slash'}).text
# print(today_weather)

# dust_info = weather_soup.select('ul.today_chart_list>li')
# dust1_info = dust_info[0].find('span', {'class': 'txt'}).text
# dust2_info = dust_info[1].find('span', {'class': 'txt'}).text
# print("초미세먼지:" + dust2_info)

# 윈도우 크기 변경 불가능하도록 설정
window.resizable(False, False)

# 큰 레이블 생성
label_text = tk.StringVar()  # 방 호수와 시간을 업데이트할 문자열 변수 생성
label = tk.Label(window, textvariable=label_text, font=(
    "Arial", 24), borderwidth=2, relief="solid", width=50, height=6)
label.place(relx=0.5, rely=0.3, anchor="center")

left_button = ctk.CTkButton(
    window, text="민원신고", command=left_button_click, width=200, height=100)
left_button.configure(border_color="#000080",
                      fg_color="#000080", font=("Arial", 16, "bold"))
left_button.place(x=50, y=320)

right_button = ctk.CTkButton(
    window, text="경고확인", command=right_button_click, width=200, height=100)
right_button.configure(border_color="#000080",
                       fg_color="#000080", font=("Arial", 16, "bold"))
right_button.place(x=560, y=320)

# dust_label = ctk.CTkLabel(window, text="현재기온: " + today_temper + "°C  날씨: " + today_weather, fg_color="transparent",
#                           width=30, height=5, font=("Arial", 14))
# dust_label.place(x=560, y=0)

room_number = "102"

thread = threading.Thread(target=response_background)
thread.start()

# update_time()  
window.attributes('-fullscreen', True)
window.mainloop()
