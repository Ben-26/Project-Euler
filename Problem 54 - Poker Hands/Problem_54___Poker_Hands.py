def determine_winner(hand):
    card_values = {**{str(i): i for i in range(2, 10)}, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    hand = hand.split(" ")
    player_1s_hand = hand[:5]
    player_2s_hand = hand[5:]

    def rank_hand(hand):
        values = sorted([card_values[card[0]] for card in hand], reverse=True)
        suits = [card[1] for card in hand]
        value_counts = {v: values.count(v) for v in values}
        unique_counts = sorted(value_counts.values(), reverse=True)
        
        is_flush = len(set(suits)) == 1
        is_straight = len(set(values)) == 5 and (max(values) - min(values) == 4)

        if is_flush and values == [14, 13, 12, 11, 10]:
            return (10, values)  # Royal Flush
        elif is_flush and is_straight:
            return (9, values)  # Straight Flush
        elif unique_counts == [4, 1]:
            four_kind_value = max(value_counts, key=lambda k: value_counts[k] == 4)
            return (8, [four_kind_value] + values)  # Four of a Kind
        elif unique_counts == [3, 2]:
            three_kind_value = max(value_counts, key=lambda k: value_counts[k] == 3)
            return (7, [three_kind_value] + values)  # Full House
        elif is_flush:
            return (6, values)  # Flush
        elif is_straight:
            return (5, values)  # Straight
        elif unique_counts == [3, 1, 1]:
            three_kind_value = max(value_counts, key=lambda k: value_counts[k] == 3)
            return (4, [three_kind_value] + values)  # Three of a Kind
        elif unique_counts == [2, 2, 1]:
            pairs = sorted([v for v in value_counts if value_counts[v] == 2], reverse=True)
            return (3, pairs + values)  # Two Pairs
        elif unique_counts == [2, 1, 1, 1]:
            pair_value = max(value_counts, key=lambda k: value_counts[k] == 2)
            return (2, [pair_value] + values)  # One Pair
        else:
            return (1, values)  # High Card

    def compare_high_cards(values1, values2):
        for v1, v2 in zip(values1, values2):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return 0
        return 0

    def compare_hands(hand1, hand2):
        rank1, values1 = rank_hand(hand1)
        rank2, values2 = rank_hand(hand2)
        if rank1 != rank2:
            return rank1 > rank2
        else:
            return compare_high_cards(values1, values2)

    return 1 if compare_hands(player_1s_hand, player_2s_hand) else 0

def main():
    with open("0054_poker.txt", "r") as poker_hands:
        counter = 0
        for hand in poker_hands:
            counter += determine_winner(hand.strip())
    print(counter)

if __name__ == "__main__":
    main()
