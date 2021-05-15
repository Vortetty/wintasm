from globs import *
from typing import List, Dict, Callable

def op_set(mem: List[int], maxmem: int, line: lineCounter, op: str, oparg: List[str], **kwargs):
    checkParams(line, op, oparg, 2, 2)

    loc = getMemLoc(maxmem, line, op, oparg, 0) # Get memory location to store
    val = getVal(mem, maxmem, line, op, oparg, 1) # Get Value to store

    mem[loc] = val
