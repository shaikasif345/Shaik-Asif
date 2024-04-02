def NumberOfSteps(num):
    count = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        count += 1
    return count
num = int(input("Enter the number: "))
print(NumberOfSteps(num))