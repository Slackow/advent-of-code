import sys

layout = list(map(list, sys.stdin.read().strip().split("\n")))

total_removed = 0
while True:
    removed = 0
    for r, row in enumerate(layout):
        for c, val in enumerate(row):
            if layout[r][c] == '.':
                continue
            # start at -1 to account for self
            neighbors = -1
            for neighbor_r in range(max(0,r-1),min(r+2,len(layout))):
                for neighbor_c in range(max(0,c-1),min(c+2,len(row))):
                    neighbors += layout[neighbor_r][neighbor_c] != '.'
            if neighbors < 4:
                layout[r][c] = '.'
                removed += 1
    total_removed += removed
    if removed < 1:
        break
print(txt := '\n'.join(''.join(row) for row in layout))
print(total_removed)
