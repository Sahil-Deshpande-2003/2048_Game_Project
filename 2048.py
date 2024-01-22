

from tkinter import Frame, Label, CENTER

# Frame, Label, CENTER are classes
# Frame and Label are classes from the tkinter library used for creating GUI elements like frames and labels

import logicsfinal 
import constants as c

# here we are importing 2 files which we have already created
# we write import constants as c so that we can use "c" in place of constants 

class Game2048(Frame):

    # frame allows you to create a box kind of thing where you can place all your widgets
    '''
    In short, widgets in Tkinter are graphical elements or components that can be used to build
    graphical user interfaces (GUIs) for your Python applications. Widgets include items such as 
    buttons, labels, text entry fields, checkboxes, radio buttons, and more.
    These widgets allow you to interact with the user and display information within a window or frame,
    making it easier to create interactive and user-friendly applications.
    '''

    def __init__(self):
        Frame.__init__(self) # a frame is created

        # Calls the constructor of the parent class (Frame) to create a GUI window.

# frame class needs an object on which it will be creating a frame, self is
# that object
        self.grid()
# Initializes the grid manager for the frame, allowing widgets to be organized in a grid layout.

        '''
        The Grid geometry manager puts the widgets in a 2-dimensional table. The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget. 


        A grid is a visual layout or structure used in graphical user interfaces (GUIs) to organize and position graphical elements (widgets)
        such as buttons, labels, and text fields.
        It is primarily used for the presentation and arrangement of GUI components within a window or frame.
        The grid defines rows and columns, where widgets are placed at specific positions within this layout.
        '''
# Tkinter has grid manager which allows to create all the widgets in the form
# of grid, so this frame looks like a grid now because of the above line

        self.master.title('2048')
    # master is the boundary, title is 2048
    # Sets the title of the game window to "2048".

        self.master.bind("<Key>", self.key_down)

# Binds the "Key" event to the self.key_down method, which handles user input.

# if any key is pressed, I will implement self.keydown function

# Creates a dictionary self.commands that maps key presses to specific movement
# functions (move_up, move_down, move_left, move_right) defined in the logicsfinal module.

        self.commands = {c.KEY_UP: logicsfinal.move_up, c.KEY_DOWN: logicsfinal.move_down,
                         c.KEY_LEFT: logicsfinal.move_left, c.KEY_RIGHT: logicsfinal.move_right
                        }


# if w is pressed move up, s is pressed move down, a for left and d for right

    # Initializes an empty list self.grid_cells to store references to the GUI grid cells.    
       
        self.grid_cells = []

# we will add some cells in this grid

        self.init_grid()

#  due to above line UI was created 

# Calls the init_grid method to create the game grid in the GUI.

# it will add the grid cells in the grid

        self.init_matrix()

# Calls the init_matrix method to initialize the game matrix.

# The initial configuration of the 2048 game typically consists of a 4x4 grid 

# (though variations with different grid sizes exist) with two randomly placed tiles containing the value 2. Rest of the cells are 0

# first starts the game,so you have a 4 x 4 matrix will all zero entries and now add 2 new 2's in this matrix
#  
#  
# due to above line matrix was created with initially 2 values as 2

# to create 4x4 matrix and add new 2's in it

        '''

        The line self.update_grid_cells() is essential in the 2048 game code for updating the graphical representation of the game grid
        based on the current state of the game matrix.
        This line is necessary for the following reasons:

        Synchronization with Game State: The game matrix (a 2D array) stores the numerical values and state of the game.
        Changes in the game state, such as moving tiles or merging them, are reflected in this matrix.
        To ensure that the graphical representation matches the game's internal state, the update_grid_cells function is called after each move.



        Updating the User Interface: The update_grid_cells function iterates through the elements of the game matrix
        and updates the corresponding labels and colors in the GUI grid cells.
        It changes the text and background colors of the labels to represent the current state of the game matrix. 
        Without this update, the GUI would not visually reflect the game's progress.




        User Feedback: It provides immediate feedback to the player by displaying the changes made in the game matrix on the screen. 
        When tiles are merged or moved, the player can see the results of their actions in real-time.

        In summary, self.update_grid_cells() is necessary to keep the graphical user interface synchronized with the game's internal state,
        ensuring that the player sees an accurate representation of the game board after each move.
        '''

        self.update_grid_cells()

# due to above line changes in UI will be reflected

# initially all grid cells were having 0's, if 2 comes, background, text colour
# needs to be changed, this is done by update_grid_cells, so it sets the 
# colour according to numbers 

        self.mainloop() # isse event loop me chale jate hai, ye aapko GUI window me rakhta hai

# Starts the Tkinter main event loop, which runs the game until the user closes the window

# it actually runs the program

    def init_grid(self):
        # By passing self as the first argument, we are essentially saying this frame (background) is a part of the current Game2048 object
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
# frame of 400 x 400 created inside the outside frame 
# so a frame was created which was initially a grid only, inside this grid
# you have created another frame of size 400 x 400 so actuaaly inside a grid 
# there is another grid, so now you need to add cells in this grid

        background.grid()

