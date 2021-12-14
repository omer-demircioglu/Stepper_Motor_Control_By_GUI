from PyQt5.QtWidgets import*
from PyQt5.QtCore import pyqtSlot
from gui import Ui_MainWindow

class controller(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @pyqtSlot(int)
    def on_horizontalSlider_valueChanged(self, current_index):

        self.ui.label.setText("değer = " + str(current_index))


uygulama = QApplication([])
pencere = dersler_7()
pencere.show()
uygulama.exec_()