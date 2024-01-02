class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end = len(arr)
        seg = []
        ans = []
        for i in range(len(arr)):
            max_idx = arr.index(end) + 1
            if 1 < max_idx and max_idx < end:
                segment = arr[0:max_idx]
                segment.reverse()
                arr[0:max_idx] = segment
                endSegment = arr[0:end]
                endSegment.reverse()
                arr[0:end] = endSegment 
                ans.append(max_idx)
                ans.append(end)
                print(ans)
            
            elif max_idx == 1:
                endSegment = arr[0:end]
                endSegment.reverse()
                arr[0: end] = endSegment
                ans.append(end)
            
            end -= 1
        return ans

        