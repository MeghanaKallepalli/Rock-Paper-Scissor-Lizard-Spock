# Pygame is a cross-platform set of Python modules designed for writing video games
# It includes computer graphics and sound libraries designed to be used with the Python programming language
# The playsound module contains only a single function named playsound() we use it for a while music of 00:00sec


from pygame import mixer
from playsound import playsound


def music():    # Function to start the music
    mixer.init()
    mixer.music.load(r"C:\Users\KATTAKART\Downloads\Feel-Good.mp3")
    mixer.music.play(-1)   # (-1)defines we can play music until the game ends


def stop():   # Function to stop the music
    mixer.music.stop()


def play():    # Function for button music
    playsound(r"C:\Users\KATTAKART\Downloads\click_effect-86995.mp3")

