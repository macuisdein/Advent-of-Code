#!/usr/bin/env python3

# I used Count for the first time. Unfortunately that did not help with Part 2, since it was more about comparisons. I looked but did not find what I wanted. So I just wrote it myself.

from collections import Counter


def get_game_number(line):
    game = line.split(":")[0]
    # print(game)
    game_number = game.split(" ")[1]
    sets = line.split(":")[1]
    return game_number, sets


def get_sets(sets):
    sets = sets.strip()
    sets = sets.split(";")
    return sets


def get_balls(set):
    balls = {}
    ball = set.split(",")
    for b in ball:
        b = b.strip()
        # print(b)
        # print(f"Ball: {b.split(' ')[1]} is {int(b.split(' ')[0])}")
        balls[b.split(" ")[1]] = int(b.split(" ")[0])
    return balls


def check_if_valid_game(ball_counter):
    colors = ["red", "blue", "green"]
    for color in colors:
        # print(ball_counter[color])
        if ball_counter[color] < 0:
            return False
    return True


def check_if_max(set_balls, max_balls):
    colors = ["red", "blue", "green"]
    for color in colors:
        # print(ball_counter[color])
        try:
            if set_balls[color] > max_balls[color]:
                max_balls[color] = set_balls[color]
        except:
            KeyError
    return max_balls


def get_power(max_balls):
    power = max_balls["red"] * max_balls["blue"] * max_balls["green"]
    return power


def part2(lines):
    games_power = {}
    for line in lines:
        max_balls = {"red": 1, "blue": 1, "green": 1}
        game_number, sets = get_game_number(line)
        sets = get_sets(sets)
        for set in sets:
            balls = get_balls(set)
            max_balls = check_if_max(balls, max_balls)
        games_power[game_number] = get_power(max_balls)
    print(f"The sum of all games power is {sum(games_power.values())}")


def main():
    games = {}
    input = open("input.txt", "r")
    lines = input.readlines()

    for line in lines:
        game_number, sets = get_game_number(line)
        sets = get_sets(sets)
        for set in sets:
            valid_ball_game = Counter({"red": 12, "blue": 14, "green": 13})
            balls = get_balls(set)
            # print(Counter(balls))
            valid_ball_game.subtract(Counter(balls))
            # print(valid_ball_game)
            is_valid_game = check_if_valid_game(valid_ball_game)
            if is_valid_game:
                continue
            else:
                break
        #  games[game_number] = ball_game
        if is_valid_game:
            games[game_number] = int(game_number)
        else:
            games[game_number] = 0

    print(f"The games are: {games}")

    print(f"The sum of all valid games is {sum(games.values())}")

    part2(lines)


if __name__ == "__main__":
    main()
