"""Small Tkinter-driven regression tests for the NAMCHESS prototype.

Run with `python tests/smoke_test.py` in a desktop session, or with
`xvfb-run -a python tests/smoke_test.py` on Linux without a visible display.
"""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "main.py"
source = APP.read_text(encoding="utf-8")
if not source.rstrip().endswith("chs.mainloop()"):
    raise RuntimeError("Unexpected main.py entry point; update this test harness.")
app_prefix = source.rsplit("chs.mainloop()", 1)[0]

CASES = {
    "opening sequence and rook path blocking": r'''
def move(src, dst):
    butom[src[0]][src[1]]()
    butom[dst[0]][dst[1]]()
move((6, 4), (4, 4))  # e2-e4
assert pclt[4][4] == 'wp' and pclt[6][4] == 's'
move((1, 4), (3, 4))  # e7-e5
assert pclt[3][4] == 'bp' and pclt[1][4] == 's'
move((7, 6), (5, 5))  # Ng1-f3
assert pclt[5][5] == 'wn' and pclt[7][6] == 's'
move((0, 1), (2, 2))  # Nb8-c6
assert pclt[2][2] == 'bn' and pclt[0][1] == 's'
old_turns = cob
move((7, 0), (5, 0))  # rook is blocked by the a-pawn
assert pclt[7][0] == 'wr' and pclt[5][0] == 's' and cob == old_turns
''',
    "white pawn rules": r'''
def move(src, dst):
    butom[src[0]][src[1]]()
    butom[dst[0]][dst[1]]()
pclt[5][4] = 'bp'; pcl[5][4] = '♟'; chsl[5][4].config(text='♟')
pclt[5][3] = 'bp'; pcl[5][3] = '♟'; chsl[5][3].config(text='♟')
move((6, 4), (4, 4))  # cannot jump over a piece
assert pclt[6][4] == 'wp' and pclt[4][4] == 's'
move((6, 4), (5, 4))  # cannot capture straight ahead
assert pclt[6][4] == 'wp' and pclt[5][4] == 'bp'
move((6, 4), (5, 3))  # diagonal capture works from starting rank
assert pclt[6][4] == 's' and pclt[5][3] == 'wp' and cob == 1
''',
    "black pawn rules": r'''
def move(src, dst):
    butom[src[0]][src[1]]()
    butom[dst[0]][dst[1]]()
cob = 1  # isolate the same cases with Black to move
pclt[2][4] = 'wp'; pcl[2][4] = '♙'; chsl[2][4].config(text='♙')
pclt[2][3] = 'wp'; pcl[2][3] = '♙'; chsl[2][3].config(text='♙')
move((1, 4), (3, 4))
assert pclt[1][4] == 'bp' and pclt[3][4] == 's'
move((1, 4), (2, 4))
assert pclt[1][4] == 'bp' and pclt[2][4] == 'wp'
move((1, 4), (2, 3))
assert pclt[1][4] == 's' and pclt[2][3] == 'bp' and cob == 2
''',
}


def main():
    xvfb = shutil.which("xvfb-run")
    passed = 0
    for name, body in CASES.items():
        test_source = app_prefix + "\n" + body + "\nchs.destroy()\n"
        command = [sys.executable, "-c", test_source]
        if xvfb:
            command = [xvfb, "-a", *command]
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=20)
        if result.returncode:
            print(f"FAIL: {name}")
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr, file=sys.stderr)
            return result.returncode
        print(f"PASS: {name}")
        passed += 1
    print(f"{passed}/{len(CASES)} smoke-test groups passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
