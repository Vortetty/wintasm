#
# Config vars
#

MEM_SIZE = 4

ENABLE_HARD_MODE = False # Makes it a true esolang, only 2 availible operations, those are sufficient for any operation

#
# Imports 
#
from globs import *
import sys
from typing import List, Dict, Callable
import shlex
import traceback
import re

from ops import ops_init

#
# Initialize possible instructions
#
ops: Dict[str, Callable[[List[int], int, int, str, List[str]], None]] = {
    "nop": lambda *x: None
}
ops_init.init(ops, ENABLE_HARD_MODE)

#
# Initialize memory
#
memory = [0]*MEM_SIZE

#
# Make comments ignorable, then split file into lines, saves a version of this processed file as well
#
file = open(sys.argv[1], "r")

code = file.read()
code = re.sub(r"""(?<=.)(?<!^)(;|\#|//)(?=([^"]*"[^"]*")*[^"]*$).*(?=(\n|$))""", "", code)

commentsTMP = re.findall(r"""/\*.*?\*/""", code, re.MULTILINE | re.DOTALL)

for commentList in commentsTMP:
    comment = "".join(commentList)
    if comment != "" and comment != "\n":
        tmp = ";" + comment.replace("\n", "\n;")
        code = code.replace(comment, tmp)

lines = code.split("\n")

f = open(sys.argv[1] + ".preprocessed", "w")
f.write(";\n;\n; This file is for debugging purposes\n;\n;\n\n" + code)
f.close()

#
# Run file line-by-line, 
# 
lineCount = lineCounter()

try:
    while lineCount.line < len(lines):
        args = shlex.split(lines[lineCount.line], posix=False)

        if len(args) > 0 and not lines[lineCount.line].strip(" ").startswith((";", "#", "//")):
            op = args.pop(0)

            op_func = ops[op]

            result = op_func(memory, len(memory), lineCount, op, args, ops=ops)
        else:
            pass

        lineCount.line += 1
except BaseException as exception:
    if type(exception) != SystemExit:
        print("Please report the following exception on the github:\n   ", "".join(traceback.format_exception(type(exception), exception, exception.__traceback__)).replace("\n", "\n    "))

print(memory)
