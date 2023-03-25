from graphics import *
import math

# Definitions
rects = 8 # squares in board line and row
WinW = 600  # horizontal size of the game board
WinH = WinW # vertical the same as horizontal
WinMidX = WinW/2
WinMidY = WinH/2
size = WinH/rects
start = 0
BLACK_PIECE = 0
WHITE_PIECE = 1
BLACK_SQUARE = 0
WHITE_SQUARE = 1
N = 0 # Disabled square for piece
E = 1 # square enabled for piece
B = 2 # square with black piece
W = 3 # square with white piece

board = [
    [N, B, N, B, N, B, N, B],
    [B, N, B, N, B, N, B, N],
    [N, B, N, B, N, E, N, B],
    [E, N, E, N, B, N, E, N],
    [N, W, N, E, N, E, N, E],
    [E, N, W, N, W, N, W, N],
    [N, W, N, W, N, W, N, W],
    [W, N, W, N, W, N, W, N],
]
# Initialize graphic window
win = GraphWin('Board', WinW, WinH)

# Draw square on board in position i(x),j(y)
def draw_square(i,j,color):
    r = Rectangle(Point(start+size*j,start + size*i),Point(start+size*j+size-1,start + size*i+size-1))
    if color == BLACK_SQUARE:
        r.setFill('black')
        r.draw(win)
    else:
        r.setFill('lightgray')
        r.draw(win)
        
# Draw piece on board in position i,y with color 0=black, 1=white        
def draw_piece(i,j,color):
    cp = Point(start+size*j + size/2, start + size*i + size/2)
    c = Circle(cp, 9*size/20)
    if color == 0:
        c.setFill('black')
        c.setOutline('lightgray')
        c.setWidth(3)
        c.draw(win)
        gc = Circle(cp, 4*size/20)
        gc.setOutline('gray')
        gc.setWidth(3)
        gc.draw(win)
    else:
        c.setFill('white')
        c.setOutline('lightgray')
        c.setWidth(3)
        c.draw(win)
        gc = Circle(cp, 4*size/20)
        gc.setOutline('lightgray')
        gc.setWidth(3)
        gc.draw(win)
# Draw checkers board
def draw_board():
    for i in range(0,rects):
        for j in range(0,rects):
            if (i+j) % 2 == 1:
                draw_square(i,j,0)
            else:
                draw_square(i,j,1)
# Draw checkers board with default pieces
def draw_board_and_pieces():
    for i in range(0,rects):
        for j in range(0,rects):
            if (i+j) % 2 == 1:
                draw_square(i,j,0)
                if i < 3:
                    draw_piece(i,j,0)           
                if i > rects - 4:
                    draw_piece(i,j,1)
            else:
                draw_square(i,j,1)
# Draw only pieces after draw board                
def draw_pieces():
    for i in range(0,rects):
        for j in range(0,rects):
            if (i+j) % 2 == 1:
                draw_square(i,j,0)
            else:
                draw_square(i,j,1)
            if board[i][j] == B:
                draw_piece(i,j,BLACK_PIECE)
            if board[i][j] == W:
                draw_piece(i,j,WHITE_PIECE)

# Test functions
#draw_board()
#draw_board_pieces()
draw_pieces()
