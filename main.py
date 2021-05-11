from globs import *
import sys
from array import array
from typing import List, Dict, Callable
import shlex

from ops import op_set
#from ops import op_xor
#from ops import op_jmpif

ops: Dict[str, Callable[[List[int], int, int, str, List[str]], None]] = {
    "nop": lambda *x: print("Nop called")
}

print("Imported")

op_set.init(ops)
#op_xor.init(ops)
#op_jmpif.init(ops)

print("inited")

memory = [0]*4

file = open(sys.argv[1], "r")
lines = file.readlines()

line = 0

print("opened and read")

while line < len(lines):
    print(line)

    args = shlex.split(lines[line], posix=False)

    if len(args) > 0:
        op = args.pop(0)

        op_func = ops[op]

        result = op_func(memory, len(memory), line, op, args)
    else:
        pass

    print(memory)