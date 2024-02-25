'''
Симуляция азартной стратегии Мартингейла на базе кидания монетки
'''
'''
ПО правилам стратегии если выиграл, то забираем выигрыш
и ставим заново по минимальной ставке.
Если проиграли - поднимаем ставку вдвое и играем дальше.
В теории конечный выигрыш отыграет все потери до этого.
Но это, конечно же, не так
'''
'''
Матожидание бросания монетки равна 1. Матожидание - это понятие в теории вероятностей,
означающее среднее значение случайной величины.
Чтобы получить матожидание, нужно умножить каждое значение величины на его вероятность
и сложить все произведения.
'''
import random  # Импорт модуля

HEADS = "heads"  # Задали константу для Орла
TAILS = "tails"  # и Решки
COIN_VALUES = [HEADS, TAILS]  # и запихнули переменные в список,
# чтобы можно было рандомно список смешивать


def flip_coin():  # Симуляция броска моентки
    return random.choice(COIN_VALUES)  # Ф-ция choiсe возвращает случайный элемент из списка


# Симуляция стратегии Мартингейла
def play_martingale(starting_funds: int, min_bet: int, max_bet: int) -> int:
# Ф-ция отдает кол-во шагов до банкротства (проигрыша).
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet
    while current_funds > 0:  # Пока еще есть деньги, делаем следующее:
        print("========")
        steps_to_loose += 1
        current_funds -= current_bet  # Вычитываем текущую ставку из банка
        print(f"{current_funds=}", f"{current_bet=}")
        flipped_coin_value = flip_coin()  # Бросаем монетку
        print(f"flipped_coin_value: {flipped_coin_value}")
        if flipped_coin_value == HEADS:  # Для простоты: игрок всегда ставит на HEADS
            win = current_bet * 2  # Фиксируем выигрыш
            print(f"{win=}")
            current_funds += win  # Добавляем выигрыш в банк
            current_bet = min_bet  # Ставка сбрасывается до минимальной
        else:
            print("loose")
            current_bet *= 2  # по правилу стратегии поднимает ставку в двое
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds
    return steps_to_loose


print(play_martingale(starting_funds=100, min_bet=1, max_bet=100))
# В конечном итоге игрок все равно придет к 0, количестов интераций будет разное.
# Вывод следующий: по этой стратегии ты выигрываешь по чуть-чуть,
# но потом разово все проиграваешь.

# Симуляция нескольких игроков
# Игроки будут начинать с одинаковым кол-вом средств
def simulate_martingale_for_n_games(starting_funds: int, min_bet: int, max_bet: int, n_games: int) -> float:
# Т.к. мы возвращаем среднее значение интераций, оно будет float
    total_steps_to_loose = 0
    for i in range(n_games):
        # Запускаем симулякию стратегии Мартингейла для одного игрока
        step_to_loose = play_martingale(starting_funds, min_bet, max_bet)
        # Прибавляем кол-во шагов к проигрышу одного игрока к общему кол-ву
        total_steps_to_loose += step_to_loose
    return total_steps_to_loose / n_games

# Пример удобного заполнения нескольких парамметров
print(
  simulate_martingale_for_n_games(
    starting_funds=100,
    min_bet=1,
    max_bet=100,
    n_games=10
  )
)

# В итоге будет все равно какое-то число.
# Если бы стратегия Мартенгейла работала, то кол-во итераций было бы бесконечным.