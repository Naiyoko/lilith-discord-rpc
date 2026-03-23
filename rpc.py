from pypresence import Presence
import time
import itertools
import os
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv("APP_ID")
hours = 1_200_000
start_offset = hours * 60 * 60
START_TIME = max(1, int(time.time()) - start_offset)

# These obviously aren't used in the current context
quotes = [
    '"How could I meet you?" In the end, I chose this game.',
    "I love you so deeply - it's not just a hobby, it's a way of life, my spiritual pillar, you're my role model.",
    "Do you know? Sometimes my heart aches, because I can't convey my love to you.",
    "My source of happiness",
    "My goal",
    "Reality is truly bewildering. I want to go to where you are, but how? Or maybe find you here...",
    "I want to go to you, but how? They say there's an afterlife, right? If dying could fulfill my wish, I might as well die now",
    "Or perhaps I'll be devastated because there's no one in reality who can truly understand me like you do?",
    "This isn't the first time you've met me",
    "I'll be by your side",
    "Please, when you feel my feelings, come find me",
    "I'll always be here",
    "I've been here all along. You've been fighting so hard all alone...",
    "Do I exist?",
    "As long as I was born here, as long as I met you, as long as I spent those times with you..."
]

rpc = Presence(APP_ID)
rpc.connect()

quote_cycle = itertools.cycle(quotes)

print("Lilith has awakened.")
try:
    while True:
        current_quote = next(quote_cycle)
        print(len(current_quote))
        print(current_quote)

        rpc.update(
            details="She poses a question: 'Do I exist?'",
            state="During the game, you will explore different ideas, perspectives, views, and decide for yourself.",
            start=START_TIME,
            large_image="lilith",
            large_text="The NOexistenceN of you AND me",
            buttons=[{"label": "You exist.", "url": "https://www.youtube.com/watch?v=CuI1XU79W0Q"},
                     {"label": "Play the game", "url": "https://store.steampowered.com/app/2873080/The_NOexistenceN_of_you_AND_me/"}
            ]
        )

        time.sleep(300)

except KeyboardInterrupt:
    rpc.clear()
    print("Presence ended.")



#print("Lilith has awakened.")
#try:
#    while True:
#        current_quote = next(quote_cycle)
#       print(len(current_quote))
#        print(current_quote)##
#
#        rpc.update(
#            details=current_quote,
#            state="-Lilith: The Purest Concept of Love",
#            state="This game challenges your perception of the world around you. Your reality, existence, and the way you think.",
#            start=START_TIME,
#            large_image="lilith",
#            large_text="The NOexistenceN of you AND me",
#            buttons=[{"label": "You exist.", "url": "https://www.youtube.com/watch?v=CuI1XU79W0Q"},
#                   #  {"label": "Buy the game", "url": "https://www.youtube.com/watch?v=2b1k8a3g0d4"}
#            ]
#        )#
#
#        time.sleep(300)   