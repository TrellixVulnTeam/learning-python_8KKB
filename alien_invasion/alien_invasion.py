import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from fighter import Fighter
import game_function as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 设置窗口标题
    pygame.display.set_caption("Enemy Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, stats)

    # 创建一艘新的战斗机、一个子弹编组和一个敌机编组
    fighter = Fighter(ai_settings, screen)
    bullets = Group()
    enemies = Group()

    # 创建敌机舰队
    gf.create_fleet(ai_settings, screen, fighter, enemies)

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, scoreboard, play_button, fighter, enemies, bullets)

        if stats.game_active:
            fighter.update()
            gf.update_bullets(ai_settings, screen, stats, scoreboard, fighter, enemies, bullets)
            gf.update_enemies(ai_settings, screen, stats, scoreboard, fighter, enemies, bullets)

        gf.update_screen(ai_settings, screen, stats, scoreboard, fighter, enemies, bullets, play_button)


run_game()
