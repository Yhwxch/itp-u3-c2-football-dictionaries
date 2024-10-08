def players_as_dictionaries(squads_list):
    players = []
    for player in squads_list:
        players_info = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8]
        }
        players.append(players_info)
    return players