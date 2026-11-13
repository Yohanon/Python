def is_niven(n: int) -> bool:
    """Check if a positive integer is a Niven (Harshad) number."""
    if n <= 0:
        return False
    digit_sum = 0
    temp = n
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    return digit_sum > 0 and n % digit_sum == 0


def niven(limit: int):
    """Print all Niven numbers from 1 up to limit."""
    if limit < 1:
        return
    for i in range(1, limit + 1):
        if is_niven(i):
            print(i, end=" ")
    print()  # Ensure trailing newline


def main():
    while True:
        try:
            num = int(input("Enter the upper limit: "))
            if num > 0:
                niven(num)
                break
            else:
                print("Enter a positive non-zero number.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break


if __name__ == "__main__":
    main()
