import sys
from PySide import QtGui
from PySide import QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        #self.setToolTip('This is a <b>QWidget</b> widget')

        rbtn = QtGui.QPushButton('Red Wine', self)
        rbtn.setToolTip('This is for <b>Red Wine</b>')
        rbtn.resize(rbtn.sizeHint())
        rbtn.move(50, 50)

        wbtn = QtGui.QPushButton('White Wine', self)
        wbtn.setToolTip('This is for <b>White Wine</b>')
        wbtn.resize(wbtn.sizeHint())
        wbtn.move(150, 50)

        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(250, 50)


        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()


#    def closeEvent(self, event):
#
#        reply = QtGui.QMessageBox.question(self, 'Message',
#            "Are you sure to quit?", QtGui.QMessageBox.Yes |
#            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
#
#        if reply == QtGui.QMessageBox.Yes:
#            event.accept()
#        else:
#            event.ignore()

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        #exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Menubar')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    #ex = Example()
    ex = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
