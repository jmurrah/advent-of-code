def dfs(r, c, index, direction):
    if index == 4:
        return 1
    if not (0 <= r < len(lines) and 0 <= c < len(lines[0])) or lines[r][c] != "XMAS"[index]:
        return 0
    
    directions = {
        "n": (-1, 0),
        "s": (1, 0),
        "e": (0, 1),
        "w": (0, -1),
        "nw": (-1, -1),
        "ne": (-1, 1),
        "sw": (1, -1),
        "se": (1, 1)
    }
    total = 0

    for dir, offset in directions.items():
        if direction == "any" or direction == dir:
            total += dfs(r + offset[0], c + offset[1], index + 1, dir)

    return total


lines = []
with open("input1.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

output = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "X":
            output += dfs(i, j, 0, "any")

print(output)