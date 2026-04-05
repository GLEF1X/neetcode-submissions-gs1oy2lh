func isValidSudoku(board [][]byte) bool {
    for i := 0; i < len(board); i++ {
		rowNums := make(map[byte]struct{})
		colOrderNums := make(map[byte]struct{})

		for j := 0; j < len(board[i]); j++ {
			// row check
			num := board[i][j]
			if _, ok := rowNums[num]; num != '.' && ok {
				return false
			}
			rowNums[num] = struct{}{}

			// col check
			colNum := board[j][i]
			if _, ok := colOrderNums[colNum]; colNum != '.' && ok {
				return false
			}
			colOrderNums[colNum] = struct{}{}

			if i % 3 == 0 && j % 3 == 0 {
				m := make(map[byte]struct{})
				for k := i; k < i+3; k++ {
					for l := j; l < j+3; l++ {
						num := board[k][l] 
						if _, ok := m[num]; num != '.' && ok {
							return false
						}
						m[num] = struct{}{}
					}
				}
			}
		}

		// first subbox
		// (0, 0) (0,1), (0,2)
		// (1, 0) (1,1), (1,2)
		// (2, 0) (2,1), (2,2)
		// (0, 0), (0, 1), (0, 2)...
		// 
	}
	return true
}
