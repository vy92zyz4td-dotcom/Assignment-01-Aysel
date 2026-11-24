def main():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            percentage = round(x / y * 100)  # raises ZeroDivisionError if y == 0
        except (ValueError, ZeroDivisionError):
            continue

        if x < 0 or x > y:
            continue
        break

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


main()