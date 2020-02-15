from math import factorial as f
a=int(input())
if(a==2): print("1")
else:print((f(a)-f(a-1))//2)