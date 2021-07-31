import math
from settings import *

# initialization
pygame.init()
color = Color()  # import color
image_tower = pygame.image.load('images/rapid_test.png')  # import tower's image

class Circle:
    def __init__(self, center, radius):     # set  center, radius
        self.center = center
        self.radius = radius

    def collide(self, enemy):
        tower_x, tower_y = self.center
        enemy_x, enemy_y = enemy.get_pos()
        # calculate the distance between towers and enemies
        distance_ET = math.sqrt((enemy_x - tower_x) ** 2 + (enemy_y - tower_y) ** 2)
        # if the enemy is in the attack_circle, return true
        if distance_ET <= self.radius:
            return True
        else:
            return False

    def draw_transparent(self, window):  # draw the attack_circle
        transparent_surface = pygame.Surface((WIN_width, WIN_height), pygame.SRCALPHA)
        transparency = 50
        pygame.draw.circle(transparent_surface, (255, 255, 255, transparency), self.center, self.radius)
        window.blit(transparent_surface, (0, 0))

class Tower:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(image_tower, (70, 70))  # set tower's size
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # set center of the tower
        self.range = 150  # set tower's attack range
        self.damage = 2   # set tower damage
        self.attack_circle = Circle(self.rect.center, self.range)  # set attack circle (class Circle())
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()
        self.is_selected = True  # the state of whether the tower is selected
        self.type = "tower"

    def is_cool_down(self):  # calculate the cd time
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
            return False
        else:
            self.cd_count = 0
            return True

    def attack(self, enemy_group):
        enemy_list = enemy_group.get()  # get enemy's list
        enemy_sum = len(enemy_list)  # save the number of enemies
        if self.is_cool_down():  # if tower is not cool down
            if enemy_list:  # if enemy_list is not None
                for n in range(0, enemy_sum):
                    target = enemy_list[n]  # target is the first enemy
                    if self.attack_circle.collide(target):
                        target.get_hurt(self.damage)
                        break

    def is_clicked(self, x, y):
        # check if mouse position is on the tower image
        pass

    def get_selected(self, is_selected):
        self.is_selected = is_selected

    def draw(self, window):
        # draw attack circle
        if self.is_clicked:
            self.attack_circle.draw_transparent(window)
        # draw tower
        window.blit(self.image, self.rect)

class TowerGroup:
    def __init__(self):  # set towers' point
        self.constructed_tower = [Tower(250, 380), Tower(420, 400), Tower(600, 400)]

    def get(self):  # return towers' point
        return self.constructed_tower

