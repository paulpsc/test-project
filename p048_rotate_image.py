def rotate(matrix):
	"""
	:type matrix: List[List[int]]
	:rtype: void Do not return anything, modify matrix in-place instead.
	"""
	L = 0
	n = len(matrix)
	n_turns = n - 1

	while(n_turns > 0):
			for iL in range(L, n-L-1 ):         # L, L+1, ... n-L-2
					tmp = matrix[L][iL]
					matrix[L][iL] = matrix[n - iL - 1][L]
					matrix[n - iL - 1][L] = matrix[n - L - 1][n - iL - 1]
					matrix[n - L - 1][n - iL - 1] = matrix[iL][n - L - 1]
					matrix[iL][n - L - 1] = tmp                         # matrix[L][iL]
			L += 1
			n_turns -= 2

def main():
	tests =[

  [ [1,2,3],  [4,5,6],  [7,8,9] ],
 
  [ [1,2,3,4],  [5,6,7,8],  [9,10,11,12],  [13, 14, 15, 16] ],

  [ [1,2,3,4,5],  [6,7,8,9,10],   [11,12,13,14,15],  [16,17,18,19,20],
   [21,22,23,24,25] ]
  ]

	for test in tests:
		print(test)
		result = rotate(test)
		print("result: ", test)
		print("")


if __name__ == '__main__':
	main()			