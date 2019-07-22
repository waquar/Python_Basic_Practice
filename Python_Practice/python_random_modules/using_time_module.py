import time

initialTimeWhile  =time.time()
k = 0

while (k < 5):
    print("Running for Waquar")
    time.sleep(1)
    k+= 1

print(time.time()- initialTimeWhile)

initialTimefor = time.time()
for item in range(5):
    print("Running for Alam")

print(time.time() - initialTimefor)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)


#(time.time() returns ticks)
#(time.localtime()) returns time is tuple
#time.asctime() converts that tuple in variable asiigened