############  Exercise taken from Hackerearth.
############  Solved using Python 3.9.5

### https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/

l = int(input())
n = int(input())

while n != 0:
    w,h = map(int, input().split())
    if w < l:
        print("UPLOAD ANOTHER")
    elif h < l:
        print("UPLOAD ANOTHER")
    if (w >= l and h >= l):
        if w == h:
            print("ACCEPTED")
        else:
            print("CROP IT")
    n -= 1
