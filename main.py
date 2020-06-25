import turtle#importing turtle module


class TrueTell:#creating a class
    def __init__(_self):
        print("creating the class instance")
       

    # The starting print in the turtle terminal.
    @staticmethod #static method can neither modify object state nor class state.
    def t_start():
        turtle.title("Guess The Word Game")
        ts = turtle.Turtle()
        ts.hideturtle()
        ts.speed(0)
        turtle.bgcolor('yellow')
        ts.penup()
        ts.goto(-300, 220)
        ts.pendown()
        ts.color('blue')
        ts.begin_fill()
        ts.write('Guess the word', font=("Arial", 20, "bold"))
        ts.end_fill()

        ts.penup()
        ts.goto(0, -250)
        ts.hideturtle()
        ts.pendown()
        ts.color('Red')
        ts.begin_fill()
        ts.write('You  have  ' + str(8) + '  attempts  left', align='center', font=("Arial", 12, "bold"))
        ts.end_fill()

    # If Correct entry is made the changes in the turtle terminal.
    @staticmethod
    def turtle_c(msg):
        tc = turtle.Turtle()
        tc.hideturtle()
        tc.speed(0)

        tc.penup()
        tc.goto(-300, 180)
        tc.color('yellow')
        tc.begin_fill()
        tc.forward(30 * len(msg))
        tc.left(90)
        tc.forward(40)
        tc.left(90)
        tc.forward(30 * len(msg))
        tc.left(90)
        tc.forward(40)
        tc.end_fill()

        tc.goto(-290, 180)
        tc.pendown()
        tc.color('blue')
        tc.begin_fill()
        tc.write(''.join(msg), font=("Arial", 20, "bold"))
        tc.end_fill()

    # When the first wrong happens print the following.
    @staticmethod
    def first_w(guess):
        fw = turtle.Turtle()
        fw.hideturtle()
        fw.speed(0)
        fw.penup()
        fw.goto(-300, -180)
        fw.pendown()
        fw.color('green')
        fw.begin_fill()
        fw.write('Wrong Guesses:', font=("Arial", 20, "bold"))
        fw.end_fill()

    #This draws individual parts of ambulance for every mistake
    @staticmethod
   
    def t_wrong(guess, miss_num):
        turtle.hideturtle()
        tw = turtle.Turtle()
        tw.hideturtle()
        tw.speed(0)
        tw.penup()
 
        if miss_num == 1:
            tw.goto(-150, 60)
            tw.pensize(3)
            tw.color('blue', 'white')
            tw.pendown()
            tw.begin_fill()
            for i in range(2):
                tw.forward(200)
                tw.right(90)
                tw.forward(150)
                tw.right(90)
            tw.end_fill()

        elif miss_num == 2:
            tw.goto(50, 10)
            tw.pensize(3)
            tw.color('blue', 'white')
            tw.pendown()
            tw.begin_fill()
            for i in range(2):
                tw.forward(100)
                tw.right(90)
                tw.forward(100)
                tw.right(90)
            tw.end_fill()
      
        elif miss_num == 3:
            tw.goto(-80, -130)
            tw.color('blue')
            tw.pendown()
            tw.begin_fill()
            tw.circle(40)
            tw.end_fill()

        elif miss_num == 4:
            tw.goto(80, -130)
            tw.color('blue')
            tw.pendown()
            tw.begin_fill()
            tw.circle(40)
            tw.end_fill()

        elif miss_num == 5:
            tw.goto(60, 0)
            tw.pensize(3)
            tw.color('blue', 'white')
            tw.pendown()
            tw.begin_fill()
            for i in range(2):
                tw.forward(70)
                tw.right(90)
                tw.forward(30)
                tw.right(90)
            tw.end_fill()

        elif miss_num == 6:
            tw.goto(-60, 70)
            tw.pensize(3)
            tw.color('blue', 'red')
            tw.pendown()
            tw.begin_fill()
            for i in range(2):
                tw.forward(20)
                tw.right(90)
                tw.forward(10)
                tw.right(90)
            tw.end_fill()

        elif miss_num == 7:
            tw.goto(-78,27)
            tw.color('red', 'red')
            tw.pendown()
            tw.begin_fill()
            for i in range(2):
                tw.forward(60)
                tw.right(90)
                tw.forward(30)
                tw.right(90)
            tw.end_fill()

        elif miss_num == 8:
            tw.goto(-64, 40)
            tw.color('red', 'red')
            tw.pendown()
            tw.begin_fill()
            for i in range(2):
                tw.forward(30)
                tw.right(90)
                tw.forward(60)
                tw.right(90)
            tw.end_fill()

        tw.penup()
        tw.goto(-250 + (miss_num - 1) * 30, -220)
        tw.hideturtle()
        tw.pendown()
        tw.color('green')
        tw.begin_fill()
        tw.write(guess + ' ', font=("Arial", 20, "bold"))
        tw.end_fill()

        tw.penup()
        tw.goto(-300, -250)
        tw.color('yellow')
        tw.begin_fill()
        tw.forward(600)
        tw.left(90)
        tw.forward(30)
        tw.left(90)
        tw.forward(600)
        tw.left(90)
        tw.forward(30)
        tw.end_fill()

        tw.penup()
        tw.goto(0, -250)
        tw.hideturtle()
        tw.pendown()
        tw.color('red')
        tw.begin_fill()
        tw.write('You  have  ' + str(8 - miss_num) + '  attempts  left', align='center', font=("Arial", 12, "bold"))
        tw.end_fill()

    # The print Function when a player wins or loses.
    @staticmethod
    def win_l(result):
        wl = turtle.Turtle()
        wl.hideturtle()
        wl.speed(0)
        wl.penup()
        wl.goto(0, 110)
        wl.pendown()
        wl.color('black')
        wl.begin_fill()
        if result == 1:
            wl.write('YOU WIN!', align='center', font=("Arial", 40, "bold"))
        elif result == 0:
            wl.write('YOU LOSE!', align='center', font=("Arial", 40, "bold"))
        wl.end_fill()


          
