import sys
lines = sys.stdin.read().strip().split('\n')

vals = [line.split() for line in lines]
ops = vals.pop()
accs = ['+*'.index(x) for x in ops]
ops = list(accs)

for row in vals:
    for i, val in enumerate(row):
        accs[i] = [int.__add__, int.__mul__][ops[i]](int(val), accs[i])
        # accs[i] = [operator.add, operator.mul][ops[i]](int(val), accs[i])

print(sum(accs))
