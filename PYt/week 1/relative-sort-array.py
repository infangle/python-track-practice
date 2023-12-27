class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        storage = [0]*1003
        ans = []
        for a1 in arr1:
            storage[a1] += 1
            print(a1)

        for a2 in arr2:
            for _ in range(storage[a2]):
                ans.append(a2)
                storage[a2] -=1

        for i in range(len(storage)): 
            for _ in range(storage[i]):
                ans.append(i)
                storage[i] -=1
        return ans
