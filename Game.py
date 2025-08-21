import random

def generate_secret():
    digits = list('0123456789')
    random.shuffle(digits)
    return ''.join(digits[:3])

def get_clues(secret, guess):
    clues = []
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            clues.append('fermi')  # Correct digit, correct position
        elif guess[i] in secret:
            clues.append('pico')   # Correct digit, wrong position
        else:
            clues.append('bagels') # Digit not in secret
    return clues

def is_valid_guess(guess):
    return len(guess) == 3 and guess.isdigit() and len(set(guess)) == 3

def play_game():
    print("Welcome to Fermi-Pico-Bagels!")
    print("Guess the 3-digit number. Digits are unique.")
    secret = generate_secret()
    attempts = 0

    while True:
        guess = input("Enter your guess: ")
        if not is_valid_guess(guess):
            print("❗ Invalid guess. Enter 3 unique digits.")
            continue

        attempts += 1
        clues = get_clues(secret, guess)

        print("Clues:", ' '.join(clues))

        if guess == secret:
            print(f"🎉 You guessed it in {attempts} attempts! The number was {secret}.")
            break

if __name__ == "__main__":
    play_game()
