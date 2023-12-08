# my method was to use a hashmap to count the number of times each card shows up and classify from there
# but this method uses less code, idk if its faster, but most importantly it accounts for having to sort
# the same classification, like KK677 and KTJJT and ultimately i feel like you would need a letter map.
# hyper neutrino ofc

letter_map = { "T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

def classify(hand):
    counts = [hand.count(card) for card in hand]
    
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0

def strength(hand):
    return (classify(hand), [letter_map.get(card, card) for card in hand])

plays = []

for line in open(0):
    hand, bid = line.split()
    plays.append((hand, int(bid)))

plays.sort(key = lambda play: strength(play[0]))

total = 0

for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid

print(total)