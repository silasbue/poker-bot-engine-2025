import random

from poker_game_runner.state import Observation
from poker_game_runner.utils import HandType, Range

BOT_NAME = "old_old_bot"


class Bot:
    @classmethod
    def get_name(cls, path):
        return BOT_NAME

    def get_name(self):
        return BOT_NAME

    def act(self, obs: Observation):
        current_round = obs.current_round

        great_hand = Range("99+, AJs+, KQs, AKo")
        good_hand = Range("77+, A8s+, K9s+, QTs+, AJo+, KQo")

        if good_hand.is_hand_in_range(obs.my_hand):
            return obs.get_max_raise()

        if current_round < 2:
            if (
                good_hand.is_hand_in_range(obs.my_hand)
                and obs.get_max_spent() < obs.get_my_player_info().stack
            ):
                return 1
            else:
                return 0
        tenpercent = int(0.1 * obs.get_my_player_info().stack)
        for x in obs.get_active_players():
            if x.stack > tenpercent:
                fuckem = True

        if fuckem:
            return tenpercent

        elif current_round < 3:
            # Will go 'all in' if the round is 4 else it will 'call'
            if (
                great_hand.is_hand_in_range(obs.my_hand)
                and obs.get_max_spent() < obs.get_my_player_info().stack
            ):
                return 1
            else:
                return 0
        else:
            return 0
        # Are we feeling lucky?
        # If yes then 'all in' else 'call'
