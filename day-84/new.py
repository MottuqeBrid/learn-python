# python time module
import time

# print("Current time in seconds since epoch:", time.time())
# time.sleep(2)
# print("After sleeping for 2 seconds:", time.time())
# print("Current local time:", time.asctime())

t = time.localtime()
formatted_time = time.strftime("%y-%m-%d %H:%M:%S", t)
print("Formatted local time:", formatted_time)
