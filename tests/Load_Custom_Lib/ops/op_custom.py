from globs import *
from typing import List, Dict, Callable

def op_and(mem: List[int], maxmem: int, line: lineCounter, op: str, oparg: List[str], **kwargs):
    checkParams(line, op, oparg, 0, 0) # make sure there are the right amount of args

    print("This is a custom op!")
