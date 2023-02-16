
total = 150
players_data = {}
now_player = {}


def is_game_running(id):
    global players_data
    return players_data[id]['game_running']


def add_win_count(id):
    global players_data
    players_data[id]['win_count'] += 1


def add_loss_count(id):
    global players_data
    players_data[id]['loss_count'] += 1


def game_start(id):
    global players_data
    players_data[id]['game_running'] = True


def game_end(id):
    global players_data
    players_data[id]['remainder'] = players_data[id]['total']
    players_data[id]['game_running'] = False


def set_candies(id, total):
    players_data[id]['total'] = total
    players_data[id]['remainder'] = total


def set_last_move(id, last_move):
    global players_data
    players_data[id]['last_move'] = last_move


def get_last_move(id):
    global players_data
    return players_data[id]['last_move']


def get_remainder(id):
    global players_data
    return int(players_data[id]['remainder'])


def set_remainder(id, count):
    global players_data
    players_data[id]['remainder'] = count


def add_player_data(id):
    global players_data
    if id not in players_data:
        players_data[id] = {
            'game_running': False,
            'total': total,
            'remainder': total,
            'win_count': 0,
            'loss_count': 0,
            'last_move': None
        }


def get_win_loss(id):
    global players_data
    return [players_data[id]['win_count'], players_data[id]['loss_count']]