#This is the main function of the program and prints the basic information of the game            
def main():
    true_tell_obj = TrueTell()
    

    true_tell_obj.t_start()
    print('\n' * 30)
    print("-----------------------WELCOME TO WORD GUESSING GAME------------------------------")#welcome msg
    print("\n--This is a Two player game , Make sure You enter player information Correctly--")
    print("\n--------------------------Enter Player Information------------------------------")#player information
    player1 = input("\nEnter 1st player name : ")
    player2 = input("\nEnter 2nd player name : ")
    print('\n' * 30)
    print("---------- "+player1+"----------")
   
    print("\n("+player1+" Make sure "+ player2+" is not peeking.)")
    print("\n(Apply Rules for Your Friend)")
    print()
    word = input("Enter your word (If the word contains a space, use '-'. eg:- 'ice-cream' ) : ")
    letters = [i.lower() for i in word]#player 1 enters the word

    print("\nYour word has been entered.\nGive the system to Player2 to start the Game.")

    print("\n" * 30)
    print("---------- "+player2+ "----------")#player 2 game begins
    print("\n(These are some basic rules)")
    print("\n~Dont repeat the same letters and dont try to act smart")
    print("\n~Dont leave Empty")

    result = 0  # 0 for no result , 1 for win/lose
    miss_num = 0  # misses by the palyer
    entered = []  # contains all the entered letters
    msg = []  # it contains the letters of correct guesses
    flg = 0

    # making msg in form of '* * * ' i.e before player guesses the word.
    for letter in letters:
        msg.append('  ') if letter == '-' else msg.append('* ')

    # Printing '* * * ' for the given word
    true_tell_obj.turtle_c(msg)

    while miss_num < 8 and not result:  # 8 chances or win
        guess = input("\nGuess a letter : ")

        if len(guess) > 1:#if u enter too many letters it appears
            print("\nwhere is your Brain roaming,You entered too many letters, Look at your keyboard.")
            continue
        try:
            guess = guess.lower()
            if not guess.isalpha():#if u enter anything else except letters it appears
                print('\nYou need to enter a letter not something else ')
                continue
        except Exception as e:
            print('You need to enter a letter not something else ')
            continue

        if guess in entered:#this makes u to not enter same letter again and again
            print("\nI already mentioned you the rule "+player2+",Dont act too Smart.")
            continue
        else:
            entered.append(guess)

        if guess in letters:
            for i in range(len(letters)):
                if letters[i] == guess:
                    msg[i] = guess + ' '

            true_tell_obj.turtle_c(msg)
            if '* ' not in msg:
                true_tell_obj.win_l(1)
                result = 1
        else:
            miss_num += 1
            if flg == 0:
                true_tell_obj.first_w(guess)
            flg = 1
            true_tell_obj.t_wrong(guess, miss_num)
            if miss_num >= 8:
                true_tell_obj.win_l(0)
                result = 1
    if result:
        input('\nPress any key to restart the game.')#this makes you to restart the game
        turtle.clearscreen()
        main()

    turtle.mainloop()


if __name__ == "__main__":
    main()
