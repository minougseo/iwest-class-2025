
with open("./회의록/20250828.txt", "rt", encoding="utf-8") as file:
    # str -> list[str]
    for line in file.read().splitlines():
        print(line)