test = int(input())

for t in range(test):
    number = input()
    l = len(number) #String input
    if(int(number[l-1]) % 2 == 0):
        print("even")
    else:
        print("odd")
