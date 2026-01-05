import pygame
import sys
import random
import math

# 初始化pygame
pygame.init()

# 屏幕设置
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("熵增粒子模拟系统 - 从有序到无序")
clock = pygame.time.Clock()

# 颜色定义
BACKGROUND = (15, 20, 35)
CONTAINER_COLOR = (40, 45, 70)
CONTAINER_BORDER = (80, 130, 250)
PARTICLE_COLOR = (100, 180, 255)
PARTICLE_HIGHLIGHT = (255, 120, 100)
UI_BG = (25, 30, 50)
UI_BORDER = (60, 100, 180)
SLIDER_BG = (40, 50, 80)
SLIDER_FG = (70, 150, 255)
BUTTON_COLOR = (40, 120, 220)
BUTTON_HOVER = (60, 140, 255)
TEXT_COLOR = (220, 230, 255)
GRID_COLOR = (30, 40, 65, 150)

# 字体
font = pygame.font.SysFont('microsoftyahei', 24)
title_font = pygame.font.SysFont('microsoftyahei', 32, bold=True)

class Slider:
    """自定义滑块控件"""
    def __init__(self, x, y, width, min_val, max_val, initial_val, label):
        self.rect = pygame.Rect(x, y, width, 10)
        self.knob_radius = 12
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.label = label
        self.knob_x = x + (initial_val - min_val) / (max_val - min_val) * width
        self.dragging = False
        
    def draw(self, surface):
        # 绘制滑块轨道
        pygame.draw.rect(surface, SLIDER_BG, self.rect, border_radius=5)
        pygame.draw.rect(surface, UI_BORDER, self.rect, 2, border_radius=5)
        
        # 绘制滑块旋钮
        knob_pos = (int(self.knob_x), self.rect.centery)
        pygame.draw.circle(surface, SLIDER_FG, knob_pos, self.knob_radius)
        pygame.draw.circle(surface, (255, 255, 255), knob_pos, self.knob_radius, 2)
        
        # 绘制标签和值
        label_text = font.render(f"{self.label}: {self.value:.2f}", True, TEXT_COLOR)
        surface.blit(label_text, (self.rect.x, self.rect.y - 30))
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                knob_rect = pygame.Rect(
                    self.knob_x - self.knob_radius,
                    self.rect.centery - self.knob_radius,
                    self.knob_radius * 2,
                    self.knob_radius * 2
                )
                if knob_rect.collidepoint(mouse_pos):
                    self.dragging = True
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
                
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x = pygame.mouse.get_pos()[0]
                # 限制滑块在轨道范围内
                self.knob_x = max(self.rect.left, min(mouse_x, self.rect.right))
                # 计算对应的值
                self.value = self.min_val + (self.knob_x - self.rect.left) / self.rect.width * (self.max_val - self.min_val)
                return True
        return False

class Button:
    """自定义按钮控件"""
    def __init__(self, x, y, width, height, text, color=BUTTON_COLOR):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hovered = False
        
    def draw(self, surface):
        color = BUTTON_HOVER if self.hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, UI_BORDER, self.rect, 2, border_radius=8)
        
        text_surf = font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.hovered:
                return True
        return False

class Particle:
    """粒子类，代表一个运动中的微观粒子"""
    def __init__(self, x, y, container):
        self.x = x
        self.y = y
        # 初始速度设为0，等待用户启动
        self.vx = 0
        self.vy = 0
        self.radius = 4
        self.color = PARTICLE_COLOR
        self.container = container
        self.trail = []  # 轨迹记录
        self.max_trail = 10  # 轨迹最大长度
        
    def update(self, temperature, container):
        # 如果粒子有速度，则更新位置并记录轨迹
        if abs(self.vx) > 0 or abs(self.vy) > 0:
            self.x += self.vx * temperature
            self.y += self.vy * temperature
            
            # 记录轨迹
            self.trail.append((self.x, self.y))
            if len(self.trail) > self.max_trail:
                self.trail.pop(0)
        
        # 边界碰撞检测 - 完全弹性碰撞
        if self.x - self.radius <= container.left:
            self.x = container.left + self.radius
            self.vx = abs(self.vx)
        elif self.x + self.radius >= container.right:
            self.x = container.right - self.radius
            self.vx = -abs(self.vx)
            
        if self.y - self.radius <= container.top:
            self.y = container.top + self.radius
            self.vy = abs(self.vy)
        elif self.y + self.radius >= container.bottom:
            self.y = container.bottom - self.radius
            self.vy = -abs(self.vy)
            
    def draw(self, surface):
        # 绘制轨迹
        for i, (trail_x, trail_y) in enumerate(self.trail):
            alpha = int(150 * (i / len(self.trail)))
            trail_color = (self.color[0], self.color[1], self.color[2], alpha)
            trail_surf = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
            pygame.draw.circle(trail_surf, trail_color, (self.radius, self.radius), self.radius * (i/len(self.trail)))
            surface.blit(trail_surf, (int(trail_x - self.radius), int(trail_y - self.radius)))
        
        # 绘制粒子
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.radius, 1)

