from operator import eq
from typing import Any, Callable, Union, Iterable, List
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

def showError(line: int=0, op: str="", params: List[str]=[], errorparamnum: Union[Iterable[int], int, None]=None, message: str="No message provided", add1toline: bool=True):
    params.append(" ")
    if type(errorparamnum) == int or iter(errorparamnum):
        errorparamnum = list(errorparamnum)

        err = f"""Error line {line+add1toline}:\n    {op} """

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

def getVal(mem: List[int], maxmem: int, line: int, op: str, oparg: List[str], opnum: int) -> int:
    if getType(oparg[opnum]) in types.INT_TYPES:
        return int(oparg[opnum], 0)
    elif getType(oparg[opnum]) == types.MEM_LOC:
        tmp = int(oparg[opnum].replace("m", "x"), 0)
        if tmp < maxmem and tmp >= 0:
            return mem[tmp]
        else:
            showError(line, op, oparg, opnum, f"Memory location \"{oparg[opnum]}\" is out of bounds")
    else:
        showError(line, op, oparg, opnum, f"Argument \"{oparg[opnum]}\" is not an integer or memory location.")

def getMemLoc(maxmem: int, line: int, op: str, oparg: List[str], opnum: int):
    if getType(oparg[opnum]) == types.MEM_LOC:
        tmp = int(oparg[opnum].replace("m", "x"), 0)
        if tmp < maxmem and tmp >= 0:
            return tmp
        else:
            showError(line, op, oparg, opnum, f"Memory location \"{oparg[opnum]}\" is out of bounds")
    else:
        showError(line, op, oparg, opnum, f"Argument \"{oparg[opnum]}\" is not an integer or memory location.")