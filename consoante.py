alfabeto = []
c = 0
for i in range(ord('A'), ord('Z')+1):
    alfabeto.insert(c, chr(i))
    c += 1
    for j in range(ord('A'), ord('Z')+1):
        alfabeto.append(chr(i)+chr(j))