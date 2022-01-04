from datetime import datetime
from playsound import playsound
alarmtime=input("Enter the time of alarm in HH:MM:SS\n")
alarmhour=alarmtime[0:2]
alarmmin=alarmtime[3:5]
alarmsec=alarmtime[6:8]
alarmperiod=alarmtime[9:11].upper()
print("Setting the alarm")
while True:
    now=datetime.now()
    nowhour=now.strftime("%I")
    nowmin = now.strftime("%M")
    nowsec = now.strftime("%S")
    nowperiod = now.strftime("%p")
    if(alarmperiod==nowperiod):
        if(alarmhour==nowhour):
            if(alarmmin==nowmin):
                if(alarmsec==nowsec):
                    print("WAKE UP!")
                    playsound('audio.mp3')
                    break

