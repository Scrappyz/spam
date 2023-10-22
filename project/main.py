import webbrowser
import time
import pyautogui
import datetime

url = 'https://www.facebook.com/messages/t/100005623201342'

# initialize flag to indicate no message sent yet this hour
message_sent_this_hour = False

while True:
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    if current_time in ('12:00 AM', '01:00 AM', '02:00 AM', '03:00 AM', '04:00 AM', '05:00 AM', '06:00 AM','07:00 AM', '08:00 AM', '09:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '01:00 PM','02:00 PM', '03:00 PM', '04:00 PM', '05:00 PM', '06:00 PM', '07:00 PM', '08:00 PM','09:00 PM', '10:00 PM', '11:00 PM'):
    
        # check if message has already been sent this hour
        if not message_sent_this_hour:
            # Open the Messenger URL, wait for it to load, type the message, and send it
            webbrowser.open(url)
            
            time.sleep(10)
            pyautogui.typewrite('magaral ka na ng law')
            pyautogui.press('enter')
            # set flag to indicate message has been sent this hour
            message_sent_this_hour = True
    else:
        # reset flag at the start of a new hour
        message_sent_this_hour = False
    # wait for one minute before checking the time again
    time.sleep(50)