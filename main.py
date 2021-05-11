from globs import *
import sys
from typing import List, Dict, Callable
import shlex
import traceback
import re

from ops import op_set
#from ops import op_xor
#from ops import op_jmpif

ops: Dict[str, Callable[[List[int], int, int, str, List[str]], None]] = {
    "nop": lambda *x: None
}

op_set.init(ops)
#op_xor.init(ops)
#op_jmpif.init(ops)

memory = [0]*4

file = open(sys.argv[1], "r")

# Read in file, remove comments, then split code into lines
code = file.read()
commentsTMP = re.findall(r"""((;|\#|//)(?=([^"]*"[^"]*")*[^"]*$).*|/\*(?=([^"]*"[^"]*")*[^"]*$)(.|\n)*?\*/(?=([^"]*"[^"]*")*[^"]*$))""", code)

comments = []

for commentList in commentsTMP:
    for comment in commentList:
        tmp = ";" + comment.replace("\n", "\n;")[:-1]
        #print(repr(comment), "->", repr(tmp))
        code = code.replace(comment, tmp)

lines = code.split("\n")

line = 0


try:
    while line < len(lines):
        args = shlex.split(lines[line], posix=False)

        if len(args) > 0 or line.startswith([";"]):
            op = args.pop(0)

            op_func = ops[op]

            result = op_func(memory, len(memory), line, op, args)
        else:
            pass

        line += 1
except BaseException as exception:
    if type(exception) != SystemExit:
        print("Please report the following exception on the github:\n   ", "".join(traceback.format_exception(type(exception), exception, exception.__traceback__)).replace("\n", "\n    "))

print(memory)
