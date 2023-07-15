def two_counts(mass, number):
    for x in range(len(mass)):
        for j in range(x+1, len(mass)):
            if mass[x] + mass[j] == number:
                return x, j


if __name__ == '__main__':
    print(two_counts([6, 2, 8, -3, 1, 1, 6, 10], 5))