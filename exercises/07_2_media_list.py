"""
In this file, let's build a list of all the books we've read (or movies we've 
watched or games we've played -- doesn't matter) in the last few months.

Assuming that you receive a comma-separated list of the name, genre, a note about your 
reaction to it, try storing it in a *structured* way.

That is to say, if I input:
Tears of the Kingdom,Action-adventure,Loved a lot but a bit over-rated in places
Cult of the Lamb,Roguelike,Probably played too much of this one
Cities:Skylines,Simulation,Classic

Then I want to see a list like this:
media = [
    { name: "Tears of the Kingdom", genre: "Action-adventure", opinion: "Loved a lot but a bit over-rated in places" },
    { name: "Cult of the Lamb", genre: "Roguelike", opinion: "Probably played too much of this one" },
    { name: "Cities:Skylines", genre: "Simulation", opinion: "Classic" },
]

We *could* have made this a list-of-lists, but by making a list of dictionaries, we can trust that the data is structured 
when we go to use it.
"""

media = []

while True:
    raw_input = input("A comma-separated list of your recent (books/games/music/movies)")
    if raw_input == "":
        break

    # Here, break your data up.


for title in media:
    # Do something fun here, if you like, but try outputting your data again.
    pass