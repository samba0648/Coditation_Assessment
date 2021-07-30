# Cell class for defining a cell
class Cell:
    # Constructor to initialize the cell name and it's status
    def __init__(self,name,isLive):
        self.cellName = name
        self.isLive = isLive
# Grid class for defining a grid of cells
class Grid:
    # Constructor to initialize the grid and size
    def __init__(self,grid,size = 8):
        self.size = size
        self.grid = grid
    #generationChange method to update the levliness of all cells for one generation
    def generationChange(self):
        for i in range(self.size):
            for j in range(self.size):
                # initialize neighbour_live of current cell to 0
                neighbour_live = 0
                # add the value of all the eight neighbours to neighbour_live
                # if the cell is in the corner edge of the grid then list index out of range will raise
                # To solve that using exception handling using try,except.
                try:
                    neighbour_live += self.grid[i-1][j-1].isLive
                except IndexError:
                    pass
                try:
                    neighbour_live += self.grid[i-1][j].isLive
                except IndexError:
                    pass
                try:
                    neighbour_live += self.grid[i-1][j+1].isLive
                except IndexError:
                    pass
                try:
                    neighbour_live += self.grid[i][j-1].isLive
                except IndexError:
                    pass
                try:
                    neighbour_live += self.grid[i][j+1].isLive
                except IndexError:
                    pass
                try:
                    neighbour_live += self.grid[i+1][j-1].isLive
                except IndexError:
                    pass
                try:
                    neighbour_live += self.grid[i+1][j].isLive
                except IndexError:
                    pass
                try:
                    neighbour_live += self.grid[i+1][j+1].isLive
                except IndexError:
                    pass
                # if the current cell is alive
                if(self.grid[i][j].isLive == 1):
                    # if alive neighbours are less than 2 or more than 3 then this cell will die
                    if(neighbour_live < 2 or neighbour_live >3):
                        self.grid[i][j].isLive = 0
                    # else current cell remails same
                # if cell is dead
                else:
                    # if 3 neighbours are alive then the current cell come to life
                    if(neighbour_live == 3):
                        self.grid[i][j].isLive = 1
    # Method to display the grid
    def displayGrid(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.grid[i][j].isLive,end=" ")
            print()
        print()
    # Method to print the status of the cell
    def displayByCellName(self,name):
        # Searching through every cell in the grid
        for subGrid in self.grid:
            for cell in subGrid:
                # If the cell name is matched then print the status
                if cell.cellName==name:
                    print(cell.isLive)
                    return
        print("Invalid cell name")
            

# main method 
if __name__=="__main__":
    initial_grid = []
    filename = "intial_input.txt"
    # initializing the grid from the text file
    with open(filename,'r') as file:
        # Reading all lines from text file into a filed
        data = file.readlines()
        row_count = 1
        # Iterating every line
        for line in data:
            col_count = 1
            cell_grid = []
            cell_line = list(map(int,line.split()))
            # Iterating every cell
            for cell in cell_line:
                cell = int(cell)
                # Dynamic name for cell
                cell_name = "Cell-"+str(row_count)+str(col_count)
                # Creating cell object
                newCell = Cell(cell_name,cell)
                # Adding it to the subgrid list
                cell_grid.append(newCell)
                col_count+=1
            # Adding subgrid to initial_grid list
            initial_grid.append(cell_grid)
            row_count+=1
            
    # grid size
    grid_size = len(initial_grid)
    # creating object for Grid
    grid = Grid(initial_grid,grid_size)
    #displaying intial grid
    grid.displayGrid()
    nextGeneration = "Yes"
    # loop as long as nextGeneration is Yes
    while(nextGeneration == "Yes"):
        print("Select a option\n1 - next generation\n2 - search cell by name")
        inp = int(input())
        # If the input is 1 then generating next generation
        if inp==1:
            # upgrading the next genearation
            grid.generationChange()
            # displaying after generation udate
            grid.displayGrid()
        # If input is 2 then searching cell status by it's name
        elif(inp==2):
            print("Enter cell name:")
            cellname = input()
            grid.displayByCellName(cellname)
        else:
            print("Wrong input")
        # Ask user if another generational change is to be carried out
        print("Do you want to Continue?")
        # Ask user to enter Yes to continue and No to exit
        print("Enter Yes or No: ")
        # reading user input
        nextGeneration = input()
        while(nextGeneration!="Yes" and nextGeneration!="No"):
            print("Wrong Input, Please enter again")
            nextGeneration = input()

