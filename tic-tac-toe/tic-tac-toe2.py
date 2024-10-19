import pygame

# Colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Constants
LINE_COLOR = BLACK
BG_COLOR = WHITE
SCREEN_SIZE = 300  
LINE_THICKNESS = 5
CELL_SIZE = SCREEN_SIZE // 3


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('Tic-Tac-Toe')

# Set up font for displaying "X" and "O"
pygame.font.init()
font = pygame.font.SysFont(None, 100)

# Set up board
board = [[None, None, None], 
         [None, None, None], 
         [None, None, None]]

current_player = "X"


# Given a mouse position as a cooordinate pair, 
# find the square where the mouse was clicked
def get_grid_pos(mouse_pos):
  x, y = mouse_pos
  row = y // (SCREEN_SIZE // 3)
  col = x // (SCREEN_SIZE // 3)
  return row, col

# Check for a win
# Returns True if there is a win, False otherwise
def check_for_win():
  
  # Check rows
  if board[0][0] == board[0][1] == board[0][2] and board[0][0] is not None:
      return True
  if board[1][0] == board[1][1] == board[1][2] and board[1][0] is not None:
      return True
  if board[2][0] == board[2][1] == board[2][2] and board[2][0] is not None:
      return True
  
  # Check columns
  if board[0][0] == board[1][0] == board[2][0] and board[0][0] is not None:
      return True
  if board[0][1] == board[1][1] == board[2][1] and board[0][1] is not None:
      return True
  if board[0][2] == board[1][2] == board[2][2] and board[0][2] is not None:
      return True
  
  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
    return True
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
    return True
  
  return False

# Update the board with a player's move
# Return True is the move is valid and was applied, False otherwise
def update_board(row, col, player):
  if board[row][col] is None: 
    board[row][col] = player
    return True
  return False

# Draw the current state of the board
def draw_board():
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, SCREEN_SIZE), LINE_THICKNESS)
    pygame.draw.line(screen, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, SCREEN_SIZE), LINE_THICKNESS)
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (SCREEN_SIZE, CELL_SIZE), LINE_THICKNESS)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * CELL_SIZE), (SCREEN_SIZE, 2 * CELL_SIZE), LINE_THICKNESS)

    # Draw the Xs and Os
    for row in range(3):
        for col in range(3):
            if board[row][col] is not None:
                # Render the player's symbol ("X" or "O")
                text = font.render(board[row][col], True, BLACK)
                # Calculate the position to center the text in the cell
                text_rect = text.get_rect(center=((col * CELL_SIZE) + CELL_SIZE // 2, (row * CELL_SIZE) + CELL_SIZE // 2))
                # Draw the text on the screen
                screen.blit(text, text_rect)


### Main Game Loop ###


running = True
while running:
    
  # Event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    # Detect mouse click
    if event.type == pygame.MOUSEBUTTONDOWN: 
      mouse_pos = pygame.mouse.get_pos()
      row, col = get_grid_pos(mouse_pos)

      # Update board, check for win, switch player (if necessary)
      if update_board(row, col, current_player):
        if check_for_win():
          running = False
        else:
          current_player = 'O' if current_player == 'X' else 'X'

  # Drawing
  screen.fill(WHITE)
  draw_board()

  pygame.display.flip()

pygame.quit()
