import sys
import ephem  # To calculate moon phases
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os
from PyQt5.QtCore import QDate
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel


def get_phase_on_day(year: int, month: int, day: int) -> float:
    """Returns a floating-point number from 0-1, where 0=new, 0.5=full, and 1=new."""
    # Create a date object for the given year, month, and day
    date = ephem.Date(datetime.date(year, month, day))
    
    # Calculate the next and previous new moons
    next_new_moon = ephem.next_new_moon(date)
    previous_new_moon = ephem.previous_new_moon(date)
    
    # Calculate lunation
    lunation = (date - previous_new_moon) / (next_new_moon - previous_new_moon)
    
    return lunation

def get_moon_phase_name(lunation: float) -> str:
    """Maps lunation value to the corresponding moon phase name."""
    if lunation < 0.03 or lunation >= 0.97:
        return "New Moon"
    elif lunation < 0.25:
        return "Waxing Crescent"
    elif lunation < 0.27:
        return "First Quarter"
    elif lunation < 0.5:
        return "Waxing Gibbous"
    elif lunation < 0.53:
        return "Full Moon"
    elif lunation < 0.75:
        return "Waning Gibbous"
    elif lunation < 0.77:
        return "Last Quarter"
    else:
        return "Waning Crescent"



class HelpDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help")
        layout = QVBoxLayout()
        
        # Add your help text here
        help_text = """Welcome to the Lunascopes App!
        
        LunaScope Help Guide

        Welcome to LunaScope!
        This app provides detailed insights into the phases of the moon, 
        its illumination, rise and set timings, and position in the sky. 
        Here’s a quick guide on how to use the app:

        1. Homepage:

        The homepage has 8 radio buttons representing different moon phases. 
        Selecting any button will display information about that phase on the right-hand side.
        You can also explore the visuals of each moon phase by clicking the 
        "Explore the Visuals" button.

        2. Lunar Phase Tracker:

        Enter a date and click on "Calculate Moon Phase" to see the moon phase 
        for that date along with an image and a fun fact.
        You can try different dates to explore different phases.

        3. Lunar Illumination:

        Enter a date and click on "Check Illumination" to get the 
        moon's illumination percentage for the selected date.

        4. Moonrise and Moonset:

        Enter a date and click "Check Moonrise and Moonset Timing" to find out 
        the moonrise and moonset times for that day.

        5. Position of the Moon:

        Enter a date and time to find out the moon's altitude, azimuth, and 
        direction at that specific moment.

        This app allows you to track and learn about the moon in a simple, intuitive way. Enjoy exploring LunaScope!
        """
        
        label = QLabel(help_text)
        layout.addWidget(label)
        self.setLayout(layout)


