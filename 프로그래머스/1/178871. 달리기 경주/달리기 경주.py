def solution(players, callings):
    
    players_ranking = {}
    
    for idx, player in enumerate(players):
        players_ranking[player] = idx
    
    for player in callings:
        
        idx = players_ranking.get(player)
        
        frontPlayer = players[idx - 1]
        
        players_ranking[player] = idx - 1
        players_ranking[frontPlayer] = idx
        
        players[idx - 1] = player
        players[idx] = frontPlayer
    
    return players