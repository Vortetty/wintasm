from globs import *
from typing import List, Dict, Callable
import os
import imp

def op_and(mem: List[int], maxmem: int, line: lineCounter, op: str, oparg: List[str], **kwargs):
        checkParams(line, op, oparg, 1, -1)                                      # Check parameter count
        directory = "ops/op_src"                                                 # Directory that modules are stored in

        list_modules=os.listdir(directory)                                       # Get a list of available modules
        for module_name in list_modules:                                         # Iterate modules
            if module_name.split('.')[-1] == 'py':                               # Check that file is a python file
                module = imp.load_source('module', directory+os.sep+module_name) # Load module 
                func = getattr(module, module_name[:-3])                         # Get the function (it should have the same name as the file)
                kwargs["ops"][module_name[3:-3]] = func                          # Put the func into the

def init(ops: Dict[str, Callable[[List[int], int, int, str, List[str]], None]]) -> None:
    ops["and"] = op_and