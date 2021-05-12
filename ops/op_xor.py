from globs import *
from typing import List, Dict, Callable

def op_xor(mem: List[int], maxmem: int, line: lineCounter, op: str, oparg: List[str]):
    checkParams(line, op, oparg, 3, 3) # make sure there are the right amount of args

    val1 = getVal(mem, maxmem, line, op, oparg, 0) # Get Value 1
    val2 = getVal(mem, maxmem, line, op, oparg, 1) # Get Value 2
    loc = getMemLoc(maxmem, line, op, oparg, 2) # Get memory location to store
    
    mem[loc] = val1 ^ val2 # xor val1 and val2 then store it

def init(ops: Dict[str, Callable[[List[int], int, int, str, List[str]], None]]) -> None:
    ops["xor"] = op_xor