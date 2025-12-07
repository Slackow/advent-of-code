import sys
vals = sys.stdin.read().strip().split('\n')

ops = vals.pop().split()
accs = ['+*'.index(x) for x in ops]
ops = list(accs)
i = 0
for col in zip(*vals):
    val = ''.join(col).strip()
    if not val:
        i += 1
        continue
    accs[i] = [int.__add__, int.__mul__][ops[i]](int(val), accs[i])

print(sum(accs))
