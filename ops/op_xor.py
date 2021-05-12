from os import error
from globs import *
from typing import List, Dict, Callable
from array import array
from colored import fg, bg, attr

def op_xor(mem: List[int], maxmem: int, line: int, op: str, oparg: List[str]):
    checkParams(line, op, oparg, 3, 3)

    val1 = getVal(mem, maxmem, line, op, oparg, 0) # Get Value 2
    val2 = getVal(mem, maxmem, line, op, oparg, 1) # Get Value 2
    loc = getMemLoc(maxmem, line, op, oparg, 2) # Get memory location to store
    
    # Assume all is well
    mem[loc] = val1 ^ val2

def init(ops: Dict[str, Callable[[List[int], int, int, str, List[str]], None]]) -> None:
    ops["set"] = op_xor