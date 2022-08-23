t = int(input())

while t != 0:
    n = int(input())
    array = list(map(int, input().split()))
    operations = 0
    index = 1
    while len(array) != 0:
        if len(array) == 1:
            del array [0]
            operations += 1
        elif array[index-1] <= array[index]:
            if index+1 != len(array):
                index += 1
            else:
                del array[0:index+1]
                operations += 1
                index = 1
        else:
            del array[0:index]
            operations += 1
            index = 1

    print(operations)

    t -= 1
