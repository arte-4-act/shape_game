import random

def generate_secret_code(shape_list):
    secret_code = []
    for i in range(4):
        secret_code.append(random.choice(shape_list))
    return secret_code

def choose_difficulty():
    while True:
        print("Choose difficulty (easy/hard): ")
        difficulty_input = (input()).lower()
        lower_difficulty_input = difficulty_input.lower()
        if lower_difficulty_input in ["easy", "hard"]:
            return lower_difficulty_input
        else:
            print("Invalid difficulty. Please choose easy or hard.")

def get_user_guess():
    guess_input = (input("Enter your guess: ")).lower()
    guess = guess_input.split()
    return guess

def evaluate_guess(guess, secret_code):
    guess_eval = guess.copy()
    secret_code_eval = secret_code.copy()
    correct_pos = 0
    wrong_pos = 0
    i = -3
    while i  <= 0:
        if guess_eval[i] == secret_code_eval[i] or guess_eval[i][0] == secret_code_eval[i][0]:
            correct_pos += 1
            guess_eval.pop(i)
            secret_code_eval.pop(i)
            i += 1
        else:
            i += 1

    k = 0
    for item in guess_eval:
        j = 0
        for item2 in secret_code_eval:
            if guess_eval[k] == secret_code_eval[j] or guess_eval[k][0] == secret_code_eval[j][0]:
                wrong_pos += 1
                break
            j += 1
        k += 1

    print("Correct position: ", correct_pos, "| Wrong position: ", wrong_pos)
    return correct_pos

def win_check(correct_pos, guess_count, difficulty, secret_code, user_guess):
    if correct_pos == 4:
        print("You cracked the code!")
        print_game_summary(guess_count, secret_code, user_guess, "WON")
        restart()
    elif guess_count == 10 and difficulty == "hard":
        print("You've reached the maximum number of attempts.")
        print_game_summary(guess_count, secret_code, user_guess, "LOST")
        restart()

def print_game_summary(guess_count, secret_code, user_guess, game_result):
    label_width = 20
    length_secret = ' '.join(secret_code)
    length_guess = ' '.join(user_guess)
    max_width = max(len(length_secret), len(length_guess))
    summary_width = label_width + 2 + max_width  # 2 for ": "
    print()
    print("-" * summary_width)
    print("Game Result Summary".center(summary_width))
    print("-" * summary_width)
    print(f"{'Secret Code':<{label_width}}: {length_secret}")
    print(f"{'Final Guess':<{label_width}}: {length_guess}")
    print(f"{'Total Attempts':<{label_width}}: {guess_count}")
    print(f"{'Game Status':<{label_width}}: {game_result.upper()}")
    print("-" * summary_width)


def restart():
    print("Do you want to play again? (yes/no): ")
    restart_input = (input()).lower()
    lower_restart_input = restart_input.lower()
    if lower_restart_input == "yes":
        main()
    elif lower_restart_input == "no":
        exit()
    else:
        print("Invalid input. Please enter yes or no.")
        restart()

def main():
    print("Welcome to Master Mind – Shape Edition!")
    shape_list = ["circle", "diamond", "heart", "oval", "pentagon", "star", "triangle"]
    secret_code = generate_secret_code(shape_list)
    guess_count = 0
    print("Possible shapes: ", shape_list)
    difficulty = choose_difficulty()
    if difficulty == "easy":
        while True:
            guess_count += 1
            user_guess = get_user_guess()
            correct_pos = evaluate_guess(user_guess, secret_code)
            win_check(correct_pos, guess_count, difficulty, secret_code, user_guess)
    elif difficulty == "hard":
        while guess_count <= 10:
            guess_count += 1
            user_guess = get_user_guess()
            correct_pos = evaluate_guess(user_guess, secret_code)
            win_check(correct_pos, guess_count, difficulty, secret_code, user_guess)

main()