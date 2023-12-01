class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        l = 0
        r = 0
        for r in range(len(command)):
            if command[r] == "G":
                ans = ans + "G"
            elif command[r] == "(":
                l = r
                r+=1
            elif command[l] == "(" and command[r] == ")":
                ans = ans + "o"
                l+=2
                r+=2
            elif command[l] == "(" and command[r] == "a":
                ans = ans + "al"
                l+=2
                r+=2
        return ans


           
        