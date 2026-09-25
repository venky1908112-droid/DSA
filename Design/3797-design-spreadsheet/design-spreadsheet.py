class Spreadsheet:
    def idx(self, cell):
        c = ord(cell[0]) - 65
        r = int(cell[1:]) - 1
        return r, c

    def __init__(self, rows: int):
        self.grid = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        r, c = self.idx(cell)
        self.grid[r][c] = value

    def resetCell(self, cell: str) -> None:
        r, c = self.idx(cell)
        self.grid[r][c] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split("+")
        ans = 0
        if a.isdigit():
            ans += int(a)
        else:
            r, c = self.idx(a)
            ans += self.grid[r][c]

        if b.isdigit():
            ans += int(b)
        else:
            r, c = self.idx(b)
            ans += self.grid[r][c]
        return ans


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)