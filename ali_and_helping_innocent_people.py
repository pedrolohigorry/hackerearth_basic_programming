'''
############  Exercise taken from Hackerearth, Codemonk.
############  Solved using Python 3.9.5

Problem: Ali and Helping innocent people

Check out the problem here: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cartag-948c2b02/

##############
'''
string = input()

## Create a tuple of 'vowels'
vowels = ('A', 'E', 'I', 'O', 'U', 'Y')

## Check if the letter is a 'vowel'. If not, then store the value as 1.
if string[2] not in vowels:
    vowel = 1
else:
    vowel = 0

## For each consecutive digits, check if the sum is even. If yes, store the
## value as 1.
if (int(string[0]) + int(string[1])) % 2 == 0:
    pair1 = 1
else:
    pair1 = 0

if (int(string[3]) + int(string[4]) ) % 2 == 0:
    pair2 = 1
else:
    pair2 = 0

if (int(string[4]) + int(string[5])) % 2 == 0:
    pair3 = 1
else:
    pair3 = 0

if (int(string[-2]) + int(string[-1]) ) % 2 == 0:
    pair4 = 1
else:
    pair4 = 0

## Only if all the previous checks are true, then the tag is valid. So, the sum
## must be equal to 5. Else, the tag is invalid. 

if (vowel + pair1 + pair2 + pair3 + pair4) == 5:
    print('valid')
else:
    print('invalid')
