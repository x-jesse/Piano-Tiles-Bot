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


# GET MOUSE POSITION FUNCTION
# This will let you "measure" the coordinates of specific points on screen by hovering your mouse over it
# Very useful - you'll see why when I talk about the design process
def get_mouse_pos():
    while True:
        print(pyautogui.position())
        time.sleep(1)




# ============================
#          MAIN BODY
# ============================
# This is where the actual code for the bot will be written
# Don't worry, it's not complicated, and I'll walk you through it in the workshop anyway :)

while True:
    ss = pyautogui.screenshot("piano tiles.jpg").convert("RGB")

    col1 = 713, 535
    col2 = 878, 535
    col3 = 1045, 535
    col4 = 1196, 535

    col1_colour = ss.getpixel(col1)
    col2_colour = ss.getpixel(col2)
    col3_colour = ss.getpixel(col3)
    col4_colour = ss.getpixel(col4)

    if col1_colour == (0, 0, 0): # if column 1 colour is black
        pyautogui.click(col1) # move cursor to col1 and click
    elif col2_colour == (0, 0, 0): # same as prev
        pyautogui.click(col2)
    elif col3_colour == (0, 0, 0):
        pyautogui.click(col3)
    elif col4_colour == (0, 0, 0):
        pyautogui.click(col4)

    # COLUMN 1
    # x=713, y=593

    # COLUMN 2
    # x=878, y=598

    # COLUMN 3
    # x=1045, y=576

    # COLUMN 4
    # x=1196, y=575



