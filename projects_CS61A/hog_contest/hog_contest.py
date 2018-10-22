"""
This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry.

Only this file will be submitted. Make sure to include any helper functions
from `hog.py` that you'll need here! For example, if you have a function to
calculate Free Bacon points, you should make sure it's added to this file
as well.

Don't forget: your strategy must be deterministic and pure.
"""

PLAYER_NAME = 'Alan_ROCKET' # Change this line!

strategy = {(99, 11): 1, (98, 11): 2, (98, 22): 2, (97, 1): 2, (97, 10): 2, (97, 12): 2, (97, 23): 2, (97, 32): 2, (97, 34): 2, (97, 56): 2, \
            (99, 11): 3, (98, 11): 10, (98, 22): 10, (97, 1): 10, (97, 10): 10, (97, 12): 10, (97, 23): 10, (97, 32): 3, (97, 34): 10, (97, 56): 10, \
            (96, 2): 1, \
            (91, 99): 3, (91, 98): 3, (91, 97): 3, (91, 96): 3, (91, 95): 3, (91, 94): 3, (91, 93): 3, (91, 92): 3, (91, 91): 3, (91, 90): 3, \
            (91, 89): 1, (91, 88): 1, (91, 79): 0, (91, 78): 0, (91, 77): 0, (91, 76): 0, (91, 69): 0, (91, 68): 0, (91, 67): 0, (91, 66): 0, \
            (91, 65): 1, (91, 64): 0}

def final_strategy(score, opponent_score):
    
    def free_bacon(score):
        tens = -1
        digits = -1
    
        tens = score // 10
        digits = score % 10
        
        return max(tens * 2 - digits, 1)

    def is_swap(player_score, opponent_score):
        player_tens = (player_score // 10) % 10
        player_digits = player_score % 10
        opponent_tens = (opponent_score // 10) % 10
        opponent_digits = opponent_score % 10

        player_abs = abs(player_tens - player_digits)
        opponent_abs = abs(opponent_tens - opponent_digits)

        return player_abs == opponent_abs


    def make_fair_dice(sides):
        def dice():
            return randint(1,sides)
        return dice
    six_sided = make_fair_dice(6)
    
    def roll_dice(num_rolls, dice=six_sided):
        total = 0
        one_roll = 0
        for i in range(0, num_rolls):
            one_roll = dice()
            if one_roll == 1:
                return 1
            else:
                total += one_roll
        return total

    strategy_roll = -1
    max_roll = 0
    temp_score = score # Only change temp_score
    free_bacon_score = free_bacon(opponent_score) # Trying free_bacon
    temp_score += free_bacon_score

    if is_swap(temp_score, opponent_score): # If swap
        max_increase = opponent_score - score
    else:
        if temp_score > 100:
            return 0
        max_increase = free_bacon_score


    try: # Looking up dictionary
        strategy_roll = strategy[(score, opponent_score)]
        return strategy_roll
    except:
        pass

    if score >= 98:
        return 10

#   free_bacon can't win
    if score >= 97:
        return 1
    if score >= 94:
        return 2
    if score >= 90:
        return 3

    for rolls in range (1, 2):
        temp_score = score

        roll_score = roll_dice(rolls)
        temp_score += roll_score

        if is_swap(temp_score, opponent_score):
            if max_increase < (opponent_score - score):
                max_increase = opponent_score - score
                max_roll = rolls
        else:
            if max_increase < roll_score:
                max_increase = roll_score
                max_roll = rolls

    if max_increase >= 12:
        return max_roll

    return 6