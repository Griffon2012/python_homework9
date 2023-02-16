import playerData as pd
import random

MINAMOUNT = 28


def is_game_running(id):
    return pd.is_game_running(id)


def game_start(id):
    pd.game_start(id)


def get_remainder(id):
    return pd.get_remainder(id)


def set_candies(id, total):
    pd.set_candies(id, total)


def first_move():
    firstMove = random.randint(1, 2)
    return firstMove


def move(id):
    global MINAMOUNT
    countForDelete = GetCountForDelete(MINAMOUNT, pd.get_remainder(id))
    remainder = pd.get_remainder(id) - countForDelete
    pd.set_remainder(id, remainder)
    pd.set_last_move(id, 2)
    return countForDelete


def move_player(id, count):
    remainder = pd.get_remainder(id) - count
    pd.set_remainder(id, remainder)
    pd.set_last_move(id, 1)


def activate_game(id):
    pd.add_player_data(id)


def GetCountForDelete(maxCount: int, nowTotalAmount: int) -> int:
    result = None
    step = maxCount + 1
    if nowTotalAmount < maxCount:
        result = nowTotalAmount
    elif nowTotalAmount % step:
        result = nowTotalAmount % step
    else:
        result = random.randint(1, maxCount)

    return result


def check_winner(id):
    if pd.get_remainder(id) <= 0:
        return pd.get_last_move(id)
    else:
        return False


def win_loss_counter(id):
    if pd.get_last_move(id) == 1:
        pd.add_win_count(id)
    else:
        pd.add_loss_count(id)


def game_end(id):
    pd.game_end(id)


def get_win_loss(id):
    return pd.get_win_loss(id)
