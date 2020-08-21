def user_answer():
    """Returns the appropriate user answer.

    :rtype: str
    :return: one of the three answers: 'to big', 'to small' or 'you win'
    """
    while True:
        input_answer = input('Enter: "To big", "To small", or "You win": ').lower().strip()
        if input_answer not in ['to big', 'to small', 'you win']:
            print('Please enter exactly one of the three answers below, try again')
            continue
        return input_answer


def guess_the_number():
    """Main function of the program."""
    input("Think a number from 0 to 1000 and I'll guess it in max 10 tries\nPress enter to start")
    min_ = 0
    max_ = 1000
    answer = None
    while answer != 'you win':
        guess = int((max_ - min_) / 2) + min_
        print("I'm guessing:", guess)
        answer = user_answer()
        if answer == "to big":
            max_ = guess
        elif answer == "to small":
            min_ = guess
    print("Hooray I won!!")


if __name__ == '__main__':
    guess_the_number()
