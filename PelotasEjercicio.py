import pygame
import random

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

FONDO = (241, 238, 238)
PELOTAS = (96, 249, 14 )


pelotas = [
    {'radius': 40, 'position': [width // 2, height // 2], 'velocity': [random.choice([-1, 1]), random.choice([-1, 1])]},
    {'radius': 20, 'position': [width // 4, height // 4], 'velocity': [random.choice([-1, 1]), random.choice([-1, 1])]},
    {'radius': 20, 'position': [width // 2, height // 4], 'velocity': [random.choice([-1, 1]), random.choice([-1, 1])]},
    {'radius': 40, 'position': [width // 4, height // 2], 'velocity': [random.choice([-1, 1]), random.choice([-1, 1])]}
]

def calcularPos(ball):
    
    ball['position'][0] += ball['velocity'][0]
    ball['position'][1] += ball['velocity'][1]

    
    if ball['position'][0] - ball['radius'] <= 0 or ball['position'][0] + ball['radius'] >= width:
        ball['velocity'][0] *= -1
    if ball['position'][1] - ball['radius'] <= 0 or ball['position'][1] + ball['radius'] >= height:
        ball['velocity'][1] *= -1
    for other_ball in pelotas:
        if other_ball != ball:
            distance = ((other_ball['position'][0] - ball['position'][0]) ** 2 +
                        (other_ball['position'][1] - ball['position'][1]) ** 2) ** 0.5
            if distance <= ball['radius'] + other_ball['radius']:
                if ball['radius'] > other_ball['radius'] / 2:
                    ball['radius'] /= 2
                else:
                    pelotas.remove(ball)
                    break

def dibujar(ball):
    pygame.draw.circle(screen, PELOTAS, ball['position'], int(ball['radius']))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(FONDO)
    for pelota in pelotas:
        calcularPos(pelota)
        dibujar(pelota)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
