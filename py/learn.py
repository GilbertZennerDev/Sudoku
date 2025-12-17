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

#also, ech muss just all indexes len(row) aus allen Rows driwwer huelen

def genUniqueRow(*aboveRows):
	row = []
	nbrs = [i for i in range(10)]
	while len(row) < 10:
		aboveNbrs = []
		nb = r.choice(nbrs)
		row.append(nb)
		nbrs.pop(nbrs.index(nb))
	print("row:", row)

def test():
	genUniqueRow()

test()

def getLine(sGs, line):
	if line == 0: return sGs[0][0:3] + sGs[1][0:3] + sGs[2][0:3]
	if line == 1: return sGs[0][3:6] + sGs[1][3:6] + sGs[2][3:6]
	if line == 2: return sGs[0][6:9] + sGs[1][6:9] + sGs[2][6:9]
	if line == 3: return sGs[3][0:3] + sGs[4][0:3] + sGs[5][0:3]
	if line == 4: return sGs[3][3:6] + sGs[4][3:6] + sGs[5][3:6]
	if line == 5: return sGs[3][6:9] + sGs[4][6:9] + sGs[5][6:9]
	if line == 6: return sGs[6][0:3] + sGs[7][0:3] + sGs[8][0:3]
	if line == 7: return sGs[6][3:6] + sGs[7][3:6] + sGs[8][3:6]
	if line == 8: return sGs[6][6:9] + sGs[7][6:9] + sGs[8][6:9]

def printLine(line, hide):
	for i, c in enumerate(line):
		if i % 3 == 0: print('|', end='')
		if hide > r.randint(0, 9): print(' ', end='')
		else: print(c, end='')
	print('|\n', end='')

def printSoduko(sGs, hide):
	print("="*30)
	for i in range(9): printLine(getLine(sGs, i), hide)

def genField():
	sGs = [[r.randint(0, 9) for i in range(9)] for i in range(9)]
	return sGs

def	main():
	av = sys.argv
	ac = len(av)
	sGs = genField()
	printSoduko(sGs, 0)
#if __name__ == '__main__': main()
