def canFree(score):
    noWin = []
    for opponent in range(1, 100):
        free_bacon_score = free_bacon(opponent) + score
        if is_swap(free_bacon_score, opponent) or free_bacon_score < 100:
            if abs(opponent//10 - opponent % 10) == 2:
                noWin.append(opponent)

    return noWin

def is_swap(player_score, opponent_score):
    player_tens = (player_score // 10) % 10
    player_digits = player_score % 10
    opponent_tens = (opponent_score // 10) % 10
    opponent_digits = opponent_score % 10

    player_abs = abs(player_tens - player_digits)
    opponent_abs = abs(opponent_tens - opponent_digits)

    return player_abs == opponent_abs

def free_bacon(score):
    tens = -1
    digits = -1
    
    tens = score // 10
    digits = score % 10
        
    return max(tens * 2 - digits, 1)

print("Still can't win:", canFree(96))