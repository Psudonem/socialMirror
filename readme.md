Social Mirror!

This project turns backloggd and letterboxd reviews into web pages to host on your website.

The purpose of this project is to provide a one stop shop for your content that you own and control, without the pains of building a one stop shop from scratch. That is, we leverage the interfaces of other popular review sites have built. This way you don't have to worry about doing the heavy lifting of copying a review from one place and pasting it into another place. The site will build itself up with minimal effort as you use these other websites.

As of right now, we take the information from the generated RSS feed. 

This project is windows only for now.

____

live demo: https://yudo.cc/socialMirrors/
____
how to use:
- this project was written with python 3.10 but should work with any version of 3
- pip install these modules (if they didn't come with python already):
    - PySimpleGUI
    - feedparser
    - os
    - subprocess
    - json
    - Beautiful soup 4 (probably)

- write whatever code you need to in update.bat, as the version provided with this website does nothing. the intention of update.bat is to send your newly generated HTML files to your web server.

- open mirrorMaster.py, enter your username for each service in the username block for each system, then click the floppy disk icon. Next time you open the program, your username will be there.

- after you have all of that done, just open mirrorMaster.py and click the service you want to generate a web page for. Once all that is done, click "NeoUp" to run the update batch file
____
Todo:

- ~standardize the style sheet in a seperate style.css~ done
- support more websites:
    - ~Myanimelist~ done
    - ~Goodreads~ done
    - Oku
- compiled language rewrite (either golang or c#)
- create sub folder for outputted html files
- ~make it easy to define your username in the mirrorMaster~ done, added user configuration
- make it easy to edit the update.bat
- make it platform agnostic (accepting batch and bash files)
- build a local JSON database to store reviews in seperately instead of pulling a new RSS feed every time < next up
