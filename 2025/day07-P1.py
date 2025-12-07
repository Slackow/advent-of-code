import sys
val = list(map(list, sys.stdin.read().strip().split('\n')))

beams = [val[0].index('S')]
splits = 0
for line in val[1:]:
    new_beams = set()
    for beam in beams:
        if line[beam] == '.':
            new_beams.add(beam)
        else:
            new_beams.add(beam-1)
            new_beams.add(beam+1)
            splits += 1
    beams = new_beams
print(splits)
