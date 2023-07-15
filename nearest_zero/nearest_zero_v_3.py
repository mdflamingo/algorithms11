# Id задачи 88963975
def find_nearest_zeros(house_nums):

    def make_symmetric(n):
        mass = list(range(1, n + 1))
        reversed_mass = list(reversed(mass))
        symmetric_seq = []
        for x in range(len(mass)):
            if mass[x] <= reversed_mass[x]:
                symmetric_seq.append(mass[x])
            else:
                symmetric_seq.append(reversed_mass[x])
        return symmetric_seq

    start_not_zero = False
    if house_nums[0] != 0:
        start_not_zero = True

    result = []
    count = 0
    for house_num in house_nums:
        if house_num != 0:
            count += 1

        elif house_num == 0 and start_not_zero:
            start_not_zero = False
            num_seq = range(count, -1, -1)
            result.extend(num_seq)
            count = 0

        elif house_num == 0 and count != 0:
            symmetric_mass = make_symmetric(count)
            result.extend(symmetric_mass)
            result.append(0)
            count = 0

        elif house_num == 0:
            result.append(0)

    result.extend(range(1, count + 1))
    return result


if __name__ == '__main__':
    house_count = int(input())
    house_numbers = list(map(int, input().split()))
    print(*find_nearest_zeros(house_numbers))
