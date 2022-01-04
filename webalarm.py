import time
import webbrowser
from playsound import playsound
set_alarm=input("Set the website alarm as H:M:S(all in two digits): ")
url=list()
n=input("Enter the no's URL: ")
for i in range(n):
    url[i] = input("Enter the website's URL: ")
actual_time=time.strftime("%I:%M:%S")
while(actual_time!=set_alarm):
    print("Time is: ",actual_time)
    actual_time = time.strftime("%I:%M:%S")
    time.sleep(600)
if actual_time==set_alarm:
    playsound('audio.mp3')
    print("You should see your webpage now :)")
    for i in range(n):
        webbrowser.open(url[i])