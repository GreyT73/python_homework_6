minimum = int(input("Minx = "))
maximum = int(input("Max = "))
l1 = [int(i) for i in input("Введите значения через пробел: ").split()]
for i in range(len(l1)):
    if l1[i] >= minimum and l1[i] <= maximum:
        print(i, end=' ')