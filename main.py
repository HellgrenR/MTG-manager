from mtgsdk import Card

# Example: Search for a card by name
card_name = "Lightning Bolt"
cards = Card.where(name=card_name).all()

# Print card details
for card in cards:
    print(f"Name: {card.name}")
    print(f"Mana Cost: {card.mana_cost}")
    print(f"Type: {card.type}")
    print(f"Set Name: {card.set_name}")
    print(card.text)
