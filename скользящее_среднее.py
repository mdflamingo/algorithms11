def slipping_middle(mass, window):
    start_sum = sum(mass[0:window])
    result = [start_sum/window]
    for e in range(1, len(mass)-window + 1):
        start_sum = start_sum - mass[e-1]
        start_sum += mass[e + window - 1]
        result.append(start_sum/window)
    return result


if __name__ == '__main__':
    a = slipping_middle([9, 3 ,2, 0, 1, 5, 1, 0, 0,], 3)
    print(*a)

