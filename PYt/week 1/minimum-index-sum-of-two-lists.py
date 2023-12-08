class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indices = {}
        for i, v in enumerate(list2):
            indices[v] = i
        res = []
        mini = float('inf')
        for i, v in enumerate(list1):
            if v in indices:
                cur = i + indices[v]  
                if cur < mini:
                    mini = cur
                    res = [v]
                elif cur == mini:
                    res.append(v)

        return res