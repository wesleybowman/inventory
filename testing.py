import sys
from PySide.QtGui import *
from PySide.QtCore import *

class TestApp(QWidget):
    def __init__(self):
        super(TestApp, self).__init__()

        self.initUI()

    def initUI(self):


        QToolTip.setFont(QFont('SansSerif', 10))
        #self.setToolTip('This is a <b>QWidget</b> widget')
        grid = QGridLayout()

        red = self.readIn('red.txt')
        white = self.readIn('white.txt')
        specialty = self.readIn('specialty.txt')
        traditional = self.readIn('traditional.txt')

        r = QLabel('Reds')
        #grid.addWidget(QLabel('Reds'),0,0)
        grid.addWidget(r,0,0)
        grid.addWidget(QLabel('Whites'),0,1)
        grid.addWidget(QLabel('Specialty'),0,2)
        grid.addWidget(QLabel('Traditional'),0,3)

        self.createButton(grid, red, 0)
        self.createButton(grid, white, 1)
        self.createButton(grid, specialty, 2)
        self.createButton(grid, traditional, 3)

#        for i,v in enumerate(red):
#            btn = QPushButton(v, self)
#            btn.setToolTip('In inventory: ' + str(red[v]))
#            grid.addWidget(btn,i+1,0)

#
#        for i,v in enumerate(white):
#            btn = QPushButton(v, self)
#            btn.setToolTip('In inventory: ' + str(red[v]))
#            grid.addWidget(btn,i+1,1)
#
#        for i,v in enumerate(specialty):
#            btn = QPushButton(v, self)
#            btn.setToolTip('In inventory: ' + str(red[v]))
#            grid.addWidget(btn,i+1,2)
#
#        for i,v in enumerate(traditional):
#            btn = QPushButton(v, self)
#            btn.setToolTip('In inventory: ' + str(red[v]))
#            grid.addWidget(btn,i+1,3)


#        rbtn = QPushButton('&Red Wine', self)
#        rbtn.clicked.connect(self.redWineWindow)
#        rbtn.setToolTip('This is for <b>Red Wine</b>')
#        rbtn.resize(rbtn.sizeHint())
#        #rbtn.move(50, 50)
#
#        wbtn = QPushButton('&White Wine', self)
#        wbtn.setToolTip('This is for <b>White Wine</b>')
#        #wbtn.clicked.connect(self.buttonClicked)
#        wbtn.clicked.connect(self.whiteWineWindow)
#        wbtn.resize(wbtn.sizeHint())
#        #wbtn.move(150, 50)

        qbtn = QPushButton('&Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())

        #grid.setSpacing(10)

        #grid.addWidget(rbtn,5,0)
        #grid.addWidget(wbtn,5,2)
        grid.addWidget(qbtn,10,10)

        self.setLayout(grid)
        #self.statusBar()

    def readIn(self,File):
        d = {}
        with open(File) as f:
            for line in f:
                (key, val) = line.split()
                d[key] = int(val)

        return d

    def createButton(self, grid, d, pos):

        for i,v in enumerate(d):
            btn = QPushButton(v, self)
            btn.setToolTip('In inventory: ' + str(d[v]))
            btn.clicked.connect(self.on_click)
            grid.addWidget(btn,i+1,pos)

    @Slot()
    def on_click(self):
        ''' Tell when the button is clicked. '''
        print('clicked')
        sender = self.sender()

        #self.statusBar().showMessage(sender.text() + ' was pressed')


    def redWineWindow(self):
        window = QMainWindow(self)
        grid = QGridLayout()

#        for i,v in enumerate(red):
#            btn = QPushButton(v,window)
#            grid.addWidget(btn,i+1,i)


        qbtn = QPushButton('&Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        grid.addWidget(qbtn, 10, 10)


        sec = QPushButton('Pinot', window)
        grid.addWidget(sec, 2,2)

        first = QPushButton('Vitis', self)
        grid.addWidget(first, 1,0)

        window.setLayout(grid)


        window.setAttribute(Qt.WA_DeleteOnClose)
        window.setWindowTitle(self.tr('Red Wine'))
        window.show()

    def whiteWineWindow(self):
        window = QMainWindow(self)
        window.setAttribute(Qt.WA_DeleteOnClose)
        window.setWindowTitle(self.tr('White Wine'))

        window.show()

    #def buttonClicked(self,d,v):

        #sender = self.sender()

#        if sender.text() == 'Quit':
#            reply = QMessageBox.question(self, 'Message',
#            "Are you sure to quit?", QtGui.QMessageBox.Yes |
#            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
#
#            if reply == QMessageBox.Yes:
#                QCoreApplication.instance().quit
#            else:
#                pass
#

        #self.statusBar().showMessage(sender.text() + ' was pressed')



class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        #exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)


        self.apptab = QTabWidget()
        self.setCentralWidget(self.apptab)
        self.apptab.addTab(TestApp(),'Inventory')


        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.statusBar()


        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Gaspereau Vineyards')
        self.show()




def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
