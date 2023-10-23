h, m = map(int, input().split(":"))

while True:
    m += 1
    if m >= 60:
        m = 0
        h += 1
        if h >= 24:
            h = 0

    if str(h).zfill(2) == str(m).zfill(2)[::-1]:
        break

palindromic_time = f"{str(h).zfill(2)}:{str(m).zfill(2)}"
print(palindromic_time)
