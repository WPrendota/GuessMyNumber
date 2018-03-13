
print("Please think of a number between 0 and 100!")

first_number = 50

print("Is your secret number "+str(first_number)+"?")

try:
    inputt = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
except:
    print("Error")

lower = 0
higher = 100
guess = first_number

while inputt != 'c':
    if inputt == 'l':
        lower = guess
        guess = int((higher+lower)/2)
    elif inputt == 'h':
        higher = guess
        guess = int((higher+lower)/2)
    print("Is your secret number "+str(guess)+"?")

    inputt = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if inputt != 'h' and inputt != 'l' and inputt != 'c':
        print("another input!")

print("Game over. Your secret number was: " + str(guess))