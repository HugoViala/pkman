import pkmath
import pkcolor

# TODO(hugo): give more parameters to the constructor ?
class GameState:
    def __init__(self):
        self.running = True
        self.player = Player(100, 100, 30, 30, 80)

class Player:
    """ class to handle all the details about a player entity """
    def __init__(self, x, y, w, h, speed):
        self.p = pkmath.v2(x, y)
        self.dp = pkmath.v2(0, 0)
        self.w = w
        self.h = h
        self.speed = speed


def updateAndRender(user_input, gamestate):
    """ update the game and render the current frame
    return a list of pkman rect to be processed by pygame """

    # TODO(hugo): maybe consider acceleration and equations of motion
    # for a better game feel
    player = gamestate.player
    player.dp = pkmath.v2(0, 0)
    if user_input.move_up:
        player.dp = pkmath.add(player.dp, pkmath.v2(0, -1))
    if user_input.move_down:
        player.dp = pkmath.add(player.dp, pkmath.v2(0, 1))
    if user_input.move_left:
        player.dp = pkmath.add(player.dp, pkmath.v2(-1, 0))
    if user_input.move_right:
        player.dp = pkmath.add(player.dp, pkmath.v2(1, 0))
    player.dp = pkmath.normalize(player.dp)
    player.dp = pkmath.times(player.speed, player.dp)
    player_next_p = pkmath.add(player.p, pkmath.times(user_input.dt, player.dp))

    tile_map = [[1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 1, 0, 1, 1],
                [1, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 1, 1],
                [1, 1, 1, 1, 1, 1, 1]]
    tile_size = 45
    tile_map_count_x = len(tile_map[0])
    tile_map_count_y = len(tile_map)

    # NOTE(hugo): collision test
    # TODO(hugo): we should check if those number are in the proper range
    # but maybe if we wrap things up it'll be obvious afterwards
    # TODO(hugo): he is getting stuck in the corner
    # maybe do a collision detection as in Handmade Hero 45 ?
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
    rect_list = []
    for i in range(tile_map_count_y):
        for j in range(tile_map_count_x):
            tile = tile_map[i][j]
            if tile == 1:
                rect_list.append((pkcolor.grey(100),
                                    (tile_size*j, tile_size*i,
                                                tile_size, tile_size)))
            else:
                rect_list.append((pkcolor.grey(0),
                                    (tile_size*j, tile_size*i,
                                                tile_size, tile_size)))

    player_rect = (player.p.x, player.p.y, player.w, player.h)
    rect_list.append((pkcolor.red, player_rect))
    return rect_list
