#!/usr/bin/env python3

class Strategy(object):
    def __init__(self,line):
        self.line = line
        if "A" in self.line:
            self.opponent = Rock()
        if "B" in self.line:
            self.opponent = Paper()
        if "C" in self.line:
            self.opponent = Scissors()
        if "X" in self.line:
            self.strategy = "lose"
        if "Y" in self.line:
            self.strategy = "draw"
        if "Z" in self.line:
            self.strategy = "win"
        self.decoded = {"opponent":self.opponent, "strategy":self.strategy}

class Result(object):
    def __init__(self):
        pass

class Win(Result):
    def __init__(self):
        pass

class Lose(Result):
    def __init__(self):
        pass

class Draw(Result):
    def __init__(self):
        pass


class Play(object):
    def __init__(self):
        return
 
class Rock(Play):
    def __init__(self):
        self.inherent_score = 1
        self.draw = "rock"
        self.win = "scissors"
        self.lose = "paper"

class Paper(Play):
    def __init__(self):
        self.inherent_score = 2
        self.draw = "paper"
        self.win = "rock"
        self.lose = "scissors"

class Scissors(Play):
    def __init__(self):
        self.inherent_score = 3
        self.draw = "scissors"
        self.win = "paper"
        self.lose = "rock"

class Round(object):
    def __init__(self,strategy):
        self.score = 0
        self.round_score = 0
        self.strategy = strategy
        self.strategy_decoded = Strategy(self.strategy).decoded
        if self.strategy_decoded["strategy"] == "win":
            self.strategy_decoded["player"] = self.strategy_decoded["opponent"].lose
        if self.strategy_decoded["strategy"] == "lose":
            self.strategy_decoded["player"] = self.strategy_decoded["opponent"].win
        if self.strategy_decoded["strategy"] == "draw":
            self.strategy_decoded["player"] = self.strategy_decoded["opponent"].draw        
        
        
        if self.strategy_decoded["player"] == "rock":
            self.strategy_decoded["player"] = Rock()
        if self.strategy_decoded["player"] == "paper":
            self.strategy_decoded["player"] = Paper()
        if self.strategy_decoded["player"] == "scissors":
            self.strategy_decoded["player"] = Scissors()        
        self.inherent_score = self.strategy_decoded["player"].inherent_score
        # Rock Cases
        if isinstance(self.strategy_decoded["opponent"],Rock) and isinstance(self.strategy_decoded["player"],Rock):
            self.round_score = 3
        if isinstance(self.strategy_decoded["opponent"],Rock) and isinstance(self.strategy_decoded["player"],Paper):
            self.round_score = 6
        if isinstance(self.strategy_decoded["opponent"],Rock) and isinstance(self.strategy_decoded["player"],Scissors):
            self.round_score = 0
        # Paper Cases
        if isinstance(self.strategy_decoded["opponent"],Paper) and isinstance(self.strategy_decoded["player"],Paper):
            self.round_score = 3
        if isinstance(self.strategy_decoded["opponent"],Paper) and isinstance(self.strategy_decoded["player"],Scissors):
            self.round_score = 6
        if isinstance(self.strategy_decoded["opponent"],Paper) and isinstance(self.strategy_decoded["player"],Rock):
            self.round_score = 0
        # Scissors Cases
        if isinstance(self.strategy_decoded["opponent"],Scissors) and isinstance(self.strategy_decoded["player"],Scissors):
            self.round_score = 3
        if isinstance(self.strategy_decoded["opponent"],Scissors) and isinstance(self.strategy_decoded["player"],Rock):
            self.round_score = 6
        if isinstance(self.strategy_decoded["opponent"],Scissors) and isinstance(self.strategy_decoded["player"],Paper):
            self.round_score = 0
        self.score = self.inherent_score + self.round_score
        print(f"Round score is {self.score}")

round_counter = 0
round_list = []
score_accumulator = 0
with open("input.txt") as file:
    for line in file:
        print(f"Round {round_counter} line is {line.strip()}")
        round_list.append(Round(line))
        score_accumulator = score_accumulator + round_list[round_counter].score
        round_counter = round_counter + 1

print(f"Total score via strategy map is {score_accumulator}")