from poker_game_runner.state import Observation
from poker_game_runner.utils import HandType, Range

BOT_NAME = "old_old_bot_fuckem"


class Bot:

    @classmethod
    def get_name_class(cls, path):
        return BOT_NAME

    def get_name(self):
        return BOT_NAME

    def act(self, obs: Observation):

        great_hand = Range("77+, A9s+, KTs, QJs, AQo+")

        if great_hand.is_hand_in_range(obs.my_hand):
            return obs.get_max_raise()

        tenpercent = int(0.1 * obs.get_my_player_info().stack)
        for x in obs.get_active_players():
            if x.stack > tenpercent:
                fuckem = True

            if fuckem:
                return tenpercent
            # 20%
            # greatHand = = Range(" 55+, A3s+, K7s+, Q8s+, j9s, T9s, A9o+, KTo+, Qjo")
            decent_hand = Range("77+, A8s+, K9s+, QTs+, AJo+, KQo")
            if decent_hand.is_hand_in_range(obs.my_hand):
                if obs.can_raise:
                    forthy = 0.4 * obs.get_my_player_info().stack
                    if obs.get_min_raise() < forthy:
                        return 0.4 * obs.get_my_player_info().stack
                return 1

            if obs.get_my_hand_type() > 4:
                return obs.get_max_raise()

            if obs.get_call_size() < 0.1 * obs.get_my_player_info().stack:
                return 1

            if obs.get_my_hand_type() <= obs.get_board_hand_type():
                return 1

            return 0
            # Returning 0 will fold or check
            # return 1 - Returning 1 will call or check
            # return x > 1 - Returning a number greater than 1 will raise
