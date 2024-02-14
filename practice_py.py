def calculate_square(num):
    return num**2


def calculate_cube(num):
    return num**3


def main():
    """
    Main function

    :return: None
    """
    numbers = [1, 2, 3, 4, 5]

    for num in numbers:
        print(f"Number: {num}")
        if num % 2 == 0:
            print(f"Square: {calculate_square(num)}")
        else:
            print(f"Cube: {calculate_cube(num)}")


if __name__ == "__main__":
    main()
