def players_by_position(squads_list):
    players_positions = {}
    for player in squads_list:
        position = player['position']
        players_positions.setdefault(position, [])
        players_positions[position].append(player)
    return players_positions