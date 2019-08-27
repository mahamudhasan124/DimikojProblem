test = int(input())

for t in range(test):
    arr = list(map(int,input().split()))
    arr.sort()
    arr = ' '.join(str(m) for m in arr)
    print("Case {}: {}".format(t+1,arr))
