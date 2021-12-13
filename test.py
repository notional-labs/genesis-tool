d = {1:2,2:4}
b = d
b[2] = 8
print(b,d)

l = []
l.append(b)
b[2] = 3
print(l,b)

import datetime
import time

print(time.time())


print(31556926 * 2 + 1639201850 + 86400)

print(1639201850 + 86400)




t = [9, "dsaff", {1:2}]

l = {1: {1: 2}, 2 : t}


t = [x for x in t if x != 9]

print(t)

def add1tol(l):
    d = l[2]
    add2tol(d) 

for i in t:
    i = 0

print(t)

def add2tol(d):
    d.append(6)

add1tol(l)
print(l)

