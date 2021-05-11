from _typeshed import NoneType
from operator import eq
from typing import Any, Callable, Union
from colored import fg, bg, attr

class typesClass():
    def __init__(self):
        self.MEM_LOC = 0
        self.HEX_INT = 1
        self.BIN_INT = 2
        self.DEC_INT = 3
        self.STR = 4

        self.INT_TYPES = [1, 2, 3]

types = typesClass()

def switch(value: Any, comp: Callable[[Any, Any], bool]=eq) -> Callable[[Any], bool]:
    return [lambda match: comp(match, value)]

def getType(val: str) -> int:
    for case in switch(val, lambda x, y:y.startswith(x)):
        if case("0m"):
            return types.MEM_LOC
        elif case("0x"):
            return types.HEX_INT
        elif case("0b"):
            return types.BIN_INT
        else:
            if val.isnumeric():
                return types.DEC_INT
            else:
                return types.STR

def showError(line: int, op: str, params: str, errorparamnum: Union[int, None]=None, message: str="No message provided", add1toline: bool=True):
    params.append(" ")

    if errorparamnum != None:
        print(
            f"""
Error line {line+add1toline}:
    {op} {" ".join(params[:errorparamnum])} {fg("red")}{attr('underlined')}{params[errorparamnum]}{attr("reset")} {" ".join(params[errorparamnum+1:])}

{message}""".strip("\n")
        )
    else:
        print(
            f"""
Error line {line+add1toline}:
    {op} {" ".join(params)}

{message}""".strip("\n")
        )
    exit()
