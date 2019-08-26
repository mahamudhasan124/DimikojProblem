test = int(input())

for t in range(test):
    number = int(input())

    sum = 0

    sum = sum + (number%10)
    sum = sum + int(number/10000)
    print("Sum =",sum)