while True:
    number_of_players = int(input("Pls enter Number of Player:\n"))
    if number_of_players < 2:
        print("this game need atleast 2 player.")
    else:
        break
scores = {}
for i in range(number_of_players):
    player = str(input(f"Pls enter {i + 1} player name:\n"))
    scores[player] = 0
while True:
    game = {'name': {}, "city": {}, "color": {}, "food": {}}
    indicator = str(input(f"Pls enter indicator:\n"))
    if len(indicator) == 1:
        for field in game.keys():
            for player in scores.keys():
                answer = str(input(f"{player} Pls enter your answer for {field}:\n"))
                if not answer.startswith(indicator):
                    answer = ""
                game[field][player] = answer
            for player, answer in game[field].items():
                if answer:
                    dup_num = list(game[field].values()).count(answer)
                    if dup_num > 1:
                        scores[player] += 5
                    elif dup_num == 1:
                        scores[player] += 10
        print(scores)
        winner = [key for key, value in scores.items() if value == max(scores.values())]
        print(f"winner is {winner}.")
    else:
        print('Indicator must be one character.')
