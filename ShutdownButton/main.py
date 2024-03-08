import os
import time


def shutdown():
    os.system("shutdown /s /t 0")


while True:
    time.sleep(0)
    shutdown()
