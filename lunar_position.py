
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDateEdit, QTimeEdit
from PyQt5.QtCore import QDate, QTime
import ephem
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


class LearnMore(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moon's Position")
        layout = QVBoxLayout()
        
        # Add your help text here
        learn_more = """Understanding the Moon's Position

        The position of the moon is determined using two key parameters: azimuth and altitude.

        Azimuth represents the moon’s horizontal direction along the horizon, measured in degrees.

        0° refers to North,

        90° refers to East,

        180° refers to South, and

        270° refers to West.

        Altitude indicates the moon’s height above the horizon. A positive altitude means the moon is 
        above the horizon, while a negative altitude means it’s below.
        
        By using these two values, you can determine the exact position of the moon in the sky at any given moment.
        """
        
        label = QLabel(learn_more)
        layout.addWidget(label)
        self.setLayout(layout)


class Ui_MainWindow_lunar_position(object):
    def setupUi(self, MainWindow_lunar_position):
        MainWindow_lunar_position.setObjectName("MainWindow_lunar_position")
        MainWindow_lunar_position.resize(1440, 780)
        MainWindow_lunar_position.setStyleSheet("background-color: rgb(0, 0, 0);")



        self.centralwidget = QtWidgets.QWidget(MainWindow_lunar_position)
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

        self.label_all_rights_reserved = QtWidgets.QLabel(self.centralwidget)
        self.label_all_rights_reserved.setGeometry(QtCore.QRect(560, 770, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_all_rights_reserved.setFont(font)
        self.label_all_rights_reserved.setStyleSheet("color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0));")
        self.label_all_rights_reserved.setObjectName("label_all_rights_reserved")
        self.label_all_rights_reserved.setCursor(QtCore.Qt.PointingHandCursor)

        self.groupBox_lunar_position = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_lunar_position.setGeometry(QtCore.QRect(490, 10, 501, 101))
        self.groupBox_lunar_position.setStyleSheet("background-color: rgb(255, 235, 202);")
        self.groupBox_lunar_position.setTitle("")
        self.groupBox_lunar_position.setObjectName("groupBox_lunar_position")



        self.heading_lunar_position = QtWidgets.QLabel(self.groupBox_lunar_position)
        self.heading_lunar_position.setGeometry(QtCore.QRect(10, 10, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Cochin")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.heading_lunar_position.setFont(font)
        self.heading_lunar_position.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.heading_lunar_position.setObjectName("heading_lunar_position")



        self.label_image_sun_rotation = QtWidgets.QLabel(self.centralwidget)
        self.label_image_sun_rotation.setGeometry(QtCore.QRect(40, 90, 561, 311))
        self.label_image_sun_rotation.setText("")
        # self.label_image_sun_rotation.setPixmap(QtGui.QPixmap("../project_folder/phases/position/Earth-Moon-Orbit-Sun.gif"))
        self.label_image_sun_rotation.setScaledContents(True)
        self.label_image_sun_rotation.setObjectName("label_image_sun_rotation")


        gif_path = os.path.join("images", "position_of_moon", "Earth-Moon-Orbit-Sun.gif")
        self.movie = QtGui.QMovie(gif_path)  # Keep a reference to the movie object
        self.label_image_sun_rotation.setMovie(self.movie)
        self.movie.start()



        self.label_image_moon_position = QtWidgets.QLabel(self.centralwidget)
        self.label_image_moon_position.setGeometry(QtCore.QRect(900, 110, 471, 301))
        self.label_image_moon_position.setText("")
        self.label_image_moon_position.setPixmap(QtGui.QPixmap("../project_folder/phases/position/moon_satellite.webp"))
        self.label_image_moon_position.setScaledContents(True)
        self.label_image_moon_position.setObjectName("label_image_moon_position")

        gif_path = os.path.join("images", "position_of_moon", "moon_satellite.webp")
        self.movie = QtGui.QMovie(gif_path)  # Keep a reference to the movie object
        self.label_image_moon_position.setMovie(self.movie)
        self.movie.start()






        self.groupBox_date_time = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_date_time.setGeometry(QtCore.QRect(80, 440, 471, 191))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setUnderline(True)
        self.groupBox_date_time.setFont(font)
        self.groupBox_date_time.setStyleSheet("\n"
"QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"}\n"
"")
        self.groupBox_date_time.setObjectName("groupBox_date_time")







        self.dateEdit_lunar_position = QtWidgets.QDateEdit(self.groupBox_date_time)
        self.dateEdit_lunar_position.setGeometry(QtCore.QRect(230, 50, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dateEdit_lunar_position.setFont(font)
        self.dateEdit_lunar_position.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_lunar_position.setStyleSheet("background-color: rgba(255, 167, 199, 102);")
        self.dateEdit_lunar_position.setObjectName("dateEdit_lunar_position")
        self.dateEdit_lunar_position.setDisplayFormat("dd/MM/yyyy")
        # self.dateEdit_lunar_position.setCalendarPopup(True)




        self.timeEdit_lunar_position = QtWidgets.QTimeEdit(self.groupBox_date_time)
        self.timeEdit_lunar_position.setGeometry(QtCore.QRect(230, 110, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.timeEdit_lunar_position.setFont(font)
        self.timeEdit_lunar_position.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.timeEdit_lunar_position.setStyleSheet("background-color: rgba(255, 167, 199, 102);")
        self.timeEdit_lunar_position.setObjectName("timeEdit_lunar_position")


        current_date = QDate.currentDate()
        current_time = QTime.currentTime()

        self.dateEdit_lunar_position.setDate(current_date)
        self.timeEdit_lunar_position.setTime(current_time)

        self.label_enter_date = QtWidgets.QLabel(self.groupBox_date_time)
        self.label_enter_date.setGeometry(QtCore.QRect(60, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_enter_date.setFont(font)
        self.label_enter_date.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.label_enter_date.setObjectName("label_enter_date")




        self.label_enter_time = QtWidgets.QLabel(self.groupBox_date_time)
        self.label_enter_time.setGeometry(QtCore.QRect(60, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_enter_time.setFont(font)
        self.label_enter_time.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.label_enter_time.setObjectName("label_enter_time")



        self.pushButton_calc_moon_position = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calc_moon_position.setGeometry(QtCore.QRect(80, 650, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_calc_moon_position.setFont(font)
        self.pushButton_calc_moon_position.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_calc_moon_position.setStyleSheet("""
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
        self.pushButton_calc_moon_position.setObjectName("pushButton_calc_moon_position")




        self.groupBox_position_of_moon = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_position_of_moon.setGeometry(QtCore.QRect(880, 440, 471, 231))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setUnderline(True)
        self.groupBox_position_of_moon.setFont(font)
        self.groupBox_position_of_moon.setStyleSheet("\n"
"QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"}\n"
"")
        self.groupBox_position_of_moon.setObjectName("groupBox_position_of_moon")
        self.label_moon_alt = QtWidgets.QLabel(self.groupBox_position_of_moon)




        self.label_moon_alt.setGeometry(QtCore.QRect(60, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_moon_alt.setFont(font)
        self.label_moon_alt.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.label_moon_alt.setObjectName("label_moon_alt")



        self.label_moon_azi = QtWidgets.QLabel(self.groupBox_position_of_moon)
        self.label_moon_azi.setGeometry(QtCore.QRect(60, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_moon_azi.setFont(font)
        self.label_moon_azi.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.label_moon_azi.setObjectName("label_moon_azi")


        
        self.labe_direction = QtWidgets.QLabel(self.groupBox_position_of_moon)
        self.labe_direction.setGeometry(QtCore.QRect(60, 170, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labe_direction.setFont(font)
        self.labe_direction.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.labe_direction.setObjectName("labe_direction")


        self.label_output_altitude = QtWidgets.QLabel(self.groupBox_position_of_moon)
        self.label_output_altitude.setGeometry(QtCore.QRect(240, 50, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_output_altitude.setFont(font)
        self.label_output_altitude.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_output_altitude.setStyleSheet("background-color: rgba(255, 167, 199, 102);")
        self.label_output_altitude.setText("")
        self.label_output_altitude.setObjectName("label_output_altitude")



        self.label_output_azimuth = QtWidgets.QLabel(self.groupBox_position_of_moon)
        self.label_output_azimuth.setGeometry(QtCore.QRect(240, 110, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_output_azimuth.setFont(font)
        self.label_output_azimuth.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_output_azimuth.setStyleSheet("background-color: rgba(255, 167, 199, 102);")
        self.label_output_azimuth.setText("")
        self.label_output_azimuth.setObjectName("label_output_azimuth")


        self.label_output_direction = QtWidgets.QLabel(self.groupBox_position_of_moon)
        self.label_output_direction.setGeometry(QtCore.QRect(240, 170, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_output_direction.setFont(font)
        self.label_output_direction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_output_direction.setStyleSheet("background-color: rgba(255, 167, 199, 102);")
        self.label_output_direction.setText("")
        self.label_output_direction.setObjectName("label_output_direction")



        self.label_learn_more = QtWidgets.QLabel(self.centralwidget)
        self.label_learn_more.setGeometry(QtCore.QRect(1040, 680, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(24)
        font.setUnderline(True)
        self.label_learn_more.setFont(font)
        self.label_learn_more.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_learn_more.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_learn_more.setObjectName("label_learn_more")
        self.label_learn_more.mousePressEvent = self.open_learn_more



        self.label_fact_position = QtWidgets.QLabel(self.centralwidget)
        self.label_fact_position.setGeometry(QtCore.QRect(600, 150, 321, 211))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(24)
        font.setUnderline(False)
        self.label_fact_position.setFont(font)
        self.label_fact_position.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_fact_position.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 249, 167);")
        self.label_fact_position.setObjectName("label_fact_position")



        self.label_image_moon_position.raise_()
        self.label_image_sun_rotation.raise_()
        self.groupBox_lunar_position.raise_()
        self.groupBox_date_time.raise_()
        self.pushButton_calc_moon_position.raise_()
        self.groupBox_position_of_moon.raise_()
        self.label_learn_more.raise_()
        self.label_fact_position.raise_()
        MainWindow_lunar_position.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_lunar_position)
        self.statusbar.setObjectName("statusbar")
        MainWindow_lunar_position.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_lunar_position)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_lunar_position)
        self.pushButton_calc_moon_position.clicked.connect(self.calculate_moon_position)


    def show_help(self):
        help_dialog = HelpDialog()
        help_dialog.exec_()

    def open_learn_more(self, event):
        learn_more = LearnMore()
        learn_more.exec()


    def retranslateUi(self, MainWindow_lunar_position):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_lunar_position.setWindowTitle(_translate("MainWindow_lunar_position", "MainWindow"))
        self.heading_lunar_position.setText(_translate("MainWindow_lunar_position", " LUNAR POSITION"))
        self.groupBox_date_time.setTitle(_translate("MainWindow_lunar_position", "Date and Time"))
        self.label_enter_date.setText(_translate("MainWindow_lunar_position", " Enter the Date:"))
        self.label_all_rights_reserved.setText(_translate("MainWindow_moonrise_moonset", " © Lunascope 2024. All Rights Reserved."))
        self.pushButton_help_main.setText(_translate("MainWindow_homepage", "HELP"))
        self.label_enter_time.setText(_translate("MainWindow_lunar_position", " Enter the Time:"))
        self.pushButton_calc_moon_position.setText(_translate("MainWindow_lunar_position", "Calculate the Position of the Moon"))
        self.groupBox_position_of_moon.setTitle(_translate("MainWindow_lunar_position", "Position of the Moon"))
        self.label_moon_alt.setText(_translate("MainWindow_lunar_position", " Moon Altitude:"))
        self.label_moon_azi.setText(_translate("MainWindow_lunar_position", " Moon Azimuth:"))
        self.labe_direction.setText(_translate("MainWindow_lunar_position", " Moon Direction:"))
        self.label_learn_more.setText(_translate("MainWindow_lunar_position", "Learn more about the positions"))
        self.label_fact_position.setText(_translate("MainWindow_lunar_position", "'The Moon is in synchronous <br>rotation with Earth, meaning <br> it  always shows the same face <br> to us.'"))
 

    def calculate_moon_position(self):
        selected_date = self.dateEdit_lunar_position.date().toString("yyyy/MM/dd")
        selected_time = self.timeEdit_lunar_position.time().toString("HH:mm:ss")

        observer = ephem.Observer()
        observer.lat = '0'  # Set latitude (you might want to adjust this)
        observer.lon = '0'  # Set longitude (adjust this as well)
        observer.date = f'{selected_date} {selected_time}'  

        moon = ephem.Moon(observer)
        moon.compute(observer)

    # Get the altitude and azimuth of the moon
        moon_alt = math.degrees(moon.alt)  # Convert radians to degrees
        moon_az = math.degrees(moon.az)    # Convert radians to degrees

    # Update the label with altitude and azimuth in degrees
        self.label_output_altitude.setText(f'{moon_alt:.2f}°')
        self.label_output_azimuth.setText(f'{moon_az:.2f}°')

    # Convert azimuth to direction
        if moon_az == 0 or moon_az == 360:
            self.label_output_direction.setText('North')
        elif 0 < moon_az < 90:
            self.label_output_direction.setText('North-East')
        elif moon_az == 90:
            self.label_output_direction.setText('East')
        elif 90 < moon_az < 180:
            self.label_output_direction.setText('South-East')
        elif moon_az == 180:
            self.label_output_direction.setText('South')
        elif 180 < moon_az < 270:
            self.label_output_direction.setText('South-West')
        elif moon_az == 270:
            self.label_output_direction.setText('West')
        elif 270 < moon_az < 360:
            self.label_output_direction.setText('North-West')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_lunar_position = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_lunar_position()
    ui.setupUi(MainWindow_lunar_position)
    MainWindow_lunar_position.setWindowTitle("Lunar Position ")
    MainWindow_lunar_position.show()
    sys.exit(app.exec_())
