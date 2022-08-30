# imported "tkinter" which is a standard GUI library which is easy and have more applications
# imported random module to randomize ron choice
# imported pillow library to insert the images and for image applications
# As messagebox itself a module we can't import directly with from tkinter import *

from tkinter import *
from random import randint
from PIL import Image, ImageTk
from Music import music, stop, play
from tkinter import messagebox


def game():
    root = Tk()  # open main window (here "root" works as an object)
    root.title('Rock Paper Scissor Lizard and Spock')
    root.config(background='azure')

    # rock,paper,scissor,lizard, spock, exit, playsound images
    rock_img = ImageTk.PhotoImage(Image.open('rock2.png'))
    paper_img = ImageTk.PhotoImage(Image.open('paper1.jpg'))
    scissor_img = ImageTk.PhotoImage(Image.open('sci2.png'))
    lizard_img = ImageTk.PhotoImage(Image.open('li1.png'))
    spock_img = ImageTk.PhotoImage(Image.open('sp1.png'))
    img_p2 = ImageTk.PhotoImage(Image.open('paper2.jpg'))
    img_r2 = ImageTk.PhotoImage(Image.open('rock1.png'))
    img_s2 = ImageTk.PhotoImage(Image.open('sci1.png'))
    img_l2 = ImageTk.PhotoImage(Image.open('li2.png'))
    img_sp2 = ImageTk.PhotoImage(Image.open('sp1.png'))
    exit_img = ImageTk.PhotoImage(Image.open('exit.jpg'))
    play_img = ImageTk.PhotoImage(Image.open('play.jpg'))
    stop_img = ImageTk.PhotoImage(Image.open('music_stop.jpg'))
    reset_img = ImageTk.PhotoImage(Image.open('reset.jpg'))

    label_ron = Label(root, image=rock_img)  # Giving rock images as default
    label_player = Label(root, image=img_r2)
    label_ron.grid(row=5, column=0)
    label_player.grid(row=5, column=6)
    label_exit = Label(root, image=exit_img)  # with Label() function we specify that where the image should be placed
    label_exit.configure(image=exit_img)
    label_play = Label(root, image=play_img)
    label_play.configure(image=play_img)
    label_splay = Label(root, image=stop_img)
    label_splay.configure(image=stop_img)
    label_reset = Label(root, image=reset_img)
    label_reset.configure(image=reset_img)

    # scoring
    ron_score = Label(text=0, font=('arial', 40, 'bold'), fg='black', bg='azure')
    player_score = Label(text=0, font=('arial', 40, 'bold'), fg='black', bg='azure')
    ron_score.grid(row=5, column=1)
    player_score.grid(row=5, column=5)

    # players indicator
    ronald_indicator = Label(root, font=('arial', 40, 'bold'), text="Ronald", fg='black', bg='azure')
    player_indicator = Label(root, font=('arial', 40, 'bold'), text="Player", fg='black', bg='azure')
    ronald_indicator.grid(row=3, column=1)
    player_indicator.grid(row=3, column=5)

    f_msg = Label(font=('arial', 30, 'bold'), fg='black', bg='azure')  # message that displays who won the game
    f_msg.grid(row=5, column=3)

    to_select = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']  # ronald choices

    def msg_up(x):  # winning  message
        f_msg['text'] = x

    def ron_up():  # update ronald score
        score = int(ron_score['text'])
        score += 1
        ron_score['text'] = str(score)

    def player_up():  # update player score
        score = int(player_score['text'])
        score += 1
        player_score['text'] = str(score)

    def back():  # to quit the game
        exit()

    def winner_check(player, ron):  # Conditions to check the winner
        if (player == 'Rock' and ron == 'Rock') or (player == 'Paper' and ron == 'Paper') or (
                player == 'Scissors' and ron == 'Scissors') or (player == 'Lizard' and ron == 'Lizard') or (
                player == 'Spock' and ron == 'Spock'):
            msg_up("It's a Tie!!")
        elif (player == 'Rock' and ron == 'Paper') or (player == 'Rock' and ron == 'Spock') or (
                player == 'Paper' and ron == 'Scissors') or (player == 'Paper' and ron == 'Lizard') or (
                player == 'Scissors' and ron == 'Rock') or (player == 'Scissors' and ron == 'Spock') or (
                player == 'Lizard' and ron == 'Scissors') or (player == 'Lizard' and ron == 'Rock') or (
                player == 'Spock' and ron == 'Lizard') or (player == 'Spock' and ron == 'Paper'):
            msg_up('Ron win !!!')
            ron_up()
        else:
            msg_up('You Win!!!')
            player_up()

    def up_choice(a):
        ron_choice = to_select[randint(0, 4)]  # randomized ron choice
        if ron_choice == 'Rock':  # images for computer
            label_ron.configure(image=rock_img)
        elif ron_choice == 'Paper':
            label_ron.configure(image=paper_img)
        elif ron_choice == 'Scissors':
            label_ron.configure(image=scissor_img)
        elif ron_choice == 'Lizard':
            label_ron.configure(image=lizard_img)
        else:
            label_ron.configure(image=spock_img)

        if a == 'Rock':  # images for user
            label_player.configure(image=img_r2)
        elif a == 'Paper':
            label_player.configure(image=img_p2)
        elif a == 'Scissors':
            label_player.configure(image=img_s2)
        elif a == 'Lizard':
            label_player.configure(image=img_l2)
        else:
            label_player.configure(image=img_sp2)

        winner_check(a, ron_choice)
        play()  # to play sound when user click the button

    # buttons to take the player choice
    Button(root, width=8, height=2, text='ROCK✊ ', font=('arial', 20, 'bold'), bg='SlateBlue2', fg='black',
           command=lambda: up_choice('Rock')).grid(row=10, column=1)
    Button(root, width=8, height=2, text='PAPER🖐', font=('arial', 20, 'bold'), bg='light green', fg='black',
           command=lambda: up_choice('Paper')).grid(row=10, column=3)
    Button(root, width=8, height=2, text='SCISSORS', font=('arial', 20, 'bold'), bg='yellow', fg='black',
           command=lambda: up_choice('Scissors')).grid(row=10, column=5)
    Button(root, width=8, height=2, text='LIZARD🤌', font=('arial', 20, 'bold'), bg='maroon1', fg='black',
           command=lambda: up_choice('Lizard')).grid(row=11, column=2)
    Button(root, width=8, height=2, text='SPOCK🖖', font=('arial', 20, 'bold'), bg='cyan', fg='black',
           command=lambda: up_choice('Spock')).grid(row=11, column=4)
    Button(root, width=150, height=130, image=exit_img, font=('arial', 20, 'bold'), bg='azure',
           borderwidth=0,
           command=lambda: back()).grid(row=12, column=6)
    Button(root, width=150, height=150, image=play_img, font=('arial', 20, 'bold'), bg='azure',
           borderwidth=0,
           command=lambda: music()).grid(row=11, column=0)
    Button(root, width=150, height=150, image=stop_img, font=('arial', 20, 'bold'), bg='azure',
           borderwidth=0,
           command=lambda: stop()).grid(row=12, column=0)

    run = True

    def reset():  # If user want to restart the game they can play again
        global run  # global key word allows you to use the variable outside for current scope
        answer = messagebox.askyesno('ALERT', 'YOU WANT TO PLAY AGAIN?')
        if answer is True:
            run = False
            root.destroy()  # destroy() function destroys the current window
            game()  # starts new game

    Button(root, width=150, height=150, image=reset_img, font=('arial', 20, 'bold'), bg='azure',
           borderwidth=0,
           command=lambda: reset()).grid(row=11, column=6)
    root.mainloop()


# game()
