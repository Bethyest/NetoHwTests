# Задание 1
def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    # Ваш алгоритм
    return(b ** 2 - 4 * a * c)

def solution(a, b, c):

    if discriminant(a, b, c) < 0:
        return 'корней нет'
    elif discriminant(a, b, c) == 0:
        return ((-b) / (2 * a))
    elif discriminant(a, b, c) > 0:
        return (((-b) + (discriminant(a, b, c))**0.5) / (2 * a), ((-b) - (discriminant(a, b, c))**0.5) / (2 * a))

# Задание 2
def solve(boys: list, girls: list):
    result = ""  # в эту строку сохраните полученные пары или сообщение "Кто-то может остаться без пары!"

    if len(boys) == len(girls):  # проверьте, что длины списков одинаковы
        for boy, girl in zip(sorted(boys),
                             sorted(girls)):  # отсортируйте пары, объедините при помощи zip и распакуйте в цикле
            if len(result) > 0:
                result += ', '
            result += (f'{boy} и {girl}')
    else:
        result = 'Кто-то может остаться без пары!'
    return result

# Задание 3
def disc_counter(models: list, available: list, manufacturers: list):
    repair_count = 0 # количество дисков, которые купит сисадмин
    ssds = [] # модели дисков из списка models, которые купит сисадмин
    # код вашего решения ниже:
    for model, avail in zip(models, available):
        if avail:
            for manufacture in manufacturers:
                if manufacture in model:
                      ssds.append(model)
                      repair_count += 1
                      break
    return ssds, repair_count # Этот код менять не нужно

if __name__ == '__main__':

    print(discriminant(1, 8, 15))
    print(discriminant(1, -13, 12))
    print(discriminant(-4, 28, -49))
    print(discriminant(1, 1, 1), '[')

    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1), '[')

    # Этот код менять не нужно
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    result = solve(boys, girls)
    assert result == "Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    boys = ['Peter', 'Alex', 'John', 'Arthur']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    result = solve(boys, girls)
    assert result == "Кто-то может остаться без пары!", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma']
    result = solve(boys, girls)
    assert result == "Кто-то может остаться без пары!", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    # Этот код менять не нужно
    models = ['480 ГБ 2.5" SATA накопитель Kingston A400', '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
              '480 ГБ 2.5" SATA накопитель ADATA SU650', '240 ГБ 2.5" SATA накопитель ADATA SU650',
              '250 ГБ 2.5" SATA накопитель Samsung 870 EVO', '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER',
              '480 ГБ 2.5" SATA накопитель WD Green', '500 ГБ 2.5" SATA накопитель WD Red SA500']
    available = [1, 1, 1, 1, 0, 1, 1, 0]
    manufacturers = ['Intel', 'Samsung', 'WD']

    result = disc_counter(models, available, manufacturers)
    assert result == (['500 ГБ 2.5" SATA накопитель Samsung 870 EVO', '480 ГБ 2.5" SATA накопитель WD Green'], 2), \
        f"Неверный результат: {result}"
    print(f"Сисадмин Василий сможет купить диски: {result[0]} и починить {result[1]} компьютера")
