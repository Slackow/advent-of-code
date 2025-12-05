import sys

ranges_raw, _ = sys.stdin.read().strip().split("\n\n")
ranges_raw = ranges_raw.split("\n")
ranges = []
for r in ranges_raw:
    low, high = [int(x) for x in r.split("-")]
    ranges.append(range(low, high + 1))

new_ranges: set[range] = set()
try_again: list[range] = ranges
while try_again:
    ranges = try_again
    try_again = []
    for r in ranges:
        for n_r in new_ranges:
            if r.start in n_r or r.stop-1 in n_r or n_r.start in r:
                break
        else: # no overlap
            new_ranges.add(r)
            continue
        # range overlaps
        new_ranges.remove(n_r)
        try_again.append(range(min(n_r.start, r.start), max(n_r.stop, r.stop)))
print(sum(map(len, new_ranges)))
