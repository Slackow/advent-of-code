ranges = input().split(',')
ranges = [x.split("-") for x in ranges]
ranges = [range(int(a), int(b)+1) for a, b in ranges]
total = 0

cache = {1:[]}
def factors(num: int) -> list[int]:
    if (r := cache.get(num)) is not None:
        return r
    res = [1]
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    cache[num] = res
    return res

for r in ranges:
    for id in r:
        s = str(id)
        options = factors(len(s))
        for i in options:
            c = s[:i]
            for start in range(i, len(s), i):
                if c != s[start:start+i]:
                    break
            else:
                break
        else:
            total -= id
        total += id
print(total)
