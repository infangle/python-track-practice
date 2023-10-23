n = int(input())
s = input()

# Initialize variables for counting 0s and 1s
count_0 = 0
count_1 = 0

# Initialize a dictionary to store the earliest occurrence of a count difference
count_diff = {0: -1}

max_length = 0

for i in range(n):
    if s[i] == '0':
        count_0 += 1
    else:
        count_1 += 1

    diff = count_0 - count_1

    if diff in count_diff:
        length = i - count_diff[diff]
        max_length = max(max_length, length)
    else:
        count_diff[diff] = i

print(max_length)
