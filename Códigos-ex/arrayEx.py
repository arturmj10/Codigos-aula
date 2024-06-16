array = []

for i in range(0, 10):
    num = int(input())
    if num <= 0:
        array.append(1)
    else:
        array.append(num)

for i in range(0, len(array)):
    print(f'X[{i}]= {array[i]}')

#---------------------------------------------

array = []

for i in range(0, 10):
    num = int(input())
    if num <= 0:
        array.append(1)
    else:
        array.append(num)

for i in range(0, len(array)):
    if array[i] <= 10:
        print(f'X[{i}]= {array[i]}')