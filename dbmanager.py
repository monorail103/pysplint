import sqlite3

# {"name": "Player1", "AVG": 0.300, "OBP": 0.370, "SLG": 0.500, "K%": 0.15, "BB%": 0.10, "single_rate": 0.5, "double_rate": 0.2, "triple_rate": 0.05, "home_run_rate": 0.05},
def getplayerdata():
    conn = sqlite3.connect('db/player.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tb_pldata')
    playerdata = c.fetchall()
    conn.close()
    return playerdata

import sqlite3

# 初期データを追加する
def addplayerdata():
    players = [
        {"name": "Player1", "at_bats": 300, "hits": 90, "strikeouts": 45, "walks": 30, "total_bases": 150, "sacrifice_flies": 5},
        {"name": "Player2", "at_bats": 280, "hits": 78, "strikeouts": 50, "walks": 22, "total_bases": 126, "sacrifice_flies": 4},
        {"name": "Player3", "at_bats": 320, "hits": 102, "strikeouts": 38, "walks": 38, "total_bases": 176, "sacrifice_flies": 6},
        {"name": "Player4", "at_bats": 250, "hits": 63, "strikeouts": 50, "walks": 18, "total_bases": 100, "sacrifice_flies": 3},
        {"name": "Player5", "at_bats": 270, "hits": 73, "strikeouts": 46, "walks": 24, "total_bases": 113, "sacrifice_flies": 4},
        {"name": "Player6", "at_bats": 290, "hits": 84, "strikeouts": 46, "walks": 29, "total_bases": 136, "sacrifice_flies": 5},
        {"name": "Player7", "at_bats": 260, "hits": 68, "strikeouts": 49, "walks": 21, "total_bases": 112, "sacrifice_flies": 4},
        {"name": "Player8", "at_bats": 310, "hits": 96, "strikeouts": 40, "walks": 34, "total_bases": 161, "sacrifice_flies": 6},
        {"name": "Player9", "at_bats": 240, "hits": 58, "strikeouts": 50, "walks": 15, "total_bases": 91, "sacrifice_flies": 3},
    ]
    conn = sqlite3.connect('db/player.db')
    c = conn.cursor()
    try:
        for player in players:
            c.execute('INSERT INTO tb_pldata (name, at_bats, hits, k, walks, total_bases, sacrifice_flies) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                      (player["name"], player["at_bats"], player["hits"], player["strikeouts"], player["walks"], player["total_bases"], player["sacrifice_flies"]))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()



# def updateplayerdata():
#     # プレイヤーのデータを更新する
    
def main():
    addplayerdata()
    playerdata = getplayerdata()
    print(playerdata)


if __name__ == "__main__":
    main()