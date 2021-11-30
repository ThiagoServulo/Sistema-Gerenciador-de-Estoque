from PySide2 import QtWidgets
import sys
from Events import Eventos


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Eventos()
    window.iniciar()
    sys.exit(app.exec_())

