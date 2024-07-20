import random

# 打撃データベース
batting_data = {
    'player_name': 'Sample Player',
    'at_bats': 400,
    'walks': 30,
    'hits': 100,
    'total_bases': 150,
    'strikeouts': 70,
    'doubles': 20,
    'triples': 5,
    'home_runs': 15,
    'groundouts': 80,
    'flyouts': 50,
    'sacrifice_flies': 5
}

# 打席数
total_plate_appearances = 443

# 各打撃結果の確率を計算
results_probabilities = {
    'single': (batting_data['hits'] - batting_data['doubles'] - batting_data['triples'] - batting_data['home_runs']) / total_plate_appearances,
    'double': batting_data['doubles'] / total_plate_appearances,
    'triple': batting_data['triples'] / total_plate_appearances,
    'home_run': batting_data['home_runs'] / total_plate_appearances,
    'walk': batting_data['walks'] / total_plate_appearances,
    'strikeout': batting_data['strikeouts'] / total_plate_appearances,
    'groundout': batting_data['groundouts'] / total_plate_appearances,
    'flyout': batting_data['flyouts'] / total_plate_appearances,
    'sacrifice_fly': batting_data['sacrifice_flies'] / total_plate_appearances
}

# 残りはアウトとして扱う
results_probabilities['other_out'] = 1 - sum(results_probabilities.values())

# 打撃結果の表示方法
def display_result(result):
    if result in ['single', 'double', 'triple', 'home_run']:
        direction = random.choice(['投', '捕', '一', '二', '三', '遊', '左', '中', '右'])
        hit_type = {'single': '安', 'double': '2', 'triple': '3', 'home_run': '本'}
        return f"{direction} {hit_type[result]}"
    elif result == 'walk':
        return '四球'
    elif result == 'strikeout':
        return random.choice(['空三振', '見三振'])
    elif result == 'groundout':
        direction = random.choice(['投', '捕', '一', '二', '三', '遊'])
        return f"{direction} ゴロ"
    elif result == 'flyout':
        direction = random.choice(['左', '中', '右'])
        return f"{direction} 飛"
    elif result == 'sacrifice_fly':
        direction = random.choice(['左', '中', '右'])
        return f"{direction} 犠飛"
    else:
        direction = random.choice(['投', '捕', '一', '二', '三', '遊', '左', '中', '右'])
        return f"{direction} 併打"

# 打撃結果を生成
def generate_batting_result():
    result = random.choices(list(results_probabilities.keys()), list(results_probabilities.values()))[0]
    return display_result(result)

# 結果を生成して表示
for _ in range(total_plate_appearances):
    print(generate_batting_result())
