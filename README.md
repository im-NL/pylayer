# pylayer

Still working on the name but this is an app that can play whatever songs you like, for free.

There will be no ads and you can play songs by name, queue entire playlists, queue spotify links, 
queue YouTube links and much more. 

View all commands in commands.txt 
OR
Type 'help' in the terminal while running the script to get a list of full commands.

Please comment any issues at 'https://github.com/im-NL/pylayer/issues' and I will try my best to 
resolve them :)

Okay, let me get one thing out of the way,
The script will kind of run on-browser but the ram usage of this script on my computer (with slimjet browser whose
setup I have provided in the setup folder) is very low. It is less than spotify itself so I would say you could even use 
this if you wanted to go for a cheaper alternative to listen to songs. You can look at the videos you want aswell!

<h1>SETTING UP</h1>

before starting, I suggest you pip install the libraries in requirements.txt 

1) You will need a google and spotify api key as I cannot provide mine. The process to get these keys is relatively 
straightforward. A spotify api key is **needed** while the google api key is optional. You can refer to these videos 
for reference on how to get those keys. 
Spotify:
Google: 
(You will need to put these key values into spotify.py and mygoogle.py yourself)

2) Please run the 'sjtwebsetup_x86.exe' file in the setup folder. This will be the browser we are going to be using 
to play the music.

3) You will have to add the chromedriver to PATH, otherwise the script will not run. You can learn how to add anything to 
PATH by using 'https://youtu.be/Y2q_b4ugPWk' (I do not own this video in any form, it is just useful so I am linking it here).

4) You shouldn't, but if you get an error saying 'unknown error: no chrome binary at C:\Program Files (x86)\\slimjet.exe', then you 
should try pressing windows button, typing 'slimjet' clicking on 'Open file location' and then copying the file location and pasting it 
on the 24TH LINE of app.py (change the part in quotation marks to the file location). Make sure you have added '\slimjet.exe' at the 
end there too.


*please note that this application is still under development and most features you suggest can be added*

You can mail me at aryan@teamcodetech.in for any suggestions. 

* you may get an ad on the first song you play, i can't quite figure out why, but they won't play otherwise
* if they do, please tell me.