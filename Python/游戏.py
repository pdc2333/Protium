import pygame
import math

# --- 配置 ---
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 简化的路径点
PATH = [(100, 100), (700, 100), (700, 500), (100, 500)]

# --- 类定义 ---

class Enemy:
    def __init__(self, path):
        self.path = path
        self.path_index = 0
        self.x, self.y = self.path[0]
        self.speed = 2
        self.health = 100
        self.radius = 15
        self.alive = True

    def update(self):
        if self.path_index < len(self.path) - 1:
            target_x, target_y = self.path[self.path_index + 1]
            dx, dy = target_x - self.x, target_y - self.y
            dist = math.sqrt(dx**2 + dy**2)
            
            if dist < self.speed:
                self.path_index += 1
            else:
                # 简单的移动逻辑
                self.x += (dx / dist) * self.speed
                self.y += (dy / dist) * self.speed
        else:
            # 到达终点，算作漏怪
            self.alive = False 
            print("敌人到达终点！")

    def draw(self, win):
        if self.alive:
            pygame.draw.circle(win, RED, (int(self.x), int(self.y)), self.radius)
            # 简易血条
            pygame.draw.rect(win, BLACK, (self.x - 15, self.y - 25, 30, 5))
            pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 25, 30 * (self.health / 100), 5))

class Projectile:
    def __init__(self, x, y, target, damage):
        self.x, self.y = x, y
        self.target = target
        self.speed = 10
        self.damage = damage
        self.radius = 5
        self.active = True

    def update(self):
        if not self.target.alive:
            self.active = False
            return

        dx, dy = self.target.x - self.x, self.target.y - self.y
        dist = math.sqrt(dx**2 + dy**2)

        if dist < self.target.radius + self.radius:
            self.target.health -= self.damage
            if self.target.health <= 0:
                self.target.alive = False
                print("敌人被击败！")
            self.active = False # 子弹击中后消失
        else:
            self.x += (dx / dist) * self.speed
            self.y += (dy / dist) * self.speed

    def draw(self, win):
        if self.active:
            pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), self.radius)

class Tower:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.range = 150
        self.damage = 20
        self.cooldown = 1000  # 毫秒
        self.last_shot_time = pygame.time.get_ticks()
        self.projectiles = []

    def update(self, enemies, current_time):
        # 寻找范围内的第一个敌人
        target = None
        for enemy in enemies:
            if enemy.alive:
                dist = math.sqrt((enemy.x - self.x)**2 + (enemy.y - self.y)**2)
                if dist <= self.range:
                    target = enemy
                    break
        
        # 射击逻辑
        if target and current_time - self.last_shot_time > self.cooldown:
            self.projectiles.append(Projectile(self.x, self.y, target, self.damage))
            self.last_shot_time = current_time
        
        # 更新子弹
        for p in self.projectiles:
            p.update()
        self.projectiles = [p for p in self.projectiles if p.active] # 清理失效子弹

    def draw(self, win):
        # 画塔身
        pygame.draw.rect(win, BLUE, (self.x - 20, self.y - 20, 40, 40))
        # 画攻击范围 (可选，用于调试)
        pygame.draw.circle(win, BLUE, (self.x, self.y), self.range, 1)
        # 画子弹
        for p in self.projectiles:
            p.draw(win)

# --- 主游戏循环 ---

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("简易塔防 Demo")
    clock = pygame.time.Clock()

    # 初始化游戏对象
    enemies = []
    towers = []
    
    # 在地图中央放置一个塔
    towers.append(Tower(400, 300))

    # 定时生成敌人
    ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ENEMY_SPAWN_EVENT, 2000) # 每2秒生成一个

    run = True
    while run:
        current_time = pygame.time.get_ticks()
        clock.tick(FPS)

        # --- 事件处理 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == ENEMY_SPAWN_EVENT:
                enemies.append(Enemy(PATH))
            # 点击鼠标放置新塔 (简单示例)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                towers.append(Tower(mx, my))

        # --- 更新 ---
        for enemy in enemies:
            enemy.update()
        
        # 清理死亡或到达终点的敌人
        enemies = [e for e in enemies if e.alive]

        for tower in towers:
            tower.update(enemies, current_time)

        # --- 绘制 ---
        win.fill(WHITE)

        # 绘制路径线
        if len(PATH) > 1:
            pygame.draw.lines(win, (200, 200, 200), False, PATH, 5)

        for enemy in enemies:
            enemy.draw(win)
        
        for tower in towers:
            tower.draw(win)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()