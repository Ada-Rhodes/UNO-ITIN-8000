# Import the dicebag
from toybox import dicebag as roll
from toybox import carddeck as draw
import os

# Roll a six sided die
print(roll.d20())
# Draw a card
print(draw.draw_cards(1))

#os.mkdir('poems')
os.path.exists('poems')
#os.mkdir('poems/mcintyre')

print(os.listdir('poems'))
os.rmdir('poems')
