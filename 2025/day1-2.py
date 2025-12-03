total = 0
dial = 50
while True:
    try:
        delta = int(input().replace('R', '').replace('L', '-'))
    except EOFError:
        print(total)
        quit()
    for i in range(abs(delta)):
        dial += 1 if delta > 0 else -1
        dial %= 100
        total += dial == 0
