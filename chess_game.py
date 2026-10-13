from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple

Position = Tuple[int, int]


@dataclass(frozen=True)
class Piece:
    color: str
    kind: str

    @property
    def symbol(self) -> str:
        symbols = {
            ("white", "king"): "♔",
            ("white", "queen"): "♕",
            ("white", "rook"): "♖",
            ("white", "bishop"): "♗",
            ("white", "knight"): "♘",
            ("white", "pawn"): "♙",
            ("black", "king"): "♚",
            ("black", "queen"): "♛",
            ("black", "rook"): "♜",
            ("black", "bishop"): "♝",
            ("black", "knight"): "♞",
            ("black", "pawn"): "♟",
        }
        return symbols[(self.color, self.kind)]


class ChessGame:
    def __init__(self) -> None:
        self.board: List[List[Optional[Piece]]] = [[None for _ in range(8)] for _ in range(8)]
        self.current_turn = "white"
        self._setup_board()

    def _setup_board(self) -> None:
        back = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        for col, kind in enumerate(back):
            self.board[0][col] = Piece("black", kind)
            self.board[7][col] = Piece("white", kind)
            self.board[1][col] = Piece("black", "pawn")
            self.board[6][col] = Piece("white", "pawn")

    def piece_at(self, pos: Position) -> Optional[Piece]:
        r, c = pos
        return self.board[r][c]

    def legal_moves(self, pos: Position) -> List[Position]:
        r, c = pos
        piece = self.piece_at(pos)
        if piece is None:
            return []
        if piece.kind == "pawn":
            return self._pawn_moves(r, c, piece.color)
        if piece.kind == "rook":
            return self._line_moves(r, c, [(1, 0), (-1, 0), (0, 1), (0, -1)], piece.color)
        if piece.kind == "bishop":
            return self._line_moves(r, c, [(1, 1), (1, -1), (-1, 1), (-1, -1)], piece.color)
        if piece.kind == "queen":
            return self._line_moves(
                r,
                c,
                [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)],
                piece.color,
            )
        if piece.kind == "king":
            return self._step_moves(
                r,
                c,
                [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)],
                piece.color,
            )
        if piece.kind == "knight":
            return self._step_moves(
                r,
                c,
                [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)],
                piece.color,
            )
        return []

    def move(self, from_pos: Position, to_pos: Position) -> bool:
        piece = self.piece_at(from_pos)
        if piece is None or piece.color != self.current_turn:
            return False
        if to_pos not in self.legal_moves(from_pos):
            return False
        fr, fc = from_pos
        tr, tc = to_pos
        self.board[tr][tc] = piece
        self.board[fr][fc] = None
        self.current_turn = "black" if self.current_turn == "white" else "white"
        return True

    def _inside(self, r: int, c: int) -> bool:
        return 0 <= r < 8 and 0 <= c < 8

    def _line_moves(self, r: int, c: int, deltas: List[Position], color: str) -> List[Position]:
        moves: List[Position] = []
        for dr, dc in deltas:
            nr, nc = r + dr, c + dc
            while self._inside(nr, nc):
                target = self.board[nr][nc]
                if target is None:
                    moves.append((nr, nc))
                else:
                    if target.color != color:
                        moves.append((nr, nc))
                    break
                nr += dr
                nc += dc
        return moves

    def _step_moves(self, r: int, c: int, deltas: List[Position], color: str) -> List[Position]:
        moves: List[Position] = []
        for dr, dc in deltas:
            nr, nc = r + dr, c + dc
            if not self._inside(nr, nc):
                continue
            target = self.board[nr][nc]
            if target is None or target.color != color:
                moves.append((nr, nc))
        return moves

    def _pawn_moves(self, r: int, c: int, color: str) -> List[Position]:
        moves: List[Position] = []
        step = -1 if color == "white" else 1
        start_row = 6 if color == "white" else 1

        forward = (r + step, c)
        if self._inside(*forward) and self.board[forward[0]][forward[1]] is None:
            moves.append(forward)
            two_forward = (r + 2 * step, c)
            if r == start_row and self._inside(*two_forward) and self.board[two_forward[0]][two_forward[1]] is None:
                moves.append(two_forward)

        for dc in (-1, 1):
            nr, nc = r + step, c + dc
            if not self._inside(nr, nc):
                continue
            target = self.board[nr][nc]
            if target is not None and target.color != color:
                moves.append((nr, nc))
        return moves
