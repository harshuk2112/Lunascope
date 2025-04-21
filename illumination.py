
import os
import ephem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel

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

class Ui_MainWindow_lunar_illumination(object):
    def setupUi(self, MainWindow_lunar_illumination):
        MainWindow_lunar_illumination.setObjectName("MainWindow_lunar_illumination")
        MainWindow_lunar_illumination.resize(1440, 790)
        MainWindow_lunar_illumination.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(MainWindow_lunar_illumination)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_help_main = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_help_main.setGeometry(QtCore.QRect(1270, 40, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(30)
        self.pushButton_help_main.setFont(font)
        self.pushButton_help_main.setObjectName("pushButton_help_main")
        self.pushButton_help_main.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_help_main.setStyleSheet("""
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
        self.pushButton_help_main.clicked.connect(self.show_help)

        self.groupBox_heading_lunar_illumination = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_heading_lunar_illumination.setGeometry(QtCore.QRect(400, 10, 641, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.groupBox_heading_lunar_illumination.setFont(font)
        self.groupBox_heading_lunar_illumination.setStyleSheet("background-color: rgb(255, 235, 202);")
        self.groupBox_heading_lunar_illumination.setTitle("")
        self.groupBox_heading_lunar_illumination.setObjectName("groupBox_heading_lunar_illumination")


        self.heading_lunar_illumination = QtWidgets.QLabel(self.groupBox_heading_lunar_illumination)
        self.heading_lunar_illumination.setGeometry(QtCore.QRect(10, 10, 621, 81))
        font = QtGui.QFont()
        font.setFamily("Cochin")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.heading_lunar_illumination.setFont(font)
        self.heading_lunar_illumination.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.heading_lunar_illumination.setObjectName("heading_lunar_illumination")



        self.label_image_moon_rotation = QtWidgets.QLabel(self.centralwidget)
        self.label_image_moon_rotation.setGeometry(QtCore.QRect(560, 130, 291, 271))
        self.label_image_moon_rotation.setText("")
        self.label_image_moon_rotation.setPixmap(QtGui.QPixmap("./images/illumination/rotation.gif"))
        self.label_image_moon_rotation.setScaledContents(True)
        self.label_image_moon_rotation.setObjectName("label_image_moon_rotation")
        gif_path = os.path.join("images", "illumination", "rotation.gif")
        self.movie = QtGui.QMovie(gif_path)  # Keep a reference to the movie object
        self.label_image_moon_rotation.setMovie(self.movie)
        self.movie.start()


        self.pushButton_check_illumination = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_check_illumination.setGeometry(QtCore.QRect(70, 550, 1271, 51))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_check_illumination.setFont(font)
        self.pushButton_check_illumination.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_check_illumination.setObjectName("pushButton_check_illumination")
        self.pushButton_check_illumination.clicked.connect(self.calculate_illumination)
        self.pushButton_check_illumination.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 156, 146);
                color: black;
                border-radius: 15px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgb(255, 232, 241);
            }
            QPushButton:pressed {
                background-color: rgb(255, 102, 87);
            }
        """)

        self.label_enter_date = QtWidgets.QLabel(self.centralwidget)
        self.label_enter_date.setGeometry(QtCore.QRect(80, 440, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(30)
        self.label_enter_date.setFont(font)
        self.label_enter_date.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_enter_date.setObjectName("label_enter_date")

        self.label_output_illumination = QtWidgets.QLabel(self.centralwidget)
        self.label_output_illumination.setGeometry(QtCore.QRect(80, 630, 1261, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_output_illumination.setFont(font)
        self.label_output_illumination.setObjectName("label_output_illumination")

        self.dateEdit_illumination = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_illumination.setCalendarPopup(True)
        self.dateEdit_illumination.setDisplayFormat("dd/MM/yyyy")
        self.dateEdit_illumination.setDate(QtCore.QDate.currentDate())  # <--- THIS LINE SETS TODAY'S DATE
        self.dateEdit_illumination.setFocusPolicy(QtCore.Qt.NoFocus)

        font = QtGui.QFont()
        font.setPointSize(40)
        self.dateEdit_illumination.setFont(font)

        self.dateEdit_illumination.setMinimumSize(QtCore.QSize(1260, 40))
        self.dateEdit_illumination.setMaximumSize(QtCore.QSize(200, 40))

        self.dateEdit_illumination.resize(200, 40)
        self.dateEdit_illumination.move(75, 490)

        self.dateEdit_illumination.setStyleSheet("""
    QDateEdit {
        font-size: 16px;
        padding-left: 10px;
        color: white;
        background-color: rgba(229, 197, 255, 120);
        border: 1px solid white;
        border-radius: 5px;
    }

    QDateEdit::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: right;
        width: 25px;
        border: none;
        # background: transparent;
    }
    
    QCalendarWidget {
        width: 3000px;  # Set the width as per your desired size
        font-size: 16px;
        background-color: rgba(229, 197, 255, 120);
    }

    QDateEdit::down-arrow {
        image: url(:/qt-project.org/styles/commonstyle/images/arrow-down-1.png);
        width: 12px;
        height: 12px;
    }
""")
        calendar = self.dateEdit_illumination.calendarWidget()
        calendar.setFixedWidth(self.dateEdit_illumination.width())

        self.label_all_rights_reserved = QtWidgets.QLabel(self.centralwidget)
        self.label_all_rights_reserved.setGeometry(QtCore.QRect(500, 770, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_all_rights_reserved.setFont(font)
        self.label_all_rights_reserved.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_all_rights_reserved.setObjectName("label_all_rights_reserved")

        MainWindow_lunar_illumination.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_lunar_illumination)
        self.statusbar.setObjectName("statusbar")
        MainWindow_lunar_illumination.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_lunar_illumination)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_lunar_illumination)

    def retranslateUi(self, MainWindow_lunar_illumination):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_lunar_illumination.setWindowTitle(_translate("MainWindow_lunar_illumination", "MainWindow"))
        self.heading_lunar_illumination.setText(_translate("MainWindow_lunar_illumination", " LUNAR ILLUMINATION"))
        self.pushButton_check_illumination.setText(_translate("MainWindow_lunar_illumination", "Check Illumination"))
        self.label_enter_date.setText(_translate("MainWindow_lunar_illumination", "Enter the date:"))
        self.label_output_illumination.setText(_translate("MainWindow_lunar_illumination", ""))
        self.pushButton_help_main.setText(_translate("MainWindow_homepage", "HELP"))
        self.label_all_rights_reserved.setText(_translate("MainWindow_lunar_illumination", " © Lunascope 2024. All Rights Reserved."))

    def calculate_illumination(self):
        # Get the selected date
        selected_date = self.dateEdit_illumination.date().toPyDate()

        # Set up the moon object
        moon = ephem.Moon()
        
        # Set the date for the moon
        moon.compute(selected_date)

        # Calculate the percentage of illumination
        illumination = moon.phase  # Phase is given in degrees (0-100)
        
        # Display the result
        self.label_output_illumination.setText(f"Moon Illumination: {illumination:.2f}%")
        return illumination

    def show_help(self):
        help_dialog = HelpDialog()
        help_dialog.exec_()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_lunar_illumination = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_lunar_illumination()
    ui.setupUi(MainWindow_lunar_illumination)
    MainWindow_lunar_illumination.setWindowTitle("Lunar Illumination ")
    MainWindow_lunar_illumination.show()
    sys.exit(app.exec_())
