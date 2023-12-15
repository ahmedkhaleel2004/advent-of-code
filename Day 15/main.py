# my personal solution
import re

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

# only thing that tripped me up was that the test case had "rn=1" in box 0 when it should be in box 30

# had to look at a solution here to confirm box_idx labelling
boxes = [{} for _ in range(256)]
for word in words:
    label = re.findall("\w+", word)[0] # easiest way to do this
    box_idx = hashfunc(label)
    if "-" in word:
        if label in boxes[box_idx]:
            del boxes[box_idx][label] # remove that key pair
    else:
        focal_length = int(word.split("=")[1])
        boxes[box_idx][label] = focal_length

for i, box in enumerate(boxes):
    power = 0
    for j, focal_length in enumerate(box.values()):
        power += (i + 1) * (j + 1) * focal_length
    total += power

print(total)