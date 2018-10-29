# pratt_james_python
Based on the starting point, I added the player an computer lives.
The reduction code was easy to write, as all I had to do was reduce the lives every time a player lost.
I originally used the syntax "lives--", this was an error i couldn't figure out for awhile.
I just reverted the syntax to "lives = lives - 1" and this fixed my problems.

The largest issue I was having was how to hide the player choices after a player had lost all of their lives.
This was resolved by using a endGame variable.
When a player runs out of lives, the endGame variable was called, then not displays the choices.

I have written this game before in PHP, the transfer to python was a challenge as for the change in structure and syntax.
Aside from that, this game was a fun challenge.
