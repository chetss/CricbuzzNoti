from mycricbuzz import get_cric_data
import time
from win10toast import ToastNotifier

toaster = ToastNotifier()
#  toaster.show_toast("Hello World!!!",
#                    "Python is 10 seconds awsm!",
#                    duration=10)


def show_notifications():

    cric_dict = get_cric_data()
    
    batting_team = cric_dict.get('batting_team')
    bowling_team = cric_dict.get('bowling_team')
    title = cric_dict.get('title')
    score = cric_dict.get('score')
    info = cric_dict.get('info')
    
    toaster.show_toast(title,
                    batting_team +" VS "+ bowling_team + "\n" 
                        "Score :: "+score + "\n"+ info,
                    #    icon_path='./cricket.ico',
                    duration=8,
                    threaded=True)    

def call_get_cric():
    import time
    starttime=time.time()
    while True:
        show_notifications()        
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))

call_get_cric()               

# Wait for threaded notification to finish
while toaster.notification_active(): time.sleep(0.1)