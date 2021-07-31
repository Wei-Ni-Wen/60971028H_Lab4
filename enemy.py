import math
from settings import *

# initialization
pygame.init()
color = Color()  # import color
image_enemy = pygame.image.load('images/enemy.png')  # import enemy's image

class Enemy:
    def __init__(self):     # set enemy's size, hp, point, move and path
        self.path = path
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.image = pygame.transform.scale(image_enemy, (40, 50))
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.health = 10
        self.max_health = 10
        self.path_index = 0
        self.move_count = 0
        self.stride = 1

    def draw_enemy(self, window):   # draw enemy
        window.blit(self.image, self.rect)
        self.draw_health_bar(window)

    def draw_health_bar(self, window):  # draw enemy's hp
        bar_width = self.rect.w * (self.health / self.max_health)
        max_bar_width = self.rect.w
        bar_height = 5
        pygame.draw.rect(window, color.red, [self.rect.x, self.rect.y - 10, max_bar_width, bar_height])
        pygame.draw.rect(window, color.green, [self.rect.x, self.rect.y - 10, bar_width, bar_height])

    def move(self):
        # count the distance of two points
        now_x, now_y = self.path[self.path_index]
        after_x, after_y = self.path[self.path_index + 1]
        distance = math.sqrt((now_x - after_x) ** 2 + (now_y - after_y) ** 2)
        max_count = int(distance / self.stride)
        # count the new point
        unit_vector_x = (after_x - now_x) / distance
        unit_vector_y = (after_y - now_y) / distance
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count

        if self.move_count <= max_count:
            self.rect.centerx = now_x + delta_x
            self.rect.centery = now_y + delta_y
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]

    def get_pos(self):
        return self.rect.center

    def get_hurt(self, damage):
        self.health -= damage

    def died(self):
        if self.health <= 0:
            return True
        return False

class EnemyGroup:
    def __init__(self):  # create enemy group
        self.gen_count = 0
        self.gen_period = 60
        self.reserved_members = []
        self.expedition = []

    def campaign(self):
        if self.gen_count > self.gen_period and self.reserved_members:
            self.expedition.append(self.reserved_members.pop())
            self.gen_count = 0
        else:
            self.gen_count += 1

    def add(self, num):
        self.reserved_members = [Enemy() for n in range(num)]

    def get(self):
        return self.expedition

    def is_empty(self):
        return False if self.reserved_members else True

    def retreat(self, enemy):
        self.expedition.remove(enemy)





