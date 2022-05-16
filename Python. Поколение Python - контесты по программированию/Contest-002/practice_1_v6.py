n = int(input())
sequence = []
i = 1
while len(sequence) < n:
    for j in range(i + len(sequence), len(sequence), -1):
        sequence.append(j)
    i += 1
print(*sequence[:n])