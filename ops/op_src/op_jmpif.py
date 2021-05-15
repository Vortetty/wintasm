from globs import *
from typing import List, Dict, Callable

def op_jmpif(mem: List[int], maxmem: int, line: lineCounter, op: str, oparg: List[str], **kwargs):
    checkParams(line, op, oparg, 4, 4) # make sure there are the right amount of args

    val1 = getVal(mem, maxmem, line, op, oparg, 0) # Get Value 1
    op_func = getOperatorFunction(mem, line, op, oparg, 1) # Operator function
    val2 = getVal(mem, maxmem, line, op, oparg, 2) # Get Value 2
    jmp_to = getVal(mem, maxmem, line, op, oparg, 3) # Get line to jump to

    if op_func(val1, val2):
        line.line = jmp_to-2
