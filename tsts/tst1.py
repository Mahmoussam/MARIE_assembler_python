from MARIE.assembler import *
from MARIE.Simulator import *

mar="""
LOAD X
Output
Halt
X, DEC 13
"""
engine=assembler()
#mobj=engine.assemble(mar)
#z=mobj.get_instructions()
with open('code2.mar','r') as file:
    mar=file.read()
    mobj=engine.assemble(mar)
    IRs=mobj.get_instructions()
    
    #sim=Simulator()
    #sim.write_to_memory(IRs)
    #sim.quit()
