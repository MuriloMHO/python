import random

def my_game():
    number = random.randint(1,10)
    while True:
        print("Let's play a game")
        choice = int(input('Enter a number between 1 and 10: '))
        if choice>10 or choice<1:
            print('Enter a number in the correct range.')
            my_game()
            
        elif choice == number:
            while True:
                    print('You won, conragulations!')
                    again = int(input('Enter 1 to play again or 2 to finish: '))
                    if again == 1:
                        print('Here we go again.')
                        my_game()
                    elif again == 2:
                        print('Thank you for playing.')
                        return
                    else:
                        print('Please, choose 1 to play again or 2 to finish.')
                        continue
                    
        elif choice == number-1 or choice == number+1:
            print('You almost got it, try again.')
            continue
        
        else:
            print('Try again.')
            continue
        
my_game()
