import psutil
import requests
import time

# Порог потребления памяти, при котором генерируется alarm (в мегабайтах)
memory_threshold = 100

# URL для отправки HTTP-запроса в случае alarm
api_url = ""

while True:
    memory_usage = psutil.virtual_memory().used / (1024 * 1024)

    if memory_usage > memory_threshold:
        response = requests.post(api_url, data={"message": "Memory usage exceeded the threshold"})
        
        if response.status_code == 200:
            print("Alarm sent successfully")
        else:
            print("Failed to send alarm")

    time.sleep(60) 