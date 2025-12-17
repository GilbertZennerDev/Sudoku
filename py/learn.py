"""
lets learn building a Sudoku Game:

I need to build a 9x9 grid. called Group
this grid needs to be split into 3x grids, each having 3x3 cells. - called smallGroup
I need to fill this grid with numbers
Each number in every cell must be unique per row, column and smallGroup

also alles opschreiwen ier ech vill coden
an schrett vir schrett maan.
"""

import sys
import random as r

def getLine(sGs, line):
	#line 0 is the first line of sG0, the first line of sG1 and also for sG2
	#line 1 is the second line
	#line 2 is the third line
	#line 3 is the first line of sG3, sG4 and sG5
	#line 6 is the first line of sG6, sG7 and sG8
	if line == 0: return sGs[0][0:3] + sGs[1][0:3] + sGs[2][0:3]
	if line == 1: return sGs[0][3:6] + sGs[1][3:6] + sGs[2][3:6]
	if line == 2: return sGs[0][6:9] + sGs[1][6:9] + sGs[2][6:9]
	if line == 3: return sGs[3][0:3] + sGs[4][0:3] + sGs[5][0:3]
	if line == 4: return sGs[3][3:6] + sGs[4][3:6] + sGs[5][3:6]
	if line == 5: return sGs[3][6:9] + sGs[4][6:9] + sGs[5][6:9]
	if line == 6: return sGs[6][0:3] + sGs[7][0:3] + sGs[8][0:3]
	if line == 7: return sGs[6][3:6] + sGs[7][3:6] + sGs[8][3:6]
	if line == 8: return sGs[6][6:9] + sGs[7][6:9] + sGs[8][6:9]
def genField():
	sGs = [[r.randint(0, 9) for i in range(9)] for i in range(9)]
	for i, g in enumerate(sGs): print(g)	
	print("="*30)
	print(getLine(sGs, 0))
	print(getLine(sGs, 1))
	print(getLine(sGs, 2))
	print(getLine(sGs, 3))
	print(getLine(sGs, 4))
	print(getLine(sGs, 5))
	print(getLine(sGs, 6))
	print(getLine(sGs, 7))
	print(getLine(sGs, 8))

def	main():
	av = sys.argv
	ac = len(av)
#	if ac != 2: return
	genField()

if __name__ == '__main__': main()
