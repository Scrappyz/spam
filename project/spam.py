import webbrowser
import time
import pyautogui
import argparse

def convertInterval(freq: str) -> float:
    t = ""
    unit = ""
    for i in range(len(freq)):
        if not freq[i].isdigit() and freq[i] != ' ':
            t = freq[:i]
            unit = freq[i:]
            break
        if i == len(freq)-1:
            i += 1
            t = freq[:i]
            unit = freq[i:]
            break
    
    t = float(t)
    if unit.startswith("ms"):
        t /= 1000
    elif unit.startswith("m"):
        t *= 60
    elif unit.startswith("h"):
        t *= 60*60
    
    return t
    
def spam(url: str, message: str, frequency: float, delay: float):
    if url:
        webbrowser.open(url)
    time.sleep(delay)
    while True:
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        time.sleep(frequency)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", nargs="?", type=str, default="", help="the url to send the message to", dest="url")
    parser.add_argument("-m", "--message", nargs=1, type=str, help="the message to send", dest="message")
    parser.add_argument("-f", "--frequency", nargs="?", type=str, default="5", help="the delay between each message", dest="frequency")
    parser.add_argument("-d", "--delay", nargs="?", type=str, default="5", help="the delay before spamming", dest="delay")
    
    args = parser.parse_args()
    print(args)
    url = args.url
    message = args.message[0]
    frequency = convertInterval(args.frequency)
    delay = convertInterval(args.delay)

    print("Press Ctrl + C to end program")
    spam(url, message, frequency, delay)
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program Terminated")
    