class ParticleSystem:
    """粒子系统管理器"""
    def __init__(self):
        self.container = pygame.Rect(50, 50, 700, 600)
        self.particles = []
        self.simulation_active = False
        self.entropy_history = []
        self.max_history = 100
        
    def create_ordered_particles(self, num_particles):
        """创建有序排列的粒子（初始低熵状态）"""
        self.particles = []
        left_half = self.container.left + self.container.width // 4
        
        for _ in range(num_particles):
            x = random.randint(self.container.left + 10, left_half)
            y = random.randint(self.container.top + 10, self.container.bottom - 10)
            particle = Particle(x, y, self.container)
            self.particles.append(particle)
            
    def start_simulation(self, temperature):
        """启动模拟，给粒子赋予随机速度"""
        if not self.simulation_active:
            for particle in self.particles:
                # 速度大小与温度相关，方向随机
                speed = 0.5 + temperature * 2
                angle = random.uniform(0, 2 * math.pi)
                particle.vx = math.cos(angle) * speed
                particle.vy = math.sin(angle) * speed
            self.simulation_active = True
            
    def reset(self):
        """重置粒子到初始有序状态"""
        self.simulation_active = False
        self.entropy_history = []
        self.create_ordered_particles(200)
        
    def update(self, temperature):
        """更新所有粒子状态"""
        if self.simulation_active:
            for particle in self.particles:
                particle.update(temperature, self.container)
                
            # 计算并记录当前熵值
            self.calculate_entropy()
            
    def calculate_entropy(self):
        """估算系统熵值（基于粒子分布的均匀程度）"""
        if not self.particles:
            return 0
            
        # 将容器分为网格，统计每个网格的粒子数
        grid_size = 8
        grid_width = self.container.width // grid_size
        grid_height = self.container.height // grid_size
        grid = [[0] * grid_height for _ in range(grid_width)]
        
        # 统计每个网格中的粒子数
        for particle in self.particles:
            grid_x = int((particle.x - self.container.left) // grid_size)
            grid_y = int((particle.y - self.container.top) // grid_size)
            if 0 <= grid_x < grid_width and 0 <= grid_y < grid_height:
                grid[grid_x][grid_y] += 1
        
        # 计算概率分布
        total_particles = len(self.particles)
        entropy = 0
        for row in grid:
            for count in row:
                if count > 0:
                    p = count / total_particles
                    entropy -= p * math.log(p)
                    
        # 归一化到0-1范围
        max_entropy = math.log(grid_width * grid_height)
        normalized_entropy = entropy / max_entropy if max_entropy > 0 else 0
        
        # 记录熵值历史
        self.entropy_history.append(normalized_entropy)
        if len(self.entropy_history) > self.max_history:
            self.entropy_history.pop(0)
            
        return normalized_entropy
    
    def draw(self, surface):
        # 绘制容器背景和网格
        pygame.draw.rect(surface, CONTAINER_COLOR, self.container)
        
        # 绘制网格线
        grid_size = 50
        for x in range(self.container.left, self.container.right, grid_size):
            pygame.draw.line(surface, GRID_COLOR, (x, self.container.top), (x, self.container.bottom), 1)
        for y in range(self.container.top, self.container.bottom, grid_size):
            pygame.draw.line(surface, GRID_COLOR, (self.container.left, y), (self.container.right, y), 1)
            
        pygame.draw.rect(surface, CONTAINER_BORDER, self.container, 3)
        
        # 绘制所有粒子
        for particle in self.particles:
            particle.draw(surface)
            
        # 绘制熵值曲线
        self.draw_entropy_graph(surface)
        
    def draw_entropy_graph(self, surface):
        """绘制熵值变化曲线"""
        if len(self.entropy_history) < 2:
            return
            
        graph_rect = pygame.Rect(
            self.container.right + 20,
            self.container.bottom - 150,
            250,
            130
        )
        
        # 绘制背景
        pygame.draw.rect(surface, UI_BG, graph_rect, border_radius=5)
        pygame.draw.rect(surface, UI_BORDER, graph_rect, 2, border_radius=5)
        
        # 绘制标题
        title = font.render("熵值变化", True, TEXT_COLOR)
        surface.blit(title, (graph_rect.x + 10, graph_rect.y + 5))
        
        # 绘制坐标轴
        pygame.draw.line(surface, TEXT_COLOR, 
                        (graph_rect.x + 10, graph_rect.bottom - 20),
                        (graph_rect.right - 10, graph_rect.bottom - 20), 2)
        pygame.draw.line(surface, TEXT_COLOR,
                        (graph_rect.x + 10, graph_rect.bottom - 20),
                        (graph_rect.x + 10, graph_rect.y + 25), 2)
        
        # 绘制曲线
        points = []
        for i, entropy in enumerate(self.entropy_history):
            x = graph_rect.x + 10 + (i / len(self.entropy_history)) * (graph_rect.width - 30)
            y = graph_rect.bottom - 20 - entropy * (graph_rect.height - 45)
            points.append((x, y))
            
        if len(points) >= 2:
            pygame.draw.lines(surface, (255, 100, 100), False, points, 3)
            
        # 绘制当前熵值
        current_entropy = self.entropy_history[-1] if self.entropy_history else 0
        entropy_text = font.render(f"当前熵值: {current_entropy:.3f}", True, (255, 150, 150))
        surface.blit(entropy_text, (graph_rect.x + 10, graph_rect.bottom - 40))

def main():
    # 创建粒子系统
    particle_system = ParticleSystem()
    particle_system.create_ordered_particles(200)  # 初始创建200个粒子
    
    # 创建UI控件
    temp_slider = Slider(780, 100, 200, 0.1, 3.0, 1.0, "温度")
    volume_slider = Slider(780, 180, 200, 0.5, 2.0, 1.0, "体积")
    
    start_button = Button(780, 260, 200, 40, "启动模拟")
    reset_button = Button(780, 320, 200, 40, "重置系统")
    
    running = True
    
    while running:
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            # 处理滑块事件
            if temp_slider.handle_event(event):
                pass
                
            if volume_slider.handle_event(event):
                # 更新容器大小
                new_width = int(700 * volume_slider.value)
                new_height = int(600 * volume_slider.value)
                particle_system.container.width = new_width
                particle_system.container.height = new_height
                
            # 处理按钮事件
            if start_button.handle_event(event):
                particle_system.start_simulation(temp_slider.value)
                
            if reset_button.handle_event(event):
                particle_system.reset()
                temp_slider.value = 1.0
                temp_slider.knob_x = temp_slider.rect.left + (1.0 - temp_slider.min_val) / (temp_slider.max_val - temp_slider.min_val) * temp_slider.rect.width
                volume_slider.value = 1.0
                volume_slider.knob_x = volume_slider.rect.left + (1.0 - volume_slider.min_val) / (volume_slider.max_val - volume_slider.min_val) * volume_slider.rect.width
                
            # 按钮悬停检测
            start_button.handle_event(event)
            reset_button.handle_event(event)
        
        # 更新粒子系统
        particle_system.update(temp_slider.value)
        
        # 绘制
        screen.fill(BACKGROUND)
        
        # 绘制标题
        title = title_font.render("熵增可视化：微观粒子运动模拟", True, (220, 230, 255))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 10))
        
        # 绘制说明文字
        instructions = [
            "• 初始状态：粒子集中在左侧（低熵）",
            "• 启动模拟：粒子开始扩散（熵增加）",
            "• 最终状态：均匀分布（高熵平衡态）",
            "• 调节温度：改变粒子运动速度",
            "• 调节体积：改变系统容器大小"
        ]
        
        for i, text in enumerate(instructions):
            text_surface = font.render(text, True, (180, 200, 255))
            screen.blit(text_surface, (780, 380 + i * 30))
        
        # 绘制粒子系统和UI控件
        particle_system.draw(screen)
        temp_slider.draw(screen)
        volume_slider.draw(screen)
        start_button.draw(screen)
        reset_button.draw(screen)
        
        # 绘制系统状态
        status = "模拟中" if particle_system.simulation_active else "已暂停"
        status_color = (100, 255, 100) if particle_system.simulation_active else (255, 150, 100)
        status_text = font.render(f"状态: {status}", True, status_color)
        screen.blit(status_text, (780, 550))
        
        particle_count = font.render(f"粒子数: {len(particle_system.particles)}", True, TEXT_COLOR)
        screen.blit(particle_count, (780, 580))
        
        # 绘制物理参数
        params_text = font.render(f"温度因子: {temp_slider.value:.2f}", True, TEXT_COLOR)
        screen.blit(params_text, (780, 610))
        
        params_text2 = font.render(f"体积因子: {volume_slider.value:.2f}", True, TEXT_COLOR)
        screen.blit(params_text2, (780, 640))
        
        # 更新显示
        pygame.display.flip()
        clock.tick(60)  # 60 FPS
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()