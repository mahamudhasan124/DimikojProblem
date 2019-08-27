import math
test = int(input())

for t in range(test):
    num = int(input())
    res = int(math.sqrt(num))
    
    if(res*res == num):
        print("YES")
    else:
        print("NO")
