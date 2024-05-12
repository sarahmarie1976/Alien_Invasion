class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (5, 8, 54)

        # Ship settings.
        self.ship_speed = 1.5
        
        # Bullet settings 
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (11, 224, 47)
        self.bullets_allowed = 30  # Add this line to define maximum bullets allowed
