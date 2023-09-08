from MARIE.AssemblerError import AssemblerSyntaxError as ASE
from MARIE.utils import *
import string
from pprint import pprint
class assembler():
    
    def __init__(self):
        self.nsys=['HEX','DEC']#numbering systems ,not sure of the name xD
    def is_hex(self,num):
        '''checks if given string represents valid hex'''
        if num[0:2]=='0x':
            num=num[2:]
        return all(c in string.hexdigits for c in num)
    def is_dec(self,num):
        '''checks if given string represents valid dec'''
        if num[0]=='+' or num[0]=='-':
            return num[1:].isdigit()
        else:
            return num.isdigit()
    def assemble(self,mar_str):
        '''assembles mar_str to machine code ,returns hex'''
        lines=mar_str.split('\n')
        #build labels table in first iteration ,and do some cleaning <eg. delete comments,remove extra whitespaces>
        lines_cnt=len(lines)
        labels={}
        MEMORY_OFFSET=0
        for idx in range(lines_cnt):
            line=lines[idx]
            line=line.split('/')[0]#remove comments
            line=line.replace('\r','').replace('\t',' ').strip()#remove whitespaces
            lines[idx]=line
            if not line:
                continue
            
            args=line.split(' ')
            args=[i for i in args if i]
            if args[0][-1]==',':#read label
                
                if len(args)<2:
                    raise ASE("Not valid operands/directive",idx+1)
                #this is a label
                directive=args[1]
                if directive in self.nsys:
                    num=args[2]
                    if (directive =='HEX' and not self.is_hex(num)) or (directive =='DEC' and not self.is_dec(num)):
                        raise ASE('Failed to parse operand',idx+1)
                    if directive=='DEC':
                        num=hex(int(num))
                    labels[args[0][0:-1]]=hex(MEMORY_OFFSET)[2:]#must be hex
                    #remove label and just leave the directive + hex at this line, so label definition doesn't make collision in second iteration
                    lines[idx]="HEX "+num
                else:
                    #raise ASE("Not valid directive numbering system",idx+1)
                    labels[args[0][0:-1]]=hex(MEMORY_OFFSET)[2:]#must be hex
                    lines[idx]=' '.join(args[1:])
            MEMORY_OFFSET+=1
        #build instructions object_code
        marie_obj=object_code()#marie machine code object
        print('Assembling:\nLabels Table:')
        pprint(labels)
        pprint(lines)
        
        for idx in range(lines_cnt):
            line=lines[idx]
            if not line:
                continue
            print(idx+1,': '+line)
            args=(line).split(' ')
            args[0]=args[0].upper()
            try:
                op=args[0]#operation
                if op in self.nsys:
                    if len(args)!=2:
                        
                        raise ASE("Not valid operands",idx+1)
                    else:
                        marie_obj.add_full_instruction(args[1],idx+1)
                    continue
                opcode=op_to_hex_table[op]
                if op in operations_require_operand:
                    #requires operand, check if given
                    if len(args)!=2:
                        
                        raise ASE("Not valid operands",idx+1)
                    #check if operand is a label
                    operand=args[1]
                    #print(operand,labels)
                    if operand in labels:
                        operand=labels[operand]
                    elif not self.is_hex(operand):
                        raise ASE('Failed to parse operand',idx+1)
                    marie_obj.add_instruction(opcode,operand,idx+1) 
                else:
                    #just add it
                    #marie_obj.add_instruction(opcode+'0'*3,l_l=idx+1)
                    marie_obj.add_full_instruction(opcode+'0'*3,idx+1)
            except KeyError:
                
                raise ASE('Unknown mnemonics',idx+1)
        print('Assembling completed!')
        return marie_obj
class object_code():
    '''represents machine code'''
    def __init__(self):
        self._instructions=[]
        self._OP_CNT=0
    def add_instruction(self,opcode,operand='000',l_l=-1):
        '''adds instruction in hex format , opcode=>1 byte ,operand =>3 bytes if required'''
        instruction='0x'+self.pad_data(opcode,1,l_l)+self.pad_data(operand,3,l_l)
        self._instructions.append(instruction)
        self.increment_OP_CNT()
    def add_full_instruction(self,instruction,l_l=-1):
        if instruction.upper()[0:2]=='0X':
            instruction=instruction[2:]
        instruction='0x'+self.pad_data(instruction,4,l_l)
        self._instructions.append(instruction)
        self.increment_OP_CNT()
    def pad_data(self,data,pdigits,l_l=-1):
        '''pads hexa data to 'pdigits' digits by adding zeros as needed'''
        if data[0:2]=='0x' or data[0:2]=='0X' :
            data=data[2:]
        ldigits=len(data)
        if ldigits>pdigits:
            raise ASE('Failed to pad data',l_l)
        elif ldigits<pdigits:
            extra=pdigits-ldigits
            data=extra*'0'+data
        return data
    def get_OP_CNT(self):
        return self._OP_CNT
    def increment_OP_CNT(self):
        self._OP_CNT+=1
    def get_instructions(self):
        return self._instructions
    def get_instructions_cnt(self):
        return len(self._instructions)
    def to_binarystring(self):
        irs=self.get_instructions()
        return '\n'.join([self.pad_data(bin(int(i,16))[2:],16) for i in irs])
    def to_hexstring(self):
        irs=self.get_instructions()
        return '\n'.join(irs)
