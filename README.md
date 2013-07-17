###Interfacing Pygame and Arduino


Once pyserial is installed (http://pyserial.sourceforge.net/pyserial.html) you have the ability to communicate between your python app or python terminal and your Arduino.


The code here is modified version of the pygamecheatsheet.py code with a few simple modifications.

###Changes

1. changed  `import pygame, sys` to  `import pygame, sys, serial` on line 9
2. added   `ser = serial.Serial('/dev/tty/usbmodem1421',115200)` on line 13
3. added serial writes via `ser.write('1')` when arrow keys are pressed (see lines 71 - 83)



###Credits

Original PygameCheatSheet Code by  ASWeigart:
https://github.com/asweigart

Link to detailed description of the pygamecheatsheet.py file
http://inventwithpython.com/pygamecheatsheet.png




