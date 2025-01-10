filepath = 'data/day7.txt'

hands = []
card_ranking_order = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
sorting_order = {'five': 0, 'four': 1, 'full_house': 2, 'three': 3, 'double': 4, 'pair': 5, 'single': 6}


def get_card_rank(card):
    return card_ranking_order.get(card, 0)


def custom_sort_key(hand_tuple):
    cards = hand_tuple[3]
    return [get_card_rank(card) for card in cards]


def replace_j(hand_to_modify: list, original_counts: dict):
    if 'J' in original_counts and original_counts['J'] != 5:
        del original_counts['J']
        most_present_card = max(original_counts, key=original_counts.get)
        hand_to_modify = [most_present_card if card == 'J' else card for card in hand_to_modify]

    return hand_to_modify


with open(filepath, 'r') as f:
    for line in f.readlines():
        hand, bet = line.strip().split()
        hand_list = [*hand]
        counts = {card: hand_list.count(card) for card in {*hand_list}}
        counts = dict(sorted(counts.items(), key=lambda item: card_ranking_order[item[0]], reverse=True))
        new_hand = replace_j(hand_list, counts)
        new_counts = {card: new_hand.count(card) for card in {*new_hand}}
        new_counts = dict(sorted(new_counts.items(), key=lambda item: card_ranking_order[item[0]], reverse=True))
        hands.append((new_hand, int(bet), new_counts, hand_list))

poker_hands = {
    "five": [],
    "four": [],
    "full_house": [],
    "three": [],
    "double": [],
    "pair": [],
    "single": []
}

for hand in hands:
    cards_in_hand, bet, card_counts, original_hand = hand

    if 5 in card_counts.values():
        poker_hands["five"].append(hand)
    elif 4 in card_counts.values():
        poker_hands["four"].append(hand)
    elif 3 in card_counts.values() and 2 in card_counts.values():
        poker_hands["full_house"].append(hand)
    elif 3 in card_counts.values():
        poker_hands["three"].append(hand)
    elif len(card_counts) == 5:
        poker_hands["single"].append(hand)
    elif 2 in card_counts.values():
        if list(card_counts.values()).count(2) == 2:
            poker_hands["double"].append(hand)
        else:
            poker_hands["pair"].append(hand)

for category in poker_hands:
    poker_hands[category] = sorted(poker_hands[category], key=custom_sort_key)

sorted_poker_hands = {k: poker_hands[k] for k in sorted(poker_hands, key=lambda x: sorting_order[x])}


all_bets = [hand[1] for category_hands in reversed(sorted_poker_hands.values()) for hand in category_hands]
result = [value * length for value, length in zip(all_bets, range(1, len(all_bets) + 1))]

print(sorted_poker_hands)
print(all_bets)
print(sum(result))
