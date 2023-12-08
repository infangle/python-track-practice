class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        space = 0
        for i, c in enumerate(s):
            if space < len(spaces) and i == spaces[space]:
                ans.append(' ')
                space += 1
            ans.append(c)
        return ''.join(ans)
                
       
        
            
        return s
            
       
            