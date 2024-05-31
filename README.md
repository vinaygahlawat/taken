# TakeN
![Unit Tests](https://github.com/vinaygahlawat/taken/actions/workflows/taken-python-unittest.yml/badge.svg)

*Note: this is just a fun hobby project I created as a way to play around with Python, and eventually I'd like to grow it into a web-based game I can play with my friends and family. It is based on the card game [Take 5](https://gamerules.com/rules/take-5/).*

## How TakeN is played:
TakeN is a turn-based card game. The objective of the game is to accumulate the least amounts of *points*, which a player gets when they take cards.

One instance of TakeN is called a **Match**. A Match is played by players, and a Match ends when a threshold of points is reached.

Once this threshold is reached, the player that has the least amount of accumulated points wins the match.
A Match can consist a single **Game** or many Games. A Game takes place when players have been dealt a **Hand** of cards, and the Game Board has been set with the initial cards.
A Game can have one **Round** or many Rounds, equivalent to the number of cards that have been dealt.

During a **Round**, each player inspects the game board and decides what card from their hand to play. Once every player has decided on a card to play, all players reveal their card to play.
Every player in a Round gets a single **Turn**. The dealer then sorts the cards by card value (not the number of *points* associated with each card), so the turns can begin. Turns are taken starting with the player that played the lowest-numbered card, based on the card number, *not the card points*. During a player's turn in that round, their card is placed on the board. One of three different results can occur:
1. If the card can be placed on the board in the appropriate row, *AND* and placing the card in that row does not exceed the maximum size of that row, then place the card in the row.
2. If the card can be placed on the board in the appropriate row, *BUT* placing the card in that row exceeds the maximum size of the row, then all the existing cards in that row are taken out of the row, the player's card is added to the row as the first card in the row, and all the points on the previous cards in the row are tallied up and added to the player's score.
3. If the card cannot be placed in any row, then the player has to choose a row to take. Their card replaces the existing cards in that row, and similar to when a row is full, the points on the cards previously in that row are tallied and added to the player's score.

A game end state is evaluated after every game. This means that even if an end state is reached in the middle of a round or turn, the game must be completed to determine the winner. In the event that all players cross the threshold of points needed to end the game, the player with the least amount of points still wins the game. (*sad trombone*)
