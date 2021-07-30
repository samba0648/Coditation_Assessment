## Coditation_Assessment
#### Things considered in the implementation
Programming language used: Python3

The input for the program is given via a text file, through which the initial grid is formed. A cell object is created for every (i,j)th element from the contents read. Each line of cells is added as a sub_grid and every sub_grid is added to the initial_grid thus forming the main grid. Cell names are generated dynamically as follows:
````
(0,0)th cell = Cell-11
(0,1)th cell = Cell-12
''
''
(i,j)th cell = Cell-(i+1)(j+1)
````
A loop is executed keeping the following two options:
1. Generating a next generation of cells.
1. Searching for the cell status by it's name

At the end of every iteration, program will ask whether to continue or not. The program will only consider `Yes` or `No` as inputs(case sensitive), otherwise it will ask to re-enter.

**list index out of range** error is handled using try, except blocks.

Time Complexity of the program is: O(N<sup>2</sup>)

#### Running the program:
I have used Python idle to implement and run the program. The text file contents should be similar to the given sample text file(intial_input.txt).
