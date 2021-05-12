from typing import List, Dict, Callable
from globs import *

# Hard mode
from ops.op_src import op_nand
from ops.op_src import op_jmpif

# Normal mode
import imp
import os

def init(ops: Dict[str, Callable[[List[int], int, lineCounter, str, List[str]], None]], ENABLE_HARD_MODE):
    op_nand.init(ops)
    op_jmpif.init(ops)

    if not ENABLE_HARD_MODE:
        directory = "ops/op_src"

        list_modules=os.listdir(directory)
        for module_name in list_modules:
            if module_name.split('.')[-1] == 'py':
                module = imp.load_source('module', directory+os.sep+module_name)
                module.init(ops)