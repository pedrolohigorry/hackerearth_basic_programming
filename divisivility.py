'''
############  Exercise taken from Hackerearth, Codemonk.
############  Solved using Python 3.9.5

Problem: Divisivility

You are provided an array A of size N that contains non-negative integers.
Your task is to determine whether the number that is formed by selecting the
last digit of all the N numbers is divisible by 10.

Note: View the sample explanation section for more clarification.

Input format
First line: A single integer N denoting the size of array
Second line: N space-separated integers.

Output format
If the number is divisible by 10, then print 'Yes'. Otherwise, print 'No'.

Sample Input
5
85 25 65 21 84

Sample Output
No

Explanation
Last digit of 85 is 5.
Last digit of 25 is 5.
Last digit of 65 is 5.
Last digit of 21 is 1.
Last digit of 84 is 4.
Therefore the number formed is 55514 which is not divisible by 10.

##############
'''

## Save the data in variables. The numbers are saved as strings
N = int(input())
data = [x for x in input().split()]
number = ''

## Loop through the array and add the last digit in the 'number variable'
for item in data:
    last_digit = item[-1]
    number += last_digit

## Turn the number variable into a number type and check if it's divisible by 10
number = int(number)

if number % 10 == 0:
    print('Yes')
else: 
    print('No')
