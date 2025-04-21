from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ephem
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel
import pytz
from datetime import datetime, time, timedelta



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



class Ui_MainWindow_moonrise_moonset(object):
    def setupUi(self, MainWindow_moonrise_moonset):
        MainWindow_moonrise_moonset.setObjectName("MainWindow_moonrise_moonset")
        MainWindow_moonrise_moonset.resize(1440, 785)
        MainWindow_moonrise_moonset.setStyleSheet("background-color: rgb(0, 0, 0);")


        self.centralwidget = QtWidgets.QWidget(MainWindow_moonrise_moonset)
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


        self.heading_lunar_position = QtWidgets.QLabel(self.centralwidget)
        self.heading_lunar_position.setGeometry(QtCore.QRect(350, 20, 731, 81))
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


        self.groupBox_heading_lunar_phase_tracker = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_heading_lunar_phase_tracker.setGeometry(QtCore.QRect(340, 10, 751, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.groupBox_heading_lunar_phase_tracker.setFont(font)
        self.groupBox_heading_lunar_phase_tracker.setStyleSheet("background-color: rgb(255, 235, 202);")
        self.groupBox_heading_lunar_phase_tracker.setTitle("")
        self.groupBox_heading_lunar_phase_tracker.setObjectName("groupBox_heading_lunar_phase_tracker")



        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(290, 80, 841, 301))
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("./images/moonrise_moonset/moon-phases-rise-times-header.webp"))
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


        self.dateEdit_moonrise = QtWidgets.QDateEdit(self.groupBox_date_moonrise)
        self.dateEdit_moonrise.setGeometry(QtCore.QRect(190, 40, 171, 40))  # Increase size

# Set the font size
        font = QtGui.QFont()
        font.setPointSize(17)  # Increase the font size
        self.dateEdit_moonrise.setFont(font)

# Set the cursor for the date edit
        self.dateEdit_moonrise.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

# Set the background color and other styling options
        self.dateEdit_moonrise.setStyleSheet("""
            background-color: rgba(255, 167, 199, 102);
            border: 2px solid #dba7c9;
            border-radius: 12px;
            padding: 5px;
            font-size: 20px;
                                        
        """)

# Set the date format and calendar popup
        self.dateEdit_moonrise.setObjectName("dateEdit_moonrise")
        self.dateEdit_moonrise.setCalendarPopup(True)
        self.dateEdit_moonrise.setDate(QDate.currentDate())
        self.dateEdit_moonrise.setDisplayFormat("dd/MM/yyyy")

