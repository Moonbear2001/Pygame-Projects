import pygame, sys

### Constants ###

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
height = 780
width = 780

b_scale = 0.3
left = b_scale * width
right = (1 - b_scale) * width
top = b_scale * width
bottom = (1 - b_scale) * height
third = ((1 - 2 * b_scale) / 3) * width
stroke_width = 6
stroke_offset = 10

cell_pos = {0: pygame.Rect(left + stroke_offset, top + stroke_offset, third - 2*stroke_offset, third - 2*stroke_offset),
            1: pygame.Rect(left + third + stroke_offset, top + stroke_offset, third - 2*stroke_offset, third - 2*stroke_offset),
            2: pygame.Rect(left + 2*third + stroke_offset, top + stroke_offset, third - 2*stroke_offset, third - 2*stroke_offset),
            3: pygame.Rect(left + stroke_offset, top + third + stroke_offset, third - 2*stroke_offset, third - 2*stroke_offset),
            4: pygame.Rect(left + third + stroke_offset, top + third + stroke_offset, third - 2*stroke_offset, third - 2*stroke_offset),
            5: pygame.Rect(left + 2*third + stroke_offset, top + third + stroke_offset, third - 2*stroke_offset, third - 2*stroke_offset),
            6: pygame.Rect(left + stroke_offset, top + 2*third + stroke_offset, third - 2*stroke_offset, third - 2*stroke_offset),
            7: pygame.Rect(left + third + stroke_offset, top + 2*third + stroke_offset, third - 2*stroke_offset, third - 2*stroke_offset),
            8: pygame.Rect(left + 2*third + stroke_offset, top + 2*third + stroke_offset, third - 2*stroke_offset, third - 2*stroke_offset),}

### Functions ###

def draw_board(surface, color, board):
    pygame.draw.line(surface, color, (left, top + third), (right, top + third), stroke_width)
    pygame.draw.line(surface, color, (left, bottom - third), (right, bottom - third), stroke_width)
    pygame.draw.line(surface, color, (left + third, top), (left + third, bottom), stroke_width)
    pygame.draw.line(surface, color, (right - third, top), (right - third, bottom), stroke_width)
    for i, cell in enumerate(board):
        if cell == 0:
            pygame.draw.ellipse(window, color, cell_pos[i], stroke_width)
        elif cell == 1:
            pygame.draw.line(window, color, (cell_pos[i].left, cell_pos[i].top), (cell_pos[i].right, cell_pos[i].bottom), stroke_width)
            pygame.draw.line(window, color, (cell_pos[i].right, cell_pos[i].top), (cell_pos[i].left, cell_pos[i].bottom), stroke_width)              


def find_cell(mouse_pos):
    """
    Returns a number between 0 and 8 representing a valid index into "board"
    Returns -1 if click irrelevant
    """
    if mouse_pos[0] > right or mouse_pos[0] < left or mouse_pos[1] < top or mouse_pos[1] > bottom:
        return -1
    elif mouse_pos[0] < left + third:
        if mouse_pos[1] < top + third:
            return 0
        elif mouse_pos[1] < bottom - third:
            return 3
        else:
            return 6
    elif mouse_pos[0] < right - third:
        if mouse_pos[1] < top + third:
            return 1
        elif mouse_pos[1] < bottom - third:
            return 4
        else:
            return 7
    else:
        if mouse_pos[1] < top + third:
            return 2
        elif mouse_pos[1] < bottom - third:
            return 5
        else:
            return 8
        

def draw_turn_info(window, player):
    font = pygame.font.Font('freesansbold.ttf', 32)
    player_sym = "X" if player == 1 else "O"
    text = font.render(f"Current move: {player_sym}", True, white)
    text_rect = text.get_rect()
    text_rect.center = (width//2, height * 0.2)
    window.blit(text, text_rect)

def check_win(board):
    if ((board[0] == board[1] == board[2] != -1) or 
        (board[3] == board[4] == board[5] != -1) or
        (board[6] == board[7] == board[8] != -1) or
        (board[0] == board[3] == board[6] != -1) or
        (board[1] == board[4] == board[7] != -1) or
        (board[2] == board[5] == board[8] != -1) or
        (board[0] == board[4] == board[8] != -1) or
        (board[2] == board[4] == board[6] != -1) ):
        return True
    return False

### Initialization ###

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")
board = [-1, -1, -1, -1, -1, -1, -1, -1, -1] # -1 = empty, 0 = X, 1 = O
fps_clock = pygame.time.Clock()
player = 0
moves_played = 0

### Game loop ###

run = True
while run:

    invalid_move = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            move_pos = find_cell(mouse_pos)
            if board[move_pos] == -1:
                board[move_pos] = player
            else:
                invalid_move = True
            player = 1 - player
            moves_played += 1

    if invalid_move: continue

    window.fill(black)
    draw_turn_info(window, player)
    draw_board(window, white, board)

    if check_win(board) or moves_played >= 9:
        run = False

    fps_clock.tick(60)
    pygame.display.update()


pygame.quit()