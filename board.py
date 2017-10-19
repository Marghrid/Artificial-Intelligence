from search import *

# TAI color
# sem cor = 0
# com cor > 0
def get_no_color():
    return 0
def no_color (c):
    return c==0
def color (c):
    return c > 0

# TAI pos
# Tuplo (l, c)
def make_pos (l, c):
    return (l, c)
def pos_l (pos):
    return pos[0]
def pos_c (pos):
    return pos[1]

def print_board (board):
    for line in board:
        for cell in line:
            print(cell, end =' ')
        print()

def board_remove_group(board, group):
    # 1. Fazer uma copia do tabuleiro
    # 2. Colocar a 0 todas as posicoes do do grupo
    # 3. Compacatacao vertical
    # 4. Compactacao horizontal
    l = []
    i = 0
    j = 0
    for line in board:
        l.append([])
        for cell in line:
            l[i].append(cell)
            j+=1
        i+=1
        
    
   
    #compacts each column vertically
    #and eliminates a column if empty (compacts horizontally)
    missing_columns = 0
    j = 0
    while j < len(board[0]):
        advance = 0
       
        if(j+missing_columns <= len(board[0])-1):         
            for i in reversed(range(0, len(board))):
                while make_pos(i-advance,j+missing_columns) in group or \
                      [i-advance,j+missing_columns] in group:
                    advance+=1
                           
                #note: we should stop loop when we see zero, because balls 
                # don't float
                if (advance > 0 or missing_columns > 0) and (i - advance) >= 0:
                    l[i][j] = l[i-advance][j+missing_columns]
                elif (i-advance) < 0:
                    l[i][j] = 0  
            
            #empty column case
            if l[len(board)-1][j] == 0:
                missing_columns += 1
                j-=1
        else:
            for i in range(0, len(board)):
                l[i][j] = 0
       
        j+=1
    
    return l

def board_find_groups(board):
    groups = []
    found = []
    i = 0
    for line in board:
        found.append([])
        for cell in line:
            found[i].append(0)
            
        i+=1
        
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            
            if color(board[i][j]):
                group = board_get_group(make_pos(i,j), board, found)
                if (not group is None):
                    groups.append(group)
                
                
    return groups

def board_get_group(pos, board, found):
    i = pos_l(pos)
    j = pos_c(pos)
    group = []
    if found[i][j] > 0:
        return None
    else:
        found[i][j] = 1
        group.append(pos)
        
        if i<len(board)-1:
            if board[i][j] == board[i+1][j]:
                g = board_get_group(make_pos(i+1,j), board, found)
                if not g is None:
                    group+=g
                    
        if i>0:
            if board[i][j] == board[i-1][j]:
                g = board_get_group(make_pos(i-1,j), board, found)
                if not g is None:
                    group+=g
                    
        if j<len(board[0])-1:
            if board[i][j] == board[i][j+1]:
                g = board_get_group(make_pos(i,j+1), board, found)
                if not g is None:
                    group+=g
                    
        if j>0:
            if board[i][j] == board[i][j-1]:
                g = board_get_group(make_pos(i,j-1), board, found)
                if not g is None:
                    group+=g
                    
        
        return group

def board_get_num_groups(board):
    count = 0;
    for line in board:
        for cell in line:
            if not no_color(cell):
                count+=1
                
    return count

class sg_state:
    def __init__(self, board):
        self.board = board
    
    def __lt__(self, other):
        return self.board < other.board
        
class same_game(Problem):
    
    def __init__(self, board):
        self.initial = sg_state(board);
    
    def actions(self, state):
        ret_actions = board_find_groups(state.board)
        return [item for item in ret_actions if len(item)>1]
    
    def result(self, state, action):
        return sg_state(board_remove_group(state.board, action))
    
    def goal_test(self, state):
        #Board is empty if the lower left slot is empty
        pos = make_pos(len(state.board)-1, 0)
        return no_color(state.board[pos_l(pos)][pos_c(pos)])
    
    def h(self, node):
        return len(board_find_groups(node.state.board))
