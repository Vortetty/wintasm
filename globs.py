from operator import eq
from typing import Any, Callable
from enum import Enum
from colored import fg, bg, attr

class types(Enum):
    MEM_LOC = 0
    HEX_INT = 1
    BIN_INT = 2
    DEC_INT = 3
    STR = 4

    INT_TYPES = [1, 2, 3]


def switch(value: Any, comp: Callable[[Any, Any], bool]=eq) -> Callable[[Any], bool]:
    return [lambda match: comp(match, value)]

def getType(val: str):
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

def showError(line, op, params, paramnum, message):
    params.append(" ")

    print(
        f"""
Error line {line}:
    {op} {params[:paramnum]} {fg("red")}{attr('underlined')}{params[paramnum]}{attr("reset")} {" ".join(params[paramnum+1:])}

{message}
        """.strip("\n")
    )
    exit()
