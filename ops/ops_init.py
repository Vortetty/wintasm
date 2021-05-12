from ops import op_set
from ops import op_xor
#from ops import op_jmpif

def init(ops: dict):
    op_set.init(ops)
    op_xor.init(ops)
    #op_jmpif.init(ops)