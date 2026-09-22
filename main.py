import random


def play_game():
    game_number = random.randint(1, 10)
    guesses = 0

    while True:
        try:
            guess = int(input("Enter a number between 1 and 10: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 10:
            print("Your guess must be between 1 and 10.")
            continue

        guesses += 1
        if guess > game_number:
            print("Lower.")
        elif guess < game_number:
            print("Higher.")
        else:
            print(f"You win in {guesses} guesses!")
            return guesses


def main():
    games_played = 0
    total_guesses = 0
    best_score = None

    while True:
        guesses = play_game()
        games_played += 1
        total_guesses += guesses
        best_score = guesses if best_score is None else min(best_score, guesses)

        average = total_guesses / games_played
        print(
            f"Games: {games_played} | Current: {guesses} guesses | "
            f"Best: {best_score} | Average: {average:.1f}"
        )

        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != "y":
            print(f"Session complete: {games_played} game(s), {total_guesses} total guesses.")
            break


if __name__ == "__main__":
    main()