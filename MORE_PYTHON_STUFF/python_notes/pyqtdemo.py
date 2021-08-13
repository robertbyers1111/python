#   +------------------------+
#---| SKELETON FOR PyQt APPS |---
#   +------------------------+

"""PyQtDemo is a simple demo using Python and PyQt5."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

__version__ = '0.1'
__author__ = 'Robert Byers'

# Create a subclass of QMainWindow to setup the app's GUI

class PyQtDemo(QMainWindow):
    """PyQtDemo's view (GUI)"""
    def __init__(self):
        """View initializer"""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('PyQtDemo')
        self.setFixedSize(235, 235)
        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

# Client code
def main():
    # Create a PyQt application instance
    pyqtdemoApp = QApplication(sys.argv)
    # Show the app's GUI
    view = PyQtDemo()
    view.show()
    # Execute the app's main loop
    sys.exit(pyqtdemoApp.exec())

if __name__ == '__main__':
    main()

