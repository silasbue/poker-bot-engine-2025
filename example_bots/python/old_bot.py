import random
import time
from math import floor

from poker_game_runner.state import Observation
from poker_game_runner.utils import HandType, Range

BOT_NAME = "old_bot"


class Bot:
    @classmethod
    def get_name_class(cls, path):
        return BOT_NAME

    def get_name(self):
        return BOT_NAME

    def __init__(self) -> None:
        self.best_hand = Range("AA")  # 0.5%
        self.great_hand = Range("QQ+")  # 1.4%
        self.good_hand = Range("88+, ATs+, KQs, AQo+")  # ~7%
        self.ok_hand = Range("55+, A3s+, K8s+, Q9s+, JTs, A9o+, KTo+, QJo")  # 18.7%
        self.bad_but_playable_hand = Range(
            "22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 82s+, 72s+, 62s+, 52s+, 42s+, 32s, A2o+, K2o+, Q2o+, J2o+, T2o+, 95o+, 85o+, 75o+, 65o"
        )
        self.great_pair = Range("JJ+")

    def get_name(self):
        return 'Kevin "bob" Hart'

    def act(self, obs: Observation):
        if obs.get_my_hand_type() >= HandType.FOUROFAKIND:
            return obs.get_max_raise()

        if obs.get_my_hand_type() >= HandType.FULLHOUSE:
            return obs.get_min_raisection_pot_raise(2)

        if obs.get_my_hand_type() >= HandType.THREEOFAKIND:
            return obs.get_fraction_pot_raise(1)

        if obs.get_my_hand_type() >= HandType.TWOPAIR:
            return obs.get_fraction_pot_raise(1)

        if self.great_hand.is_hand_in_range(obs.my_hand):
            return obs.get_max_raise()

        if self.good_hand.is_hand_in_range(obs.my_hand):
            return obs.get_fraction_pot_raise(1)

        if self.ok_hand.is_hand_in_range(obs.my_hand):
            return 1
        else:
            return 0
