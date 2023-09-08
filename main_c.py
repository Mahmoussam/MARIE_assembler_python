from MARIE.assembler import assembler
from MARIE.Simulator import Simulator
from MainEditorWindowUI import *
from PyQt5.QtWidgets import QMessageBox
import threading
class MainEditorWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.engine=assembler()
        self.mobj=None
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.init_ui_signals()
    def init_ui_signals(self):
        self.ui.assembleBtn.clicked.connect(self._assemble_clicked)
        self.ui.simulateBtn.clicked.connect(self._simulate_clicked)
        self.ui.codeEditor.textChanged.connect(self._code_changed)
    def _assemble_clicked(self):
        print('Assemble button clicked!')
        self.ui.hex_PText.clear()
        self.ui.mc_PText.clear()
        mar=self.ui.codeEditor.toPlainText()#marie assembly code
        print('zz')
        try:
            self.mobj=self.engine.assemble(mar)
            
            self.ui.hex_PText.appendPlainText(self.mobj.to_hexstring())
            self.ui.mc_PText.appendPlainText(self.mobj.to_binarystring())
        except Exception as ex:
            self.alert(str(ex))
        
    def _simulate_clicked(self):
        print('simulation button clicked!')
        if self.mobj is not None:
            th = threading.Thread(target=self._sim_ins, args=(self.mobj.get_instructions(),))
            th.start()
    def _code_changed(self):
        self.mobj=None
    def _sim_ins(self,instructions):
        print('Thread echo')
        sim=Simulator()
        sim.write_to_memory(instructions)
        print('done simulation')
    def alert(self,msg_txt,title='Error'):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(msg_txt)
        msg.setWindowTitle(title)
        msg.exec_()

if __name__=='__main__':
    app = QtWidgets.QApplication([])
    MainWindow = MainEditorWindow()
    
    MainWindow.show()
    
    app.exec_()
    
