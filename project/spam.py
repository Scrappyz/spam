import webbrowser
import time
import pyautogui
import argparse

def convertFrequency(freq: str) -> int:
    t = ""
    unit = ""
    for i in range(len(freq)):
        if (not freq[i].isdigit() and freq[i] != ' ') or i == len(freq)-1:
            t = freq[:i]
            unit = freq[i:]
            break
    
    t = int(t)
    if unit.startswith("min"):
        t *= 60
    elif unit.startswith("hour"):
        t *= 60*60
    
    return t
    
def spam(url: str, message: str, frequency: int):
    webbrowser.open(url)
    time.sleep(10)
    while True:
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        time.sleep(frequency)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", nargs=1, type=str, help="the url to send the message to", dest="url")
    parser.add_argument("-m", "--message", nargs=1, type=str, help="the message to send", dest="message")
    parser.add_argument("-f", "--frequency", nargs=1, help="the delay between each message", dest="frequency")
    
    args = parser.parse_args()
    url = args.url[0]
    message = args.message[0]
    frequency = args.frequency[0]

    frequency = convertFrequency(frequency)
    print("Press Ctrl + C to end program")
    #spam(url, message, frequency)
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program Terminated")
    