class Ui_MainWindow_lunar_phase_tracker(object):

    def setupUi(self, MainWindow_lunar_phase_tracker):
        MainWindow_lunar_phase_tracker.setObjectName("MainWindow_lunar_phase_tracker")
        MainWindow_lunar_phase_tracker.resize(1440, 785)
        font = QtGui.QFont()
        font.setFamily("Bodoni 72")
        font.setBold(True)
        font.setWeight(75)
        MainWindow_lunar_phase_tracker.setFont(font)
        MainWindow_lunar_phase_tracker.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(MainWindow_lunar_phase_tracker)
        self.centralwidget.setObjectName("centralwidget")

        self.label_heading_lunar_phase_tracker = QtWidgets.QLabel(self.centralwidget)
        self.label_heading_lunar_phase_tracker.setGeometry(QtCore.QRect(20, 30, 731, 81))
        font = QtGui.QFont()
        font.setFamily("Cochin")
        font.setPointSize(50)
        font.setBold(True)
        self.label_heading_lunar_phase_tracker.setFont(font)
        self.label_heading_lunar_phase_tracker.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_heading_lunar_phase_tracker.setObjectName("label_heading_lunar_phase_tracker")

        self.groupBox_heading_lunar_phase_tracker = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_heading_lunar_phase_tracker.setGeometry(QtCore.QRect(10, 20, 751, 101))
        self.groupBox_heading_lunar_phase_tracker.setStyleSheet("background-color: rgb(255, 235, 202);")
        self.groupBox_heading_lunar_phase_tracker.setTitle("")
        self.groupBox_heading_lunar_phase_tracker.setObjectName("groupBox_heading_lunar_phase_tracker")

        self.pushButton_help_main = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_help_main.setGeometry(QtCore.QRect(1290, 30, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(30)
        self.pushButton_help_main.setFont(font)
        self.pushButton_help_main.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 142, 0);
                color: black;
                border-radius: 15px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgb(255, 186, 22);
            }
            QPushButton:pressed {
                background-color: rgb(255, 102, 87);
            }
        """)
        self.pushButton_help_main.clicked.connect(self.show_help)


        self.label_all_rights_reserved = QtWidgets.QLabel(self.centralwidget)
        self.label_all_rights_reserved.setGeometry(QtCore.QRect(560, 790, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_all_rights_reserved.setFont(font)
        self.label_all_rights_reserved.setStyleSheet("color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0));")
        self.label_all_rights_reserved.setObjectName("label_all_rights_reserved")
        self.label_all_rights_reserved.setCursor(QtCore.Qt.PointingHandCursor)


        self.pushButton_help_main.setObjectName("pushButton_help_main")
        self.pushButton_help_main.setCursor(QtCore.Qt.PointingHandCursor)

        self.label_image_eight_moon = QtWidgets.QLabel(self.centralwidget)
        self.label_image_eight_moon.setGeometry(QtCore.QRect(10, 130, 761, 281))
        self.label_image_eight_moon.setText("")
        self.label_image_eight_moon.setPixmap(QtGui.QPixmap("./images/lunar_phase_tracker/moon-phases.webp"))
        self.label_image_eight_moon.setScaledContents(True)
        self.label_image_eight_moon.setObjectName("label_image_eight_moon")
        self.label_image_eight_moon.setCursor(QtCore.Qt.PointingHandCursor)

        self.label_lunar_select_date = QtWidgets.QLabel(self.centralwidget)
        self.label_lunar_select_date.setGeometry(QtCore.QRect(20, 400, 751, 61))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(35)
        self.label_lunar_select_date.setFont(font)
        self.label_lunar_select_date.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_lunar_select_date.setObjectName("label_lunar_select_date")
        self.label_lunar_select_date.setCursor(QtCore.Qt.PointingHandCursor)

        self.dateEdit_lunar = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_lunar.setGeometry(QtCore.QRect(20, 455, 760, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dateEdit_lunar.setFont(font)
        self.dateEdit_lunar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_lunar.setStyleSheet("background-color: rgba(229, 197, 255, 120);\n"
                                          "color: rgb(255, 255, 255);")
        self.dateEdit_lunar.setObjectName("dateEdit_lunar")
        # self.dateEdit_lunar.setCalendarPopup(True)
        self.dateEdit_lunar.setDate(QDate.currentDate())
        self.dateEdit_lunar.setDisplayFormat("dd/MM/yyyy")
        self.dateEdit_lunar.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        # QCalendarWidget - always visible
        self.calendar_lunar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar_lunar.setGeometry(QtCore.QRect(20, 500, 750, 180))  # Just below the DateEdit
        font = QtGui.QFont()
        font.setPointSize(15)
        self.calendar_lunar.setFont(font)
        self.calendar_lunar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calendar_lunar.setStyleSheet("background-color: rgba(229, 197, 255, 120);\n"
                                  "color: rgb(255, 255, 255);")
        self.calendar_lunar.setObjectName("calendar_lunar")

# Connect calendar's selected date to update the DateEdit
        self.calendar_lunar.selectionChanged.connect(self.update_dateedit_from_calendar)

        self.pushButton_calc_moon_phase = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calc_moon_phase.setGeometry(QtCore.QRect(20, 700, 761, 51))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(25)
        font.setBold(True)
        self.pushButton_calc_moon_phase.setFont(font)
        self.pushButton_calc_moon_phase.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_calc_moon_phase.setStyleSheet("""
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
        self.pushButton_calc_moon_phase.setObjectName("pushButton_calc_moon_phase")

        self.label_name_of_phase = QtWidgets.QLabel(self.centralwidget)
        self.label_name_of_phase.setGeometry(QtCore.QRect(850, 140, 551, 61))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(35)
        font.setUnderline(True)
        self.label_name_of_phase.setFont(font)
        self.label_name_of_phase.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_name_of_phase.setObjectName("label_name_of_phase")

        self.label_fun_fact = QtWidgets.QLabel(self.centralwidget)
        self.label_fun_fact.setGeometry(QtCore.QRect(850, 630, 551, 171))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(22)
        self.label_fun_fact.setFont(font)
        self.label_fun_fact.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_fun_fact.setWordWrap(True)
        self.label_fun_fact.setObjectName("label_fun_fact")

        self.label_phase_loaded_image = QtWidgets.QLabel(self.centralwidget)
        self.label_phase_loaded_image.setGeometry(QtCore.QRect(850, 220, 441, 441))
        self.label_phase_loaded_image.setScaledContents(True)
        self.label_phase_loaded_image.setObjectName("label_phase_loaded_image")

        MainWindow_lunar_phase_tracker.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_lunar_phase_tracker)
        self.statusbar.setObjectName("statusbar")
        MainWindow_lunar_phase_tracker.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_lunar_phase_tracker)
        self.pushButton_calc_moon_phase.clicked.connect(self.calculate_moon_phase)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_lunar_phase_tracker)
        self.label_heading_lunar_phase_tracker.raise_()

    def retranslateUi(self, MainWindow_lunar_phase_tracker):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_lunar_phase_tracker.setWindowTitle(_translate("MainWindow_lunar_phase_tracker", "Lunar Phase Tracker"))
        self.label_heading_lunar_phase_tracker.setText(_translate("MainWindow_lunar_phase_tracker", "   LUNAR PHASE TRACKER"))
        self.pushButton_help_main.setText(_translate("MainWindow_lunar_phase_tracker", "HELP"))
        self.label_lunar_select_date.setText(_translate("MainWindow_lunar_phase_tracker", "Select a date to view the lunar phase for that day:"))
        self.pushButton_calc_moon_phase.setText(_translate("MainWindow_lunar_phase_tracker", "Calculate Moon Phase"))
        self.label_name_of_phase.setText(_translate("MainWindow_lunar_phase_tracker", ""))
        self.label_fun_fact.setText(_translate("MainWindow_lunar_phase_tracker", ""))
        self.label_all_rights_reserved.setText(_translate("MainWindow_moonrise_moonset", " © Lunascope 2024. All Rights Reserved."))
        self.label_phase_loaded_image.setText(_translate("MainWindow_lunar_phase_tracker", ""))


    def update_dateedit_from_calendar(self):
        selected_date = self.calendar_lunar.selectedDate()
        self.dateEdit_lunar.setDate(selected_date)


    def calculate_moon_phase(self):
        try:
            selected_date = self.dateEdit_lunar.date()
            year = selected_date.year()
            month = selected_date.month()
            day = selected_date.day()
            lunation = get_phase_on_day(year, month, day)
            phase_name = get_moon_phase_name(lunation)


            self.label_name_of_phase.setText(f"Moon Phase: {phase_name}")
            self.update_moon_image(phase_name)
            self.update_moon_fact(phase_name)
            return phase_name
        except ValueError:
            QMessageBox.critical(None, "Error", "Invalid date format. Please enter a date in YYYY-MM-DD format.")
            return None
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An error occurred: {e}")
            return None
      

    def update_moon_image(self, phase_name):
        image_directory = os.path.expanduser('./images/lunar_phase_tracker/phases_of_moon')
        image_file = os.path.join(image_directory, f'{phase_name.lower().replace(" ", "_")}.png')

        # Check if the image file exists
        if os.path.exists(image_file):
            # Update the image on the label
            self.label_phase_loaded_image.setPixmap(QtGui.QPixmap(image_file))
        else:
            print(f"Image not found: {image_file}")



    def update_moon_fact(self, phase_name):
        # A dictionary to store fun facts for each moon phase
        moon_facts = {
            "New Moon": "Fun Fact : <br> The New Moon is not visible to the naked eye, as the sun and moon are aligned.",
            "Waxing Crescent": "Fun Fact : <br> This phase signifies the growth of the moon, as more of its surface becomes visible.",
            "First Quarter": "Fun Fact : <br> The First Quarter Moon is commonly known as a Half Moon.",
            "Waxing Gibbous": "Fun Fact : <br> This phase occurs when the moon is more than half full, but not completely illuminated.",
            "Full Moon": "Fun Fact : <br> The Full Moon is fully illuminated and marks the middle of the lunar cycle.",
            "Waning Gibbous": "Fun Fact : <br> The Waning Gibbous is the phase after the Full Moon, as the moon begins to wane.",
            "Last Quarter": "Fun Fact : <br> This phase is also called a Half Moon, as the moon is half illuminated.",
            "Waning Crescent": "Fun Fact : <br> This is the last phase before the New Moon, with just a sliver of the moon visible."
        }

        # Update the fun fact based on the moon phase
        self.label_fun_fact.setText(moon_facts.get(phase_name, ""))

    def show_help(self):
        help_dialog = HelpDialog()
        help_dialog.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_lunar_phase_tracker = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_lunar_phase_tracker()
    ui.setupUi(MainWindow_lunar_phase_tracker)
    MainWindow_lunar_phase_tracker.setWindowTitle("Lunar Phase Tracker ")
    MainWindow_lunar_phase_tracker.show()
    sys.exit(app.exec_())