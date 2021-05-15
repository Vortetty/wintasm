from typing import List, Dict, Callable
from globs import lineCounter

# Hard mode
from ops.op_src import op_nand
from ops.op_src import op_jmpif

# Normal mode
import imp
import os

def init(ops: Dict[str, Callable[[List[int], int, lineCounter, str, List[str]], None]], ENABLE_HARD_MODE):
    ops["nand"] = op_nand.op_nand                                                # The bare minimum modules
    ops["jmpif"] = op_jmpif.op_jmpif                                             # The bare minimum modules

    if not ENABLE_HARD_MODE:                                                     # Dont enable everything unless hard mode is off
        directory = "ops/op_src"                                                 # Directory that modules are stored in

        list_modules=os.listdir(directory)                                       # Get a list of available modules
        for module_name in list_modules:                                         # Iterate modules
            if module_name.split('.')[-1] == 'py':                               # Check that file is a python file
                module = imp.load_source('module', directory+os.sep+module_name) # Load module 
                func = getattr(module, module_name[:-3])                         # Get the function (it should have the same name as the file)
                ops[module_name[3:-3]] = func                                    # Set the function to the proper name