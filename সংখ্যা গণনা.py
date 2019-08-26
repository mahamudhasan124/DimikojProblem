test = int(input())

for t in range(test):
    number = input()
    l = len(number)
    start = 0
    count = 1
    for i in range(l):
        if(number[i] != " "):
            start = 1
        elif(number[i] == " "):
            if(start == 1):
                count+=1
                start = 0

    print(count)


