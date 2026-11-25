def convert_number(value):
    number = int(value)
    if number < 0:
        raise ValueError("Enter a non-negative whole number.")

    print(f"Decimal:     {number}")
    print(f"Binary:      {number:b}")
    print(f"Octal:       {number:o}")
    print(f"Hexadecimal: {number:X}")


if __name__ == "__main__":
    try:
        convert_number(input("Enter a non-negative whole number: ").strip())
    except ValueError:
        print("Please enter a non-negative whole number using digits only.")
