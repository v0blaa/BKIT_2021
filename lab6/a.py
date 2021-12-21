import random


def aaaa():
    cards = {random.randint(1, 4): random.randint(2, 11)}
    return cards

if __name__ == '__main__':
    cards = aaaa()
    new_card = aaaa()
    cards[int(str(new_card)[1])] = new_card[int(str(new_card)[1])]
    print(cards)