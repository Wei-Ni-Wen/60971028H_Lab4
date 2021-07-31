from settings import *
from enemy import EnemyGroup
from tower import TowerGroup

# initialization
pygame.init()
pygame.display.set_caption("My TD game")  # show title
color = Color()     # import color
image = Image()     # import image

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIN_width, WIN_height))  # set window size
        self.image_BG = pygame.transform.scale(image.BG, (WIN_width, WIN_height))  # set image_background size
        # set image_hp and image_hpgray size
        self.hp_images = [pygame.transform.scale(image.hp, (40, 40)),
                          pygame.transform.scale(image.hpgray, (40, 40))]
        self.enemies = EnemyGroup()
        self.towers = TowerGroup()
        self.base = pygame.Rect(430, 90, 195, 130)

    def select(self, x, y):
        pass

    def collide_base(self, enemy):
        # set collide_base's point and collide_base's size
        en_x, en_y = enemy.get_pos()
        x, y = self.base.center
        width, height = self.base.w, self.base.h
        if x - width//2 < en_x < x + width//2 and y - height//2 < en_y < y + height//2:
            return True
        return False

    def draw(self):
        # draw background and menu
        self.window.blit(image.BG, (0, 0))
        pygame.draw.rect(self.window, color.black, [0, 0, WIN_width, 80])
        self.window.blit(image.muse, (700, 0))
        self.window.blit(image.sound, (780, 0))
        self.window.blit(image.conti, (860, 0))
        self.window.blit(image.pause, (940, 0))
        # draw enemy
        for en in self.enemies.get():
            en.draw_enemy(self.window)
            en.draw_health_bar(self.window)
        # draw tower
        for tw in self.towers.get():
            tw.draw(self.window)

    def game_run(self):
        # game loop
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(FPS)
            # event loop
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # quit the game
                if event.type == pygame.QUIT:
                    run = False
                # generate enemy of the next wave
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n and self.enemies.is_empty():
                        self.enemies.add(5)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.select(self.towers, x, y)
            # tower loop
            for tw in self.towers.get():
                tw.attack(self.enemies)
            # enemy loop
            self.enemies.campaign()
            for en in self.enemies.get():   # let enemies move
                en.move()
                # delete the enemy if it die
                if en.died():
                    self.enemies.retreat(en)
                # delete the enemy if it reach the base
                if self.collide_base(en):
                    self.enemies.retreat(en)
            # draw everything
            self.draw()
            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()
