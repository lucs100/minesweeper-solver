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
    
    def cellToCoords(self, idx) -> tuple[int, int]:
        """
        Returns a cell's coordinates. The top-left cell is (0, 0).
        """
        x = idx % self.width
        y = idx // self.width
        return (x, y)
    
    def cellHasMine(self, idx) -> bool:
        """
        Returns whether a cell contains a mine.
        """
        return idx in self._mine_locations
    
    def getSurroundingMineCount(self, idx) -> int:
        """
        Returns the number of mines in the 8 adjacent cells.
        If the current cell has a mine, returns -1. #TODO: May be redundant.
        """
        if self.cellHasMine(idx):
            return -1

        x, y = self.cellToCoords(idx)
        xMin = max(x-1, 0)
        xMax = min(x+1, self.width-1)
        yMin = max(y-1, 0)
        yMax = min(y+1, self.height-1)

        mineCount = 0
        for x in range(xMin, xMax+1):
            for y in range(yMin, yMax+1):
                mineCount += self.cellHasMine(self.coordsToCell(x, y))
        return mineCount

    
    def showGrid(self, showCounts=False, printLines=True) -> str:
        """
        Returns a string representation of the grid. Each "x" represents a mine.
        If showCounts is enabled, also shows the number of surrounding mines. 
        """
        outStr = ""
        for y in range(self.height):
            outStr += "|"
            for x in range(self.width):
                cell = self.coordsToCell(x, y)
                if self.cellHasMine(cell):
                    outStr += "x|"
                else:
                    label = " "
                    if showCounts:
                        label = self.getSurroundingMineCount(cell)
                    outStr += f"{label}|"
            if printLines:
                print(outStr)
                outStr = ""
            else:
                outStr += "\n"
        if not printLines:
            return outStr

    def __repr__(self) -> str:
        return self.showGrid(printLines=False)

if __name__ == "__main__":
    myMinesweeper = Minesweeper(50, 10, 95, (2, 5))
    print(myMinesweeper)
    print(f"Cell locations: {myMinesweeper._mine_locations}")
