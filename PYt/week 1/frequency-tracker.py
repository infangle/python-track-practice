class FrequencyTracker:
    def __init__(self):
        self.freq = defaultdict(int)
        self.ft = defaultdict(int)
    def add(self, number: int) -> None:
        self.freq[number] += 1
        self.ft[self.freq[number]] += 1
        self.ft[self.freq[number] - 1] -=1


    def deleteOne(self, number: int) -> None:
        if number in self.freq:

            self.freq[number] -= 1
            self.ft[self.freq[number]] += 1
            self.ft[self.freq[number] + 1] -=1
            if self.freq[number] == 0:
                self.freq.pop(number)

            

        

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.ft and self.ft[frequency] != 0:
            return True
        else:
            return False        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency) 1;3 
