class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) >= len(nums2):
            range_ = max(nums1)
            itr = nums2
            stored = nums1
        else:
            range_ = max(nums2)
            itr = nums1
            stored = nums2
        store1 = [0]*1005
        store2 = [0]*1005
        ans = []
        for num1 in stored:
            store1[num1] += 1

        for num2 in itr:
            store2[num2] += 1

        for num in itr:
            for i in range(min(store1[num], store2[num])):
                ans.append(num)
                store1[num] = 0
                store2[num] = 0
        return ans
