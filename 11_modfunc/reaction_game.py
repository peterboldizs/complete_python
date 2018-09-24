import time
from time import time as my_timer
from time import perf_counter
from time import monotonic

import random

input("press enter to start")
wait_time = random.randint(1, 5)
time.sleep(wait_time)

start_time = perf_counter()
input("press enter to stop")
end_time = perf_counter()

print("started at " + time.strftime("%X", time.localtime(start_time)))
print("ended at " + time.strftime("%X", time.localtime(end_time)))
print("first reaction time: {} seconds".format(end_time - start_time))

print("once again using monotonic")
input("press enter to start")
wait_time = random.randint(1, 5)
time.sleep(wait_time)

start_time = monotonic()
input("press enter to stop")
end_time = monotonic()

print("started at " + time.strftime("%X", time.localtime(start_time)))
print("ended at " + time.strftime("%X", time.localtime(end_time)))
print("second reaction time: {} seconds".format(end_time - start_time))

