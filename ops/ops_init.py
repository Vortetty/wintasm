from typing import List, Dict, Callable
from globs import *

# Hard mode
from ops import op_nand
from ops import op_jmpif

# Normal mode
from ops import op_set
from ops import op_xor
from ops import op_and
from ops import op_not

def init(ops: Dict[str, Callable[[List[int], int, lineCounter, str, List[str]], None]], ENABLE_HARD_MODE):
    op_nand.init(ops)
    op_jmpif.init(ops)

    if not ENABLE_HARD_MODE:
        op_set.init(ops)
        op_xor.init(ops)
        op_and.init(ops)
        op_not.init(ops)