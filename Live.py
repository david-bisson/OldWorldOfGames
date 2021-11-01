def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print('Here you can find many cool games to play.')


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    shift = 0
    while 1 > shift or 3 < shift:
        try:
            shift = int(input("Please enter your choice (1 - 3) : "))
        except ValueError:
            print
            "That wasn't an integer :("
    shift = 0
    while 1 > shift or 5 < shift:
        try:
            shift = int(input("Please choose difficulty (1 - 5) : "))
        except ValueError:
            print
            "That wasn't an integer :("

    print("Thank you for playing Squid Games")
