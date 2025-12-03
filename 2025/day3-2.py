total = 0
def jolt(line: str, digits: int) -> int:
    result = ""
    for i in range(digits-1, -1, -1):
        result += max(line[:-i] if i else line)
        line = line[line.index(result[-1])+1:]
    return int(result)
while True:
    try:
        total += jolt(input(), digits=12)
    except EOFError:
        print(total)
        quit()
