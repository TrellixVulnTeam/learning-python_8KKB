class Settings():
    """创建《敌机入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 战斗机的设置
        self.fighter_speed_factor = 1.5
        self.fighter_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullets_allowed = 100

        # 敌机设置
        self.enemy_speed_factor = 3
        self.fleet_drop_factor = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 加快游戏节奏的进度
        self.speedup_scale = 1.1
        # 敌机点数提高的速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行变化的设置"""
        self.fighter_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.enemy_speed_factor = 3

        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 记分
        self.enemy_points = 50

    def increase_speed(self):
        """提高速度设置和敌机速度"""
        self.fighter_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.enemy_speed_factor *= self.speedup_scale

        self.enemy_points = int(self.enemy_points * self.score_scale)
