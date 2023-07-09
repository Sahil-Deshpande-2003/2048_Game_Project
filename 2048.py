

from tkinter import Frame, Label, CENTER

# Frame, Label, CENTER are classes

import logicsfinal 
import constants as c

# here we are importing 2 files which we have already created
# we write import constants as c so that we can use "c" in place of constants 

class Game2048(Frame):

# frame allows you to create a box kind of thing where you can place all your widgets

    def __init__(self):
        Frame.__init__(self) # a frame is created

# frame class needs an object on which it will be creating a frame, self is
# that object
        self.grid()
# Tkinter has grid manager which allows to create all the widgets in the form
# of grid, so this frame looks like a grid now because of the above line

        self.master.title('2048')
# master is the boundary, title is 2048

        self.master.bind("<Key>", self.key_down)

# if any key is pressed, I will implement self.keydown function
        self.commands = {c.KEY_UP: logicsfinal.move_up, c.KEY_DOWN: logicsfinal.move_down,
                         c.KEY_LEFT: logicsfinal.move_left, c.KEY_RIGHT: logicsfinal.move_right
                        }

# LogicsFinal apan ne banayi hai
# if w is pressed move up, s is pressed move down

        
        
        self.grid_cells = []

# we will add some cells in this grid

        self.init_grid()

#  due to above line UI was created 

# it will add the grid cells in the grid

        self.init_matrix()

# first starts the game,so you have a 4 x 4 matrix will all zero entries and now add 2 new 2's in this matrix
#  
#  
# due to above line matrix was created with initially 2 values as 2

# to create 4x4 matrix and add new 2's in it

        self.update_grid_cells()

# due to above line changes in UI will be reflected

# initially all grid cells were having 0's, if 2 comes, background, text colour
# needs to be changed, this is done by update_grid_cells, so it sets the 
# colour according to numbers 

        self.mainloop()

# it actually runs the program

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
# frame of 400 x 400 created inside the outside frame 
# so a frame was created which was initially a grid only, inside this grid
# you have created another frame of size 400 x 400 so actuaaly inside a grid \
# there is another grid, so now you need to add cells in this grid

        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,# so width=400/4=100
                             height=c.SIZE / c.GRID_LEN)
                
                # cell is itself is a frame

                cell.grid(row=i, column=j, padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING)
        
# adding the cell to the grid at row = i and column = j

                t = Label(master=cell, text="",
                          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=5, height=2)

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
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)


    def init_matrix(self):

# all the blocks (i.e. L1,L2,L3,L4,...) get created

        self.matrix = logicsfinal.start_game()
# above line tells us that if "w" is pressed you have to move up and since  LogicsFinal
# needs a matrix so I am passing self.matrix as argument in key_down function

# above line returns a 2D matrix with all values = 0, using this ,matrix we will be making
# changes in this L1,L2,... wala matrix so it means we are internally maintaining
# another matrix, and all the changes made in this matrix are reflected in this UI (i . e.
# L1,L2,.. wala matrix) 

        logicsfinal.add_new_2(self.matrix)
# here we have added a new 2
        logicsfinal.add_new_2(self.matrix)
# here again we have added a new 2

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
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
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                logicsfinal.add_new_2(self.matrix)

# if there is any change then only you need to add a 2

                self.update_grid_cells()

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