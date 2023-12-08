file = open("input.py", "r")
lines = file.readlines()

length = len(lines)

total_score = 0


def process_cards(length, cards_to_process, card_count, lines):
    # print(f"Card count = {card_count}")
    for x in range(1, length + 1):
        if cards_to_process[str(x)] != 0:
            header = str(lines[x - 1].split(":", 1)[0]).strip()
            header = header.split()[1]
            # print(f"Processing card {header}")
            card_count[header] = card_count[header] + 1
            no_header = str(lines[x - 1].split(":", 1)[1]).strip()
            winning = str(no_header.split("|", 1)[0]).strip()
            my_cards = str(no_header.split("|", 1)[1]).strip()

            # print(f"Wining is {winning}")
            # print(f"My cards are {my_cards}")

            winning = str(winning).split()
            my_cards = str(my_cards).split()
            # print(f"Winning is {winning}")
            # print(f"My cards are {my_cards}")

            winning_card = False

            scoring = []

            for number in my_cards:
                if number in winning:
                    scoring.append(number)
                    winning_card = True
                else:
                    pass
            #  print(f"Length of scoring: {len(scoring)}")

            for y in range(len(scoring)):
                cards_to_process[str(int(header) + y + 1)] = (
                    cards_to_process[str(int(header) + y + 1)] + 1
                )
            # print(f"Reduce cards-- {cards_to_process[str(x)]}")
            cards_to_process[str(x)] = cards_to_process[str(x)] - 1
            # print(f"Reduce cards-- {cards_to_process[str(x)]}")
    return cards_to_process, card_count


# print(len(lines))
winning_lines = []
winning_copies = []
for x in range(len(lines)):
    score = 0
    # print(type(line))
    no_header = str(lines[x].split(":", 1)[1]).strip()
    winning = str(no_header.split("|", 1)[0]).strip()
    my_cards = str(no_header.split("|", 1)[1]).strip()

    # print(f"Wining is {winning}")
    # print(f"My cards are {my_cards}")

    winning = str(winning).split()
    my_cards = str(my_cards).split()
    # print(f"Winning is {winning}")
    # print(f"My cards are {my_cards}")

    scoring = []

    for number in my_cards:
        if number in winning:
            scoring.append(number)
    # print(f"Scoring is {scoring}")
    # print(f"Length of scoring is {len(scoring)}")

    # print(f"Winning lines now at {winning_lines}")

    if len(scoring) == 0:
        score = 0
    elif len(scoring) == 1:
        score = 1
    else:
        score = 1
        for item in range(1, len(scoring)):
            score = score * 2

    # print(f"Game score is {score}")
    total_score = total_score + score


print(f"Part 1 Total score is {total_score}")

cards_to_process = {}

for x in range(1, len(lines) + 1):
    cards_to_process[str(x)] = 1


part_2_scoring = 0
card_count = {}
for x in range(1, len(lines) + 1):
    card_count[str(x)] = 0

# print(f"Card count = {card_count}")

# cards_to_process, card_count = process_cards(length, cards_to_process, card_count, lines)

notFinished = True

while notFinished:
    if sum(cards_to_process.values()) == 0:
        notFinished = False
        print(f"Done-- Total cards = {sum(card_count.values())}")
        print(f"Card count: {card_count}")
    else:
        print(f"Not Done", flush=False, end="\r")
        # print(f"Not Done -- still to do = {cards_to_process}", end="")
        # print(f"Sum of values= {sum(cards_to_process.values())}")
        cards_to_process, card_count = process_cards(
            length, cards_to_process, card_count, lines
        )
