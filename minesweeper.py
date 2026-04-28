# Defines the Minesweeper class.
from random import randint

class Minesweeper:
    def __init__(self, width, height, mines):
        # Assertions
        assert width >= 1, "Width must be at least 1."
        assert height >= 1, "Height must be at least 1."
        # assert mines >= 1, "Mine count must be at least 1."
        assert mines <= height * width, f"Mine count cannot be more than {height*width}."

        self.width = width
        self.height = height
        self._mine_locations = [[[0] * width] for _ in range(height)]  #hidden :3

        # Populate minefield
        while sum([sum(x) for x in self._mine_locations]) < mines:
            candidateX = randint(0, width-1)
            candidateY = randint(0, height-1)
            print(candidateX, candidateY)
            self._mine_locations[candidateX][candidateY] = 1

if __name__ == "__main__":
    myMinesweeper = Minesweeper(10, 10, 1)
    # print(myMinesweeper.height)
    # print(myMinesweeper.width)
    for row in myMinesweeper._mine_locations:
        print(row)
