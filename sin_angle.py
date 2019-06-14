#set 5 player 6
import math

a=int(input())

a=math.radians(a)
a=math.sin(a)

if 0<a<1:
	print(round(a,2))
else:
	print(round(a))
