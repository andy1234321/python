import random

life = 10
length = 3

answer = random.randint(100, 999)

answer = str(answer)

while life:
    is_guessed = False
    print("=" * 10)

    print("жизней:", end="")
    for i in range(life):
        print("❤", end="")
    print()
    guess = input("предположение:")
    if len(guess) != length or not guess.isdigit():
        print("число от 100 до 999!")
        continue
    if guess == answer:
        print("победа🏆")
        is_guessed = True
        break
    if not is_guessed:
        for i in range(length):
            if guess[i] == answer[i]:
                print("Fermi😎")
                is_guessed = True
                break
    if not is_guessed:
        for char in guess:
            if char in answer:
                print("pico😉")
                is_guessed = True
                break
    if not is_guessed:
        print("bagels😭")
    life -= 1