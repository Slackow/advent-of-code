import sys

ranges, ingredients = sys.stdin.read().strip().split("\n\n")

ranges_raw = ranges.split("\n")
ingredients = ingredients.split("\n")

ranges = []
for r in ranges_raw:
    low, high = [int(x) for x in r.split("-")]
    ranges.append(range(low, high + 1))

ingredients = [int(x) for x in ingredients]
print(len([x for x in ingredients if any(a for a in ranges if x in a)]))
