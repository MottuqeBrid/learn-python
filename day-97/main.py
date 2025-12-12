# Multitherading in python
import threading
import time


def func(sec):
    print(f"Function {sec} started")
    time.sleep(sec)
    print(f"Function {sec} ended")


# func(2)
t1 = threading.Thread(target=func, args=[2])
t2 = threading.Thread(target=func, args=[4])
t3 = threading.Thread(target=func, args=[6])

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
