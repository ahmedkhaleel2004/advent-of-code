# my personal solution

words = open(0).read().split(",")

words[-1] = words[-1][:-1]

def hashfunc(step):
    local = 0
    for char in step:
        local += ord(char)
        local *= 17
        local = local % 256
    return local

total = 0

for word in words:
    total += hashfunc(word)

print(total)