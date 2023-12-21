class OrderedStream:

    def __init__(self, n: int):
        self.chunk = [None] * n
        self.ptr = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.chunk[idKey - 1] = value
        res = []


        for i in range(self.ptr, self.n):
            if self.chunk[i] != None:
                res.append(self.chunk[i])
            else:
                self.ptr = i
                break

        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)