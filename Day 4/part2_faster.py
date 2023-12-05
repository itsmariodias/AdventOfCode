file = open("input.txt", "r")
cards = file.read().split(sep="\n")

cards_tracker = [1] * len(cards)

for card in cards:
    card_number = int(card.split(":")[0].split()[1])
    numbers = card.split(":")[1]
    winning_numbers = numbers.split("|")[0].strip().split()
    your_numbers = numbers.split("|")[1].strip().split()

    points = 0
    for number in your_numbers:
        if number in winning_numbers:
            points += 1

    for i in range(card_number, card_number + points):
        cards_tracker[i] += 1 * cards_tracker[card_number-1]

print(sum(cards_tracker))
