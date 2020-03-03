import random

num_to_guess = str(random.randint(1000,10000))
print('Number:' + num_to_guess)

user_guess= input('Enter your first guess: ')
#print('first guess: ' + user_guess)
while len(user_guess) != 4:
    user_guess = input('Try again. Please enter a 4 digit number: ')
    #print('another guess: ' + user_guess)

cow = 0
bull = 0

def compare_numbers(user_guess, num_to_guess):
    for i in range(0,3):
        for x in range(0,3):
            if user_guess[i] == num_to_guess[x] and i == x:
                global bull
                bull += 1
            if user_guess[i] == num_to_guess[x] and i != x:
                global cow
                cow += 1

compare_numbers(user_guess, num_to_guess)

if bull != 4:
    if cow == 0 and bull == 0:
        print('None of those numbers are correct.')
        user_guess = input('Guess again: ')
    elif cow == 1 or bull == 1:
        print(str(cow) + ' Cow ' + ', ' + str(bull) + ' Bull')
        user_guess = input('Keep guessing: ')
    elif cow > 1 and bull > 1:
        print(str(cow) + ' Cows ' + ', ' + str(bull) + ' Bulls')
        user_guess = input('Keep guessing: ')
else:
    print('You got it! The number was: ' + str(num_to_guess) + '.')

#print(cow + 'Cow(s)')
#print(bull + 'Bull(s)')
