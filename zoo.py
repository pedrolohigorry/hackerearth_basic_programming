'''
############  Exercise taken from Hackerearth, Codemonk.
############  Solved using Python 3.9.5

Problem: Zoos

You are required to enter a word that consists of x and y that denote the
number of Zs and Os respectively. The input word is considered similar to word
zoo if 2 * x = y.

Determine if the entered word is similar to word 'zoo'.

For example, words such as 'zzoooo' and 'zzzoooooo' are similar to word 'zoo'
but not the words such as 'zzooo' and 'zzzooooo'.

Input format
First line: A word that starts with several Zs and continues by several Os.
Note: The maximum length of this word must be 20.

Output format
Print 'Yes' if the input word can be considered as the string 'zoo'.
Otherwise, print 'No'.

Sample Input
zzzoooooo

Sample Output
Yes

##############
'''

word = input()

## z and o will count the amount of z's and o's
z = 0
o = 0

## Iterate through each letter. If it's 'z', then add 1 to z count.
## If it's not a 'z', then it must be and 'o' and add 1 to o count.
for letter in word:
    if letter == 'z':
        z += 1
    else:
        o += 1

## Check for the condition 2 * x = y
if 2 * z == o :
    print('Yes')
else:
    print('No')
