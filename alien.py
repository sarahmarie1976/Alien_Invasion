import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/Aliens.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    # Place this function inside your main game class where the fleet is created.
    def _create_fleet(self):
        """Create a fleet of aliens that is centered and has vertical breathing space."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)

        # Calculate the center offset
        fleet_width = number_aliens_x * (2 * alien_width)
        margin_left = (self.settings.screen_width - fleet_width) // 2

        # Calculate number of rows and the starting y position for some breathing space
        available_space_y = self.settings.screen_height - (3 * alien_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create each row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number, margin_left, alien_width, alien_height)

    def _create_alien(self, alien_number, row_number, margin_left, alien_width, alien_height):
        """Create an alien and place it in the row with proper alignment."""
        alien = Alien(self)
        alien.x = margin_left + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)
