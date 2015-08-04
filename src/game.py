import pygame
import pkmath
import pkcolor

# TODO(hugo): add a tilemap and basic collision detection to handle a level
class Player:
    """ class to handle all the details about a player entity """
    def __init__(self, x, y, w, h):
        self.p = pkmath.v2(x, y)
        self.dp = pkmath.v2(0, 0)
        self.w = w
        self.h = h


def updateAndRender(user_input, window_surface,
                    player):
    """ update the game and render the current frame """
    # TODO(hugo): maybe consider acceleration and equations of motion
    # for a better game feel
    # TODO(hugo): diagonal are faster
    player.dp = pkmath.v2(0, 0)
    if user_input.move_up:
        player.dp = pkmath.add(player.dp, pkmath.v2(0, -50))
    if user_input.move_down:
        player.dp = pkmath.add(player.dp, pkmath.v2(0, 50))
    if user_input.move_left:
        player.dp = pkmath.add(player.dp, pkmath.v2(-50, 0))
    if user_input.move_right:
        player.dp = pkmath.add(player.dp, pkmath.v2(50, 0))
    player_next_p = pkmath.add(player.p, pkmath.times(user_input.dt, player.dp))

    tile_map = [[1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 1, 0, 1, 1],
                [1, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 1, 1]]
    tile_size = 45
    tile_map_count_x = len(tile_map[0])
    tile_map_count_y = len(tile_map)

    player_tl_tile_x = int(player_next_p.x / tile_size)
    player_tl_tile_y = int(player_next_p.y / tile_size)
    player_br_tile_x = int((player_next_p.x + player.w) / tile_size)
    player_br_tile_y = int((player_next_p.y + player.h) / tile_size)

    if tile_map[player_tl_tile_y][player_tl_tile_x] == 0:
        if tile_map[player_br_tile_y][player_br_tile_x] == 0:
            if tile_map[player_tl_tile_y][player_br_tile_x] == 0:
                if tile_map[player_br_tile_y][player_tl_tile_x] == 0:
                    player.p = player_next_p

    # NOTE(hugo): Rendering
    for i in range(tile_map_count_y):
        for j in range(tile_map_count_x):
            tile = tile_map[i][j]
            if tile == 1:
                window_surface.fill(pkcolor.grey(100),
                                    pygame.Rect(tile_size*j, tile_size*i,
                                                tile_size, tile_size))
            else:
                window_surface.fill(pkcolor.grey(0),
                                    pygame.Rect(tile_size*j, tile_size*i,
                                                tile_size, tile_size))

    player_rect = pygame.Rect(player.p.x, player.p.y, player.w, player.h)
    window_surface.fill(pkcolor.red, player_rect)
    return (player.p.x, player.p.y)
