"""
Общий смысл такой - по факту делим весь входной
список на кусочки от ноля до ноля.
Т.е. на такие, как 0 3 8 34 или 0 9 2 0.
Как создать под них симметричную последовательность [0 1 2 1 0]
мы умеем -  с помощью твоего метода,
который я доработал и засунул
в функцию make_simetric.

Проблема заключалась в хвостах:
например у списка [11, 21, 0, 2, 3, 0, 6, 8]
хвостами я называю числа от:
- начала и до первого 0 (в нашем случае 11, 21)
- от последнего 0 до конца списка (в нашем случае 6, 8).
Для них есть отдельные условия.

В общем же случае я сначала определяю,
начинается ли входная последовательность с 0,
тк от этого зависит значение переменной
start_not_zero (в переводе начинается не с нуля).
Если начальная последовательность начинает не 0,
то start_not_zero=True.
"""


def make_simetric(n):
    """ Получаем число n и делаем симметричный список.
        Например, дают нам число 6 и мы делаем список
        1 2 3 3 2 1.
    """
    mass = list(range(1, n + 1))
    reversed_mass = list(reversed(mass))
    result = []
    for x in range(len(mass)):
        if mass[x] <= reversed_mass[x]:
            result.append(mass[x])
        else:
            result.append(reversed_mass[x])
    return result


# Входные данные
n = int(input())
numbers = list(map(int, input().split()))

# Переменная, по который мы отслеживаем, является ли
# первая цифра во входной последовательности нулем.
# [ 7 , 3 ,0 , ....]
start_not_zero = False
if numbers[0] != 0:
    start_not_zero = True

# Результирующий список
result = []
# Счетчик того, сколько раз были цифры до следующего 0
# (Спойлер: 0 может уже и не встретиться)
# Важно, что он начинается с 1
count = 1
# Буферный список, в который записываются значения счетчика count.
# Потом, когда встречается ноль, длина списка передается в
# функцию make_simetric и она формирует симметричную последовательность цифр
# simetric_mass, которую мы присоединяем к результирующему списку result
# ВАЖНЫЙ МОМЕНТ - если 0 так и не встретился, а в buffer уже что-то есть,
# то надо не забыть его присоединить к результату (делаем это после цикла)
buffer = []

# Основной цикл, в котором проходимся по входным числам
for x in numbers:
    # Проверяем, что очередная цифра не 0, тогда прибавляем счетчик
    # в буфер и увеличиваем счетчик на 1 (поэтому счетчик начинается с 1!!!)
    if x != 0:
        buffer.append(count)
        count += 1

    # Условие, которое срабатывает, когда мы встретили 0
    # и ОДНОВРЕМЕННО проверяем, что список начинался не с 0,
    # то есть перед этим были какие-то цифры
    # [ 9, 8, 2, 0 ....] - 9 8 2 - те самые цифры, которые шли перед 0
    # поэтому нам надо наш буфер, в котором на данный момент [1, 2, 3]
    # реверснуть и превратить в [3, 2 , 1], после не забыв прибавить 0
    elif x == 0 and start_not_zero:
        # Сразу делаем фолс чтобы больше условие не сработало,
        # ведь цифры идущие перед первым 0, встретились только один раз
        start_not_zero = False
        # Реверсим буфер, добавляем в финальный список, добавляем попавшийся 0,
        # и обнуляем буфер и счетчик
        buffer = reversed(buffer)
        result.extend(buffer)
        result.append(0)
        buffer = []
        count = 1

    # Условие, которое срабатывает, когда мы встретили 0
    # и проверяем, что в буфере что-то есть, затем используем
    # функцию make_simetric и ее результат добавляем в результат.
    # Не забываем добавить в результат попавшийся 0
    # Пример: начальный список [ ... 0, 34, 25, 1, 0 ...]
    # в буфере уже [1, 2, 3], симметричная последовательность
    # [1, 2 , 1] - добавляем в результат, не забывая потом добавить еще 0
    elif x == 0 and buffer:
        simetric_mass = make_simetric(len(buffer))
        result.extend(simetric_mass)
        result.append(0)
        buffer = []
        count = 1
    # Попался ноль, а в буфере нема.
    # Пример: начальный список по типу [... 0, 0, ...]
    elif x == 0:
        result.append(0)
# Не забываем добавить буфер, который копился, а 0 больше не встретился
# Пример: [ ...0, 21, 1, 32, 23] - как раз один из хвостов,
# о которых говорил в начале
result.extend(buffer)

print(*result)