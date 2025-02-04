from random import *
import pickle

def gamb_game():
     
     #definig a function to play again
     
     def play_again():
              do_you = input('Want to play again? Type "yes" or "no": ').lower()
              if do_you == 'yes':
                   print('Oh shit, here we go again.')
                   print('')
                   gamb_game()
                   
              elif do_you == 'no':
                   exit()
                   
              else:
                   print('Just accept yes or no.')
                   print('')
                   play_again()

     #starter money (just the first time you play
                   
     global money
     money = float(1000)

     #reading the actual money you have from money.txt
     
     file = open('money.txt', 'rb')
     money = pickle.load(file)

     #game start

     while True:

         #spin generator
         
         print('Your money: {}'.format(money))
         sp_1 = randint(0, 9)
         sp_2 = randint(0, 9)
         sp_3 = randint(0, 9)

         #input and input check

         try:
              gamb = float(input('Enter your gamble: '))

         except ValueError:
              print('Enter just number. i.e 1000 or 1000.5')
              print('')
              gamb_game()

         if money < gamb or gamb <= 0:
              print("Enter a valid value for money or don't try to spend more than you have.")
              print('')
              gamb_game()

         #displaying money and making sure you actually spend the money

         money = money - gamb 
         print(sp_1, sp_2, sp_3) 

         #prize check

         if sp_1 == 3 and sp_2 == 9 and sp_3 == 9:
             money = money + gamb*9
             print('Once in life! Gamble x9')
             print('')
             
         elif sp_1 == 3 and sp_2 == 3 and sp_3 == 3:
             money = money + gamb*6
             print('You are really lucky! Gamble x6')
             print('')
            
         elif sp_1 == 3 and sp_2 == 3 and sp_3 == 3:
             money = money + gamb*3
             print('Good one! Gamble x3')
             print('')

         elif sp_1 == sp_2 and sp_1 == sp_3:
             money = money + gamb + gamb*(5/2)
             print('WOW! Gamble x2.5')
             print('')

         elif sp_1 == sp_2 or sp_1 == sp_3 or sp_2 == sp_3:
             money = money + gamb + gamb*(3/2)
             print('Nice! Gamble x1.5')
             print('')
            
         else:
             print('Not this time.')
             print('')

         #checking if player lost

         if money <= 0:
              money = 1000
              str(money)
              file = open('money.txt', 'wb')
              pickle.dump(money, file)
              file.close()
              print('You lost all your money')
              print('')
              play_again()

         #write your current money to money.txt

         str(money)
         file = open('money.txt', 'wb')
         pickle.dump(money, file)
         file.close()
     
gamb_game()



