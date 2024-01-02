class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        l = len(processorTime)

        processorTime.sort()
        tasks.sort(reverse =True)

        maxi = 0

        for i in range(l):
            maxi = max(maxi, processorTime[i] + max(tasks[i*4:i*4+4]))

        return maxi
        