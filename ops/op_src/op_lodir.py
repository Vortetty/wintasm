from globs import *
from typing import List, Dict, Callable
import os
import imp
import re

def op_lodir(mem: List[int], maxmem: int, line: lineCounter, op: str, oparg: List[str], **kwargs):
    checkParams(line, op, oparg, 1, 1)                                                         # Check parameter count

    directory = None                                                                           # Initialize directory var

    if not os.path.isabs(getStr(mem, maxmem, line, op, oparg, 0)):                             # Determine if directory is absolute
        directory = os.path.join(kwargs["scriptDir"], getStr(mem, maxmem, line, op, oparg, 0)) # Relative dir
    else: directory = getStr(mem, maxmem, line, op, oparg, 0)                                  # Absolute dir

    list_modules=os.listdir(directory)                                                         # Get a list of available modules
    for module_name in list_modules:                                                           # Iterate modules
        if re.search(r"op_.*\.py", module_name):                                               # Check that file is a python file
            module = imp.load_source('module', directory+os.sep+module_name)                   # Load module 
            func = getattr(module, module_name[:-3])                                           # Get the function (it should have the same name as the file)
            kwargs["ops"][module_name[3:-3]] = func                                            # Put the func into the
