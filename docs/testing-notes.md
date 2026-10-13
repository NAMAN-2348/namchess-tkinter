# Testing notes

## Automated smoke checks

The baseline application was run under a virtual X display, and the repeatable checks are available in [`tests/smoke_test.py`](../tests/smoke_test.py). Run `python tests/smoke_test.py` from a desktop session, or use `xvfb-run -a python tests/smoke_test.py` on Linux without a visible display. The scripted checks cover:

- White e-pawn: e2 to e4.
- Black e-pawn: e7 to e5.
- White knight: g1 to f3.
- Black knight: b8 to c6.
- A rook move blocked by its own pawn was rejected.
- A pawn could not capture a piece directly forward.
- A pawn's two-square advance was rejected when its intermediate square was occupied.
- A pawn could capture diagonally from its starting rank.
- The same pawn restrictions were checked for Black.

Python syntax compilation was also run on `main.py` and the four archived complete iterations. These checks do not establish that all chess rules are implemented correctly.

## Important tests still needed

- All legal and illegal moves for each piece.
- Sliding pieces blocked by pieces in between, for every direction.
- Pawn movement and captures in all columns and rows, including board edges.
- Moves that would leave the moving side's king in check.
- Check, checkmate, and stalemate positions.
- Special moves: castling, en passant, and promotion.
- Captures, turn order, and repeated invalid selections.

Treat NAMCHESS as an educational prototype, not as an authoritative chess arbiter.