# Set size policy for resizing
        self.dateEdit_moonrise.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)




        self.label_enter_date_moonrise = QtWidgets.QLabel(self.groupBox_date_moonrise)
        self.label_enter_date_moonrise.setGeometry(QtCore.QRect(20, 40, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_enter_date_moonrise.setFont(font)
        self.label_enter_date_moonrise.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.label_enter_date_moonrise.setObjectName("label_enter_date_moonrise")


        self.label_enter_location_moonrise = QtWidgets.QLabel(self.groupBox_date_moonrise)
        self.label_enter_location_moonrise.setGeometry(QtCore.QRect(20, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_enter_location_moonrise.setFont(font)
        self.label_enter_location_moonrise.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.label_enter_location_moonrise.setObjectName("label_enter_location_moonrise")




        self.groupBox_moonrise = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_moonrise.setGeometry(QtCore.QRect(510, 460, 391, 171))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setUnderline(True)
        self.groupBox_moonrise.setFont(font)
        self.groupBox_moonrise.setStyleSheet("\n"
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
        self.groupBox_moonrise.setObjectName("groupBox_moonrise")



        self.label_moonrise_time = QtWidgets.QLabel(self.groupBox_moonrise)
        self.label_moonrise_time.setGeometry(QtCore.QRect(20, 50, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_moonrise_time.setFont(font)
        self.label_moonrise_time.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.label_moonrise_time.setText("")
        self.label_moonrise_time.setObjectName("label_moonrise_time")
        self.label_moonrise_time.setText(" Please enter the date.")




        self.groupBox_moonset_time = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_moonset_time.setGeometry(QtCore.QRect(940, 460, 391, 171))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setUnderline(True)
        self.groupBox_moonset_time.setFont(font)
        self.groupBox_moonset_time.setStyleSheet("\n"
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
        self.groupBox_moonset_time.setObjectName("groupBox_moonset_time")




        self.label_moonset_time = QtWidgets.QLabel(self.groupBox_moonset_time)
        self.label_moonset_time.setGeometry(QtCore.QRect(20, 50, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_moonset_time.setFont(font)
        self.label_moonset_time.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);")
        self.label_moonset_time.setText("")
        self.label_moonset_time.setObjectName("label_moonset_time")
        self.label_moonset_time.setText(" Please enter the date.")



        self.pushButton_calc_moonrise = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calc_moonrise.setGeometry(QtCore.QRect(80, 650, 1261, 51))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_calc_moonrise.setFont(font)
        self.pushButton_calc_moonrise.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_calc_moonrise.setStyleSheet("""
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
        self.pushButton_calc_moonrise.setObjectName("pushButton_calc_moonrise")
        self.pushButton_calc_moonrise.clicked.connect(self.calculate_moonrise_moonset)




        self.label_image.raise_()
        self.groupBox_heading_lunar_phase_tracker.raise_()
        self.heading_lunar_position.raise_()
        self.groupBox_date_moonrise.raise_()
        self.groupBox_moonrise.raise_()
        self.groupBox_moonset_time.raise_()
        self.label_all_rights_reserved.raise_()
        self.pushButton_calc_moonrise.raise_()
        
        MainWindow_moonrise_moonset.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_moonrise_moonset)
        self.statusbar.setObjectName("statusbar")
        MainWindow_moonrise_moonset.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_moonrise_moonset)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_moonrise_moonset)

    def retranslateUi(self, MainWindow_moonrise_moonset):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_moonrise_moonset.setWindowTitle(_translate("MainWindow_moonrise_moonset", "MainWindow"))
        self.heading_lunar_position.setText(_translate("MainWindow_moonrise_moonset", " MOONRISE AND MOONSET"))
        self.groupBox_date_moonrise.setTitle(_translate("MainWindow_moonrise_moonset", "Date  "))
        self.pushButton_help_main.setText(_translate("MainWindow_homepage", "HELP"))
        self.label_enter_date_moonrise.setText(_translate("MainWindow_moonrise_moonset", " Enter the Date:"))
        self.label_enter_location_moonrise.setText(_translate("MainWindow_moonrise_moonset", " Enter the Location:"))
        self.label_all_rights_reserved.setText(_translate("MainWindow_moonrise_moonset", " © Lunascope 2024. All Rights Reserved."))
        self.groupBox_moonrise.setTitle(_translate("MainWindow_moonrise_moonset", "MoonRise"))
        self.groupBox_moonset_time.setTitle(_translate("MainWindow_moonrise_moonset", "MoonSet"))
        self.pushButton_calc_moonrise.setText(_translate("MainWindow_moonrise_moonset", "Calculate the MoonRise and MoonSet Timings "))
        self.comboBox.raise_()
        self.comboBox.setItemText(0, _translate("MainWindow", "Delhi"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Mumbai"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Bangalore"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Kolkata"))

# import pytz
# from datetime import datetime


    def calculate_moonrise_moonset(self):
    # Get the date from the date input
        selected_date = self.dateEdit_moonrise.date().toPyDate()
    
    # Get the selected city from the comboBox
        selected_city = self.comboBox.currentText().strip()

    # Define coordinates for each city
        city_coordinates = {
            "Delhi": {'lat': '28.6139', 'lon': '77.2090', 'elev': 216},
            "Mumbai": {'lat': '19.0760', 'lon': '72.8777', 'elev': 14},
            "Bangalore": {'lat': '12.9716', 'lon': '77.5946', 'elev': 920},
            "Kolkata": {'lat': '22.5726', 'lon': '88.3639', 'elev': 9}
        }

        if selected_city not in city_coordinates:
            self.label_moonrise_time.setText("Invalid city selected")
            self.label_moonset_time.setText("")
            return None

    # Set up observer based on selected city
        observer = ephem.Observer()
        observer.lat = city_coordinates[selected_city]['lat']
        observer.lon = city_coordinates[selected_city]['lon']
        observer.elev = city_coordinates[selected_city]['elev']
        observer.date = selected_date  # Still in UTC

        moon = ephem.Moon()
        moonrise_time = observer.next_rising(moon)
        moonset_time = observer.next_setting(moon)

    # Convert to IST manually using pytz
        ist = pytz.timezone("Asia/Kolkata")

        moonrise_utc = ephem.localtime(moonrise_time)
        moonset_utc = ephem.localtime(moonset_time)

        moonrise_ist = moonrise_utc.astimezone(ist)
        moonset_ist = moonset_utc.astimezone(ist)

        self.label_moonrise_time.setText(f" Moonrise: {moonrise_ist.strftime('%I:%M %p')}")
        self.label_moonset_time.setText(f" Moonset: {moonset_ist.strftime('%I:%M %p')}")
        return {
        'moonrise': moonrise_ist.strftime('%I:%M %p'),
        'moonset': moonset_ist.strftime('%I:%M %p')
    }



    
    def show_help(self):
        help_dialog = HelpDialog()
        help_dialog.exec_()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_moonrise_moonset = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_moonrise_moonset()
    ui.setupUi(MainWindow_moonrise_moonset)
    MainWindow_moonrise_moonset.setWindowTitle("Moonrise and Moonset ")
    MainWindow_moonrise_moonset.show()
    sys.exit(app.exec_())