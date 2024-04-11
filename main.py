import tkinter as tk
from tkinter import messagebox

class ChessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Chess Game")

        self.board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                      ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                      ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]

        self.current_player = 'white'
        self.selected_piece = None
        self.create_board()

    def create_board(self):
        self.tiles = []
        for i in range(8):
            row = []
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "gray"
                tile = tk.Label(self.master, text=self.board[i][j], bg=color, width=5, height=2, font=("Arial", 12, "bold"))
                tile.grid(row=i, column=j)
                tile.bind("<Button-1>", lambda e, i=i, j=j: self.on_tile_click(i, j))
                row.append(tile)
            self.tiles.append(row)

    def on_tile_click(self, row, col):
        piece = self.board[row][col]
        if piece.strip() != '' and self.current_player == 'white' and piece.isupper():
            if self.selected_piece:
                self.tiles[self.selected_piece[0]][self.selected_piece[1]].config(bg=self.get_tile_color(self.selected_piece[0], self.selected_piece[1]))
            self.selected_piece = (row, col)
            self.tiles[row][col].config(bg='yellow')
        elif piece.strip() != '' and self.current_player == 'black' and piece.islower():
            if self.selected_piece:
                self.tiles[self.selected_piece[0]][self.selected_piece[1]].config(bg=self.get_tile_color(self.selected_piece[0], self.selected_piece[1]))
            self.selected_piece = (row, col)
            self.tiles[row][col].config(bg='yellow')
        elif self.selected_piece:
            if self.move_piece(self.selected_piece, (row, col)):
                self.current_player = 'black' if self.current_player == 'white' else 'white'
            if self.selected_piece:
                self.tiles[self.selected_piece[0]][self.selected_piece[1]].config(bg=self.get_tile_color(self.selected_piece[0], self.selected_piece[1]))
            self.selected_piece = None

    def move_piece(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        piece = self.board[from_row][from_col]
        if self.current_player == 'white' and piece.isupper():
            if self.is_valid_move(from_pos, to_pos):
                self.board[to_row][to_col] = piece
                self.board[from_row][from_col] = ' '
                self.tiles[from_row][from_col].config(text=' ')
                self.tiles[to_row][to_col].config(text=piece)
                return True
            else:
                messagebox.showinfo("Invalid Move", "Invalid move, try again.")
                return False
        elif self.current_player == 'black' and piece.islower():
            if self.is_valid_move(from_pos, to_pos):
                self.board[to_row][to_col] = piece
                self.board[from_row][from_col] = ' '
                self.tiles[from_row][from_col].config(text=' ')
                self.tiles[to_row][to_col].config(text=piece)
                return True
            else:
                messagebox.showinfo("Invalid Move", "Invalid move, try again.")
                return False
        else:
            return False

    def is_valid_move(self, from_pos, to_pos):
        # Implement valid move logic here
        return True

    def get_tile_color(self, row, col):
        return "white" if (row + col) % 2 == 0 else "gray"

def main():
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()