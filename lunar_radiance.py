from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ephem
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel
import pytz
import datetime
from datetime import timedelta
from skyfield.api import load, Topos
from skyfield import almanac
from skyfield.almanac import find_discrete, moon_phases
from pytz import timezone
import pytz

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



class Ui_MainWindow_lunar_light(object):
    def setupUi(self, MainWindow_lunar_light):
        MainWindow_lunar_light.setObjectName("MainWindow_lunar_light")
        MainWindow_lunar_light.resize(1440, 785)
        MainWindow_lunar_light.setStyleSheet("background-color: rgb(0, 0, 0);")


        self.centralwidget = QtWidgets.QWidget(MainWindow_lunar_light)
        self.centralwidget.setObjectName("centralwidget")


        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(270, 560, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setStyleSheet("""
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




        self.heading_lunar_light = QtWidgets.QLabel(self.centralwidget)
        self.heading_lunar_light.setGeometry(QtCore.QRect(350, 20, 800, 81))
        font = QtGui.QFont()
        font.setFamily("Cochin")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.heading_lunar_light.setFont(font)
        self.heading_lunar_light.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.heading_lunar_light.setObjectName("heading_lunar_light")




        self.groupBox_heading_lunar_light = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_heading_lunar_light.setGeometry(QtCore.QRect(340, 10, 820, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.groupBox_heading_lunar_light.setFont(font)
        self.groupBox_heading_lunar_light.setStyleSheet("background-color: rgb(255, 235, 202);")
        self.groupBox_heading_lunar_light.setTitle("")
        self.groupBox_heading_lunar_light.setObjectName("groupBox_heading_lunar_light")



        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(290, 150, 850, 400))
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("./images/lunar_light/FGicVTjLV85SWuS8sJg3fJ.jpg"))
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")



        self.groupBox_date_moonrise = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_date_moonrise.setGeometry(QtCore.QRect(80, 460, 391, 171))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setUnderline(True)
        self.groupBox_date_moonrise.setFont(font)
        self.groupBox_date_moonrise.setStyleSheet("\n"
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
        self.groupBox_date_moonrise.setObjectName("groupBox_date_moonrise")



        self.dateEdit_lunar_light = QtWidgets.QDateEdit(self.groupBox_date_moonrise)
        self.dateEdit_lunar_light.setGeometry(QtCore.QRect(190, 40, 171, 40))  # Increase size

# Set the font size
        font = QtGui.QFont()
        font.setPointSize(17)  # Increase the font size
        self.dateEdit_lunar_light.setFont(font)

# Set the cursor for the date edit
        self.dateEdit_lunar_light.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

# Set the background color and other styling options
        self.dateEdit_lunar_light.setStyleSheet("""
            background-color: rgba(255, 167, 199, 102);
            border: 2px solid #dba7c9;
            border-radius: 12px;
            padding: 5px;
            font-size: 20px;
                                        
        """)

# Set the date format and calendar popup
        self.dateEdit_lunar_light.setObjectName("dateEdit_lunar_light")
        self.dateEdit_lunar_light.setCalendarPopup(True)
        self.dateEdit_lunar_light.setDate(QDate.currentDate())
        self.dateEdit_lunar_light.setDisplayFormat("dd/MM/yyyy")

# Set size policy for resizing
        self.dateEdit_lunar_light.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)


        self.label_enter_date_lunar_light = QtWidgets.QLabel(self.groupBox_date_moonrise)
        self.label_enter_date_lunar_light.setGeometry(QtCore.QRect(20, 40, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_enter_date_lunar_light.setFont(font)
        self.label_enter_date_lunar_light.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.label_enter_date_lunar_light.setObjectName("label_enter_date_lunar_light")


        self.label_enter_location_lunar_light = QtWidgets.QLabel(self.groupBox_date_moonrise)
        self.label_enter_location_lunar_light.setGeometry(QtCore.QRect(20, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_enter_location_lunar_light.setFont(font)
        self.label_enter_location_lunar_light.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.label_enter_location_lunar_light.setObjectName("label_enter_location_lunar_light")

        self.groupBox_lunation_time = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_lunation_time.setGeometry(QtCore.QRect(510, 460, 391, 171))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setUnderline(True)
        self.groupBox_lunation_time.setFont(font)
        self.groupBox_lunation_time.setStyleSheet("\n"
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
        self.groupBox_lunation_time.setObjectName("groupBox_lunation_time")



        self.label_lunation_time = QtWidgets.QLabel(self.groupBox_lunation_time)
        self.label_lunation_time.setGeometry(QtCore.QRect(20, 50, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_lunation_time.setFont(font)
        self.label_lunation_time.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.label_lunation_time.setText("")
        self.label_lunation_time.setObjectName("label_lunation_time")
        self.label_lunation_time.setText(" Please enter the date.")




        self.groupBox_occulation_time = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_occulation_time.setGeometry(QtCore.QRect(940, 460, 391, 171))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setUnderline(True)
        self.groupBox_occulation_time.setFont(font)
        self.groupBox_occulation_time.setStyleSheet("\n"
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
        self.groupBox_occulation_time.setObjectName("groupBox_occulation_time")




        self.label_occulation_time = QtWidgets.QLabel(self.groupBox_occulation_time)
        self.label_occulation_time.setGeometry(QtCore.QRect(20, 50, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_occulation_time.setFont(font)
        self.label_occulation_time.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.label_occulation_time.setText("")
        self.label_occulation_time.setObjectName("label_occulation_time")
        self.label_occulation_time.setText(" Please enter the date.")



        self.pushButton_calc_lunar_radiance = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calc_lunar_radiance.setGeometry(QtCore.QRect(80, 650, 1261, 51))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_calc_lunar_radiance.setFont(font)
        self.pushButton_calc_lunar_radiance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_calc_lunar_radiance.setStyleSheet("""
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
        self.pushButton_calc_lunar_radiance.setObjectName("pushButton_calc_lunar_radiance")
        self.pushButton_calc_lunar_radiance.clicked.connect(self.calculate_lunar_radiance)




        self.label_image.raise_()
        self.groupBox_heading_lunar_light.raise_()
        self.heading_lunar_light.raise_()
        self.groupBox_date_moonrise.raise_()
        self.groupBox_lunation_time.raise_()
        self.groupBox_occulation_time.raise_()
        self.label_all_rights_reserved.raise_()
        self.pushButton_calc_lunar_radiance.raise_()
        
        MainWindow_lunar_light.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_lunar_light)
        self.statusbar.setObjectName("statusbar")
        MainWindow_lunar_light.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_lunar_light)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_lunar_light)

    def retranslateUi(self, MainWindow_lunar_light):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_lunar_light.setWindowTitle(_translate("MainWindow_lunar_light", "MainWindow"))
        self.heading_lunar_light.setText(_translate("MainWindow_lunar_light", " LUNAR RADIANCE DURATION"))
        self.groupBox_date_moonrise.setTitle(_translate("MainWindow_lunar_light", "GeoDate  "))
        self.pushButton_help_main.setText(_translate("MainWindow_homepage", "HELP"))
        self.label_enter_date_lunar_light.setText(_translate("MainWindow_lunar_light", " Enter the Date:"))
        self.label_enter_location_lunar_light.setText(_translate("MainWindow_lunar_light", " Enter the Location:"))
        self.label_all_rights_reserved.setText(_translate("MainWindow_lunar_light", " © Lunascope 2024. All Rights Reserved."))
        self.groupBox_lunation_time.setTitle(_translate("MainWindow_lunar_light", "Lunation"))
        self.groupBox_occulation_time.setTitle(_translate("MainWindow_lunar_light", "Occulation"))
        self.pushButton_calc_lunar_radiance.setText(_translate("MainWindow_lunar_light", "Calculate the Lunar Radiance Duration "))
        self.comboBox.raise_()
        self.comboBox.setItemText(0, _translate("MainWindow", "Delhi"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Mumbai"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Bengaluru"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Kolkata"))

        self.city_coords = {
            "Delhi": (28.6139, 77.2090),
            "Mumbai": (19.0760, 72.8777),
            "Bengaluru": (12.9716, 77.5946),
            "Kolkata": (22.5726, 88.3639)
        }

        # Load ephemeris and timescale once
        self.eph = load('de421.bsp')
        self.ts = load.timescale()

    def calculate_lunar_radiance(self):
        from_zone = timezone('UTC')
        to_zone = timezone('Asia/Kolkata')  # IST conversion

        selected_date = self.dateEdit_lunar_light.date().toPyDate()
        city = self.comboBox.currentText()

    # Coordinates
        latitude, longitude = self.city_coords[city]
        observer = Topos(latitude_degrees=latitude, longitude_degrees=longitude)

    # Use preloaded eph and ts
        eph = self.eph
        ts = self.ts

    # Time range for one day
        t0 = ts.utc(selected_date.year, selected_date.month, selected_date.day)
        t1 = ts.utc((selected_date + timedelta(days=1)).year,
                    (selected_date + timedelta(days=1)).month,
                    (selected_date + timedelta(days=1)).day)

    # Find Moonrise and Moonset times
        f = almanac.risings_and_settings(eph, eph['Moon'], observer)
        times, events = almanac.find_discrete(t0, t1, f)

    # Default values
        rise_time = "Not visible"
        set_time = "Not visible"

        for t, event in zip(times, events):
            dt_utc = t.utc_datetime()
            dt_ist = dt_utc.replace(tzinfo=from_zone).astimezone(to_zone)
            formatted_time = dt_ist.strftime('%I:%M %p')

            if event == 1 and rise_time == "Not visible":
                rise_time = formatted_time  # Moonrise
            elif event == 0 and set_time == "Not visible":
                set_time = formatted_time  # Moonset

    # Display the results
        self.label_lunation_time.setText(f"Lunation: {rise_time}")
        self.label_occulation_time.setText(f"Occultation: {set_time}")


    def show_help(self):
        help_dialog = HelpDialog()
        help_dialog.exec_()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_lunar_light = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_lunar_light()
    ui.setupUi(MainWindow_lunar_light)
    MainWindow_lunar_light.setWindowTitle("Lunar Radiance Duration ")
    MainWindow_lunar_light.show()
    sys.exit(app.exec_())