from typing import List

from Names import Names
import random


def shoot(min_score):
    return max(min_score, random.randint(0, 11))


def shoot_arrows(min_score):
    points = []
    for i in range(Archer.MAX_ARROWS):
        points[i] = shoot(min_score)


def let_archer_shoot(archer, is_beginner):
    for i in range(Archer.MAX_ROUNDS):
        archer.register_score_for_round(i, shoot_arrows(0 if is_beginner else 1))


def generate_archers(nr_of_archers):
    pass


def generate_archers(nr_of_archers: int):
    archers = list[Archer]
    for i in range(nr_of_archers):
        archer = Archer(Names.next_first_name(), Names.next_surname())


class Archer:
    MAX_ARROWS = 3
    MAX_ROUNDS = 10

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def register_score_for_round(self, round, points: List[int]):
        pass

    def get_total_score(self):
        return 0
