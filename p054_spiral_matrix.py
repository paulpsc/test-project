def get_top_row(matrix):
    return matrix[0], matrix[1:]

def get_right_col(matrix):
    n_row = len(matrix)

    row=[]
    for i_row in range(n_row):
        row.append(matrix[i_row].pop())
    return row, matrix

def get_bot_row_r(matrix):
    n_row = len(matrix)
    matrix[n_row-1].reverse()
    return matrix[n_row-1], matrix[:n_row-1]

def get_left_col_r(matrix):
    n_row = len(matrix)
    row = []
    for i_row in range(n_row):
        row.append(matrix[i_row][0])
        matrix[i_row] = matrix[i_row][1:]

    row.reverse()
    return row, matrix

def spiralOrder(matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		
		result=[]

		if (matrix == []):
				return []
		else:
				n_row = len(matrix)
				n_col = len(matrix[0])

				if (n_row == 1):
						row, matrix = get_top_row(matrix)
						result = result + row
						return result
				elif (n_col == 1):
						row, matrix = get_right_col(matrix)
						result = result + row
						return result
				else:

						side = 0  # 0: top, 1: right, 2: bottom, 3: left
						while(n_row > 1 and n_col > 1):
								if (side %4 == 0):
										row, matrix = get_top_row(matrix)
										result = result + row
								elif (side %4 == 1):
										row, matrix = get_right_col(matrix)
										result = result + row
								elif (side %4 == 2):
										row, matrix = get_bot_row_r(matrix)
										result = result + row
								elif (side %4 == 3):
										row, matrix = get_left_col_r(matrix)
										result = result + row

								n_row = len(matrix)
								n_col = len(matrix[0])
								side += 1

						if (side %4 == 0):                          # skip get_top_row to get_right_col
								row, matrix = get_right_col(matrix)
								result = result + row
						elif (side %4 == 1):                        # skip get_right_col to get_bot_row_r
								row, matrix = get_bot_row_r(matrix)
								result = result + row
						elif (side %4 == 2):                        # skip get_bot_row_r to get_left_col_r
								row, matrix = get_left_col_r(matrix)
								result = result + row
						elif (side %4 == 3):                        # skip get_left_col_r to get_top_row
								row, matrix = get_top_row(matrix)
								result = result + row

						return result

def main():
	tests = [
		[ [1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]
    ],

   [
    [2,3,4],
    [5,6,7],
    [8,9,10],
    [11,12,13]
   ],

   [
    [1,2,3],
    [4,5,6],
    [7,8,9]
   ],

   [
   [1,2,3],
   ]

	]

	for test in tests:
		print(test)
		result = spiralOrder(test)
		print("result: ",result)
		print("")


if __name__ == '__main__':
	main()