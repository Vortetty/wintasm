from globs import *
from typing import List, Dict, Callable
from array import array
from colored import fg, bg, attr

def op_set(mem: List[int], maxmem: int, line: int, op: str, oparg: List[str]):
    print("op_set called")

    if getType(oparg[0]) == types.MEM_LOC:
        val = 0
        loc = 0

        oparg.append("")

        # Get Value
        if getType(oparg[1]) in types.INT_TYPES:
            val = int(oparg[1], 0)
        elif getType(oparg[1]) == types.MEM_LOC:
            tmp = int(oparg[1].replace("m", "x"), 0)
            if tmp < maxmem and tmp >= 0:
                val = mem[tmp]
            else:
                showError(line, op, oparg, 0, f"Memory location \"{oparg[1]}\" is out of bounds")
        else:
            showError(line, op, oparg, 0, f"Argument \"{oparg[1]}\" is not an integer or memory location.")

        # Get location
        if getType(oparg[0]) == types.MEM_LOC:
            tmp = int(oparg[0].replace("m", "x"), 0)
            if tmp < maxmem and tmp >= 0:
                loc = mem[tmp]
            else:
                showError(line, op, oparg, 0, f"Memory location \"{oparg[0]}\" is out of bounds")
        else:
            showError(line, op, oparg, 0, f"Argument \"{oparg[0]}\" is not a memory location.")
        
        # Assume all is well
        mem[loc] = val
        
    else:
        showError(line, op, oparg, 0, f"Argument \"{oparg[0]}\" is an invalid memory location.")

def init(ops: Dict[str, Callable[[List[int], int, int, str, List[str]], None]]) -> None:
    ops["set"] = op_set