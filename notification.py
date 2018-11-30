# import notify2

# notify2.Notification('test',message='tset').show()

import time
from mycricbuzz import get_cric_data
from win10toast import ToastNotifier
toaster = ToastNotifier()

# toaster.show_toast("Hello World!!!",
#                    "Python is 10 seconds awsm!",
#                    duration=10)


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
                   duration=5,
                   threaded=True)                   

# Wait for threaded notification to finish
while toaster.notification_active(): time.sleep(0.1)