import sys

import pygame

class AlienInvasion:
  """"Initialize class to manage game assets and behavior."""
  
  def __init__(self):
    """"Initialize the game, & create game resources."""
    pygame.init()
    self.clock = pygame.time.Clock()
    
    self.screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color. 
    self.bg_color = (230, 230, 230)
    
    
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      # What for keyboard & mouse events. 
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
          
        # Redraw the screen during each pass through the loop. 
        self.screen.file(self.bg_color)
          
        # Make the most recently drawn screen visible. 
        pygame.display.flip()
        self.clock.tick(60)
        
if __name__ == '__main__':
  # Make a game instance, & run the game.add()
  ai = AlienInvasion()
  ai.run_game()