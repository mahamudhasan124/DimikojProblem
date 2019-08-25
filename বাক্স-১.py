test = int(input())

for x in range(test):
    star = int(input())

    for i in range(star):
        for j in range(star):
            print("*",end="")
        print("")
    if(x<test-1):
        print("")
