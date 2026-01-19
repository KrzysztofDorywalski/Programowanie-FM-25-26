import pygame
import random
import sys

# ---------- USTAWIENIA ----------
WIDTH = 600
HEIGHT = 400
FPS = 60

WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
BLACK = (0, 0, 0)

# ---------- INICJALIZACJA ----------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zimowa Ucieczka Bałwana")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 20)
big_font = pygame.font.SysFont("arial", 40)

# ---------- KLASY ----------

class Snowman:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 80
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        self.x = max(40, min(WIDTH - 40, self.x))

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), 25)
        pygame.draw.circle(screen, WHITE, (self.x, self.y - 35), 20)
        pygame.draw.circle(screen, WHITE, (self.x, self.y - 65), 15)


class Snowflake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-200, 0)
        self.speed = random.randint(2, 4)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.reset()

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), 5)


class Drop:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-300, 0)
        self.speed = random.randint(3, 6)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.reset()

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), 6)


# ---------- FUNKCJE ----------

def check_collision(player, snowflakes, drops):
    global score, lives, game_over

    for s in snowflakes:
        if distance(player.x, player.y, s.x, s.y) < 30:
            score += 1
            s.reset()

    for d in drops:
        if distance(player.x, player.y, d.x, d.y) < 30:
            lives -= 1
            d.reset()
            if lives <= 0:
                game_over = True


def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5


def draw_hud():
    score_text = font.render(f"Punkty: {score}", True, BLACK)
    lives_text = font.render(f"Zycia: {lives}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 35))


def draw_game_over():
    text = big_font.render("GAME OVER", True, BLACK)
    score_text = font.render(f"Wynik: {score}", True, BLACK)
    screen.blit(text, (WIDTH//2 - 100, HEIGHT//2 - 20))
    screen.blit(score_text, (WIDTH//2 - 50, HEIGHT//2 + 20))


# ---------- START GRY ----------

player = Snowman()
snowflakes = [Snowflake() for _ in range(5)]
drops = [Drop() for _ in range(3)]

score = 0
lives = 3
game_over = False

# ---------- PĘTLA GŁÓWNA ----------

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    screen.fill((180, 220, 255))  # zimowe niebo

    if not game_over:
        player.move(keys)
        player.draw()

        for s in snowflakes:
            s.fall()
            s.draw()

        for d in drops:
            d.fall()
            d.draw()

        check_collision(player, snowflakes, drops)
        draw_hud()

    else:
        draw_game_over()

    pygame.display.flip()
