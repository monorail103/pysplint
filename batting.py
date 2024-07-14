import random

# 塁を進める関数
def advance_bases(hit, bases, score):
    if hit == 4:
        score += sum(bases) + 1
        bases = [False, False, False]
    else:
        for i in range(2, -1, -1):
            if bases[i]:
                if i + hit >= 3:
                    score += 1
                else:
                    bases[i + hit] = True
                bases[i] = False
        if hit < 4:
            bases[hit - 1] = True
    return bases, score

# 打席の結果を決定する関数
def at_bat(player, sign):
    strikes = 0
    balls = 0
    outs = 0
    hittype = ""
    while strikes < 3 and balls < 4:
        if sign == "bunt":
            hittype = "bunt"
            return hittype, 1, balls, strikes, outs
        elif sign == "swing_away":
            action = random.choice(["swing", "miss"])
        else:
            action = random.choice(["swing", "miss", "take"])
        
        if action == "swing":
            if random.random() < player["AVG"] + (0.05 if sign == "swing_away" else 0):
                hit_type = random.random()
                if hit_type < player["single_rate"]:
                    hittype = "single"
                    return hittype, 1, balls, strikes, outs
                elif hit_type < player["single_rate"] + player["double_rate"]:
                    hittype = "double"
                    return hittype, 2, balls, strikes, outs
                elif hit_type < player["single_rate"] + player["double_rate"] + player["triple_rate"]:
                    hittype = "triple"
                    return hittype, 3, balls, strikes, outs
                else:
                    hittype = "home run"
                    return hittype, 4, balls, strikes, outs
            else:
                strikes += 1
        elif action == "miss":
            strikes += 1
        elif action == "take":
            if random.random() < player["BB%"]:
                balls += 1
            else:
                strikes += 1
    if balls == 4:
        hittype = "walk"
        return hittype, 1, balls, strikes, outs
    else:
        hittype = random.choice(["strikeout", "groundout", "flyout", "lineout"])
        outs += 1
        return hittype, 0, balls, strikes, outs
