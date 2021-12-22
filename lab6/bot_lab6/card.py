class Card:
    def __init__(self, suit, number, weight):
        self.id = suit + "__" + number
        self.suit = suit
        self.number = number
        self.weight = weight
        if self.suit == "Clubs":
            self.directory = "cards/" + self.suit + "/" + self.number + ".png"

    def print_card_name(self):
        return self.suit + " " + self.number

    # def dir_to_card_picture(self):
    #     if self.suit == "Clubs":
    #         directory = "cards/" + self.suit + "/" + self.number + ".JPG"
    #         return directory