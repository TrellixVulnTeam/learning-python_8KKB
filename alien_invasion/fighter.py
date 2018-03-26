import pygame
from pygame.sprite import Sprite


class Fighter(Sprite):

    def __init__(self, ai_settings, screen, *groups):
        """初始化战斗机并设置其初始位置"""
        super().__init__()
        self.screen = screen
        # 获取关于战斗机的设置
        self.ai_settings = ai_settings

        # 加载战斗机图像并获取其外接矩形
        self.image = pygame.image.load('images/fighter.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘战斗机放在屏幕底部中央
        self.center_fighter()

        # 在战斗机的属性centerx和bottom中存储小数值
        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # 移动标志
        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整战斗机的位置"""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.ai_settings.fighter_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.fighter_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.fighter_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.fighter_speed_factor

        # 更新rect对象
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom

    def blitme(self):
        """在指定位置绘制战斗机"""
        self.screen.blit(self.image, self.rect)

    def center_fighter(self):
        """将战机放在屏幕底部中央"""
        self.centerx = self.rect.centerx = self.screen_rect.centerx
        self.bottom = self.rect.bottom = self.screen_rect.bottom
