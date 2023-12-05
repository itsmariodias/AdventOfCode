file = open("input.txt", "r")
original_cards = file.read().split(sep="\n")


def process_cards(cards):
    total_cards = 0
    for card in cards:
        card_number = int(card.split(":")[0].split()[1])
        numbers = card.split(":")[1]
        winning_numbers = numbers.split("|")[0].strip().split()
        your_numbers = numbers.split("|")[1].strip().split()

        points = 0
        for number in your_numbers:
            if number in winning_numbers:
                points += 1

        card_copies = original_cards[card_number:card_number + points]

        total_cards += process_cards(card_copies) + points
    return total_cards


print(process_cards(original_cards) + len(original_cards))
