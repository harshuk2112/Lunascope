import os
import sys
import ephem
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QWidget
from PyQt5.QtWidgets import QMessageBox






class HelpDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help")
        layout = QVBoxLayout()
        
        # Add your help text here
        help_text = """Welcome to the LunaScope App!

LunaScope Help Guide

Welcome to LunaScope!  
This app provides detailed insights into the phases of the moon, its illumination, rise and set timings, and position in the sky. \nHere's a quick guide on how to use the app:

1. Homepage:  
The homepage displays 6 sections, each represented by a button. You can navigate between these sections to explore different aspects of the moon.

2. Lunar Phase Tracker:  
Enter a date and click "Calculate Moon Phase" to view the moon phase for that day along with an image and a fun fact.

3. Lunar Illumination:  
Enter a date and click "Check Illumination" to find out the moon's illumination percentage for the selected date.

4. Lunar Radiance Duration:  
In this section, you can calculate the duration for which the moon’s radiance is visible based on the current phase. Enter a date to find out.

5. Moonrise and Moonset:  
Enter a date and click "Check Moonrise and Moonset Timing" to get the rise and set times of the moon for that day.

6. Position of the Moon:  
Enter a date and time to find the moon’s altitude, azimuth, and direction at that specific moment.

7. Lunar Eclipse:  
Track and explore upcoming lunar eclipses. This section provides dates and details of the next lunar eclipses.

Astroscope:  
Clicking the LunaScope logo at any time takes you to the Astroscope section, where you can explore celestial bodies beyond the moon.

Enjoy exploring the moon with LunaScope and uncover the wonders of the night sky!
"""

        
        label = QLabel(help_text)
        layout.addWidget(label)
        self.setLayout(layout)



