
class AssemblerSyntaxError(Exception):
    def __init__(self,msg,line_num):
        self._msg=msg
        self._line_num=line_num
        super().__init__(f"SyntaxError:{self._msg}\n at line:{str(self._line_num)}")
class MemoryLimitException(Exception):
    def __init__(self,msg):
        self._msg=msg
        super().__init__(f"MemoryLimitException:{self._msg}")
