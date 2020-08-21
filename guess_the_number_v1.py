from random import randint


def guess_the_number():
    """Get number from user and analyze if it matches a random number in the range 1 - 100."""
    rnd = randint(1, 100)

    while True:
        num = input('Guess the number: ')
        try:
            num = float(num)
        except ValueError:
            print("It's not a number!")
        else:
            if num < rnd:
                print('To small!')
                continue
            elif num > rnd:
                print('To big!')
                continue
            else:
                print('You win!')
                break


if __name__ == '__main__':
    guess_the_number()
