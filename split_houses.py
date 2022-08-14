'''
############  Exercise taken from Hackerearth, Codemonk.
############  Solved using Python 3.9.5

Problem: Split Houses

You live in a village. The village can be represented as a line that contains n
grids. Each grid can be denoted as a house that is marked as 'H' or a blank
space that is marked as '.' (a dot).

A person lives in each house. A person can move to a grid if it is adjacent to
that person. Therefore, the grid must be present on the left and right side of
that person.

Now, you are required to put some fences that can be marked as 'B' on some
blank spaces so that the village can be divided into several pieces. A person
cannot walk past a fence but can walk through a house.

You are required to divide the house based on the following rules:

-  A person cannot reach a house that does not belong to that specific person.
-  The number of grids each person can reach is the same and it includes the
grid in which the house is situated.
-  In order to show that you are enthusiastic and if there are many answers,
then you are required to print the one where most fences are placed.

Your task is to decide whether there is a possible solution. Print the possible solution.

Input format
First line: An integer n that represents the number of grids (1 <= n <= 20)
Second line: n characters that indicate the villages that are represented
as 'H' or '.' .

Output format
The output must be printed in the following format:
- First line: If possible, then print 'YES'. Otherwise, print 'NO'.
- Second line: If the answer is 'YES', then print the way to do so.

Sample Input
5
H...H

Sample Output
YES
HBBBH

Explanation
-  Each person can reach 1 grid. Each person can reach his own houses only.
-  Note that HB.BH also works. Each person can reach only 1 grid.
-  But H..BH does not work. Because the first person can reach 3 grids but the
second one can only reach 1.
-  H...H does not work either. The first person can reach the second person's .
house which is bad.
-  So you need to print HBBBH because it has the most fences.

##############
'''

## Get the input
n = int(input())
village = input()

## new_village is the new village with the fences
new_village = ''
old_letter = ''

for letter in village:
    ## Checking if there are 2 'H' next to each other. If yes, then there's
    ## no solution. So, print 'NO' and stop script
    if letter == old_letter and letter == 'H':
        print('NO')
        raise SystemExit(0)

    ## Check if it's letter is 'H' or '.' . So, add to new_village or change it
    ## to 'B'
    if letter == 'H':
        old_letter = 'H'
        new_village += 'H'
    if letter == '.':
        old_letter = '.'
        new_village += 'B'

## If we are out of the loop, then the solution is possible. So, we print 'YES'
## and then the solution
print('YES')
print(new_village)
