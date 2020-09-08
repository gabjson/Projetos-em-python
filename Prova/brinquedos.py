F,I = input().split(' ')

F = int(F)
I = int(I)
G = 0

if F > 150 and I > 12:
    G = G + 1
if F > 140 and I > 14:
    G = G + 1 
if F > 170 or I > 16:
    G = G + 1

print(G)
