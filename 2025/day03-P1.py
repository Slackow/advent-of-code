total = 0
def jolt(line: str) -> int:
    left_max = line[0]
    jolt_max = 0
    for i in line[1:]:
        jolt_max = max(jolt_max, int(left_max + i))
        left_max = max(left_max, i)
    return jolt_max
while True:
    try:
        total += jolt(input())
    except EOFError:
        print(total)
        quit()