class Ui_MainWindow_lunar_eclipse(object):
    def setupUi(self, MainWindow_lunar_eclipse):
        MainWindow_lunar_eclipse.setObjectName("MainWindow_lunar_eclipse")
        MainWindow_lunar_eclipse.resize(1440, 778)
        MainWindow_lunar_eclipse.setStyleSheet("background-color: rgb(0, 0, 0);")



        self.centralwidget_lunar_eclipse = QtWidgets.QWidget(MainWindow_lunar_eclipse)
        self.centralwidget_lunar_eclipse.setObjectName("centralwidget_lunar_eclipse")

        self.window = MainWindow_lunar_eclipse



        self.groupBox_eclipse_heading = QtWidgets.QGroupBox(self.centralwidget_lunar_eclipse)
        self.groupBox_eclipse_heading.setGeometry(QtCore.QRect(340, 10, 771, 101))
        self.groupBox_eclipse_heading.setStyleSheet("background-color: rgb(255, 235, 202);")
        self.groupBox_eclipse_heading.setTitle("")
        self.groupBox_eclipse_heading.setObjectName("groupBox_eclipse_heading")



        self.heading_lunar_eclipse = QtWidgets.QLabel(self.groupBox_eclipse_heading)
        self.heading_lunar_eclipse.setGeometry(QtCore.QRect(10, 10, 751, 81))
        font = QtGui.QFont()
        font.setFamily("Cochin")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.heading_lunar_eclipse.setFont(font)
        self.heading_lunar_eclipse.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.heading_lunar_eclipse.setObjectName("heading_lunar_eclipse")



        self.label_eclipse_giphy = QtWidgets.QLabel(self.centralwidget_lunar_eclipse)
        self.label_eclipse_giphy.setGeometry(QtCore.QRect(1110, 250, 351, 351))
        self.label_eclipse_giphy.setStyleSheet("border-radius: 20px;")
        self.label_eclipse_giphy.setText("")
        self.label_eclipse_giphy.setScaledContents(True)
        self.label_eclipse_giphy.setObjectName("label_eclipse_giphy")

        gif_path = os.path.join("images", "lunar_eclipse", "eclipse_gif_2.gif")
        self.movie = QtGui.QMovie(gif_path)  # Keep a reference to the movie object
        self.label_eclipse_giphy.setMovie(self.movie)
        self.movie.start()



        self.pushButton_check_eclipse = QtWidgets.QPushButton(self.centralwidget_lunar_eclipse)
        self.pushButton_check_eclipse.setGeometry(QtCore.QRect(340, 190, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_check_eclipse.setFont(font)
        self.pushButton_check_eclipse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_check_eclipse.setObjectName("pushButton_check_eclipse")
        self.pushButton_check_eclipse.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 156, 146);   /* Background color */
                color: black;                /* Text color */
                border-radius: 15px;         /* Rounded edges */
                padding: 10px;               /* Padding for aesthetics */
            }
            QPushButton:hover {
                background-color: rgb(255, 232, 241);  /* Background color when hovered */
                color: black;                /* Text color */
                border-radius: 15px;         /* Rounded edges */
                padding: 10px;
            }
            QPushButton:pressed {
                background-color: rgb(255, 102, 87);     
                color: black;                /* Text color */
                border-radius: 15px;         /* Rounded edges */
                padding: 10px;
            }
        """)
        self.pushButton_check_eclipse.clicked.connect(self.show_widgets)
        self.pushButton_check_eclipse.clicked.connect(self.show_eclipses)




        self.label_enter_year = QtWidgets.QLabel(self.centralwidget_lunar_eclipse)
        self.label_enter_year.setGeometry(QtCore.QRect(340, 130, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_enter_year.setFont(font)
        self.label_enter_year.setStyleSheet("    color: rgb(255, 255, 255);\n"
"")
        self.label_enter_year.setObjectName("label_enter_year")



        self.comboBox_eclipse_year = QtWidgets.QComboBox(self.centralwidget_lunar_eclipse)
        self.comboBox_eclipse_year.setGeometry(QtCore.QRect(920, 130, 181, 41))
        self.comboBox_eclipse_year.setObjectName("comboBox_eclipse_year")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.addItem("")

        self.comboBox_eclipse_year.setItemText(50, "")
        self.comboBox_eclipse_year.addItem("")
        self.comboBox_eclipse_year.setItemText(51, "")
        self.comboBox_eclipse_year.setStyleSheet("""
    QComboBox {
        border: 2px solid #dba7c9;  /* Light pink border */
        border-radius: 12px;         /* Curved edges */
        background-color: rgba(255, 167, 199, 102); /* Pastel pink */
        padding: 5px;
        font-size: 20px;
        font-family: 'Segoe UI'; /* Or any font you prefer */
    }

    QComboBox::drop-down {
        border-left: 1px solid #dba7c9;  /* Border for the dropdown */
        border-radius: 0px 10px 10px 0px; /* Curved only on the right side */
        width: 30px;
    }

    QComboBox::down-arrow {
        image: url(./images/moonrise_moonset/Chevron-icon-drop-down-menu-WHITE);
        width: 10px;
        height: 10px; 
    }
