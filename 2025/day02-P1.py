ranges = input().split(',')
ranges = [x.split("-") for x in ranges]
ranges = [range(int(a), int(b)+1) for a, b in ranges]
total = 0
for r in ranges:
    for id in r:
        s = str(id)
        split = len(s) // 2
        if s[:split] == s[split:]:
            total += id
print(total)
