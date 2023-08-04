import spidev
import time
import requests
import json
import time

# 데이터를 전송할 URL
url = "ip주소/hosil"
i = 0

# MCP3008 SPI 채널 및 핀 번호
SPI_CHANNEL = 0
SPI_CE0_PIN = 8

data = {'h_sound2': "초기값",
        'h_alert2': '0',
        'h_room2': '102'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


# SPI 인터페이스 초기화(아날로그로 변환하기 위해 사용)
spi = spidev.SpiDev()
spi.open(0, SPI_CHANNEL)
spi.max_speed_hz = 1000000


def read_adc(channel):
    # MCP3008에서 아날로그 값을 읽어오기
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data


try:
    while True:
        # 사운드 센서 1을 연결한 MCP3008의 채널 번호
        sound_channel_1 = 0
        sound_value_1 = read_adc(sound_channel_1)

        # 사운드 센서 2를 연결한 MCP3008의 채널 번호
        sound_channel_2 = 1
        sound_value_2 = read_adc(sound_channel_2)

        # 두 사운드 센서 값의 평균 계산
        # 센서1의 민감도가 안좋아 정확한 value값만 사용
        
        if (sound_value_1 > 600):
            sound_value_1 = sound_value_2
            data["h_sound2"] = sound_value_2
        
        else:
            data["h_sound2"] = sound_value_2
            
            
        response = requests.post(url, data=json.dumps(data), headers=headers)
            # response = requests.post(url, json=data)

            # 응답 출력
        print(response.text)

        # 응답 확인
        try:
            # 응답 데이터를 딕셔너리로 변환
            response_data = response.json()

            # 딕셔너리 형태로 출력
            print(response_data)
        except (json.JSONDecodeError, ValueError):
            print("Error: Failed to decode response data as JSON")

        time.sleep(1)

except KeyboardInterrupt:
    spi.close()
