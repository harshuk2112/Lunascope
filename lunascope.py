# Importing standard Python modules
import os         # For interacting with the operating system (e.g., file paths)
import sys        # For accessing system-specific parameters and functions
import subprocess # For running external processes (used to open other scripts or files)

# Importing PyQt5 modules for GUI development
from PyQt5.QtCore import pyqtSignal, Qt          # Core functionalities and constants
from PyQt5 import QtCore, QtGui, QtWidgets       # Base Qt modules for GUI creation
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel

# Importing astronomical calculation library
import ephem      # For performing astronomical calculations (e.g., moon phases, positions)

# Importing custom UI modules for different sections of the LunaScope application
from lunar_phase_tracker import Ui_MainWindow_lunar_phase_tracker
from phase_image_homepage import Ui_MainWindow_photo
from lunar_position import Ui_MainWindow_lunar_position
from lunar_radiance import Ui_MainWindow_lunar_light
from moonrise_moonset import Ui_MainWindow_moonrise_moonset
from illumination import Ui_MainWindow_lunar_illumination
from lunar_eclipse import Ui_MainWindow_lunar_eclipse
from astroscope_window import Ui_MainWindow_astroscope

# Suppress error messages in the console (not recommended for debugging)
sys.stderr = open(os.devnull, 'w')


# Custom QLabel that emits a signal when clicked
# Useful for making images or labels interactive in the GUI
class ClickableLabel(QLabel):
    clicked = pyqtSignal()  # Custom signal emitted on mouse click

    def mousePressEvent(self, event):
        self.clicked.emit()  # Emit the signal when label is clicked


# HelpDialog class creates a simple dialog window to display help/instructions
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
        
        label = QLabel(help_text)  # Create a label with help/instructional text
        layout.addWidget(label)    # Add the label to the dialog's layout
        self.setLayout(layout)     # Set the layout for the dialog window


