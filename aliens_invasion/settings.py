class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initialize the game's statics settings"""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 680
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullllet settings
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60 ,60)
        self.bullet_allowed = 3

        # Aliens settings
        self.fleet_drop_speed = 10

        #How quickly the game speeds up.
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.alien_speed

