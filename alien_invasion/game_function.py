import sys
from time import sleep

import pygame

from bullet import Bullet
from enemy import Enemy


def check_keydown_events(event, ai_settings, screen, fighter, bullets):
    """响应按键按下事件"""
    if event.key == pygame.K_RIGHT:
        # 允许向右移动飞机
        fighter.moving_right = True
    elif event.key == pygame.K_LEFT:
        fighter.moving_left = True
    elif event.key == pygame.K_UP:
        fighter.moving_up = True
    elif event.key == pygame.K_DOWN:
        fighter.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, fighter, bullets, False)
    elif event.key == pygame.K_b:
        fire_bullet(ai_settings, screen, fighter, bullets, True)


def check_keyup_events(event, fighter):
    if event.key == pygame.K_RIGHT:
        fighter.moving_right = False
    elif event.key == pygame.K_LEFT:
        fighter.moving_left = False
    elif event.key == pygame.K_UP:
        fighter.moving_up = False
    elif event.key == pygame.K_DOWN:
        fighter.moving_down = False


def check_events(ai_settings, screen, stats, scoreboard, play_button, fighter, enemies, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, fighter, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, fighter)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, scoreboard, play_button, fighter, enemies, bullets, mouse_x,
                              mouse_y)


def check_play_button(ai_settings, screen, stats, scoreboard, play_button, fighter, enemies, bullets, mouse_x, mouse_y):
    """在玩家单击按钮时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        scoreboard.prep_score()
        scoreboard.prep_high_score()
        scoreboard.prep_level()

        # 清空敌机列表和子弹列表
        enemies.empty()
        bullets.empty()

        # 创建一群新的敌机，并让战机居中
        create_fleet(ai_settings, screen, fighter, enemies)
        fighter.center_fighter()


def update_screen(ai_settings, screen, stats, scoreboard, fighter, enemies, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 绘制所有子弹
    for bullet in bullets.sprites():
        bullet.bliteme()
    # 绘制战斗机
    fighter.blitme()
    # 绘制敌机
    enemies.draw(screen)
    # 显示得分
    scoreboard.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, scoreboard, fighter, enemies, bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_enemy_collisions(ai_settings, screen, stats, scoreboard, fighter, enemies, bullets)


def check_bullet_enemy_collisions(ai_settings, screen, stats, scoreboard, fighter, enemies, bullets):
    """响应子弹和敌机的碰撞"""
    # 检查是否有子弹击中了敌机，若是则删除子弹和相应的敌机
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)

    if collisions:
        stats.score += ai_settings.enemy_points * len(collisions.values())
        scoreboard.prep_score()
        check_high_score(stats, scoreboard)

    # 如果消灭了整群敌机
    if len(enemies) == 0:
        # 删除现有子弹，并新建一群敌机
        bullets.empty()
        ai_settings.increase_speed()

        # 提高等级
        stats.level += 1
        scoreboard.prep_level()

        create_fleet(ai_settings, screen, fighter, enemies)


def fire_bullet(ai_settings, screen, fighter, bullets, is_bomb):
    """如果还没有达到极限，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        # 创建一颗子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, fighter, is_bomb)
        bullets.add(new_bullet)


def get_number_enemies_x(ai_settings, enemy_width):
    """计算每行可以容纳多少敌机"""
    available_space_x = ai_settings.screen_width - 2 * enemy_width
    number_enemies_x = int(available_space_x / (2 * enemy_width))
    return number_enemies_x


def get_number_rows(ai_settings, fighter_height, enemy_height):
    """计算屏幕可以容纳多少行敌机"""
    available_space_y = (ai_settings.screen_height - (3 * enemy_height) - fighter_height)
    number_rows = int(available_space_y / (2 * enemy_height))
    return number_rows


def create_enemy(ai_settings, screen, enemies, enemy_number, row_number):
    """创建一艘敌机，并放在当前行"""
    enemy = Enemy(ai_settings, screen)
    # 宽度涉及到小数，所以弄到另一个变量中
    enemy_width = enemy.rect.width
    enemy.x = enemy_width + 2 * enemy_width * enemy_number
    enemy.rect.x = enemy.x
    enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number

    enemies.add(enemy)


def create_fleet(ai_settings, screen, fighter, enemies):
    """创建敌机舰队"""
    # 创建一个敌机，并计算每行可以容纳多少敌机，以及可以容纳多少行
    enemy = Enemy(ai_settings, screen)
    number_enemies_x = get_number_enemies_x(ai_settings, enemy.rect.width)
    number_rows = get_number_rows(ai_settings, fighter.rect.height, enemy.rect.height)

    # 创建敌机群
    for row_number in range(number_rows):
        for enemy_number in range(number_enemies_x):
            create_enemy(ai_settings, screen, enemies, enemy_number, row_number)


def check_fleet_edges(ai_settings, enemies):
    """有敌机到达屏幕边缘时采取相应的措施"""
    for enemy in enemies:
        if enemy.check_edgs():
            change_fleet_direction(ai_settings, enemies)
            break


def change_fleet_direction(ai_settings, enemies):
    """将敌机群下移，并改变移动方向"""
    for enemy in enemies:
        enemy.rect.y += ai_settings.fleet_drop_factor
    ai_settings.fleet_direction *= -1


def fighter_hit(ai_settings, screen, stats, scoreboard, fighter, enemies, bullets):
    """响应被敌机碰撞到的战斗机"""
    # 将fighter_left - 1
    if stats.fighters_left > 0:
        stats.fighters_left -= 1

        # 更新记分牌
        scoreboard.prep_fighters()

        # 清空敌机列表和子弹列表
        enemies.empty()
        bullets.empty()

        # 创建一群新的敌机，并将战机放置在屏幕底端中央
        fighter.center_fighter()
        create_fleet(ai_settings, screen, fighter, enemies)

        # 暂停0.5s
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_enemies_bottom(ai_settings, stats, screen, scoreboard, fighter, enemies, bullets):
    """检查是否有敌机到达屏幕底端"""
    screen_rect = screen.get_rect()
    for enemy in enemies:
        if enemy.rect.bottom >= screen_rect.bottom:
            # 像战机被撞倒一样处理
            fighter_hit(ai_settings, screen, stats, scoreboard, fighter, enemies, bullets)
            break


def update_enemies(ai_settings, screen, stats, scoreboard, fighter, enemies, bullets):
    """检查是否有敌机位于屏幕边缘，并更新所有敌机位置"""
    check_fleet_edges(ai_settings, enemies)
    enemies.update()

    # 检测敌机和战斗机之间的碰撞
    if pygame.sprite.spritecollideany(fighter, enemies):
        fighter_hit(ai_settings, screen, stats, scoreboard, fighter, enemies, bullets)

    # 检查是否有敌机到达屏幕底端
    check_enemies_bottom(ai_settings, stats, screen, scoreboard, fighter, enemies, bullets)


def check_high_score(stats, scoreboard):
    """检查是否产生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()
