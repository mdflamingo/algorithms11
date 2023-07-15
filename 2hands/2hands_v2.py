# Id задачи 88963886
def play_2hands(buttons, field):
    score = 0
    if not field:
        return score

    numbers = set(field)
    for number in numbers:
        count_buttons = field.count(number)
        if count_buttons <= buttons:
            score += 1
    return score


if __name__ == '__main__':
    one_player_buttons = int(input())
    available_buttons = one_player_buttons * 2

    game_field = []
    for _ in range(4):
        row = list(map(int, input().replace('.', '')))
        game_field.extend(row)

    game_score = play_2hands(available_buttons, game_field)
    print(game_score)
