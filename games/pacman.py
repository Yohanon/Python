import os
import random
from collections import deque

# Compact symmetrical maze (15 columns x 9 rows)
# '#' = Wall, '.' = Dot
MAZE_TEMPLATE = [
    "###############",
    "#......#......#",
    "#.####.#.####.#",
    "#.............#",
    "#.##.#####.##.#",
    "#......#......#",
    "#.####...####.#",
    "#.............#",
    "###############",
]

START_PAC = (7, 7)
START_GHOST = (3, 7)

# ANSI Colors
COLOR_WALL = "\033[94m"        # Blue
COLOR_PACMAN = "\033[93m\033[1m" # Bold Yellow
COLOR_GHOST = "\033[91m\033[1m"  # Bold Red
COLOR_DOT = "\033[37m"         # White
COLOR_SCORE = "\033[92m\033[1m" # Bold Green
COLOR_RESET = "\033[0m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_ghost_move(maze, ghost_pos, pac_pos):
    """Calculate the next move for the ghost towards Pac-Man."""
    gr, gc = ghost_pos

    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = gr + dr, gc + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != "#":
            neighbors.append((nr, nc))

    if not neighbors:
        return ghost_pos

    # 30% chance of random wander to give the player a fair escape chance
    if random.random() < 0.30:
        return random.choice(neighbors)

    # BFS distance map from Pac-Man to navigate walls
    dist = {pac_pos: 0}
    queue = deque([pac_pos])
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < len(maze)
                and 0 <= nc < len(maze[0])
                and maze[nr][nc] != "#"
                and (nr, nc) not in dist
            ):
                dist[(nr, nc)] = dist[(r, c)] + 1
                queue.append((nr, nc))

    # Choose the neighbor that gets closest to Pac-Man
    return min(neighbors, key=lambda pos: dist.get(pos, float("inf")))


def draw_board(maze, pac_pos, ghost_pos, score, dots_left, lives, message=""):
    """Render the game board and stats in the terminal."""
    clear_screen()
    print("=" * 31)
    print("           PAC-MAN")
    print("=" * 31)
    print(f" Score: {COLOR_SCORE}{score:<4}{COLOR_RESET} | Dots: {dots_left:<2} | Lives: {lives}")
    print("-" * 31)

    for r in range(len(maze)):
        row_display = []
        for c in range(len(maze[0])):
            if (r, c) == pac_pos:
                row_display.append(f"{COLOR_PACMAN}P{COLOR_RESET}")
            elif (r, c) == ghost_pos:
                row_display.append(f"{COLOR_GHOST}G{COLOR_RESET}")
            elif maze[r][c] == "#":
                row_display.append(f"{COLOR_WALL}#{COLOR_RESET}")
            elif maze[r][c] == ".":
                row_display.append(f"{COLOR_DOT}.{COLOR_RESET}")
            else:
                row_display.append(" ")
        print(" ".join(row_display))

    print("=" * 31)
    if message:
        print(f" >> {message}")
        print("-" * 31)
    print(" Controls: [W] Up  [A] Left  [S] Down  [D] Right  [Q] Quit")


def play_game():
    """Run a single round of Pac-Man."""
    grid = [list(row) for row in MAZE_TEMPLATE]
    pac_pos = START_PAC
    ghost_pos = START_GHOST

    # Pac-Man starts on an empty space
    if grid[pac_pos[0]][pac_pos[1]] == ".":
        grid[pac_pos[0]][pac_pos[1]] = " "

    dots_left = sum(row.count(".") for row in grid)
    score = 0
    lives = 3
    message = "Welcome to Pac-Man! Eat all dots to win."

    directions = {
        "w": (-1, 0),
        "s": (1, 0),
        "a": (0, -1),
        "d": (0, 1),
    }

    while True:
        draw_board(grid, pac_pos, ghost_pos, score, dots_left, lives, message)
        message = ""

        try:
            user_input = input("\n Move: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nGame exited.")
            return False

        if user_input == "q":
            print("\nThanks for playing!")
            return False

        moves = [ch for ch in user_input if ch in directions]
        if not moves:
            message = "Invalid input! Use W, A, S, D to move."
            continue

        for move in moves:
            dr, dc = directions[move]
            nr, nc = pac_pos[0] + dr, pac_pos[1] + dc

            # Move Pac-Man if destination is not a wall
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
                pac_pos = (nr, nc)
                if grid[nr][nc] == ".":
                    grid[nr][nc] = " "
                    score += 10
                    dots_left -= 1

            # Check if Pac-Man ran into Ghost
            if pac_pos == ghost_pos:
                lives -= 1
                if lives > 0:
                    pac_pos = START_PAC
                    ghost_pos = START_GHOST
                    message = f"Ghost caught you! Lives remaining: {lives}"
                    break
                else:
                    draw_board(grid, pac_pos, ghost_pos, score, dots_left, lives, "GAME OVER! The ghost caught you.")
                    return True

            # Check if all dots are eaten
            if dots_left == 0:
                draw_board(grid, pac_pos, ghost_pos, score, dots_left, lives, f"VICTORY! You ate all the dots! Final Score: {score}")
                return True

            # Move Ghost
            ghost_pos = get_ghost_move(grid, ghost_pos, pac_pos)

            # Check if Ghost caught Pac-Man
            if pac_pos == ghost_pos:
                lives -= 1
                if lives > 0:
                    pac_pos = START_PAC
                    ghost_pos = START_GHOST
                    message = f"Ghost caught you! Lives remaining: {lives}"
                    break
                else:
                    draw_board(grid, pac_pos, ghost_pos, score, dots_left, lives, "GAME OVER! The ghost caught you.")
                    return True


def main():
    while True:
        keep_playing = play_game()
        if not keep_playing:
            break
        try:
            choice = input("\nPlay again? (y/n): ").strip().lower()
            if choice != "y":
                print("Goodbye!")
                break
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