""")



        self.label_total_image = QtWidgets.QLabel(self.centralwidget_lunar_eclipse)
        self.label_total_image.setGeometry(QtCore.QRect(10, -10, 261, 251))
        self.label_total_image.setStyleSheet("border-radius: 20px;")
        self.label_total_image.setText("")
        self.label_total_image.setPixmap(QtGui.QPixmap("./images/lunar_eclipse/total.webp"))
        self.label_total_image.setScaledContents(True)
        self.label_total_image.setObjectName("label_total_image")
        self.label_total_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))



        self.label_penumbral_image = QtWidgets.QLabel(self.centralwidget_lunar_eclipse)
        self.label_penumbral_image.setGeometry(QtCore.QRect(-60, 230, 381, 231))
        self.label_penumbral_image.setStyleSheet("border-radius: 20px;")
        self.label_penumbral_image.setText("")
        self.label_penumbral_image.setPixmap(QtGui.QPixmap("./images/lunar_eclipse/penumbral.webp"))
        self.label_penumbral_image.setScaledContents(True)
        self.label_penumbral_image.setObjectName("label_penumbral_image")
        self.label_penumbral_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))



        self.label_partial_image = QtWidgets.QLabel(self.centralwidget_lunar_eclipse)
        self.label_partial_image.setGeometry(QtCore.QRect(0, 490, 251, 241))
        self.label_partial_image.setStyleSheet("border-radius: 20px;")
        self.label_partial_image.setText("")
        self.label_partial_image.setPixmap(QtGui.QPixmap("./images/lunar_eclipse/partial.webp"))
        self.label_partial_image.setScaledContents(True)
        self.label_partial_image.setObjectName("label_partial_image")
        self.label_partial_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))



        self.label_total_text = QtWidgets.QLabel(self.centralwidget_lunar_eclipse)
        self.label_total_text.setGeometry(QtCore.QRect(10, 200, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_total_text.setFont(font)
        self.label_total_text.setStyleSheet("    color: rgb(255, 255, 255);\n"
"")
        self.label_total_text.setObjectName("label_total_text")
        self.label_total_text.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))



        self.label_penumbral_text = QtWidgets.QLabel(self.centralwidget_lunar_eclipse)
        self.label_penumbral_text.setGeometry(QtCore.QRect(20, 460, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_penumbral_text.setFont(font)
        self.label_penumbral_text.setStyleSheet("    color: rgb(255, 255, 255);\n"
"")
        self.label_penumbral_text.setObjectName("label_penumbral_text")
        self.label_penumbral_text.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))



        self.label_partial_text = QtWidgets.QLabel(self.centralwidget_lunar_eclipse)
        self.label_partial_text.setGeometry(QtCore.QRect(20, 720, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_partial_text.setFont(font)
        self.label_partial_text.setStyleSheet("    color: rgb(255, 255, 255);\n"
"")
        self.label_partial_text.setObjectName("label_partial_text")
        self.label_partial_text.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))



        self.textEdit_eclipse = QtWidgets.QTextEdit(self.centralwidget_lunar_eclipse)
        self.textEdit_eclipse.setGeometry(QtCore.QRect(340, 250, 771, 511))
        self.textEdit_eclipse.setStyleSheet("color: rgb(255, 255, 255);\n" \
)
        self.textEdit_eclipse.setObjectName("textEdit_eclipse")
        font = QtGui.QFont()
        font.setPointSize(25)
        # font.setUnderline(True)
        self.textEdit_eclipse.setFont(font)
        self.textEdit_eclipse.setReadOnly(True)  # 🔒 make it non-editable
        self.textEdit_eclipse.setFocusPolicy(Qt.NoFocus)
        # self.textEdit_eclipse.setVisible(False)




        self.label_lunascope_copywright = QtWidgets.QLabel(self.centralwidget_lunar_eclipse)
        self.label_lunascope_copywright.setGeometry(QtCore.QRect(570, 770, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_lunascope_copywright.setFont(font)
        self.label_lunascope_copywright.setStyleSheet("    color: rgb(255, 255, 255);\n"
"")
        self.label_lunascope_copywright.setObjectName("label_lunascope_copywright")




        self.pushButton_help = QtWidgets.QPushButton(self.centralwidget_lunar_eclipse)
        self.pushButton_help.setGeometry(QtCore.QRect(1270, 40, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_help.setFont(font)
        self.pushButton_help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_help.setStyleSheet("background-color: rgb(255, 156, 146);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_help.setObjectName("pushButton_help")
        self.pushButton_help.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 142, 0);   /* Background color */
                color: black;                /* Text color */
                border-radius: 15px;         /* Rounded edges */
                padding: 10px;               /* Padding for aesthetics */
            }
            QPushButton:hover {
                background-color: rgb(255, 186, 22);  /* Background color when hovered */
                color: black;                /* Text color */
                border-radius: 15px;         /* Rounded edges */
                padding: 10px;
            }
            QPushButton:pressed {
                background-color: rgb(255, 102, 87);     
                color: black;                /* Text color */
                border-radius: 15px;         /* Rounded edges */
                padding: 10px;
            }
                                                
        """
        )

       
        self.setup_label_clicks()





        self.pushButton_help.clicked.connect(self.show_help)
        self.label_eclipse_giphy.setVisible(False)
        self.label_total_image.setVisible(False)
        self.label_total_text.setVisible(False)
        self.label_partial_image.setVisible(False)
        self.label_partial_text.setVisible(False)
        self.label_penumbral_image.setVisible(False)
        self.label_penumbral_text.setVisible(False)





        self.groupBox_eclipse_heading.raise_()
        # self.label_eclipse_giphy.raise_()
        self.label_enter_year.raise_()
        self.comboBox_eclipse_year.raise_()
        self.label_total_image.raise_()
        self.label_penumbral_image.raise_()
        self.label_partial_image.raise_()
        self.label_total_text.raise_()
        self.label_penumbral_text.raise_()
        self.label_partial_text.raise_()
        self.textEdit_eclipse.raise_()
        self.pushButton_check_eclipse.raise_()
        self.label_lunascope_copywright.raise_()
        self.pushButton_help.raise_()
        MainWindow_lunar_eclipse.setCentralWidget(self.centralwidget_lunar_eclipse)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_lunar_eclipse)
        self.statusbar.setObjectName("statusbar")
        MainWindow_lunar_eclipse.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_lunar_eclipse)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_lunar_eclipse)
        


    def setup_label_clicks(self):
        self.label_total_image.mousePressEvent = self.show_total_info
        self.label_total_text.mousePressEvent = self.show_total_info
        self.label_partial_image.mousePressEvent = self.show_partial_info
        self.label_partial_text.mousePressEvent = self.show_partial_info
        self.label_penumbral_image.mousePressEvent = self.show_penumbral_info
        self.label_penumbral_text.mousePressEvent = self.show_penumbral_info

    def show_total_info(self, event):
        QMessageBox.information(self.window, "Total Lunar Eclipse",
        "🌕 A Total Lunar Eclipse occurs when the Earth comes between the Sun and the Moon, "
        "and the Earth’s shadow completely covers the Moon. The moon often turns a reddish color. "
        "\n\nAlso called a 'Blood Moon'. 🔴")

    def show_partial_info(self, event):
         QMessageBox.information(self.window, "Partial Lunar Eclipse",
        "🌗 A Partial Lunar Eclipse happens when only a part of the Moon enters Earth's shadow. "
        "This causes a portion of the Moon to appear darker. It looks like a bite has been taken out of it! 🍪")

    def show_penumbral_info(self, event):
         QMessageBox.information(self.window, "Penumbral Lunar Eclipse",
        "🌑 A Penumbral Lunar Eclipse is subtle and occurs when the Moon passes through Earth's penumbral shadow. "
        "The moon slightly dims but it’s often hard to notice with the naked eye. 👀")


    def show_help(self):
        help_dialog = HelpDialog()
        help_dialog.exec_()

    def retranslateUi(self, MainWindow_lunar_eclipse):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_lunar_eclipse.setWindowTitle(_translate("MainWindow_lunar_eclipse", "MainWindow"))
        self.heading_lunar_eclipse.setText(_translate("MainWindow_lunar_eclipse", " LUNAR ECLIPSE EXPLORER"))
        self.pushButton_check_eclipse.setText(_translate("MainWindow_lunar_eclipse", "Check for Lunar Eclipse"))
        self.label_enter_year.setText(_translate("MainWindow_lunar_eclipse", " Please enter the year you would like to check for lunar eclipses:"))
        self.comboBox_eclipse_year.setItemText(0, _translate("MainWindow_lunar_eclipse", "2000"))
        self.comboBox_eclipse_year.setItemText(1, _translate("MainWindow_lunar_eclipse", "2001"))
        self.comboBox_eclipse_year.setItemText(2, _translate("MainWindow_lunar_eclipse", "2002"))
        self.comboBox_eclipse_year.setItemText(3, _translate("MainWindow_lunar_eclipse", "2003"))
        self.comboBox_eclipse_year.setItemText(4, _translate("MainWindow_lunar_eclipse", "2004"))
        self.comboBox_eclipse_year.setItemText(5, _translate("MainWindow_lunar_eclipse", "2005"))
        self.comboBox_eclipse_year.setItemText(6, _translate("MainWindow_lunar_eclipse", "2006"))
        self.comboBox_eclipse_year.setItemText(7, _translate("MainWindow_lunar_eclipse", "2007"))
        self.comboBox_eclipse_year.setItemText(8, _translate("MainWindow_lunar_eclipse", "2008"))
        self.comboBox_eclipse_year.setItemText(9, _translate("MainWindow_lunar_eclipse", "2009"))
        self.comboBox_eclipse_year.setItemText(10, _translate("MainWindow_lunar_eclipse", "2010"))
        self.comboBox_eclipse_year.setItemText(11, _translate("MainWindow_lunar_eclipse", "2011"))
        self.comboBox_eclipse_year.setItemText(12, _translate("MainWindow_lunar_eclipse", "2012"))
        self.comboBox_eclipse_year.setItemText(13, _translate("MainWindow_lunar_eclipse", "2013"))
        self.comboBox_eclipse_year.setItemText(14, _translate("MainWindow_lunar_eclipse", "2014"))
        self.comboBox_eclipse_year.setItemText(15, _translate("MainWindow_lunar_eclipse", "2015"))
        self.comboBox_eclipse_year.setItemText(16, _translate("MainWindow_lunar_eclipse", "2016"))
        self.comboBox_eclipse_year.setItemText(17, _translate("MainWindow_lunar_eclipse", "2017"))
        self.comboBox_eclipse_year.setItemText(18, _translate("MainWindow_lunar_eclipse", "2018"))
        self.comboBox_eclipse_year.setItemText(19, _translate("MainWindow_lunar_eclipse", "2019"))
        self.comboBox_eclipse_year.setItemText(20, _translate("MainWindow_lunar_eclipse", "2020"))
        self.comboBox_eclipse_year.setItemText(21, _translate("MainWindow_lunar_eclipse", "2021"))
        self.comboBox_eclipse_year.setItemText(22, _translate("MainWindow_lunar_eclipse", "2022"))
        self.comboBox_eclipse_year.setItemText(23, _translate("MainWindow_lunar_eclipse", "2023"))
        self.comboBox_eclipse_year.setItemText(24, _translate("MainWindow_lunar_eclipse", "2024"))
        self.comboBox_eclipse_year.setItemText(25, _translate("MainWindow_lunar_eclipse", "2025"))
        self.comboBox_eclipse_year.setItemText(26, _translate("MainWindow_lunar_eclipse", "2026"))
        self.comboBox_eclipse_year.setItemText(27, _translate("MainWindow_lunar_eclipse", "2027"))
        self.comboBox_eclipse_year.setItemText(28, _translate("MainWindow_lunar_eclipse", "2028"))
        self.comboBox_eclipse_year.setItemText(29, _translate("MainWindow_lunar_eclipse", "2030"))
        self.comboBox_eclipse_year.setItemText(30, _translate("MainWindow_lunar_eclipse", "2031"))
        self.comboBox_eclipse_year.setItemText(31, _translate("MainWindow_lunar_eclipse", "2032"))
        self.comboBox_eclipse_year.setItemText(32, _translate("MainWindow_lunar_eclipse", "2033"))
        self.comboBox_eclipse_year.setItemText(33, _translate("MainWindow_lunar_eclipse", "2034"))
        self.comboBox_eclipse_year.setItemText(34, _translate("MainWindow_lunar_eclipse", "2035"))
        self.comboBox_eclipse_year.setItemText(35, _translate("MainWindow_lunar_eclipse", "2036"))
        self.comboBox_eclipse_year.setItemText(36, _translate("MainWindow_lunar_eclipse", "2037"))
        self.comboBox_eclipse_year.setItemText(37, _translate("MainWindow_lunar_eclipse", "2038"))
        self.comboBox_eclipse_year.setItemText(38, _translate("MainWindow_lunar_eclipse", "2039"))
        self.comboBox_eclipse_year.setItemText(39, _translate("MainWindow_lunar_eclipse", "2040"))
        self.comboBox_eclipse_year.setItemText(40, _translate("MainWindow_lunar_eclipse", "2041"))
        self.comboBox_eclipse_year.setItemText(41, _translate("MainWindow_lunar_eclipse", "2042"))
        self.comboBox_eclipse_year.setItemText(42, _translate("MainWindow_lunar_eclipse", "2043"))
        self.comboBox_eclipse_year.setItemText(43, _translate("MainWindow_lunar_eclipse", "2044"))
        self.comboBox_eclipse_year.setItemText(44, _translate("MainWindow_lunar_eclipse", "2045"))
        self.comboBox_eclipse_year.setItemText(45, _translate("MainWindow_lunar_eclipse", "2046"))
        self.comboBox_eclipse_year.setItemText(46, _translate("MainWindow_lunar_eclipse", "2047"))
        self.comboBox_eclipse_year.setItemText(47, _translate("MainWindow_lunar_eclipse", "2048"))
        self.comboBox_eclipse_year.setItemText(48, _translate("MainWindow_lunar_eclipse", "2049"))
        self.comboBox_eclipse_year.setItemText(49, _translate("MainWindow_lunar_eclipse", "2050"))
        self.label_total_text.setText(_translate("MainWindow_lunar_eclipse", "Total Lunar Eclipse"))
        self.label_penumbral_text.setText(_translate("MainWindow_lunar_eclipse", "Penumbral Lunar Eclipse"))
        self.label_partial_text.setText(_translate("MainWindow_lunar_eclipse", "Partial Lunar Eclipse"))
        self.label_lunascope_copywright.setText(_translate("MainWindow_lunar_eclipse", "© Lunascope 2024. All Rights Reserved."))
        self.pushButton_help.setText(_translate("MainWindow_lunar_eclipse", "HELP"))


    def show_widgets(self):
        if getattr(self, "widgets_shown", False):  # agar pehle hi dikha diye gaye hain
                return  # kuch mat kar, simply return

        self.widgets_shown = True
        widgets = [
            self.label_eclipse_giphy,
            self.label_total_image,
            self.label_total_text,
        #     self.textEdit_eclipse,
            self.label_partial_image,
            self.label_partial_text,
            self.label_penumbral_image,
            self.label_penumbral_text
            


        ]

        for widget in widgets:
            widget.setVisible(True)

            opacity_effect = QGraphicsOpacityEffect()
            widget.setGraphicsEffect(opacity_effect)
            opacity_effect.setOpacity(0)

            animation = QPropertyAnimation(opacity_effect, b"opacity")
            animation.setDuration(1000)
            animation.setStartValue(0)
            animation.setEndValue(1)
            animation.setEasingCurve(QEasingCurve.InOutQuad)
            animation.start()

            widget.animation = animation



    def show_eclipses(self):
        selected_year = self.comboBox_eclipse_year.currentText().strip()
        display_text = f"🌑 Showing lunar eclipses for the year {selected_year}:\n\n"
        count = 0

        try:
                with open("lunar_eclipse.txt", "r", encoding="utf-8") as file:
                     for line in file:
                         parts = [part.strip() for part in line.strip().split("|")]
                         if len(parts) == 6 and parts[0] == selected_year:
                              count += 1
                              display_text += (
                                  f"🌘 Eclipse {count}:\n"
                                  f"📅 Date: {parts[1]}\n"
                                  f"⏰ Time: {parts[2]}\n"
                                  f"⏳ Duration: {parts[3]}\n"
                                  f"🌔 Type: {parts[4]}\n"
                                  f"🌍 Visible in: {parts[5]}\n\n"
                              )

                if count == 0:  
                     display_text += "🚫 No eclipse data available for this year."

        except FileNotFoundError:
             display_text = "❗ Error: lunar_eclipse.txt file not found."

        self.textEdit_eclipse.setPlainText(display_text)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_lunar_eclipse = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_lunar_eclipse()
    ui.setupUi(MainWindow_lunar_eclipse)
    MainWindow_lunar_eclipse.show()
    sys.exit(app.exec_())
