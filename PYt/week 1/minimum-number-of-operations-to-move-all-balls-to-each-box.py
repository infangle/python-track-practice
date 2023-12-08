class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        i=0
        j=i+1
        answer=[]
        count=0
        while i < len(boxes):
            while j <=len(boxes)-1:
                if boxes[j]=="1":
                    count+=abs(i-j)
                j+=1
            answer.append(count)
            i=i+1
            j=0  
            count=0
        return answer