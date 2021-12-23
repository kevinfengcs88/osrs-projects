# osrs-projects
[Old School RuneScape](https://oldschool.runescape.com/) is a massively multiplayer online role-playing game (MMORPG) released by Jagex Limited in 2013. It serves as a nostalgic portal to the world of Gielinor
for many, based off of the servers of the original game, RuneScape, from 2007. In OSRS, you can do whatever you want: Whether it is slaying dragons or chopping down trees,
you, as the player, set the pace of the game. 

I began playing RuneScape as a child, only four or five years of age. I knew very little about the game (and little about life), but I did know that slaying giant rats,
chopping down trees, and lighting campfires made for a fun time. Little did I know, I would be able to experience the world of Gielinor once again in the summer going into my
sophomore year of high school. It came in the form of Old School RuneScape, a game that is still updated every week and regularly gets new content. It still features
the same, nostalgic polygon graphics that dominated the early 2000s of videogames, and has a playerbase that is actually growing, despite its age. 

A massive multiplayer game with such an active community inevitably leads to player-led projects and creations. The largest community-driven projects is 
[RuneLite](https://runelite.net/), an open-source client for the game that introduces plugins and features that makes the user experience much smoother. At the 
[GitHub page](https://github.com/runelite) for RuneLite, you can find the HTML framework for its website, the Java code that makes its plugins possible, and much more.

Inspired by projects like RuneLite, I decided to make projects for OSRS myself. It wasn't too difficult generating ideas, as the game and available online tools
presented their own problems; I only needed to pick them out and then implement a solution through code. This repository contains all of my coding projects pertaining to Old School RuneScape.

## zulrah.py
I found myself fighting one of RuneScape's most popular bosses, [Zulrah](https://oldschool.runescape.wiki/w/Zulrah)
, a snake boss that grants players bountiful rewards when slain. The Zulrah fight works through rotations, as the snake boss disappears under poison waste only to
reappear elsewhere. It takes on different forms, which can only be damaged with appropriate gear, and covers the island that the player stands on in poison clouds.
These complicated rotations makes Zulrah helpers, like this [one](https://nightfirecat.github.io/zulrahguide/), quite popular. However, these guides usually miss out
on some form of information. Most of the time, I found myself getting stuck in poison clouds and taking unnecessary damage due to a lack of info on the diagram. I had already
made the drawings of Zulrah's rotations with additional information on my iPad in response to this, but swiping through the pages of a virtual notebook to get to the rotation I needed was quite primitive.
I did a bit of research on how to make a GUI with [tkinter](https://docs.python.org/3/library/tkinter.html) in Python, imported my rotation images, and created
a fully functional [Zulrah GUI](https://github.com/kevinfengcs88/osrs-projects/blob/main/zulrah.py) with my own images to aid me in my Zulrah bossing.

## sheets.py
Old School RuneScape has its own player-driven economy. Players gather resources, such as fish, logs, potions, weapons, etc. and sell them on the 
[Grand Exchange](https://oldschool.runescape.wiki/w/Grand_Exchange) to other players who pay with coins, the in-game currency. Prices fluctuate just as they do in
the real world economy: As a resource becomes more scarce (supply is low), players have to pay more coins for it, and the opposite is also true. 
