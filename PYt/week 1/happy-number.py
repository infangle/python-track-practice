class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 2:
            return False
        visited = set()
        while n != 1:
            n = str(n)
            new_n = 0
            for i in range(len(n)):
                new_n += (int(n[i])) ** 2
            n = new_n
            if new_n in visited:
                return False

            else:
                visited.add(new_n)
        
        return True
        