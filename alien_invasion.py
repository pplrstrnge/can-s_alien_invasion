import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()

        self.settings = Settings()
        

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height))

        pygame.display.set_caption("Can's Alien Invasion")
        self.ship = Ship(self)


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
                
    def _check_events(self):
         #watch keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False


    def _update_screen(self):
        #Redraw screen during each pass through the loop
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        
        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
   #Make game instance, and run the game
   ai = AlienInvasion()
   ai.run_game()