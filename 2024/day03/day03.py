import re


lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

output, enabled = 0, True
for line in lines:
    for r in range(len(line)):
        if line[r] != ")":
            continue
        if line[r-3:r+1] == "do()":
            enabled = True
        if line[r-6:r+1] == "don't()":
            enabled = False
            continue

        if not enabled:
            continue

        l = r
        while l >= 0 and line[l] != "m":
            l -= 1
            
        if re.search("^mul\(\d{1,3},\d{1,3}\)$", line[l:r+1]):
            print(line[l+4:r])
            n1, n2 = line[l+4:r].split(",")
            output += (int(n1) * int(n2))

print(output)
