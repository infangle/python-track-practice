class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result = len(plants)
        current_capacity = capacity

        for i in range(len(plants)):
            if plants[i] >  current_capacity:
                result += 2*i
                current_capacity = capacity
            current_capacity -= plants[i]
        return result
        