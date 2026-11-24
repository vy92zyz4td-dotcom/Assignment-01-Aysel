def main():
    time = input("What time is it? ")
    hours = convert(time)

    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")


def convert(time):
    time = time.strip().lower()
    period = None

    if time.endswith("a.m.") or time.endswith("p.m."):
        period = time[-4:]
        time = time[:-4].strip()

    hours, minutes = time.split(":")
    hours = int(hours)

    if period:
        hours = hours % 12
        if period == "p.m.":
            hours += 12

    return hours + int(minutes) / 60


if __name__ == "__main__":
    main() 