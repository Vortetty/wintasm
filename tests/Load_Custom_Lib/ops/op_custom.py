from globs import *
from typing import List, Dict, Callable

def op_custom(mem: List[int], maxmem: int, line: lineCounter, op: str, oparg: List[str], **kwargs):
    checkParams(line, op, oparg, -1, -1) # make sure there are the right amount of args

    print("This is a custom op!")
