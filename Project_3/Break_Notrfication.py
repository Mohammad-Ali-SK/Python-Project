from plyer import notification
import time

if __name__=="__main__":
    while True:
        notification.notify(
            title = "*** Take Rest ***",
            message = "Take a nap you are continuously doing work so nap is important..",
            app_icon = None,  # You can replace None with the path to your .ico file
            timeout = 5
        )
        time.sleep(10)