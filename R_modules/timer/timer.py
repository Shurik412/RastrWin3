import time

t = time.time()

sleep(5)

t2 = time.time()
d = t2 - t

print(time.strftime("%M [минут] %S [секунд]", time.localtime(d)))
