def find_mas(r, c):
    if not (1 <= r < len(lines) - 1 and 1 <= c < len(lines[0]) - 1):
        return 0
    
    tl = lines[r-1][c-1]
    tr = lines[r-1][c+1]
    bl = lines[r+1][c-1]
    br = lines[r+1][c+1]

    return 1 if {tl, br} == {'M', 'S'} and {tr, bl} == {'M', 'S'} else 0


lines = []
with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

output = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "A":
            output += find_mas(i, j)

print(output)
