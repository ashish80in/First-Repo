# import datetime
# now=datetime.datetime .now()

# # current_time = now.time()
# # print(now)
# current_date=now .date()
# print(current_date)
import datetime
import time
while True:
    now=datetime.datetime.now()
    print("Current Date:", "Current Time:", now.strftime("%H:%M:%S"))
    time.sleep(1)

    break




