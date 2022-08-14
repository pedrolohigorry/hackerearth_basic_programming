'''
############  Exercise taken from Hackerearth, Codemonk.
############  Solved using Python 3.9.5

Problem: Maximum borders

You are given a table with  rows and  columns. Each cell is colored with white
or black. Considering the shapes created by black cells, what is the maximum
border of these shapes? Border of a shape means the maximum number of
consecutive black cells in any row or column without any white cell in between.

A shape is a set of connected cells. Two cells are connected if they share an
edge. Note that no shape has a hole in it.

Input format

The first line contains denoting the number of test cases.
The first line of each test case contains integers  denoting the number of rows
and columns of the matrix. Here, '#' represents a black cell and '.' represents
a white cell.
Each of the next lines contains integers.

Output format
Print the maximum border of the shapes.

Sample Input
2
2 15
.....####......
.....#.........
7 9
...###...
...###...
..#......
.####....
..#......
...#####.
.........

Sample Output
4
5

##############
'''

t = int(input())  # save the number of testcases

while t != 0:  ## will go through all testcases until reach 0 t left

    ## save the numbers of rows and n and and number of rotations
    nm = list(map(int, input().split()))
    n = nm[0] ## number of rows
    m = nm[1] ## number of items in columns, either . or #

    max_blacks = 0   ## the number asked for in each testcase

    for line in range(n):    ## iterate through each line
	    row = input()
	    blacks_line = 0  ## Counter of amount of '#' for each line

        ## Check if each item i has a '#'.
	    for i in row:
	        if i == "#":
		        blacks_line += 1

        ## If number is black_lines is bigger than the maximum of blacks so far,
        ## then keep that value in max_blacks variable.
	    if blacks_line > max_blacks:
		    max_blacks = blacks_line
	
    print(max_blacks)

    t -= 1  ## reduce the number of testcases by 1 for the while loop to end
