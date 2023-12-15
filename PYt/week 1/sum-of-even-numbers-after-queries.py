class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = []
        e_sum = 0
        for num in nums:
            if num % 2 == 0:
                e_sum += num
        for val, index in queries:
            prev_num = nums[index]
            nums[index] += val
            if nums[index] % 2 == 0 and prev_num % 2 != 0:
                e_sum += nums[index]
            elif nums[index] % 2 == 0 and prev_num % 2 == 0:
                e_sum += (nums[index] - prev_num)
            elif nums[index] % 2 != 0 and prev_num % 2 == 0:
                e_sum -= prev_num
            

            even_sum.append(e_sum)


        return even_sum


            
        