import tkinter as tk
from tkinter import messagebox
import chess

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.board = chess.Board()
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.draw_board()

    def draw_board(self):
        colors = ["white", "gray"]
        for i in range(8):
            for j in range(8):
                color = colors[(i + j) % 2]
                self.canvas.create_rectangle(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, fill=color)
        self.draw_pieces()

    def draw_pieces(self):
        self.canvas.delete("pieces")
        for i in range(64):
            row = i // 8
            col = i % 8
            piece = self.board.piece_at(i)
            if piece is not None:
                self.canvas.create_text(col * 50 + 25, row * 50 + 25, text=str(piece), tags="pieces")

    def move_piece(self, start, end):
        move = chess.Move.from_uci(start + end)
        if move in self.board.legal_moves:
            self.board.push(move)
            self.draw_pieces()
            if self.board.is_checkmate():
                messagebox.showinfo("Game Over", "Checkmate! You Win!")
            elif self.board.is_stalemate():
                messagebox.showinfo("Game Over", "Stalemate! It's a Draw!")
            else:
                self.make_ai_move()

    def make_ai_move(self):
        # Here you can implement your AI logic to make a move
        pass

def on_click(event):
    col = event.x // 50
    row = event.y // 50
    pos = chr(ord('a') + col) + str(8 - row)
    if game.clicked_piece is None:
        game.clicked_piece = pos
    else:
        game.move_piece(game.clicked_piece, pos)
        game.clicked_piece = None

root = tk.Tk()
game = ChessGame(root)
game.clicked_piece = None
game.canvas.bind("<Button-1>", on_click)
root.mainloop()