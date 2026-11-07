class StockSpanner:

    def __init__(self):
        self._arr = []

    def next(self, price: int) -> int:
        res = 1
        i = len(self._arr) - 1
        while i >= 0 and self._arr[i] <= price:
            res += 1
            i -= 1

        self._arr.append(price)
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)