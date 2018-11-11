a = []

for line in open('result.txt').read().split('\n'):
    if line[0] == 'Q' and line[1] == 'C' and line[2] == 'T' and line[3] == 'F':
        a.append(line)

print(a)
