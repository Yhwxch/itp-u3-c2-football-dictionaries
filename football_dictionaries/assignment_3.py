def players_by_country_and_position(squads_list):
    players_country_position = {}
    for player in squads_list:
        country = player['country']
        position = player['position']
        
        # Ensure the country is in the dictionary
        if country not in players_country_position:
            players_country_position[country] = {}
        
        # Ensure the position is in the country's dictionary
        if position not in players_country_position[country]:
            players_country_position[country][position] = []
        
        # Append the player to the correct country and position list
        players_country_position[country][position].append(player)
    
    return players_country_position
