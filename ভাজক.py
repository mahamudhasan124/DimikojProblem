test = int(input())

for i in range(test):
    number = int(input())
    print("Case",i+1,end=": ")
    for x in range(1,number):

        if((number % x) == 0):
            print(x,end=" ")
    print(number)
