import random
ROMS = 3
COLS = 4
def main():
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for r in range(ROMS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)

    print(values)
main()