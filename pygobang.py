import tkinter as tk

# Constants for the board size and the stone size
BOARD_SIZE = 19
CELL_SIZE = 50
STONE_RADIUS = 22

# Initialize variables
stones = {}

def draw_board(canvas):
    """Draw the Go board grid."""
    for i in range(BOARD_SIZE):
        # Draw vertical lines
        canvas.create_line(
            CELL_SIZE * (i + 1), CELL_SIZE, 
            CELL_SIZE * (i + 1), CELL_SIZE * BOARD_SIZE,
            fill="black"
        )
        # Draw horizontal lines
        canvas.create_line(
            CELL_SIZE, CELL_SIZE * (i + 1), 
            CELL_SIZE * BOARD_SIZE, CELL_SIZE * (i + 1),
            fill="black"
        )

def place_or_remove_stone(event):
    """Place or remove a stone on the board."""
    x, y = event.x, event.y
    grid_x = round((x - CELL_SIZE) / CELL_SIZE)
    grid_y = round((y - CELL_SIZE) / CELL_SIZE)

    if 0 <= grid_x < BOARD_SIZE and 0 <= grid_y < BOARD_SIZE:
        if (grid_x, grid_y) in stones:
            # Remove stone
            canvas.delete(stones[(grid_x, grid_y)])
            del stones[(grid_x, grid_y)]
        else:
            # Place stone
            color = "black" if len(stones) % 2 == 0 else "white"
            stone = canvas.create_oval(
                CELL_SIZE * (grid_x + 1) - STONE_RADIUS,
                CELL_SIZE * (grid_y + 1) - STONE_RADIUS,
                CELL_SIZE * (grid_x + 1) + STONE_RADIUS,
                CELL_SIZE * (grid_y + 1) + STONE_RADIUS,
                fill=color, outline='black', width=2
            )
            stones[(grid_x, grid_y)] = stone

# Set up the main application window
root = tk.Tk()
root.title("Go Board")
root.resizable(False, False)

# Set up the canvas to draw the board and stones
canvas = tk.Canvas(
    root, width=CELL_SIZE * (BOARD_SIZE + 1), 
    height=CELL_SIZE * (BOARD_SIZE + 1), bg="tan"
)
canvas.pack()

# Draw the initial board
draw_board(canvas)

# Bind mouse click event to placing/removing stones
canvas.bind("<Button-1>", place_or_remove_stone)

# Start the Tkinter event loop
root.mainloop()
