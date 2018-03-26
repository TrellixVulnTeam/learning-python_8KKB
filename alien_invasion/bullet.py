import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹类"""

    def __init__(self, ai_settings, screen, fighter, is_bomb):
        """在战斗机所处的位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen

        bullet_img_uri = 'images/bullet.png'
        bomb_img_uri = 'images/bomb.png'
        # 加载子弹图像并获取其外接矩形
        if not is_bomb:
            self.image = pygame.image.load(bullet_img_uri)
        else:
            self.image = pygame.image.load(bomb_img_uri)
        self.rect = self.image.get_rect()
        # 设置子弹初始位置
        self.rect.centerx = fighter.rect.centerx
        self.rect.top = fighter.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        # 加载其飞行速度
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def bliteme(self):
        self.screen.blit(self.image, self.rect)
