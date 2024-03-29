import random
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
# it means [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    return mat
# creating a 4x4 matrix of only 0's

def add_new_2(mat):
    
    r = random.randint(0,3) 
    # The line r = random.randint(0, 3) is a Python code snippet that generates a random integer
    # between 0 (inclusive) and 3 (inclusive) using the randint function from the random module
    c = random.randint(0,3)
    while(mat[r][c] != 0):
        r = random.randint(0,3)
        c = random.randint(0,3)
    
    # as you can put 2 only where there is no number present 
    # i.e. 0 is present
    mat[r][c] = 2

def reverse(mat):

# reversing a matrix means we want to reverse each row of matrix 

    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    
    return new_mat

def transpose(mat):
    
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

def merge(mat):

    '''
    significance of changed : New 2 is added in the matrix if and only if there is a change in the matrix
    If I perform a left move and the matrix remains as it is then there is no need to add a new 2 in the matrix

    '''
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j]!=0:
                mat[i][j] = mat[i][j]*2
                mat[i][j+1] = 0
                changed = True

# if the "if" statement is executed, we have changed the matrix, hence make changed = True

# also, this logic of merge is designed mainly for left move

               

    return mat,changed
            
def compress(mat):

    # bring the non zero numbers closer to each other
    
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                
                # pos denotes column number of the element in new_matrix so if pos=j means no change happened
                # cause if pos = j, then the original state of the matrix is retained
                

                if j!= pos:
                    changed = True
                pos+=1
    return new_mat,changed

def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid,changed1 = compress(transposed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid,changed



def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid,changed

def move_right(grid):
    
    reversed_grid = reverse(grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid,changed

def move_left(grid):
    new_grid,changed1 = compress(grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    # since compress return new_grid and changed both so while calling function we need to give 2 values
    # so thats why we write temp, however temp is useless for us
    return new_grid,changed

    
def get_current_state(mat):
    # Anywhere 2048 is present
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048):
                return 'WON'

    #Anywhere 0 is present it means 2 can come at that place so game is not over
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 0):
                return 'GAME NOT OVER'

    # Every Row and Column except last row and last column
    for i in range(3):
        for j in range(3):
            if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
# as if these elements are equal, they can combine so that a 0 is created and 0 is created means game is
# not over
                return 'GAME NOT OVER'
    #Last Row
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'GAME NOT OVER'
    #Last Column
    
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'GAME NOT OVER'
        
    return 'LOST'
