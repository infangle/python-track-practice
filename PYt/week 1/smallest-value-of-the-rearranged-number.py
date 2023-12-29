class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            isNeg = True
        else:
            isNeg = False
        str_num = str(num)
        if str_num[0] == '-':
            str_num = str_num[1:]
        num_list = [int(n) for n in str_num]
        
        #sorting the number
        if len(num_list) <=1:
            ans = num
        for i in range(1, len(num_list)):
            key = num_list[i]
            j = i - 1

            while j>=0 and key < num_list[j]:
                num_list[j+1] = num_list[j]
                j -= 1
            num_list[j+1] = key



        #reordering the ans
        ans = 0
        if not isNeg:
            #reordering the leading zero
            if len(num_list) >=2:
                if num_list[0] == 0:
                    for i in range(len(num_list)):
                        if num_list[i] > 0:
                            num_list[0] = num_list[i]
                            num_list[i] = 0
                            break
                
            for n in num_list:
                ans *= 10 #arranging digit
                ans += n  #adding each digit

        else:
            ans = 0
            #reversing the order to find the smallest possible answer
            for i in range(len(num_list)-1, -1, -1):
                
                ans *= 10
                ans += num_list[i]

            #returning the sign
            ans *= (-1)

        return int(ans)
        