# Class that defines the layout and widgets for the homepage/main window
class Ui_MainWindow_homepage(object):
    def setupUi(self, MainWindow_homepage):
        # Set window properties
        MainWindow_homepage.setObjectName("MainWindow_homepage")
        MainWindow_homepage.resize(1438, 776)
        MainWindow_homepage.setStyleSheet("background-color: rgb(0, 0, 0);")

        # Create and set central widget (container for other widgets)
        self.centralwidget = QtWidgets.QWidget(MainWindow_homepage)
        self.centralwidget.setObjectName("centralwidget")

        # Add a 'Help' push button to the main window
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
        self.pushButton_help_main.clicked.connect(self.show_help) #Connect with function show_help to display help_text

        # Lunascope Label: All Rights Reserved
        self.label_all_rights_reserved = QtWidgets.QLabel(self.centralwidget)
        self.label_all_rights_reserved.setGeometry(QtCore.QRect(560, 770, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_all_rights_reserved.setFont(font)
        self.label_all_rights_reserved.setStyleSheet("color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0));")
        self.label_all_rights_reserved.setObjectName("label_all_rights_reserved")
        self.label_all_rights_reserved.setCursor(QtCore.Qt.PointingHandCursor)


        self.label_textbox_info = QtWidgets.QLabel(self.centralwidget)
        self.label_textbox_info.setGeometry(QtCore.QRect(970, 310, 451, 101))  # Adjust the geometry as needed
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        self.label_textbox_info.setFont(font)
        self.label_textbox_info.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_textbox_info.setText("Dive into the enchanting world of lunar phases!<br>Simply select a radio button to learn more.")
        self.label_textbox_info.setObjectName("label_textbox_info")
        self.label_textbox_info.setStyleSheet("color: rgb(250, 255, 169);")
        self.label_textbox_info.setWordWrap(True)

 
        self.label_open_image = QtWidgets.QLabel(self.centralwidget)
        self.label_open_image.setGeometry(QtCore.QRect(1090, 400, 451, 71))  # Adjust the geometry as needed
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        font.setUnderline(True)
        self.label_open_image.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_open_image.setFont(font)
        self.label_open_image.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_open_image.setText("Explore the visuals")
        self.label_open_image.setObjectName("label_textbox_info")
        self.label_open_image.setStyleSheet("color: rgb(250, 255, 169);")
        self.label_open_image.setWordWrap(True)
        self.label_open_image.mousePressEvent = self.open_moon_phase_image


        self.label_logo_lunascope = ClickableLabel(self.centralwidget)
        self.label_logo_lunascope.setGeometry(QtCore.QRect(460, 0, 561, 201))
        self.label_logo_lunascope.setObjectName("label_logo_lunascope")

# Set image
        pixmap = QtGui.QPixmap("./images/homepage/logo.png")
        if not pixmap.isNull():
            self.label_logo_lunascope.setPixmap(pixmap)
        else:
            print("Image not found or path is incorrect!")

        self.label_logo_lunascope.setScaledContents(True)
        self.label_logo_lunascope.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_logo_lunascope.setToolTip("Click to open AstroScope")
        self.label_logo_lunascope.clicked.connect(self.open_astroscope)


        self.label_animated_moon = QtWidgets.QLabel(self.centralwidget)
        self.label_animated_moon.setGeometry(QtCore.QRect(450, 220, 511, 311))
        self.label_animated_moon.setScaledContents(True)
        self.label_animated_moon.setObjectName("label_animated_moon")
        # Set up the GIF for the animated moon
        gif_path = os.path.join("images", "homepage", "phases_of_moon.gif")
        self.movie = QtGui.QMovie(gif_path)  # Keep a reference to the movie object
        self.label_animated_moon.setMovie(self.movie)
        self.movie.start()


        self.pushButton_lunar_phase_tracker = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_lunar_phase_tracker.setGeometry(QtCore.QRect(150, 560, 331, 71))
        self.pushButton_lunar_phase_tracker.setCursor(QtCore.Qt.PointingHandCursor)
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        font.setBold(True)
        self.pushButton_lunar_phase_tracker.setFont(font)
        # self.pushButton_lunar_phase_tracker.setStyleSheet("background-color: rgb(255, 156, 146);")
        self.pushButton_lunar_phase_tracker.setStyleSheet("""
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
        self.pushButton_lunar_phase_tracker.setObjectName("pushButton_lunar_phase_tracker")
        self.pushButton_lunar_phase_tracker.clicked.connect(self.open_lunar_phase_tracker)


        self.pushButton_moon_illumination = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_moon_illumination.setGeometry(QtCore.QRect(550, 560, 331, 71))
        self.pushButton_moon_illumination.setCursor(QtCore.Qt.PointingHandCursor)
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        font.setBold(True)
        self.pushButton_moon_illumination.setFont(font)
        # self.pushButton_moon_illumination.setStyleSheet("background-color: rgb(255, 156, 146);")
        self.pushButton_moon_illumination.setStyleSheet("""
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
        self.pushButton_moon_illumination.setObjectName("pushButton_moon_illumination")
        self.pushButton_moon_illumination.clicked.connect(self.open_lunar_illumination)


        self.pushButton_moonrise_and_moonset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_moonrise_and_moonset.setGeometry(QtCore.QRect(150, 660, 331, 71))
        self.pushButton_moonrise_and_moonset.setCursor(QtCore.Qt.PointingHandCursor)
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        font.setBold(True)
        self.pushButton_moonrise_and_moonset.setFont(font)
        self.pushButton_moonrise_and_moonset.setStyleSheet("background-color: rgb(255, 156, 146);")
        self.pushButton_moonrise_and_moonset.setStyleSheet("""
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
        self.pushButton_moonrise_and_moonset.setObjectName("pushButton_moonrise_and_moonset")
        self.pushButton_moonrise_and_moonset.clicked.connect(self.open_moonrise_moonset)


        self.pushButton_position_of_moon = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_position_of_moon.setGeometry(QtCore.QRect(550, 660, 331, 71))
        self.pushButton_position_of_moon.setCursor(QtCore.Qt.PointingHandCursor)
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        font.setBold(True)
        self.pushButton_position_of_moon.setFont(font)
        self.pushButton_position_of_moon.setStyleSheet("background-color: rgb(255, 156, 146);")
        self.pushButton_position_of_moon.setObjectName("pushButton_position_of_moon")

        self.pushButton_position_of_moon.clicked.connect(self.open_lunar_position)

        self.pushButton_position_of_moon.setStyleSheet("""
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


        self.pushButton_lunar_light = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_lunar_light.setGeometry(QtCore.QRect(950, 560, 331, 71))
        self.pushButton_lunar_light.setCursor(QtCore.Qt.PointingHandCursor)
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        font.setBold(True)
        self.pushButton_lunar_light.setFont(font)
        # self.pushButton_lunar_phase_tracker.setStyleSheet("background-color: rgb(255, 156, 146);")
        self.pushButton_lunar_light.setStyleSheet("""
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
        self.pushButton_lunar_light.setObjectName("pushButton_lunar_light")
        self.pushButton_lunar_light.clicked.connect(self.open_lunar_light)


        self.pushButton_lunar_eclipse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_lunar_eclipse.setGeometry(QtCore.QRect(950, 660, 331, 71))
        self.pushButton_lunar_eclipse.setCursor(QtCore.Qt.PointingHandCursor)
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        font.setBold(True)
        self.pushButton_lunar_eclipse.setFont(font)
        # self.pushButton_lunar_phase_tracker.setStyleSheet("background-color: rgb(255, 156, 146);")
        self.pushButton_lunar_eclipse.setStyleSheet("""
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
        self.pushButton_lunar_eclipse.setObjectName("pushButton_lunar_eclipse")
        self.pushButton_lunar_eclipse.clicked.connect(self.open_lunar_eclipse)


        self.label_eight_phases = QtWidgets.QLabel(self.centralwidget)
        self.label_eight_phases.setGeometry(QtCore.QRect(70, 220, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Big Caslon")
        font.setPointSize(26)
        self.label_eight_phases.setFont(font)
        self.label_eight_phases.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_eight_phases.setObjectName("label_eight_phases")


        self.radioButton_new_moon = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_new_moon.setGeometry(QtCore.QRect(70, 290, 141, 41))
        self.radioButton_new_moon.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton_new_moon.setStyleSheet("background-color: rgba(229, 197, 255, 120);\n"
"color: rgb(255, 255, 255);")
        self.radioButton_new_moon.setObjectName("radioButton_new_moon")

        self.radioButton_waxing_crescent = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_waxing_crescent.setGeometry(QtCore.QRect(290, 290, 141, 41))
        self.radioButton_waxing_crescent.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton_waxing_crescent.setStyleSheet("background-color: rgba(229, 197, 255, 120);\n"
"color: rgb(255, 255, 255);")
        self.radioButton_waxing_crescent.setObjectName("radioButton_waxing_crescent")

        self.radioButton_waxing_gibbous = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_waxing_gibbous.setGeometry(QtCore.QRect(290, 350, 141, 41))
        self.radioButton_waxing_gibbous.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton_waxing_gibbous.setStyleSheet("background-color: rgba(229, 197, 255, 120);\n"
"color: rgb(255, 255, 255);")
        self.radioButton_waxing_gibbous.setObjectName("radioButton_waxing_gibbous")

        self.radioButton_first_quarter = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_first_quarter.setGeometry(QtCore.QRect(70, 350, 141, 41))
        self.radioButton_first_quarter.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton_first_quarter.setStyleSheet("background-color: rgba(229, 197, 255, 120);\n"
"color: rgb(255, 255, 255);")
        self.radioButton_first_quarter.setObjectName("radioButton_first_quarter")

        self.radioButton_waning_gibbous = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_waning_gibbous.setGeometry(QtCore.QRect(290, 410, 141, 41))
        self.radioButton_waning_gibbous.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton_waning_gibbous.setStyleSheet("background-color: rgba(229, 197, 255, 120);\n"
"color: rgb(255, 255, 255);")
        self.radioButton_waning_gibbous.setObjectName("radioButton_waning_gibbous")

        self.radioButton_full_moon = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_full_moon.setGeometry(QtCore.QRect(70, 410, 141, 41))
        self.radioButton_full_moon.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton_full_moon.setStyleSheet("background-color: rgba(229, 197, 255, 120);\n"
"color: rgb(255, 255, 255);")
        self.radioButton_full_moon.setObjectName("radioButton_full_moon")

        self.radioButton_last_quarter = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_last_quarter.setGeometry(QtCore.QRect(70, 470, 141, 41))
        self.radioButton_last_quarter.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton_last_quarter.setStyleSheet("background-color: rgba(229, 197, 255, 120);\n"
"color: rgb(255, 255, 255);")
        self.radioButton_last_quarter.setObjectName("radioButton_last_quarter")

        self.radioButton_waning_crescent = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_waning_crescent.setGeometry(QtCore.QRect(290, 470, 141, 41))
        self.radioButton_waning_crescent.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton_waning_crescent.setStyleSheet("background-color: rgba(229, 197, 255, 120);\n"
"color: rgb(255, 255, 255);")
        self.radioButton_waning_crescent.setObjectName("radioButton_waning_crescent")

        self.radioButton_new_moon.clicked.connect(self.update_info)     
        self.radioButton_waxing_crescent.clicked.connect(self.update_info)
        self.radioButton_first_quarter.clicked.connect(self.update_info)
        self.radioButton_waxing_gibbous.clicked.connect(self.update_info)
        self.radioButton_full_moon.clicked.connect(self.update_info)
        self.radioButton_waning_gibbous.clicked.connect(self.update_info)
        self.radioButton_last_quarter.clicked.connect(self.update_info)
        self.radioButton_waning_crescent.clicked.connect(self.update_info)


        MainWindow_homepage.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_homepage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_homepage)


    def update_info(self):
        phase_info = {
            "New Moon": "A New Moon occurs when the moon is between the Earth and the Sun.",
            "Waxing Crescent": "A Waxing Crescent Moon is when the moon is less than half illuminated.",
            "First Quarter": "The First Quarter Moon occurs when half of the moon is illuminated.",
            "Waxing Gibbous": "A Waxing Gibbous Moon is when more than half of the moon is illuminated.",
            "Full Moon": "A Full Moon occurs when the entire moon is illuminated.",
            "Waning Gibbous": "A Waning Gibbous Moon is when the moon is still illuminated but decreasing.",
            "Last Quarter": "The Last Quarter Moon occurs when half of the moon is illuminated on the left side.",
            "Waning Crescent": "A Waning Crescent Moon is when the moon is less than half illuminated and decreasing.",
        }

        title = ""
        if self.radioButton_new_moon.isChecked():
            title = "New Moon"
        elif self.radioButton_waxing_crescent.isChecked():
            title = "Waxing Crescent"
        elif self.radioButton_first_quarter.isChecked():
            title = "First Quarter"
        elif self.radioButton_waxing_gibbous.isChecked():
            title = "Waxing Gibbous"
        elif self.radioButton_full_moon.isChecked():
            title = "Full Moon"
        elif self.radioButton_waning_gibbous.isChecked():
            title = "Waning Gibbous"
        elif self.radioButton_last_quarter.isChecked():
            title = "Last Quarter"
        elif self.radioButton_waning_crescent.isChecked():
            title = "Waning Crescent"
    
    # Update the label text if a radio button is selected
        if title:
            self.label_textbox_info.setText(f"{title}: {phase_info[title]}")
    def open_lunar_phase_tracker(self):
        self.MainWindow_lunar_phase_tracker = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_lunar_phase_tracker()
        self.ui.setupUi(self.MainWindow_lunar_phase_tracker)
        self.MainWindow_lunar_phase_tracker.setWindowTitle("Lunar Phase Tracker ")
        self.MainWindow_lunar_phase_tracker.show()

    def open_moon_phase_image(self, event):
        self.MainWindow_photo = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_photo()
        self.ui.setupUi(self.MainWindow_photo)
        self.MainWindow_photo.setWindowTitle("Phases of Moon")
        self.MainWindow_photo.show()


    def open_lunar_position(self):
        self.MainWindow_lunar_position = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_lunar_position()
        self.ui.setupUi(self.MainWindow_lunar_position)
        self.MainWindow_lunar_position.setWindowTitle("Lunar Position ")
        self.MainWindow_lunar_position.show()


    def open_moonrise_moonset(self):
        self.MainWindow_moonrise_moonset = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_moonrise_moonset()
        self.ui.setupUi(self.MainWindow_moonrise_moonset)
        self.MainWindow_moonrise_moonset.setWindowTitle("Moonrise and Moonset ")
        self.MainWindow_moonrise_moonset.show()

    def open_lunar_illumination(self):
        self.MainWindow_lunar_illumination = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_lunar_illumination()
        self.ui.setupUi(self.MainWindow_lunar_illumination)
        self.MainWindow_lunar_illumination.setWindowTitle("Lunar Illumination ")
        self.MainWindow_lunar_illumination.show()


    def open_lunar_light(self):
        self.MainWindow_lunar_light = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_lunar_light()
        self.ui.setupUi(self.MainWindow_lunar_light)
        self.MainWindow_lunar_light.setWindowTitle("Lunar Radiance Duration ")
        self.MainWindow_lunar_light.show()


    def open_lunar_eclipse(self):
        self.MainWindow_lunar_eclipse = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_lunar_eclipse()
        self.ui.setupUi(self.MainWindow_lunar_eclipse)
        self.MainWindow_lunar_eclipse.show()

    def open_astroscope(self):
        print("Astroscope logo clicked!")
        self.MainWindow_astroscope = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_astroscope()
        self.ui.setupUi(self.MainWindow_astroscope)
        self.MainWindow_astroscope.setWindowTitle("Astroscope")
        self.MainWindow_astroscope.show()

    def show_help(self):
        help_dialog = HelpDialog()
        help_dialog.exec_()

    def retranslateUi(self, MainWindow_homepage):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_homepage.setWindowTitle(_translate("MainWindow_homepage", "MainWindow"))
        self.pushButton_help_main.setText(_translate("MainWindow_homepage", "HELP"))
        self.pushButton_lunar_phase_tracker.setText(_translate("MainWindow_homepage", "Lunar Phase Tracker"))
        self.pushButton_lunar_light.setText(_translate("MainWindow_homepage", "Lunar Radiance Duration"))
        self.pushButton_lunar_eclipse.setText(_translate("MainWindow_homepage", "Lunar Eclipse Explorer"))
        self.pushButton_moon_illumination.setText(_translate("MainWindow_homepage", "Lunar Illumination"))
        self.pushButton_moonrise_and_moonset.setText(_translate("MainWindow_homepage", "Moonrise and Moonset"))
        self.pushButton_position_of_moon.setText(_translate("MainWindow_homepage", "Position of the Moon"))
        self.label_all_rights_reserved.setText(_translate("MainWindow_moonrise_moonset", " © Lunascope 2024. All Rights Reserved."))
        self.label_eight_phases.setText(_translate("MainWindow_homepage", "Eight Phases of the Moon :"))
        self.radioButton_new_moon.setText(_translate("MainWindow_homepage", "New Moon"))
        self.radioButton_waxing_crescent.setText(_translate("MainWindow_homepage", "Waxing Crescent"))
        self.radioButton_waxing_gibbous.setText(_translate("MainWindow_homepage", "Waxing Gibbous"))
        self.radioButton_first_quarter.setText(_translate("MainWindow_homepage", "First Quarter"))
        self.radioButton_waning_gibbous.setText(_translate("MainWindow_homepage", "Waning Gibbous"))
        self.radioButton_full_moon.setText(_translate("MainWindow_homepage", "Full Moon"))
        self.radioButton_last_quarter.setText(_translate("MainWindow_homepage", "Last Quarter"))
        self.radioButton_waning_crescent.setText(_translate("MainWindow_homepage", "Waning Crescent"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_homepage = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_homepage()
    ui.setupUi(MainWindow_homepage)
    MainWindow_homepage.setWindowTitle("LunaScope")
    MainWindow_homepage.show()
    sys.exit(app.exec_())