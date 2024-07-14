import pygame
import sys
from batting import at_bat, advance_bases

# Pygameの初期化
pygame.init()

# 画面サイズの設定
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("シンプル野球シミュレーション")

# フォントの設定
font = pygame.font.Font(None, 36)

# 選手データ
players = [
    {"name": "Player1", "AVG": 0.300, "OBP": 0.370, "SLG": 0.500, "K%": 0.15, "BB%": 0.10, "single_rate": 0.5, "double_rate": 0.2, "triple_rate": 0.05, "home_run_rate": 0.05},
    {"name": "Player2", "AVG": 0.280, "OBP": 0.340, "SLG": 0.450, "K%": 0.18, "BB%": 0.08, "single_rate": 0.6, "double_rate": 0.15, "triple_rate": 0.05, "home_run_rate": 0.05},
    {"name": "Player3", "AVG": 0.320, "OBP": 0.390, "SLG": 0.550, "K%": 0.12, "BB%": 0.12, "single_rate": 0.4, "double_rate": 0.25, "triple_rate": 0.1, "home_run_rate": 0.1},
    {"name": "Player4", "AVG": 0.250, "OBP": 0.310, "SLG": 0.400, "K%": 0.20, "BB%": 0.07, "single_rate": 0.5, "double_rate": 0.2, "triple_rate": 0.05, "home_run_rate": 0.05},
    {"name": "Player5", "AVG": 0.270, "OBP": 0.330, "SLG": 0.420, "K%": 0.17, "BB%": 0.09, "single_rate": 0.55, "double_rate": 0.15, "triple_rate": 0.05, "home_run_rate": 0.05},
    {"name": "Player6", "AVG": 0.290, "OBP": 0.350, "SLG": 0.470, "K%": 0.16, "BB%": 0.10, "single_rate": 0.5, "double_rate": 0.2, "triple_rate": 0.05, "home_run_rate": 0.05},
    {"name": "Player7", "AVG": 0.260, "OBP": 0.320, "SLG": 0.430, "K%": 0.19, "BB%": 0.08, "single_rate": 0.55, "double_rate": 0.15, "triple_rate": 0.05, "home_run_rate": 0.05},
    {"name": "Player8", "AVG": 0.310, "OBP": 0.380, "SLG": 0.520, "K%": 0.13, "BB%": 0.11, "single_rate": 0.45, "double_rate": 0.2, "triple_rate": 0.1, "home_run_rate": 0.1},
    {"name": "Player9", "AVG": 0.240, "OBP": 0.300, "SLG": 0.380, "K%": 0.21, "BB%": 0.06, "single_rate": 0.6, "double_rate": 0.1, "triple_rate": 0.05, "home_run_rate": 0.05},
]

# ゲームの状態
inning = 1
outs = 0
bases = [False, False, False]  # 一塁、二塁、三塁
score = 0
current_player_index = 0
game_active = False
sign = "none"  # サインの初期値
strikes = 0
balls = 0

# ボタンの描画関数
def draw_button(text, x, y, width, height, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    color = (0, 200, 0) if action == sign else (0, 255, 0)
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surf = font.render(text, True, (0, 0, 0))
    screen.blit(text_surf, (x + 10, y + 10))
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1 and action is not None:
            return action
    return None

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_active:
                game_active = True
                current_player = players[current_player_index]
                hittype, hit, balls, strikes, outs = at_bat(current_player, sign)
                if hit > 0:
                    bases, score = advance_bases(hit, bases, score)
                    
                if balls < 4 and strikes < 3:
                    game_active = False
                else:
                    current_player_index = (current_player_index + 1) % 9
                    balls = 0
                    strikes = 0
                    game_active = False
    
    # 画面の背景色を設定
    screen.fill((0, 128, 0))
    
    # 野球場のひし形を描画
    pygame.draw.polygon(screen, (255, 255, 255), [(400, 100), (700, 300), (400, 500), (100, 300)], 5)
    
    # 塁の表示
    base_positions = [(400, 100), (700, 300), (400, 500), (100, 300)]
    for i, base in enumerate(bases):
        color = (255, 0, 0) if base else (255, 255, 255)
        pygame.draw.circle(screen, color, base_positions[i], 20)
    
    # スコアとアウトの表示
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    outs_text = font.render(f"Outs: {outs}", True, (255, 255, 255))
    screen.blit(score_text, (50, 50))
    screen.blit(outs_text, (50, 100))
    
    # 打席に立っている打者の名前と打率の表示
    current_player = players[current_player_index]
    player_text = font.render(f"At Bat: {current_player['name']} - AVG: {current_player['AVG']}", True, (255, 255, 255))
    screen.blit(player_text, (50, 150))
    
    # ボール・ストライクのカウント表示
    count_text = font.render(f"Balls: {balls} Strikes: {strikes}", True, (255, 255, 255))
    screen.blit(count_text, (50, 200))
    
    # 画面の更新
    pygame.display.flip()

pygame.quit()
sys.exit()
