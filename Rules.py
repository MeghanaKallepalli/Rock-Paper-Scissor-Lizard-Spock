from tkinter import *
from game import game
from tkinter import messagebox


def rules():
    root = Tk()  # open main window (here "root" works as an object)
    root.title('Rock Paper Scissor Lizard and Spock')
    root.resizable(False, False)
    root.config(background='black')
    bg = PhotoImage(file='play.png')

    label_instructions = Label(root, text='Rules/Simple way to win the game...\n    ->Spock smashes Scissors\n'
                                        '->Scissor cuts Paper\n->Paper covers Rock\n->Rock crushes Lizard\n'
                                        '->Lizard poisons Spock\n->Scissor decapitates Lizard\n->Rock crushes Scissor\n'
                                        '->Spock vaporizes Rock\n->Lizard eats Paper\n->Paper disproves Spock',
                               font=('arial', 20, 'bold'), fg='gold', bg='black')
    label_instructions.grid(row=5, column=0)
    run = True

    def reset():  # If user want to restart the game they can play again
        global run  # global key word allows you to use the variable outside for current scope
        answer = messagebox.askyesno('ALERT', 'LET\'S START THE GAME')
        if answer is True:
            run = False
            root.destroy()  # destroy() function destroys the current window
            game()  # starts new game

    Button(root, width=150, height=150, image=bg, font=('arial', 20, 'bold'), bg='black',
           borderwidth=0, command=lambda: reset()).grid(row=5, column=6)

    root.mainloop()


# rules()



