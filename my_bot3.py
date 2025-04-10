import random
import time

from poker_game_runner.state import Observation
from poker_game_runner.utils import HandType, Range

BOT_NAME = "LisBot"  # Change this to your bot's name


class Bot:
    @classmethod
    def get_name_class(cls, path):
        return BOT_NAME

    def get_name(self):
        return BOT_NAME

    def act(self, obs: Observation):
        best_hand = Range("AA")  # 0.5%
        great_hand = Range("QQ+")  # 1.4%
        good_hand = Range("88+, ATs+, KQs, AQo+")  # ~7%
        ok_hand = Range("55+, A3s+, K8s+, Q9s+, JTs, A9o+, KTo+, QJo")  # 18.7%
        bad_but_playable_hand = Range(
            "22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 82s+, 72s+, 62s+, 52s+, 42s+, 32s, A2o+, K2o+, Q2o+, J2o+, T2o+, 95o+, 85o+, 75o+, 65o"
        )
        great_pair = Range("JJ+")
        aggresiveness = 0.6

        match obs.small_blind:
            case 20:
                aggresiveness += 0.05
            case 30:
                aggresiveness += 0.05
            case 40:
                aggresiveness += 0.1
            case 50:
                aggresiveness += 0.1
            case 60:
                aggresiveness += 0.1

        if len(obs.get_active_players()) <= 3:
            aggresiveness += 0.2

        if obs.get_my_hand_type() >= HandType.FOUROFAKIND:
            if random.random() * aggresiveness > 0.5:
                return obs.get_max_raise()
            else:
                return obs.get_fraction_pot_raise(3)

        if obs.get_my_hand_type() >= HandType.FULLHOUSE:
            if random.random() * aggresiveness > 0.5:
                return obs.get_fraction_pot_raise(4)
            else:
                return obs.get_fraction_pot_raise(3)

        if obs.get_my_hand_type() >= HandType.THREEOFAKIND:
            if random.random() * aggresiveness > 0.5:
                return obs.get_fraction_pot_raise(2)
            else:
                return obs.get_fraction_pot_raise(1)

        if obs.get_my_hand_type() >= HandType.TWOPAIR:
            if random.random() * aggresiveness > 0.5:
                return obs.get_fraction_pot_raise(1.4)
            else:
                return obs.get_fraction_pot_raise(0.7)

        if great_hand.is_hand_in_range(obs.my_hand):
            return obs.get_max_raise()

        if good_hand.is_hand_in_range(obs.my_hand):
            return obs.get_fraction_pot_raise(1)

        if ok_hand.is_hand_in_range(obs.my_hand):
            return 1
        else:
            return 0

        return obs.get_max_raise()  # All-in
