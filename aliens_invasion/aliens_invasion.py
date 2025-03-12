import sys
import pygame


from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()
        self.alien = pygame.sprite.Group()

        self._create_fleet()

        # Set the background color.
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullet()
            self._update_screen()
            self._update_aliens()
            self.clock.tick(60)

    def _check_event(self):
        """Renpond to keypresses and mouse evenets."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
        
    def _check_keydown_events(self, event):
        """Responds to keypress."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_ESCAPE:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responds to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullet) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)

    def _update_bullet(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet postion.
        self.bullet.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullet.copy():
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""
        # Remove any bullets and aliens that have been collided.
        collisions = pygame.sprite.groupcollide(
            self.bullet, self.alien, False, True
        )

        if not self.alien:
            # Destroy existing bullets and create new fleet.
            self.bullet.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.alien.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.alien):
            print("Ship hit!!!")

    def _create_fleet(self):
            """Create the fleet of aliens."""
            # Create an alien and keep adding aliens until there's no room lleft.
            # Spacing between aliens is one alien width and one alien height.
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size

            current_x, current_y = alien_width, alien_height
            while current_y < (self.settings.screen_height - 3 * alien_height):
                while current_x < (self.settings.screen_width - 2 * alien_width):
                    self._create_alien(current_x, current_y)
                    current_x += 2 * alien_width

                # Finished a roe; reset x value, and incremet y value.
                current_x = alien_width
                current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.alien.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.alien.sprites():
            if alien.check_edge():
                self._change_fleet_direction()

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.alien.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.alien.draw(self.screen)

        for bullet in self.bullet.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()