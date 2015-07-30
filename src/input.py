import pygame


def processInput():
    user_input = {}
    user_input["MoveUp"] = False
    user_input["MoveDown"] = False
    user_input["MoveLeft"] = False
    user_input["MoveRight"] = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                user_input["MoveLeft"] = True
            if event.key == pygame.K_UP:
                user_input["MoveUp"] = True
            if event.key == pygame.K_RIGHT:
                user_input["MoveRight"] = True
            if event.key == pygame.K_DOWN:
                user_input["MoveDown"] = True
    return user_input