# The Grid geometry manager puts the widgets in a 2-dimensional table. The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget. This method is used to organize widgets in a table-like structure, arranging them in rows and columns.

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,# so width=400/4=100
                             height=c.SIZE / c.GRID_LEN)
                
                # cell is itself is a frame, cell represents a cell in the grid.
                '''
                This line uses the grid() method to position and display the cell frame within the grid layout. The parameters are:

                row=i: Specifies the row in the grid where the cell frame should be placed. The value of i is used as the row index.
                column=j: Specifies the column in the grid where the cell frame should be placed. The value of j is used as the column index.
                padx=c.GRID_PADDING: Specifies horizontal padding (in pixels) around the cell frame.
                pady=c.GRID_PADDING: Specifies vertical padding (in pixels) around the cell frame.
                '''
                cell.grid(row=i, column=j, padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING)
        
# adding the cell to the grid at row = i and column = j
                
# Tkinter Label is a widget that is used to implement display boxes where you can place text or images.

                t = Label(master=cell, text="",
                          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=5, height=2)
# master=cell: Specifies the parent widget for the label. In this case, it's the cell frame, indicating that the label (t) is a child of the cell frame.
# text="": Sets the initial text content of the label to an empty string
# inside the cell, you are adding a label, label is another widget which is used
# to denote a text box, since this cell was a grid, so label is also a grid
#   justify=CENTER means adding text as center,
#  font=c.FONT means default font added in the constant, text is of 
# width 5 and height 2
# numbers are getting changed so labels are getting changed so we are appending
# labels in grid_row 

# inside the cell, the text and background colour is getting changed so numbers are getting
# changed that means label is getting changed, the cell will remain same 
# so thats why we are appending labels in grid_row (t is label) and inside grid cells
# we have appended grid_row so our row is like [L1,L2,L3,L4] , another is 
# [L5,L6,L7,L8], another is [L9,L10,L11,L12] and last is [L13,L14,L15,L16]

# inside a cell, there is only label so label covers the cell, if we change background colour
# of label so automatically cell's background colour will change  
                t.grid() # # The Grid geometry manager puts the widgets in a 2-dimensional table. The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget. This method is used to organize widgets in a table-like structure, arranging them in rows and columns.

                # t.grid(row=0, column=0)  # Place the label in the first row and first column of the grid

                #  If you don't specify row and column values explicitly, it will automatically position the widget in the first available row and column.

                # so here create a label 't' and insert in the 1st available row and column in the grid

                grid_row.append(t) # grid_row is a list that represents a single row in the grid.

            self.grid_cells.append(grid_row) # self.grid_cells is a list that represents the entire grid in the game.


    def init_matrix(self):

# all the blocks (i.e. L1,L2,L3,L4,...) get created

        self.matrix = logicsfinal.start_game() # append 4 lists in a list in which each list has 4 0's
# above line tells us that if "w" is pressed you have to move up and since  LogicsFinal
# needs a matrix so I am passing self.matrix as argument in key_down function

# above line returns a 2D matrix with all values = 0, using this ,matrix we will be making
# changes in this L1,L2,... wala matrix so it means we are internally maintaining
# another matrix, and all the changes made in this matrix are reflected in this UI (i . e.
# L1,L2,.. wala matrix) 

        logicsfinal.add_new_2(self.matrix) # insert a new 2 at random position provided no other number is present there i.e. 0 is present
# here we have added a new 2
        logicsfinal.add_new_2(self.matrix)
# here again we have added a new 2

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY) # by default all the values in the grid are 0
# as for 0, text should be empty and background color shoudl be this 
#  BACKGROUND_COLOR_CELL_EMPTY, so configure will do that 
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number])

# so here if new_number is 2, it will be converted to string ,
# bg=c.BACKGROUND_COLOR_DICT[new_number] means you'll set the background colour of 
# new_number by taking help of dictionary 

# this line--> fg=c.CELL_COLOR_DICT[new_number] is used to set the correct text colour 
# for new_number 

        self.update_idletasks()

# above line waits until all the colors get changed 

# so basically update_grid_cells makes changes in UI using the matrix that you have 
# maintained

    def key_down(self, event):

# event.char gives the key which is pressed
# repr gives the printable part of that key 
        key = repr(event.char)
        if key in self.commands:

# self.commands contains "w","s","a","d", so if any one of them is pressed then only
# we consider
            self.matrix, changed = self.commands[repr(event.char)](self.matrix) # self.commands[repr(event.char)] will return logicsfinal.move_up or down or right or left and to call the respective function which is present in logicsfinal.py, you need to pass the grid as argument which is self.matrix here
            if changed:
                logicsfinal.add_new_2(self.matrix)

# if there is any change then only you need to add a 2

                self.update_grid_cells() # configure the [text,bg and fg(color of each number)](of each number) for each number in this updated grid

# update_grid_cells changes the UI cause a new 2 is added 

                changed = False
# by default changed is False so we again set changed as False 
                if logicsfinal.get_current_state(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if logicsfinal.get_current_state(self.matrix) == 'LOST':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)



gamegrid = Game2048()
