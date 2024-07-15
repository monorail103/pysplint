import sqlite3

# {"name": "Player1", "AVG": 0.300, "OBP": 0.370, "SLG": 0.500, "K%": 0.15, "BB%": 0.10, "single_rate": 0.5, "double_rate": 0.2, "triple_rate": 0.05, "home_run_rate": 0.05},
def getplayerdata():
    conn = sqlite3.connect('db/players.db')
    c = conn.cursor()
    c.execute('SELECT * FROM players WHERE source = ?', (source,))
    playerdata = c.fetchone()
    conn.close()
    return playerdata

def updateplayerdata():
    # プレイヤーのデータを更新する
    