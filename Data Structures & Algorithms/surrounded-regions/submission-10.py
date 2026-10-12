class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(start_r, start_c):
            stack = [(start_r, start_c)]
            visited[start_r][start_c] = True

            region = []
            touches_border = False

            while stack:
                r, c = stack.pop()
                region.append((r, c))

                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    touches_border = True

                for nr, nc in (
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1),
                ):
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and board[nr][nc] == "O"
                        and not visited[nr][nc]
                    ):
                        visited[nr][nc] = True
                        stack.append((nr, nc))

            return region, touches_border

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] != "O" or visited[r][c]:
                    continue

                region, touches_border = dfs(r, c)

                if not touches_border:
                    for rr, cc in region:
                        board[rr][cc] = "X"