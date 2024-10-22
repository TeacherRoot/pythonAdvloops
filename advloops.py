'''
numberTriangle will draw this type of triangle
Start at startNum and run for "rows" rows
10
11 12
13 14 15
16 17 18 19
20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36 37
38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54
'''

def numberTriangle(startNum, rows):
  pass

'''
Draw a square of o's with "rows" rows
E.g. n = 3
oooooo
o    o
oooooo
 
E.g. n = 8
oooooooooooooooo
o              o
o              o
o              o
o              o
o              o
o              o
oooooooooooooooo
'''
def oSquare(rows):
  pass

''' 
Draw a square with a diamond in the middle:
E.g. n = 3
 
1 3 5 5 3 1
3 5     5 3
5         5
5         5
3 5     5 3
1 3 5 5 3 1
 
E.g. n = 5
1 3 5 7 9 9 7 5 3 1
3 5 7 9     9 7 5 3
5 7 9         9 7 5
7 9             9 7
9                 9
9                 9
7 9             9 7
5 7 9         9 7 5
3 5 7 9     9 7 5 3
1 3 5 7 9 9 7 5 3 1
'''
def diamondSquare(n):
  pass

''' main program '''

numberTriangle(10, 9)
numberTriangle(5, 1)
numberTriangle(3, 10)

oSquare(3)
oSquare(8)

diamondSquare(3)
diamondSquare(5)
diamondSquare(8)
