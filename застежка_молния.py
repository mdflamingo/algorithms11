# mass_size = int(input())
# mass_1 = list(map(int, input().split()))
# mass_2 = list(map(int, input().split()))
#
# result = []
# for x in range(mass_size):
#     result.append(mass_1[x])
#     result.append(mass_2[x])
# print(*result)

# v2

len_mass = int(input())
massiv_1 = list(map(int, input().split()))
massiv_2 = list(map(int, input().split()))

result = list(zip(massiv_1, massiv_2))
print(*result)
new_result = []
for el in result:
    new_result += el
print(*new_result)
