
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_photo(object):
    def setupUi(self, MainWindow_photo):
        MainWindow_photo.setObjectName("MainWindow_photo")
        MainWindow_photo.resize(1434, 783)
        MainWindow_photo.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_photo)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 1431, 761))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./images/homepage/Phases of Moon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow_photo.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_photo)
        self.statusbar.setObjectName("statusbar")
        MainWindow_photo.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_photo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_photo)

    def retranslateUi(self, MainWindow_photo):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_photo.setWindowTitle(_translate("MainWindow_photo", "MainWindow_photo"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_photo = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_photo()
    ui.setupUi(MainWindow_photo)
    MainWindow_photo.setWindowTitle("Phases of Moon")
    MainWindow_photo.show()
    sys.exit(app.exec_())
