class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = []
        visited = set()

        def backtrack(i, j):
            if "".join(result) == word:
                return True
            
            if board[i][j] != word[max(len(result) - 1, 0)]:
                return False

            for r, c in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                if not 0 <= r < len(board) or not 0 <= c < len(board[0]):
                    continue
                
                # repeat the same char
                if (r, c) in visited:
                    continue

                if len(result) >= len(word):
                    continue
                
                result.append(board[r][c])
                visited.add((i, j))
                if backtrack(r, c):
                    return True

                result.pop()
                visited.remove((i, j))
            
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                result.append(board[i][j])
                if backtrack(i, j):
                    return True
                visited.clear()
                result.pop()

        return False
        