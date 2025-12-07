import sys
val = list(map(list, sys.stdin.read().strip().split('\n')))

beams = {val[0].index('S'): 1}
splits = 0
for line in val[1:]:
    new_beams = {}
    for beam, power in beams.items():
        if line[beam] == '.':
            new_beams[beam] = new_beams.get(beam, 0) + beams[beam]
        else:
            new_beams[beam-1] = new_beams.get(beam-1, 0) + beams[beam]
            new_beams[beam+1] = new_beams.get(beam+1, 0) + beams[beam]
    beams = new_beams
print(sum(beams.values()))
