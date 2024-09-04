def check_guess(lucky_number: int, user_guess: str) -> str:
    try:
        guess = int(user_guess)
    except ValueError:
        raise ValueError("Input must be a number")

    if guess < 1 or guess > 100:
        raise ValueError("Number out of range")

    if guess == lucky_number:
        return "BINGO"
    elif guess < lucky_number:
        return "guess higher"
    else:
        return "guess lower"


def play_guessing_game():
    import random
    lucky_number = random.randint(1, 100)

    while True:
        try:
            user_guess = input("Guess a number between 1-100: ")
            feedback = check_guess(lucky_number, user_guess)
            print(feedback)
            if feedback == "BINGO":
                break
        except Exception as ex:
            print(ex)
