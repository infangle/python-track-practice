class RandomizedSet:

    def __init__(self):
        self.lis = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.lis)
            self.lis.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            index = self.dict[val]
            last_el = self.lis[-1]
            self.lis[index] = last_el
            self.lis.pop()
            self.dict[last_el] = index
            del self.dict[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.lis)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()