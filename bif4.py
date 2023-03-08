import time
import math

n = int(input())
ms = int(input())
time.sleep(ms/1000)

print("Square root of {} after {} miliseconds is {}".format(n, ms, math.sqrt(n)))