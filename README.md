# Suave

A song masher made on a steamdeck at deltahacks in 6 hours. Ultimately this is proof that the Steamdeck can very easily be used as a dev machine with some finagling. 

Usage:
> python3 main.py

Dependencies:
> pip3 install youtube-dl flask pydub

Functionality:
Suave lets you take 2 youtube links (usecase is songs), download the content as mpeg, convert to mp3, and then overlay the two songs on top of each other.

Next steps:
* Shifting the position at which the songs are overlayed
* BPM shifting
* Parallel song download

* 'I'm feeling lucky' where Suave picks an instrumental and an acapella with the same BPM at random and overlays them.
