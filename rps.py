import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Well = 3
    Fire = 4
    
translator = {
    0: 'камень',
    1: 'бумага',
    2: 'ножницы',
    3: 'колодец',
    4: 'огонь'
}

def get_user_selection():
    user_input = input("\nСделайте выбор — (камень[0], бумага[1], ножницы[2], колодец[3], огонь[4]): ")
    selection = int(user_input)
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    score = 0
    if user_action == computer_action:
        print(f"Оба пользователя выбрали {translator[user_action]}. Ничья!")
        score += 3
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Камень бьет ножницы! Вы победили!")
            score += 2
        elif computer_action == Action.Fire:
            print("Камень гасит огонь! Вы победили!")
            score += 2
        elif computer_action == Action.Well:
            print("Камень тонет в колодце! Вы проиграли.")
            score += 1
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
            score += 1
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Бумага оборачивает камень! Вы победили!")
            score += 2
        elif computer_action == Action.Well:
            print("Бумага накрывает колодец! Вы победили!")
            score += 2
        elif computer_action == Action.Fire:
            print("Бумага горит в огне! Вы проиграли!")
            score += 1
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
            score += 1
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Ножницы режут бумагу! Вы победили!")
            score += 2
        elif computer_action == Action.Well:
            print("Ножницы режут колодезную верёвку! Вы победили!")
            score += 2
        elif computer_action == Action.Fire:
            print("Ножницы плавятся в огне! Вы проиграли!")
            score += 1
        else:
            print("Камень бьет ножницы! Вы проиграли.")
            score += 1
    elif user_action == Action.Well:
        if computer_action == Action.Rock:
            print("Колодец топит камень! Вы победили!")
            score += 2
        elif computer_action == Action.Fire:
            print("Колодец гасит огонь! Вы победили!")
            score += 2
        elif computer_action == Action.Paper:
            print("Бумага накрывает колодец! Вы проиграли!")
            score += 1
        else:
            print("Ножницы режут колодезную верёвку! Вы проиграли!")
            score += 1
    elif user_action == Action.Fire:
        if computer_action == Action.Rock:
            print("Огонь тушится камнем! Вы проиграли!")
            score += 1
        elif computer_action == Action.Well:
            print("Огонь тушится в колодце! Вы проиграли!")
            score += 1
        elif computer_action == Action.Paper:
            print("Огонь сжигает бумагу! Вы победили!")
            score += 2
        else:
            print("Ножницы плавятся в огне! Вы победили!")
            score += 2
    return score

print("Привет! Ты активировал игру «Камень, ножницы, бумага, колодец и огонь».\n")

while True:
    try:
        number_of_games = int(input("Укажи, сколько игр ты хочешь сыграть: "))
    except ValueError as e:
        print(f"Некорректный ввод. Введите числовое значение.")
        continue

    user_score, computer_score, tied_score = 0, 0, 0

    while number_of_games > 0:
        try:
            user_action = get_user_selection()
        except ValueError as e:
            range_str = f"[0, {len(Action) - 1}]"
            print(f"Некорректный ввод. Введите значение из промежутка {range_str}.")
            continue

        computer_action = get_computer_selection()
        result_game = determine_winner(user_action, computer_action)

        if result_game == 1:
            computer_score += 1
        elif result_game == 2:
            user_score += 1
        elif result_game == 3:
            tied_score += 1

        number_of_games -= 1

    print(f"\nВаш счет: {user_score} | Счёт противника: {computer_score} | Ничья: {tied_score}")

    if user_score == computer_score:
        print("По итогам всех игр - ничья!\n")
    elif user_score > computer_score:
        print("По итогам всех игр, вы одерживаете победу! :)\n")
    else:
        print("Увы, но по итогам всех игр, побеждает компьютер.\n ")

    play_again = input("Сыграем еще? (да/нет): ")
    if play_again.lower() != "да":
        print("Спасибо за проведенное время! Пока!")
        break