class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        nums_left = 0
        nums_right = nums.count(1)
        div_score = defaultdict(list)
        score = nums_right + nums_left
        div_score[score].append(0)
        for i in range( len(nums)):
            score = 0
            if nums[i] == 0:
                nums_left += 1
            elif nums[i] == 1:
                nums_right -= 1
            score = nums_left + nums_right
            div_score[score].append(i+1)
       
        maxi_score = max(div_score.keys())
        return div_score[maxi_score] 
        
        
          

        