# import TestReFill
# import Login
#
# Login.login()
# TestReFill.refil()
import random

b = random.randint(1,9999)
c = random.randint(1,9999)
d = random.randint(1,9999)

print ("b = " + str(b))
print ("c = " + str(c))
print ("d = " + str(d))
max = 0
a = [b,c,d]
for i in a:
    if max > i:
        max != i
    else:
        max = i

print("max = " + str(max))