import curses, random
from math import sqrt

from .models import Window


LOGO = [
    " _____         ",
    "|_   _|__ _ __ ",
    "  | |/ _ \\ `  \\",
    "  | |  __/ || |",
    "  |_|\\___\\_||_|"
]


def main(screen, n=4):
    # This is the only time the whole screen is ever refreshed. But if you
    # don't refresh it, screen.getkey will clear it, because curses is awful.
    screen.refresh()

    # Turn off visible cursor.
    curses.curs_set(False)

    # Create screen objects.
    content, logo = init_windows(screen, n)

    # Write logo to screen.
    draw_logo(logo)

    # Create grid.
    grid = [-1 for i in range(n*n)]

    # Start with two tiles.
    new_tile(grid)
    new_tile(grid)

    while not (win(grid) or lose(grid)):
        show_grid(content, grid)

        # Block, waiting for input.
        try:
            key = screen.getkey().upper()
        except:
            # On resize, getkey screws up once (maybe more).
            pass

        if key == 'Q':
            return
        elif key in ('W', 'K', 'KEY_UP'):
            move_up(grid)
        elif key in ('S', 'J', 'KEY_DOWN'):
            move_down(grid)
        elif key in ('A', 'H', 'KEY_LEFT'):
            move_left(grid)
        elif key in ('D', 'L', 'KEY_RIGHT'):
            move_right(grid)

    # TODO: For win and loss messages, replace the logo with WIN or LOSE
    if win(grid):
        raise Exception("You win!")

    raise Exception("You lose!")
    # TODO Add ability to restart games with ENTER once won or lost


def win(grid):
    return any(map(lambda x: x > 9, grid))


def lose(grid):
    return False
    # TODO: Check if the grid is full and there are no available moves.
    # (Full and no identical spaces adjacent to each other.)


def new_tile(grid):
    empty = [i for i in range(len(grid)) if grid[i] < 0]
    index = random.choice(empty)
    grid[index] = random.randint(0, 1)


def move_up(grid):
    move(grid, lambda i, n: slice(i, None, n))


def move_down(grid):
    move(grid, lambda i, n: slice(-(i + 1), None, -n))


def move_left(grid):
    move(grid, lambda i, n: slice(i * n, i * n + n, None))


def move_right(grid):
    move(grid, lambda i, n: slice(-(i * n + 1), -(i * n + 1 + n), -1))


def move(grid, index_function):
    n = int(sqrt(len(grid)))
    old_grid = list(grid)       # Keep a copy for later comparison.

    for i in range(n):
        index = index_function(i, n)
        grid[index] = cascade(grid[index])

    # Did a move actually happen?
    if old_grid != grid:
        new_tile(grid)


def cascade(segment):
    for tile_to_move in range(1, len(segment)):
        # Check if current space has a tile in it.
        if segment[tile_to_move] == -1:
            continue

        # If it does, check if current tile can move anywhere.
        target_space = None
        for potential_space in range((tile_to_move - 1), -1, -1):
            # Is potential_space occupied?
            if segment[potential_space] == -1:
                # If potential_space is empty, the tile can move to it. (But
                # keep checking, in case it can move further.)
                target_space = potential_space
            else:
                if segment[potential_space] == segment[tile_to_move]:
                    # If potential_space is the same, the tile can move to it.
                    target_space = potential_space

                # If potential_space is occupied, we're not moving further.
                break


        # Did we find someplace to move the tile?
        if target_space is None:
            continue

        # Move the tile.
        if segment[target_space] == segment[tile_to_move]:
            # Combine tiles.
            segment[target_space] += 1
        else:
            # Move the tile.
            segment[target_space] = segment[tile_to_move]

        segment[tile_to_move] = -1

    return segment


def init_windows(screen, n):
    logo_height = len(LOGO)
    logo_width = max(len(r) for r in LOGO)

    logo = Window(
        screen, logo_height, logo_width, max_lines=len(LOGO), border=False
    )

    content_height = n + 2          # Includes border
    content_width = n * 2 - 1 + 4   # Includes border and space to either side
    content_offset = max((logo_width - content_width) // 2, 0)

    content = Window(
        screen, content_height, content_width, row_offset=logo_height + 1,
        col_offset=content_offset, max_lines=4
    )

    return (content, logo)


def draw_logo(window):
    for i, line in enumerate(LOGO):
        window.write(
            line, row_offset=i, col_offset=window.centre(line),
            attr=curses.A_BOLD
        )

    window.refresh()


def show_grid(window, grid):
    n = int(sqrt(len(grid)))

    for r in range(n):
        row = ['{:1}'.format(i if i > -1 else '') for i in grid[(r*4):(r*4+4)]]
        window.write(' '.join(row), row_offset=r)

    window.refresh()
