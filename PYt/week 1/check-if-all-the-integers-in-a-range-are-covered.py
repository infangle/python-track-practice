class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      given_nums = {num for num in range(left, right+1)}
      myset = set()
      for interval in ranges:
        ran = {x for x in range(interval[0], interval[1]+1)}
        myset.update(ran)
      
      if given_nums <= myset:
        return True
      else:
        return False

        
        