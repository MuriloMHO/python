class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initialize the game's settings"""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 680
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 3

        # Bullllet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60 ,60)
        self.bullet_allowed = 3