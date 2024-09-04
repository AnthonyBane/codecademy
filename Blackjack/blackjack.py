from typing import List
import random


class Card:
    """Card class hold suit and rank."""

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def get_value(self) -> int:
        """Returns the value of the card based on rank.

        Returns:
            int: Value of card rank.
        """
        if self.rank in ["Jack", "Queen", "King"]:
            return 10
        elif self.rank == "Ace":
            return 11
        else:
            return int(self.rank)


class Deck:
    """A deck of cards class."""

    ranks = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

    def __init__(self) -> None:
        self.deck_cards = self.new_deck()
        self.shuffle_deck()

    def new_deck(self) -> List:
        """Generates a new deck.

        Returns:
            List: A new organised deck.
        """
        return [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def draw_card(self) -> Card:
        """Returns the top card from the deck.

        Returns:
            Card: Card from deck.
        """
        if self.deck_cards:
            return self.deck_cards.pop()
        else:
            raise ValueError("Deck is empty!")

    def shuffle_deck(self) -> None:
        """Shuffles the deck."""
        random.shuffle(self.deck_cards)

    def remaining_cards(self) -> int:
        """Returns the numbers of cards remaining in the deck.

        Returns:
            int: Number of remaining cards in deck.
        """
        return len(self.deck_cards)


class Participant:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card: Card) -> None:
        """Adds a card to the participants deck and the value to their score.

        Args:
            card (Card): A new card.
        """
        self.hand.append(card)
        self.score += card.get_value()

    def reset(self) -> None:
        """Resets a participants hand and score."""
        self.hand = []
        self.score = 0

    def show_hand(self) -> List:
        """Displays the participants hand and score."""
        print(f"{self.name} has the {', '.join(str(card) for card in self.hand)} with score {self.score}")


class Player(Participant):
    """A player at the table.

    Args:
        Participant (_type_): _description_
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.hand = []

    def __repr__(self) -> str:
        return f"Player name is {self.name}"


class Dealer(Participant):
    def __init__(self, name: str = "The Dealer") -> None:
        super().__init__(name)

    def __repr__(self) -> str:
        return "This is the dealer."

    def first_card(self) -> Card:
        """Returns the first card in the dealer's hand.

        Raises:
            ValueError: If no cards are in hand, error raised.

        Returns:
            Card: Card item.
        """
        if self.hand[0]:
            return self.hand[0]
        else:
            raise ValueError("Dealer's hand is empty.")


def main():
    """Blackjack main method."""
    dealer = Dealer()
    player = Player("Dave")
    # player = Player(input("Enter a name: "))
    deck = Deck()

    print("Dealer is given two cards.")
    dealer.add_card(deck.draw_card())
    dealer.add_card(deck.draw_card())

    print(f"Dealer's first card is the {dealer.first_card()}")
    print("Dealer's second card is hidden.")

    player.add_card(deck.draw_card())
    player.add_card(deck.draw_card())

    end_turn = False

    while not end_turn:
        player.show_hand()
        new_card = input("Do you want to draw another card? y/n: ")
        if new_card == "y":
            player.add_card(deck.draw_card())
            if player.score > 21:
                print(f"Oh no, {player.name} went bust!")
                end_turn = True
        elif new_card == "n":
            print("Turn over!")
            print(f"Final score for {player.name} is :{player.score}")
            end_turn = True
        else:
            print("You must enter either y or n.")

    end_turn_dealer = False

    while not end_turn_dealer:
        if dealer.score > 21:
            print(f"{dealer.name} went bust! {player.name} wins!")
            end_turn_dealer = True
            continue

        dealer.show_hand()
        if dealer.score < 17:
            print(f"{dealer.name} must draw another card")
            dealer.add_card(deck.draw_card())
        else:
            print(f"{dealer.name}'s score is above 16 but not bust, dealer sticks.")
            end_turn_dealer = True

    if (dealer.score >= player.score or player.score > 21) and dealer.score < 22:
        print(f"{dealer.name} wins this time.")
    else:
        print(f"{player.name} wins!")


if __name__ == "__main__":
    main()
