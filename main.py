"""Overview: Rock Paper Scissor Lizard and Spock is the variation of Rock Paper Scissors made popular by the television
 show The Big Bang Theory.
 Hint:You might not understand the relation between spock and paper here spock means a scientist and the paper which is
 discovered by this scientist, So paper can disprove spock."""


from tkinter import *
from Rules import rules


def game():
    root = Tk()  # open main window (here "root" works as an object)
    root.title('Let\'s play')
    root.config(background='azure')
    root.resizable(False, False)

    bg = PhotoImage(file='Background.png')
    rule = PhotoImage(file='rules.png')
    bg_label = Label(root, image=bg)
    bg_label.grid(row=5, column=4)

    def reset():  # Function to play again
        root.destroy()  # destroy() function destroys the current window
        rules()  # starts new game

    Button(root, width=200, height=200, image=rule, font=('arial', 25, 'italic bold'), bg='azure',
           borderwidth=0, command=lambda: reset()).grid(row=5, column=112)

    root.mainloop()


game()
