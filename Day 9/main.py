# absolutely crazy recursion solution
# my solution would have been way too long since i was 
# just going to do what it said to do with way too much memory and looping

def extrapolate(arr):
    if all(x == 0 for x in arr):
        return 0
    
    deltas = [y - x for x,y in zip(arr, arr[1:])]
    diff = extrapolate(deltas)
    return arr[-1] + diff

total = 0

for line in open(0):
    nums = list(map(int, line.split()))
    total += extrapolate(nums)

print(total)