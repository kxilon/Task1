arr = []
n = int(input())

for i in range(n):
    arr.append(i + 1)

arr1 = []
m = int(input())
num = 0
counter = 0


while(num != 1):
    for i in range(m):

        if counter < n:
            arr1.append(arr[counter])
        else:
            counter -= n
            arr1.append(arr[counter])


        counter += 1
    counter -= 1

    if arr1[len(arr1) - 1] == 1:
        num = 1


for i in range(0, len(arr1), m):
    print(arr1[i], end='')
