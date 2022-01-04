from win10toast import ToastNotifier
toaster=ToastNotifier()
toaster.show_toast("Notification","Alert! Yes",threaded=True,icon_path=None,duration=3)
import time

while toaster.notification_active():
    time.sleep(0.1)