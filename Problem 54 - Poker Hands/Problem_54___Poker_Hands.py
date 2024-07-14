
"""
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
Straight Flush: All cards are consecutive values of same suit.
Four of a Kind: Four cards of the same value.
Full House: Three of a kind and a pair.
Flush: All cards of the same suit.
Straight: All cards are consecutive values.
Three of a Kind: Three cards of the same value.
Two Pairs: Two different pairs.
One Pair: Two cards of the same value.
High Card: Highest value card.
"""

def poker():
    return 0 


if __name__ == "__main__":
    games = open('0054_poker.txt', 'r')
    wins = 0
    for game in games:
        wins += poker(game)
    print(wins)

