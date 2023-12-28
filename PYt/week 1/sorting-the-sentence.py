class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split()
        ans = [" "]*(len(s_list)+1)
        print(ans)
        for word in s_list:
            i = int(word[-1])
            ans[i] = word[:-1]
    
        output = " ".join(ans)
        return output.strip()