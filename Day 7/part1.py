from collections import Counter
import functools

file = open("input.txt", "r")
lines = file.read().split(sep="\n")

card_values = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def determine_strength(x):
    x_counter = Counter(x).most_common()
    if x_counter[0][1] == 5:
        return 1
    elif x_counter[0][1] == 4:
        return 2
    elif x_counter[0][1] == 3 and x_counter[1][1] == 2:
        return 3
    elif x_counter[0][1] == 3:
        return 4
    elif x_counter[0][1] == 2 and x_counter[1][1] == 2:
        return 5
    elif x_counter[0][1] == 2:
        return 6
    else:
        return 7


def compare_cards(x, y):
    for i in range(5):
        if x[i] != y[i]:
            return card_values.index(x[i]) - card_values.index(y[i])
    return 0


def compare(x, y):
    x_strength = determine_strength(x)
    y_strength = determine_strength(y)

    if x_strength == y_strength:
        return compare_cards(x, y)
    else:
        return x_strength - y_strength


hands = []
hands_bid_map = dict()

for line in lines:
    hand, bid = line.split()
    hands.append(hand)
    hands_bid_map[hand] = int(bid)

hands.sort(key=functools.cmp_to_key(compare))
hands.reverse()
print(hands)

output = sum([idx * hands_bid_map[hand] for idx, hand in enumerate(hands, start=1)])

print(output)
