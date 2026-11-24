grocery = {}

while True:
    try:
        item = input().strip().lower()
    except EOFError:
        break

    if item:
        grocery[item] = grocery.get(item, 0) + 1

for item in sorted(grocery):
    print(grocery[item], item.upper()) 