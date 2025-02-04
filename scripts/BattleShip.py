import random

#setting all ships place

def game():
    crusier = random.randint(1, 15)
    destr_1 = random.randint(2, 14)
    destr_2 = destr_1-1 or destr_1+1

    #making sure that it does not overlap

    destr_check = crusier != destr_1 and crusier != destr_2

    if not destr_check:
        game()
        return

    #for debug
    
    print('- DEBUG - Crusier: {} Destroyer: {}, {}'.format(crusier, destr_1, destr_2))

    #keeping track of guesses

    guess_list = []
    sunk_destr = {'destr_1': False, 'destr_2': False}
    sunk_ships = {'crusier': False, 'destr_1': False, 'destr_2': False}

    #start of the loop

    while True:
        def ships():
            try:
                guess = int(input('Enter a number between 1 and 15: '))
            except ValueError:
                print('Please, enter a number.')
                return ships()

            if guess < 1 or guess > 15:
                print('Enter a number within the range.')
                return ships()

            if guess in guess_list:
                print('You already guessed that number.')
                return
            #guesses output and round count

            guess_list.append(guess)
            round_count = len(guess_list)
            print('Round {} of 7'.format(round_count))
            print('Your guesses: {}'.format(guess_list))

            #check if it hit any ship
            
            if guess == crusier:
                print('You sunk the crusier!')
                sunk_ships['crusier'] = True
            elif guess == destr_1:
                print('You hit the first part of the destroyer!')
                sunk_destr['destr_1'] = True
                sunk_ships['destr_1'] = True
            elif guess == destr_2:
                print('You hit the second part of the destroyer!')
                sunk_destr['destr_2'] = True
                sunk_ships['destr_2'] = True
            else:
                print('You missed!')

            #checking if the crusier and all ships have been sunk

            if all(sunk_ships.values()):
                print('Congragulations, you won!')
                play_again()

            if all(sunk_destr.values()):
                print('You sunk the destroyer')
                return ships()

            #finish the game on the seventh round

            if round_count == 7:
                print('You lost!')
                play_again()
        ships()
        
        def play_again():
                again = input('Enter "yes" to play again or "no" to exit: ').lower()
                if again == 'yes':
                    game()
                elif again == 'no':
                    print('Thanks for playing!')
                    exit()
                else:
                    print('Enter "yes" or "no"')
                    play_again()
game()
