import random
import re


# Список слов для угадывания
words = [
    "apple", "banana", "cherry", "dragonfruit", "elephant",
    "guitar", "hospital", "internet", "jungle", "kangaroo"
]

def play_game():
    secret_word = random.choice(words)
    attempts = 0
    max_attempts = 6  # Максимум попыток


    print("\033[1;36m╔══════════════════════════════════╗\033[0m")
    print("\033[1;36m║   УГАДАЙ СЛОВО (на английском)    ║\033[0m")
    print("\033[1;36m╚══════════════════════════════════╝\033[0m")
    print(f"\033[0;34mЯ загадал слово из {len(secret_word)} букв. У вас {max_attempts} попыток!\033[0m")


    while attempts < max_attempts:
        print(f"\n\033[1;33mПопытка {attempts + 1}/{max_attempts}:\033[0m")
        user_guess = input("  Ваше слово: ").strip().lower()

        # Проверка ввода: только буквы, не пустое
        if not user_guess.isalpha():
            print("\033[1;31m❌ Введите только буквы (без цифр и символов)!\033[0m")
            continue
        if len(user_guess) == 0:
            print("\033[1;31m❌ Поле не может быть пустым!\033[0m")
            continue

        attempts += 1

        # Угадал?
        if user_guess == secret_word:
            print(f"\033[1;32m🎉 ПОЗДРАВЛЯЕМ! Вы угадали: «{secret_word}»!\033[0m")
            print(f"\033[0;32mВы потратили {attempts} попытку(и).\033[0m")
            return

        # Подсказки (если не угадал)
        print("\033[0;35m┌ Подсказки:\033[0m")

        # 1. Длина
        print(f!│ Ваше слово: {len(user_guess)} букв; загаданное: {len(secret_word)} букв")


        # 2. Совпадения по позициям
        correct_positions = 0
        for i in range(min(len(user_guess), len(secret_word))):
            if user_guess[i] == secret_word[i]:
                correct_positions += 1
        print(f!│ Совпадает {correct_positions} букв на правильных позициях")


        # 3. Общие буквы (без учёта позиции)
        common_letters = set(user_guess) & set(secret_word)
        if common_letters:
            print(f!│ Общие буквы: {sorted(common_letters)} (всего {len(common_letters)})")
        else:
            print("│ Общих букв нет")


        print("\033[0;35m└──────────────────────────────┘\033[0m")

    # Проигрыш
    print(f"\033[1;31m💥 Увы! Вы не угадали. Загаданное слово: «{secret_word}».\033[0m")


# Запуск игры
if __name__ == "__main__":
    play_game()
    # Предложение сыграть ещё
    while True:
        play_again = input("\nХотите сыграть ещё? (да/нет): ").strip().lower()
        if play_again in ["да", "y", "yes"]:
            play_game()
        elif play_again in ["нет", "n", "no"]:
            print("\033[0;34mСпасибо за игру! До встречи!\033[0m")
            break
        else:
            print("\033[1;31mВведите «да» или «нет».\033[0m")
