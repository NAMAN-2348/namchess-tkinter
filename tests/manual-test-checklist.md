# Manual test checklist

Use this list when testing changes. Mark an item only after testing it in the GUI.

- [ ] The board opens and all 32 pieces are displayed in the correct starting squares.
- [ ] White moves first; turns alternate after accepted moves.
- [ ] Each piece's valid movement patterns work.
- [ ] A piece cannot move through another piece when its movement pattern is blocked.
- [ ] A piece cannot capture a piece of its own colour.
- [ ] Pawns move forward, can move two squares only when allowed and unobstructed, and capture diagonally.
- [ ] Knight moves work even when pieces surround the knight.
- [ ] Sliding pieces stop at the first occupied square.
- [ ] The king cannot move into check and cannot be captured.
- [ ] Check, checkmate, and stalemate are detected correctly.
- [ ] Castling, en passant, and promotion are implemented and tested, or are clearly documented as unsupported.
- [ ] Invalid actions do not crash the application or corrupt the board state.

## Pawn-specific regression checks

- [ ] A pawn moves one square forward only into an empty square.
- [ ] A pawn moves two squares from its starting rank only if both squares ahead are empty.
- [ ] A pawn cannot capture a piece directly forward.
- [ ] A pawn captures diagonally when an opposing piece is present.
- [ ] Starting-rank pawns may capture diagonally if an opposing piece is on that diagonal.
- [ ] Verify the same cases for both colours.
