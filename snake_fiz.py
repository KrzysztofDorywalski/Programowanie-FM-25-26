# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:53:21 2024

@author: KD
"""

import pygame, sys, random
from pygame.math import Vector2

pygame.init()

BACK_COL = (170, 200, 95)

cell_size = 25
num_of_cells = 25

class Food:
    def __init__(self):
        self.position = self.gen_rand_pos()
    def draw(self):
        food_rect = pygame.Rect(self.position.x*cell_size, self.position.y*cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 20, 20), food_rect, 0, 7)
    def gen_rand_pos(self):
        pos = Vector2(random.randint(0, num_of_cells-1),random.randint(0, num_of_cells-1))
        return pos

class Snake:
    def __init__(self):
        self.start()
    def draw(self):
        for element in self.body:
            snake_rect = pygame.Rect(element.x*cell_size, element.y*cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (40, 50, 25), snake_rect, 0, 7)
    def update(self):
        if self.growth == True:
            self.body.insert(0, self.body[0]+self.direction)
            self.growth = False
        else:
            self.body = self.body[:-1]
            self.body.insert(0, self.body[0]+self.direction)
    def start(self):
        self.body = [Vector2(10,9), Vector2(9,9), Vector2(8,9)]
        self.direction = Vector2(1,0)
        self.growth = False
    
screen = pygame.display.set_mode((cell_size*num_of_cells,cell_size*num_of_cells))
pygame.display.set_caption('SSSnake!!!')

food = Food()
food2 = Food()
snake = Snake()

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

def game_over():
    print('Looooser!!!!')
    snake.start()
    food.position = food.gen_rand_pos()
    food2.position = food2.gen_rand_pos()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SNAKE_UPDATE:
            snake.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != Vector2(0,1):
                snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN and snake.direction != Vector2(0,-1):
                snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT and snake.direction != Vector2(-1,0):
                snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT and snake.direction != Vector2(1,0):
                snake.direction = Vector2(-1,0)
    screen.fill(BACK_COL)
    food.draw()
    food2.draw()
    snake.draw()
    if snake.body[0] == food.position:
        food.position = food.gen_rand_pos()
        snake.growth = True
    if snake.body[0] == food2.position:
        food2.position = food2.gen_rand_pos()
        snake.growth = True
    if snake.body[0].x == num_of_cells or snake.body[0].x == -1:
        game_over()
    if snake.body[0].y == num_of_cells or snake.body[0].y == -1:
        game_over()
    tail = snake.body[1:]
    if snake.body[0] in tail:
        game_over()
    pygame.display.update()







