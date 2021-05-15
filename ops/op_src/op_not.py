from globs import *
from typing import List, Dict, Callable

def op_not(mem: List[int], maxmem: int, line: lineCounter, op: str, oparg: List[str], **kwargs):
    checkParams(line, op, oparg, 3, 3) # make sure there are the right amount of args

    val1 = getVal(mem, maxmem, line, op, oparg, 0) # Get Value 1
    loc = getMemLoc(maxmem, line, op, oparg, 1) # Get memory location to store
    
    mem[loc] = ~val1 # not val1

def init(ops: Dict[str, Callable[[List[int], int, int, str, List[str]], None]]) -> None:
    ops["noy"] = op_not