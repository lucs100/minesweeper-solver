# Defines the Minesweeper class.
import random

class Minesweeper:
    def __init__(self, width: int, height: int, mines: int, initialClick: tuple[int, int] = (-1, -1)):
        # Assertions
        assert width >= 1, "Width must be at least 1."
        assert height >= 1, "Height must be at least 1."
        assert mines >= 1, "Mine count must be at least 1."
        assert mines <= (height * width) - 1, f"Mine count cannot be more than {(height * width) - 1}."

        self.width = width
        self.height = height
        self.cellCount = width * height

        # Distribute mines; don't put them on the initial click location, if it exists
        if initialClick == (-1, -1):
            mineCandidates = range(self.cellCount)
        else:
            assert 0 <= initialClick[0] < width, "Initial click was out of bounds (x)." 
            assert 0 <= initialClick[1] < height, "Initial click was out of bounds (y)." 
            initialClickCell = self.coordsToCell(*initialClick)
            mineCandidates = (
                list(range(0, initialClickCell))
                + list(range(initialClickCell + 1, self.cellCount))
            )
        self._mine_locations = sorted(random.sample(mineCandidates, k=mines)) #hidden :3
    
    def coordsToCell(self, x, y) -> int:
        """
        Returns the cell ID from a given coordinate pair.
        """
        return x + y * self.width
    
    def cellHasMine(self, idx) -> bool:
        """
        Returns whether a cell contains a mine.
        """
        return idx in self._mine_locations
    
    def showGridWithMines(self) -> str:
        """
        Returns a string representation of the grid. Each "x" represents a mine.
        """
        outStr = ""
        for y in range(self.height):
            outStr += "|"
            for x in range(self.width):
                cell = self.coordsToCell(x, y)
                if self.cellHasMine(cell):
                    outStr += "x|"
                else:
                    outStr += " |"
            outStr += "\n"
        return outStr

    def __repr__(self) -> str:
        return self.showGridWithMines()

if __name__ == "__main__":
    myMinesweeper = Minesweeper(50, 10, 95, (2, 5))
    print(myMinesweeper)
    print(f"Cell locations: {myMinesweeper._mine_locations}")
