# GITHUB STARTER CODE :)
# You can clone this repo or just copy paste this into a new python file
# I've added some high-level explanations for the code as comments
# The computer will ignore everything after a '#' symbol, so it won't affect the code
# If you have any questions, feel free to ask in the chat or dm me on discord (imapanda#0001)
# Most importantly, have fun! ;)

# MODULE IMPORTS
# You don't need to worry about this stuff lol, I'll go over it in the workshop anyway
import pyautogui
import time
from win32gui import GetForegroundWindow, GetWindowText


# GET MOUSE POSITION FUNCTION
# This will let you "measure" the coordinates of specific points on screen by hovering your mouse over it
# Very useful - you'll see why when I talk about the design process
def get_mouse_pos():
    while True:
        print(pyautogui.position())
        time.sleep(1)


# This part technically isn't necessary for the bot to run, it just makes your life a lot easier
# It prevents the program from starting until you switch over to the game window (which is run from your browser)
YOUR_BROWSER = "TYPE YOUR BROWSER HERE"
# type your browser above: if you're on Google Chrome, the line should look like
# YOUR_BROWSER = "Google Chrome"
activeWin = ''
while YOUR_BROWSER not in activeWin:
    activeWin = GetWindowText(GetForegroundWindow())





# ============================
#          MAIN BODY
# ============================
# This is where the actual code for the bot will be written
# Don't worry, it's not complicated, and I'll walk you through it in the workshop anyway :)
while 'Google Chrome' in activeWin:

    activeWin = GetWindowText(GetForegroundWindow()) # ignore this lol, its just a continuation of the stuff from before

    # COLUMN 1

    # COLUMN 2

    # COLUMN 3

    # COLUMN 4
