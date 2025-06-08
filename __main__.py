import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mydesign import Ui_MainWindow
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pushbutton = self.pushButton
        pushbutton.clicked.connect(lambda: self.label_2.isEnabled(True))
        pushbutton.clicked.connect(lambda: self.buttonBox.isEnabled(True))
        for i in range(1, 10):
            checkbox = getattr(self, f'checkBox_{i}')
            if checkbox.isChecked() and pushbutton.clicked:
                checkbox.isChecked(False)
                checkbox.isEnabled(False)

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())



