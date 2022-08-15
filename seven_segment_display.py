'''
############  Exercise taken from Hackerearth, Codemonk.
############  Solved using Python 3.9.5

Problem: Seven-Segment Display

Check out the problem here: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seven-segment-display-nov-easy-e7f87ce0/

##############
'''

## Get the number of testcases and loop through them with a while loop
t = int(input())

while t != 0:

    number = input()

    ## Create this dictionary that has the amount of matchsticks used in the
    ## display to create each number
    dictionary = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}

    ## Next count the amount of total matchsticks that can be used to form
    ## a number
    matchsticks = 0
    for letter in number:
        matchsticks += dictionary[letter]

    ## There are two possibilities:
    ## 1) If the amount of matchsticks is even, then the biggest number is
    ## just a lot of '1'.
    ## Example: '88' is formed with 7 + 7 matchsticks, a total of 14. So, we can
    ## make 7 times the number '1'. The biggest number is '1111111'.

    ## 2) If the amount of matchsticks is odd, then the biggest that we can form
    ## with 3 matchsticks is a '7' (check out the dictionary above).
    ## So, in this case the number starts with '7' and then all the '1' that we
    ## can form with the available matchsticks.
    ## Example: '34' is formed by 5 + 4 matchsticks, a total of 9. So we can
    ## form one '7' and three '1'. The biggest number is '7111'.
    max_number = ''
    ones = matchsticks // 2

    ## Check if the total amount of matchsticks is even and form the biggest
    ## number using possibility 1).
    if matchsticks % 2 == 0:
        for num in range(ones):
            max_number += '1'
        print(int(max_number))
    ## Else, if not even, then the number is odd. And form the number using
    ## possiblity 2).
    else:
        max_number = '7'
        for num in range(ones-1):
            max_number += '1'
        print(int(max_number))

    t -= 1
