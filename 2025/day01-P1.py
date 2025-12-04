total = 0
dial = 50
while True:
    try:
        delta = int(input().replace('R', '').replace('L', '-'))
    except EOFError:
        print(total)
        quit()
    dial = (dial + delta) % 100
    total += dial == 0
