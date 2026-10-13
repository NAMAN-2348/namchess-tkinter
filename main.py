import tkinter as tk

from chess_game import ChessGame


class ChessApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("NamChess Tkinter Prototype")
        self.game = ChessGame()
        self.selected = None
        self.squares = []
        self.status = tk.StringVar(value="White to move")
        self._build_ui()
        self._render_board()

    def _build_ui(self) -> None:
        board_frame = tk.Frame(self.root)
        board_frame.pack(padx=8, pady=8)
        for r in range(8):
            row = []
            for c in range(8):
                btn = tk.Button(
                    board_frame,
                    width=4,
                    height=2,
                    font=("Arial", 20),
                    command=lambda rr=r, cc=c: self._on_click((rr, cc)),
                )
                btn.grid(row=r, column=c)
                row.append(btn)
            self.squares.append(row)
        tk.Label(self.root, textvariable=self.status).pack(pady=(0, 8))

    def _render_board(self) -> None:
        legal = self.game.legal_moves(self.selected) if self.selected is not None else []
        for r in range(8):
            for c in range(8):
                piece = self.game.piece_at((r, c))
                text = piece.symbol if piece else ""
                bg = "#f0d9b5" if (r + c) % 2 == 0 else "#b58863"
                if self.selected == (r, c):
                    bg = "#f7ec6e"
                elif (r, c) in legal:
                    bg = "#7ecf85"
                self.squares[r][c].configure(text=text, bg=bg, activebackground=bg)

    def _on_click(self, pos) -> None:
        piece = self.game.piece_at(pos)
        if self.selected is None:
            if piece and piece.color == self.game.current_turn:
                self.selected = pos
        else:
            if self.game.move(self.selected, pos):
                self.selected = None
                turn = "White" if self.game.current_turn == "white" else "Black"
                self.status.set(f"{turn} to move")
            elif piece and piece.color == self.game.current_turn:
                self.selected = pos
            else:
                self.selected = None
        self._render_board()


def main() -> None:
    root = tk.Tk()
    ChessApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
