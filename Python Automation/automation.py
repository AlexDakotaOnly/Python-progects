import schedule
import time
from credentials import mobile_number
import requests
def send_message():
    resp = requests.post('https://textbelt.com/text', {
      'phone': mobile_number,
      'message': 'Not good',
      'key': 'textbelt',
    })
    print(resp.json())


# schedule.every().day.at("6:30").do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)