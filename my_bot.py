import random
import time

from poker_game_runner.state import Observation
from poker_game_runner.utils import HandType, Range

BOT_NAME = "Python Bot"  # Change this to your bot's name


class Bot:
    @classmethod
    def get_name_class(cls, path):
        return BOT_NAME

    def get_name(self):
        return BOT_NAME

    best_hand = Range("AA")  # 0.5%
    great_hand = Range("QQ+")  # 1.4%
    good_hand = Range("88+, ATs+, KQs, AQo+")  # ~7%
    ok_hand = Range("55+, A3s+, K8s+, Q9s+, JTs, A9o+, KTo+, QJo")  # 18.7%
    bad_but_playable_hand = Range(
        "22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 82s+, 72s+, 62s+, 52s+, 42s+, 32s, A2o+, K2o+, Q2o+, J2o+, T2o+, 95o+, 85o+, 75o+, 65o"
    )
    great_pair = Range("JJ+")

    def act(self, obs: Observation):
        s = obs.player_infos[obs.my_index].stack / obs.big_blind
        match obs.current_round:
            case 4:
                if obs.get_my_hand_type >= HandType.FOUROFAKIND:
                    return obs.get_max_raise()

                if obs.get_my_hand_type() >= HandType.FOUROFAKIND:
                    return obs.get_max_raise()

                if obs.get_my_hand_type() >= HandType.FULLHOUSE:
                    return obs.get_min_raisection_pot_raise(2)

                if obs.get_my_hand_type() >= HandType.THREEOFAKIND:
                    return obs.get_fraction_pot_raise(1)

                if obs.get_my_hand_type() >= HandType.TWOPAIR:
                    return obs.get_fraction_pot_raise(1)
            case _:
                if Range("55+, A5s+, K9s+, Q9s+, JTs, A9o+, KTo+").is_hand_in_range(
                    obs.my_hand
                ):
                    return obs.get_fraction_pot_raise(1)
                return 0
        return 0
