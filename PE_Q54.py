"""
In the card game poker, 
a hand consists of five cards and are ranked, 
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; 

for example, a pair of eights beats a pair of fives (see example 1 below). 
But if two ranks tie, for example, both players have a pair of queens, 
then highest cards in each hand are compared (see example 4 below); 
if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 

the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

Considerations:
With 1000 hands it doesnt need to be efficient
Check hands top top down (royal flush --> high card)
Good use case for new python 3.10 case statements?
"""

value_base_zero = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


def _monotonic_increasing(L):
    return all(x + 1 == y for x, y in zip(L, L[1:]))


def _count_max(L):
    return _count_n(L, 0)


def _count_n(L, n):
    return sorted([(L.count(i), i) for i in set(L)], key=lambda x: x[0], reverse=True)[
        n
    ]


p1 = []
p2 = []

# Generate hands of both players
with open("supplementary/p054_poker.txt") as f:
    for hand in f.readlines():
        hand = hand.split()
        p1.append(hand[:5])
        p2.append(hand[5:])

ranked_hands = []  # Lower hand rank is better
all_hands = p1 + p2

for hand in all_hands:

    suits = []
    values = []
    for card in hand:
        values.append(value_base_zero[card[0]])
        suits.append(len(set(card[1])))

    values.sort()

    if suits == 1 and values == [8, 9, 10, 11, 12]:  # Royal Flush
        ranked_hands.append((0))
    elif suits == 1 and _monotonic_increasing(values):  # Streight Flush
        ranked_hands.append((1, max(values)))
    elif (c := _count_max(values))[0] == 4:  # Four of a kind
        ranked_hands.append((2, c[1]))
    elif (c := _count_max(values))[0] == 3 and (d := _count_n(values, 1))[
        0
    ] == 2:  # Full House
        ranked_hands.append((3, c[1]))
    elif suits == 1:  # Flush
        ranked_hands.append((4, max(values)))
    elif _monotonic_increasing(values):  # Streight
        ranked_hands.append((5, max(values)))
    elif (c := _count_max(values))[0] == 3:  # 3 of a Kind
        ranked_hands.append((6, c[1]))
    elif (c := _count_max(values))[0] == 2 and (d := _count_n(values, 1))[
        0
    ] == 2:  # Two Pair
        ranked_hands.append((7, c[1], d[1]))
    elif (c := _count_max(values))[0] == 2:  # Pair
        ranked_hands.append((8, c[1]))
    else:  # High Card
        ranked_hands.append((9, max(values)))

wins = 0
idx = 0
for i, j in zip(ranked_hands, ranked_hands[1000:]):
    print(all_hands[idx], all_hands[1000 + idx])
    print(i, j)
    if i[0] < j[0]:
        wins += 1
    elif i[0] == j[0]:
        if i[1] > j[1]:
            wins += 1
    idx += 1

print(wins)