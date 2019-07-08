import sys
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

DEAD = 0
ALIVE = 1

# TODO grids are always square...
def empty_grid(n):
    return [[DEAD] * n for _ in range(n)]

GOSPER_GLIDER_GUN = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


def gosper_glider_gun_grid():
    # hacky but for convolve2d and the boundary conditions...
    offset = 0
    p = len(GOSPER_GLIDER_GUN)
    q = len(GOSPER_GLIDER_GUN[0])

    grid = empty_grid(2 * max(p, q))

    for i in range(p):
        for j in range(q):
            grid[i + offset][j + offset] = GOSPER_GLIDER_GUN[i][j]

    return grid


def random_grid(n, p=0.5):
    # seed the RNG so that benchmarking is fair
    random.seed(1)
    grid = empty_grid(n)
    for i in range(n):
        for j in range(n):
            if p > random.uniform(0, 1):
                grid[i][j] = ALIVE

    return grid


def empty_numpy_grid(n):
    return np.zeros((n, n))

def step(grid):
    n = len(grid)
    updated = empty_grid(n)

    for i in range(n):
        for j in range(n):
            neighbours = 0

            if i != 0:
                # N
                if grid[i - 1][j] == ALIVE:
                    neighbours += 1

                # NE
                if j != n - 1 and grid[i - 1][j + 1] == ALIVE:
                    neighbours += 1

            if j != n - 1:
                # E
                if grid[i][j + 1] == ALIVE:
                    neighbours += 1

                # SE
                if i != n - 1 and grid[i + 1][j + 1] == ALIVE:
                    neighbours += 1

            if i != n - 1:
                # S
                if grid[i + 1][j] == ALIVE:
                    neighbours += 1

                # SW
                if j != 0 and grid[i + 1][j - 1] == ALIVE:
                    neighbours += 1

            if j != 0:
                # W
                if grid[i][j - 1] == ALIVE:
                    neighbours += 1

                # SW
                if i != 0 and grid[i - 1][j - 1] == ALIVE:
                    neighbours += 1

            state = grid[i][j]

            if state == DEAD:
                if neighbours == 3:
                    state = ALIVE
            elif state == ALIVE:
                if neighbours < 2 or neighbours > 3:
                    state = DEAD
                else:
                    state = ALIVE

            updated[i][j] = state

    return updated


def matplotlib_animation(grid, step_func=step):
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.axis('off')
    im = ax.imshow(grid)

    def animate(frame):
        im.set_data(animate.grid)
        animate.grid = step_func(animate.grid)
        return (im,)

    animate.grid = grid

    ani = animation.FuncAnimation(fig, animate, frames=400, interval=100, blit=True)

    return ani


def make_gosper_gif():
    grid = gosper_glider_gun_grid()
    ani = matplotlib_animation(grid)
    ani.save("gosper.gif", dpi=80, writer="pillow")


if __name__ == "__main__":
    # TODO hacky use click or something
    if len(sys.argv) > 1:
        if sys.argv[1] == 'gosper':
            if len(sys.argv) == 3 and sys.argv[2] == "--make-gif":
                make_gosper_gif()
            else:
                grid = gosper_glider_gun_grid()
                ani = matplotlib_animation(grid)
                plt.show()
        else:
            print('TODO add more patterns')
    else:
        print("Usage: python life.py <pattern> [--make-gif]")