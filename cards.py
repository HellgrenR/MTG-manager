from mtgsdk import Card

# Example: Search for a card by name
card_name = "Wrath of god"
cards = Card.where(name=card_name).all()

print(cards[0])

# Print card details
print(vars(cards[0]))

