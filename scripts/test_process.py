import random
import time
total_len = 1000000
a = []
print("Running")

for i in range(total_len):
    a.append(random.randint(-1000,1000))

while(True):
    # time.sleep(0.001)
    # if(random.random()>0.9):
    a[random.randint(0,total_len-1)] = a[random.randint(0,total_len-1)]
