from typing import Any, Callable, Union, Iterable, List
from colored import fg, bg, attr
import operator

class typesClass():
    def __init__(self):
        self.MEM_LOC = 0
        self.HEX_INT = 1
        self.BIN_INT = 2
        self.DEC_INT = 3
        self.STR = 4
        self.OPERATOR = 5

        self.INT_TYPES = [1, 2, 3]
        self.OPERATORS = ["==", "!=", ">", "<", ">=", "<="]

types = typesClass()

def switch(value: Any, comp: Callable[[Any, Any], bool]=operator.eq) -> Callable[[Any], bool]:
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
            elif val in types.OPERATORS:
                return types.OPERATOR
            else:
                return types.STR

def isIterable(obj: Any):
    return hasattr(obj, '__iter__')

def showError(line: int=0, op: str="", params: List[str]=[], errorparamnum: Union[Iterable[int], int, None]=None, message: str="No message provided", add1toline: bool=True):
    params.append(" ")
    if type(errorparamnum) == int or isIterable(errorparamnum):
        if not isIterable(errorparamnum):
            errorparamnum = [errorparamnum]

        err = f"""Error line {line+add1toline}:\n    {op}"""

        itercnt = 0
        for i in params:
            err += f""" {fg("red")}{attr('underlined')}{i}{attr("reset")}""" if itercnt in errorparamnum else f" {i}"
            itercnt += 1

        err += f"\n\n{message}"

        print(err)

    else:
        print(
            f"""
Error line {line+add1toline}:
    {op} {" ".join(params)}

{message}""".strip("\n")
        )
    exit()

def checkParams(line: int, op: str, oparg: List[str], minops: int=-1, maxops: int=-1) -> bool:
    if len(oparg) > maxops and maxops != -1:
        showError(line=line, op=op, params=oparg, errorparamnum=range(minops, len(oparg)), message=f"Too many arguments")
        return False
    elif len(oparg) < minops and minops != -1:
        showError(line=line, op=op, params=oparg, errorparamnum=None, message=f"Too few arguments")
        return False
    
    return True

def getVal(mem: List[int], maxmem: int, line: int, op: str, oparg: List[str], argnum: int) -> int:
    if getType(oparg[argnum]) in types.INT_TYPES:
        return int(oparg[argnum], 0)
    elif getType(oparg[argnum]) == types.MEM_LOC:
        tmp = int(oparg[argnum].replace("m", "x"), 0)
        if tmp < maxmem and tmp >= 0:
            return mem[tmp]
        else:
            showError(line, op, oparg, argnum, f"Memory location \"{oparg[argnum]}\" is out of bounds")
    else:
        showError(line, op, oparg, argnum, f"Argument \"{oparg[argnum]}\" is not an integer or memory location.")

def getMemLoc(maxmem: int, line: int, op: str, oparg: List[str], argnum: int):
    if getType(oparg[argnum]) == types.MEM_LOC:
        tmp = int(oparg[argnum].replace("m", "x"), 0)
        if tmp < maxmem and tmp >= 0:
            return tmp
        else:
            showError(line, op, oparg, argnum, f"Memory location \"{oparg[argnum]}\" is out of bounds")
    else:
        showError(line, op, oparg, argnum, f"Argument \"{oparg[argnum]}\" is not an integer or memory location.")

def getOperatorFunction(maxmem: int, line: int, op: str, oparg: List[str], argnum: int):
    if getType(oparg[argnum]) == types.OPERATOR:
        if oparg[argnum] == "==":
            return operator.eq
        elif oparg[argnum] == "!=":
            return operator.ne
        elif oparg[argnum] == ">":
            return operator.gt
        elif oparg[argnum] == "<":
            return operator.lt
        elif oparg[argnum] == ">=":
            return operator.ge
        elif oparg[argnum] == "<=":
            return operator.le
        else:
            showError(line, op, oparg, argnum, f"Internal error processing argument \"{oparg[argnum]}\". Please report on the github and include full code") 
    else:
        showError(line, op, oparg, argnum, f"Argument \"{oparg[argnum]}\" is not an operator.")