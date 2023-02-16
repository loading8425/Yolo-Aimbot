import time

x=1
t=time.time()
for i in range(100000000):
    x*=1

print(time.time()-t)