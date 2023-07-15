# print(*range(1, 3 +1))
#
# def make_simetric(n):
#     """ Получаем число n и делаем симметричный список.
#         Например, дают нам число 6 и мы делаем список
#         1 2 3 3 2 1.
#     """
#     mass = list(range(1, n + 1))
#     reversed_mass = list(reversed(mass))
#     result = []
#     for x in range(len(mass)):
#         if mass[x] <= reversed_mass[x]:
#             result.append(mass[x])
#         else:
#             result.append(reversed_mass[x])
#     return result
#
# print(make_simetric(0))


if __name__ == '__main__':
    l = ( x for x in range(3))
    print(type(l))