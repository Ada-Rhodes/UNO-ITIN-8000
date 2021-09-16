# Import the dicebag
from toybox import dicebag as roll
from toybox import carddeck as draw

# Roll a six sided die
print(roll.d20())
# Draw a card
print(draw.draw_cards(1))
