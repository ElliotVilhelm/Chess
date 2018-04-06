from utils import int_sq120_sq64

init_board = "xxxxxxxxxx" \
             "xxxxxxxxxx" \
             "xrnbqkbnrx" \
             "xppppppppx" \
             "xoooooooox" \
             "xoooooooox" \
             "xoooooooox" \
             "xoooooooox" \
             "xPPPPPPPPx" \
             "xRNBQKBNRx" \
             "xxxxxxxxxx" \
             "xxxxxxxxxx"

sq120 = int_sq120_sq64()

# Common squares
A1 = 91
H1 = 98
A8 = 21
H8 = 28

# State indexes
BOARD_INDEX = 0
TURN_INDEX = 1
EN_PAS_INDEX = 2
HALF_MOVE_INDEX = 3
FULL_MOVE_INDEX = 4
C_PERM_INDEX = 5
WK_SQ_INDEX = 6
BK_SQ_INDEX = 7
# Castle Perm indexes
WKC_INDEX = 0
WQC_INDEX = 1
BKC_INDEX = 2
BQC_INDEX = 3

# Castle States
CASTLE_NEW = 0
CASTLE_OPEN = 1
CASTLED = 2
CASTLE_VOIDED = -1

black_pieces = "pnbrq"
white_pieces = "PNBRQ"  # excludes king
all_white = "PKQRNBP"  # includes king
all_black = "pkqrnbp"
black_sliders = "qrb"
white_sliders = "QRB"
all_pieces = "KQRBNPkqrbnp"
ranks = "87654321"
