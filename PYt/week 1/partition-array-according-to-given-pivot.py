class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pre_pivot = []
        post_pivot = []
        during_pivot = []
        for n in nums:
            if n < pivot:
                pre_pivot.append(n)
            elif n == pivot:
                during_pivot.append(n)
            else:
                post_pivot.append(n)

        return (pre_pivot + during_pivot + post_pivot)

        
        