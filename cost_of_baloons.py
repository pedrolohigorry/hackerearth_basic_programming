'''
############  Exercise taken from Hackerearth, Codemonk.
############  Solved using Python 3.9.5

Problem: Cost of baloons

You are conducting a contest at your college. This contest consists of two
problems and n participants. You know the problem that a candidate will solve
during the contest.

You provide a balloon to a participant after he or she solves a problem. There
are only green and purple-colored balloons available in a market. Each problem
must have a balloon associated with it as a prize for solving that specific
problem. You can distribute balloons to each participant by performing the
following operation:

1)  Use green-colored balloons for the first problem and purple-colored
balloons for the second problem
    OR
2)  Use purple-colored balloons for the first problem and green-colored
balloons for the second problem

You are given the cost of each balloon and problems that each participant solve.
Your task is to print the minimum price that you have to pay while purchasing
balloons.

Input format

First line: t that denotes the number of test cases (1 <= t <= 10)
For each test case:
-  First line: Cost of green and purple-colored balloons
-  Second line:  that denotes the number of participants (1 <= n <= 10)
Next n lines: Contain the status of users. A value of '1' means that the
participant solved the problem. A value of '0' means that the participant didn't
solved the problem.

Output format
For each test case, print the minimum cost that you have to pay to purchase
balloons.

Sample Input
2           ## number of testcases
9 6         ## cost of green and purple ballons for testcase 1
10          ## total number of participants for testcase 1
1 1         ## problems solved by each participant
1 1
0 1
0 0
0 1
0 0
0 1
0 1
1 1
0 0
1 9         ## cost of green and purple ballons for testcase 2
10          ## total number of participants for testcase 2
0 1
0 0
0 0
0 1
1 0
0 1
0 1
0 0
0 1
0 0

Sample Output
69
14

##############
'''

## Get the number of testcases and loop through them with a while loop
t = int(input())

while t != 0:
    ## Get the cost of greens and purple balloons and the amount of participants
    gp = list(map(int, input().split()))
    cost_green = gp[0]
    cost_purple = gp[1]
    n = int(input())

    ## Variables to count the total number of problems 1 and 2 solved
    total_problem_1 = 0
    total_problem_2 = 0

    ## Loop through all the participants and add the totals
    for participant in range(n):
        p_1, p_2 = map(int, input().split())
        total_problem_1 += p_1
        total_problem_2 += p_2

    ## Calculate the total with green balloons for problem 1
    first_green = total_problem_1 * cost_green + total_problem_2 * cost_purple
    ## Calculate the total with purple ballons for problem 1
    first_purple = total_problem_1 * cost_purple + total_problem_2 * cost_green

    ## Check which combinations is the cheapest
    if first_green < first_purple:
        print(first_green)
    else:
        print(first_purple)

    t -= 1
