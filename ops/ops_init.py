from typing import List, Dict, Callable
from ops import op_set
from ops import op_xor
from ops import op_nand
from ops import op_jmpif
from globs import *

def init(ops: Dict[str, Callable[[List[int], int, lineCounter, str, List[str]], None]], ENABLE_HARD_MODE):
    op_set.init(ops)
    op_nand.init(ops)
    op_jmpif.init(ops)

    if not ENABLE_HARD_MODE:
        op_xor.init(ops)