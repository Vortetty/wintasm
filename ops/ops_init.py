from typing import List, Dict, Callable
from ops import op_set
from ops import op_xor
from ops import op_jmpif

def init(ops: Dict[str, Callable[[List[int], int, int, str, List[str]], None]]):
    op_set.init(ops)
    op_xor.init(ops)
    op_jmpif.init(ops)