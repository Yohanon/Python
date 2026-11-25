def pattern(n):
    """Print a diamond pattern of stars with width 2*n - 1."""
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)


if __name__ == "__main__":
    pattern(5)
