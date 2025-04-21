
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from datetime import datetime
from datetime import date as dt_date
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QWidget
import ephem


zodiac_traits = {
    "Aries": {
        "traits": "As the first sign of the zodiac, Aries is a natural-born leader. They are fiercely independent, adventurous, and full of enthusiasm. Aries individuals are known for their courage and determination. While they can be impulsive at times, their energy and optimism make them pioneers who are never afraid to take risks.",
        "lucky_number": 9,
        "lucky_color": "Red",
        "element": "Fire",
        "gemstone": "Ruby💎\n\nEnergizes and inspires passion, vitality, and courage.",
        "horoscope": "Today is brimming with potential for new beginnings. Your fiery energy makes it a perfect time to take initiative. Trust your instincts and don’t hold back from expressing your ideas."
    },
    "Taurus": {
        "traits": "Taurus is grounded and dependable. These individuals value stability, loyalty, and comfort. They are patient and practical but also deeply connected to beauty, art, and nature. Taureans are hardworking and known for their perseverance, often taking a steady approach to success.",
        "lucky_number": 6,
        "lucky_color": "Green",
        "element": "Earth",
        "gemstone": "Emerald💎\n\nEncourages growth, balance, and emotional healing.",
        "horoscope": "Slow and steady wins the race today. Focus on nurturing your goals with consistency. Surround yourself with soothing environments—nature or music may help you unwind and reconnect with yourself."
    },
    "Gemini": {
        "traits": "Gemini is lively, quick-witted, and endlessly curious. These individuals are excellent communicators and love to explore new ideas. They adapt easily and have a youthful energy, though they can sometimes be seen as inconsistent. Their dual nature makes them both thoughtful and spontaneous.",
        "lucky_number": 5,
        "lucky_color": "Yellow",
        "element": "Air",
        "gemstone": "Agate💎\n\nProvides emotional stability, grounding, and inner strength.",
        "horoscope": "Today may present a flurry of conversations and ideas. Embrace your curiosity and don’t shy away from engaging in something new. Your words hold power—use them to uplift, motivate, or even comfort someone close."
    },
    "Cancer": {
        "traits": "Cancer is deeply intuitive and emotional. They are incredibly nurturing and protective of loved ones. Cancers often have a strong connection to their home and roots. Though sensitive, they possess a hidden strength and resilience that helps them navigate even the toughest storms.",
        "lucky_number": 2,
        "lucky_color": "White",
        "element": "Water",
        "gemstone": "Pearl💎\n\nCultivates calmness, sincerity, and integrity.",
        "horoscope": "Your emotions are your strength today. It’s a good time to connect with family or reflect on your inner world. Trust your gut feelings—they’re trying to guide you toward healing or meaningful connection."
    },
    "Leo": {
        "traits": "Leos are charismatic, creative, and love to be in the spotlight. Ruled by the Sun, they exude warmth and confidence. They are natural leaders with a flair for drama and a generous heart. Leos are often loyal and brave, and they inspire others with their boldness.",
        "lucky_number": 1,
        "lucky_color": "Gold",
        "element": "Fire",
        "gemstone": "Peridot💎\n\nBrings positivity, reduces stress, and promotes emotional balance.",
        "horoscope": "Step into your power today, Leo. Your presence is impossible to ignore. Use this spotlight to create something meaningful or uplift those around you. A spontaneous gesture may lead to heartfelt appreciation."
    },
    "Virgo": {
        "traits": "Virgos are analytical, kind, and detail-oriented. They have a deep need for order and perfection, but this stems from their desire to be helpful and practical. Virgos are humble yet incredibly intelligent, always striving to improve themselves and others.",
        "lucky_number": 5,
        "lucky_color": "Grey",
        "element": "Earth",
        "gemstone": "Sapphire💎\n\nBrings wisdom, mental clarity, and protection.",
        "horoscope": "Today, small efforts will yield big results. Your attention to detail can help resolve lingering issues. Don’t be too hard on yourself—progress is better than perfection. Stay grounded and trust the process."
    },
    "Libra": {
        "traits": "Libra is ruled by Venus, making them lovers of beauty, balance, and harmony. They are diplomatic, fair-minded, and highly social. Libras strive for peace in their surroundings and relationships, and their charming nature often draws others to them.",
        "lucky_number": 6,
        "lucky_color": "Pink",
        "element": "Air",
        "gemstone": "Opal💎\nEnhances creativity and emotional expression.",
        "horoscope": "Seek harmony in all things today. Whether it’s resolving a misunderstanding or creating something beautiful, your sense of balance is your superpower. A calm, graceful approach will get you further than force."
    },
    "Scorpio": {
        "traits": "Scorpios are intense, passionate, and fiercely loyal. They have a mysterious aura and a deep emotional intelligence. Scorpios are not afraid of transformation and often experience rebirth through challenges. They value truth, depth, and emotional connection.",
        "lucky_number": 9,
        "lucky_color": "Black",
        "element": "Water",
        "gemstone": "Topaz💎\n\nAttracts abundance and supports emotional stability.",
        "horoscope": "You may find yourself digging deeper today—into ideas, emotions, or even relationships. Trust your instincts and be honest with yourself. The truth you uncover can lead to meaningful change."
    },
    "Sagittarius": {
        "traits": "Sagittarians are free-spirited, optimistic, and philosophical. They seek truth, adventure, and higher knowledge. Sagittarians are often the life of the party, blending wisdom with humor. They need space to explore and grow, both physically and mentally.",
        "lucky_number": 3,
        "lucky_color": "Purple",
        "element": "Fire",
        "gemstone": "Turquoise💎\n\nAids healing, communication, and inner calm.",
        "horoscope": "Adventure calls your name today. Whether it's a new idea or place, allow your curiosity to guide you. Don’t worry about the outcome—sometimes the journey brings the greatest gifts."
    },
    "Capricorn": {
        "traits": "Capricorns are disciplined, responsible, and ambitious. They work hard and are often seen as the achievers of the zodiac. With a calm and practical approach, they build success slowly but surely. Loyalty and tradition are important to them.",
        "lucky_number": 8,
        "lucky_color": "Brown",
        "element": "Earth",
        "gemstone": "Garnet💎\n\nBoosts confidence and inspires love and devotion.",
        "horoscope": "Today is about focus and commitment. Stick to your goals, even if progress feels slow. Your efforts are laying strong foundations. Avoid shortcuts—your strength lies in perseverance."
    },
    "Aquarius": {
        "traits": "Aquarians are innovative, independent, and often ahead of their time. They think differently and are deeply concerned with humanitarian causes. Aquarius energy is electric, full of ideas, and thrives on freedom and unconventional paths.",
        "lucky_number": 4,
        "lucky_color": "Blue",
        "element": "Air",
        "gemstone": "Amethyst💎\n\nCalms the mind and enhances intuition and clarity.",
        "horoscope": "A unique idea or perspective may light up your mind today. Share it—it could spark change. Embrace your individuality and remember, your way may be the way someone else needed to see."
    },
    "Pisces": {
        "traits": "Pisces are dreamy, compassionate, and deeply intuitive. They are artistic and spiritual, often having a rich inner world. Pisceans are gentle souls who feel deeply and connect easily with others' emotions. Their empathy is their greatest strength.",
        "lucky_number": 7,
        "lucky_color": "Sea Green",
        "element": "Water",
        "gemstone": "Aquamarine💎\n\nPromotes peace, courage, and clear communication.",
        "horoscope": "Let your imagination run free today. You might feel extra sensitive—use it to create or connect with someone who needs empathy. Quiet moments will bring profound clarity if you allow them."
    }
}

moon_phase_traits = {
    "New Moon": (
        "✨ You were born under the New Moon — a time of beginnings, mystery, and deep potential.\n"
        "People born during this phase are visionary souls, often drawn to fresh ideas, new paths, and unexplored possibilities. "
        "You're not afraid to dream big, and though you may be reserved at times, your inner world is rich with purpose and creativity."
    ),
    "Waxing Crescent": (
        "🌒 Your moon phase is Waxing Crescent — a symbol of growth, hope, and silent determination.\n"
        "You are optimistic, forward-looking, and filled with aspirations. "
        "You believe in slow but steady progress and have the quiet strength to build something meaningful from scratch. "
        "Your persistence often sets you apart."
    ),
    "First Quarter": (
        "🌓 You were born under the First Quarter Moon — a phase of action, tension, and decisions.\n"
        "You're naturally courageous and resilient. Challenges fuel your drive instead of stopping you. "
        "You often find yourself at crossroads and are skilled at making bold decisions when it counts. "
        "Your determination inspires those around you."
    ),
    "Waxing Gibbous": (
        "🌔 Your phase is Waxing Gibbous — the phase of refinement, patience, and near-completion.\n"
        "You are thoughtful, analytical, and a perfectionist at heart. "
        "You constantly seek to improve — whether it's yourself, your work, or your surroundings. "
        "You believe the magic lies in the details, and you're not afraid to go the extra mile."
    ),
    "Full Moon": (
        "🌕 You were born under the Full Moon — a time of illumination, intensity, and clarity.\n"
        "You're vibrant, emotionally expressive, and deeply intuitive. "
        "You have a magnetic presence and often attract attention without even trying. "
        "Balance is your journey — between inner desires and outer realities. "
        "Your life is about shining bright, but also finding inner peace."
    ),
    "Waning Gibbous": (
        "🌖 Your moon phase is Waning Gibbous — symbolic of sharing, teaching, and reflection.\n"
        "You are wise, generous, and deeply compassionate. "
        "You enjoy helping others and often find fulfillment in giving back. "
        "Your life path might involve mentoring, healing, or guiding. "
        "You're a natural nurturer with an old soul."
    ),
    "Last Quarter": (
        "🌗 Born during the Last Quarter Moon — a phase of transition, release, and wisdom.\n"
        "You're realistic, thoughtful, and excellent at letting go of what no longer serves you. "
        "You’re often introspective and philosophical, always questioning and re-evaluating. "
        "Transformation is your strength, and you help others see what truly matters."
    ),
    "Waning Crescent": (
        "🌘 Your moon phase is Waning Crescent — a time of surrender, dreams, and spiritual closure.\n"
        "You are deeply intuitive, sensitive, and attuned to the unseen. "
        "Often reflective and gentle, you carry wisdom from past experiences and have a calming presence. "
        "You may prefer solitude or quiet moments, where your imagination and empathy thrive."
    )
}



zodiac_compatibility_map = {
    "Aries": {
        "best": ["Leo", "Sagittarius", "Gemini", "Aquarius"],
        "good": ["Aries", "Libra"],
        "average": ["Taurus", "Cancer"],
        "challenging": ["Capricorn", "Virgo", "Scorpio", "Pisces"]
    },
    "Taurus": {
        "best": ["Virgo", "Capricorn", "Cancer", "Pisces"],
        "good": ["Taurus", "Scorpio"],
        "average": ["Gemini", "Leo"],
        "challenging": ["Aries", "Sagittarius", "Aquarius", "Libra"]
    },
    "Gemini": {
        "best": ["Libra", "Aquarius", "Aries", "Leo"],
        "good": ["Gemini", "Sagittarius"],
        "average": ["Taurus", "Cancer"],
        "challenging": ["Virgo", "Pisces", "Capricorn", "Scorpio"]
    },
    "Cancer": {
        "best": ["Scorpio", "Pisces", "Taurus", "Virgo"],
        "good": ["Cancer", "Capricorn"],
        "average": ["Aries", "Gemini"],
        "challenging": ["Leo", "Aquarius", "Libra", "Sagittarius"]
    },
    "Leo": {
        "best": ["Aries", "Sagittarius", "Gemini", "Libra"],
        "good": ["Leo", "Aquarius"],
        "average": ["Taurus", "Cancer"],
        "challenging": ["Scorpio", "Pisces", "Virgo", "Capricorn"]
    },
    "Virgo": {
        "best": ["Taurus", "Capricorn", "Cancer", "Scorpio"],
        "good": ["Virgo", "Pisces"],
        "average": ["Leo", "Gemini"],
        "challenging": ["Aries", "Libra", "Sagittarius", "Aquarius"]
    },
    "Libra": {
        "best": ["Gemini", "Aquarius", "Leo", "Sagittarius"],
        "good": ["Libra", "Aries"],
        "average": ["Cancer", "Capricorn"],
        "challenging": ["Taurus", "Virgo", "Scorpio", "Pisces"]
    },
    "Scorpio": {
        "best": ["Cancer", "Pisces", "Virgo", "Capricorn"],
        "good": ["Scorpio", "Taurus"],
        "average": ["Aries", "Libra"],
        "challenging": ["Gemini", "Leo", "Sagittarius", "Aquarius"]
    },
    "Sagittarius": {
        "best": ["Aries", "Leo", "Libra", "Aquarius"],
        "good": ["Sagittarius", "Gemini"],
        "average": ["Capricorn", "Scorpio"],
        "challenging": ["Taurus", "Cancer", "Virgo", "Pisces"]
    },
    "Capricorn": {
        "best": ["Taurus", "Virgo", "Scorpio", "Pisces"],
        "good": ["Capricorn", "Cancer"],
        "average": ["Sagittarius", "Libra"],
        "challenging": ["Aries", "Gemini", "Leo", "Aquarius"]
    },
    "Aquarius": {
        "best": ["Gemini", "Libra", "Aries", "Sagittarius"],
        "good": ["Aquarius", "Leo"],
        "average": ["Virgo", "Capricorn"],
        "challenging": ["Taurus", "Cancer", "Scorpio", "Pisces"]
    },
    "Pisces": {
        "best": ["Cancer", "Scorpio", "Taurus", "Capricorn"],
        "good": ["Pisces", "Virgo"],
        "average": ["Leo", "Libra"],
        "challenging": ["Aries", "Gemini", "Sagittarius", "Aquarius"]
    }
}



def get_compatibility_score(zodiac1, zodiac2):
    relation = zodiac_compatibility_map.get(zodiac1)
    if not relation:
        return 0, "Invalid Zodiac Sign 🤷‍♀️"

    if zodiac2 in relation["best"]:
        return 90, "Perfect Match 💖"
    elif zodiac2 in relation["good"]:
        return 75, "Harmonious Pair 😊"
    elif zodiac2 in relation["average"]:
        return 60, "Needs Effort 🤔"
    elif zodiac2 in relation["challenging"]:
        return 45, "Challenging Pair 😅"
    else:
        return 50, "Neutral Connection 😐"
    
def clean_zodiac_name(name):
    return name.split(" ")[0]
        


def get_zodiac_sign(day, month):
        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
                return "Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
                return "Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
                return "Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
                return "Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
                return "Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
                return "Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
                return "Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
                return "Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
                return "Sagittarius"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
                return "Capricorn"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
                return "Aquarius"
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
                return "Pisces"

def get_phase_on_day(year: int, month: int, day: int) -> float:
    """Returns a floating-point number from 0-1, where 0=new, 0.5=full, and 1=new."""
    # Create a date object for the given year, month, and day
    date = ephem.Date(dt_date(year, month, day))
    
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
    




class Ui_MainWindow_astroscope(object):
    def setupUi(self, MainWindow_astroscope):
        MainWindow_astroscope.setObjectName("MainWindow_astroscope")
        MainWindow_astroscope.resize(1440, 772)
        MainWindow_astroscope.setStyleSheet("background-color: rgb(0, 0, 0);")



        self.centralwidget_astroscope = QtWidgets.QWidget(MainWindow_astroscope)
        self.centralwidget_astroscope.setObjectName("centralwidget_astroscope")



        self.label_astroscope_logo = QtWidgets.QLabel(self.centralwidget_astroscope)
        self.label_astroscope_logo.setGeometry(QtCore.QRect(490, 5, 481, 151))
        self.label_astroscope_logo.setText("")
        self.label_astroscope_logo.setPixmap(QtGui.QPixmap("./images/astroscope/astro_logo.png"))
        self.label_astroscope_logo.setScaledContents(True)
        self.label_astroscope_logo.setObjectName("label_astroscope_logo")
        self.label_astroscope_logo.setVisible(True)


        
        self.label_bg_astro = QtWidgets.QLabel(self.centralwidget_astroscope)
        self.label_bg_astro.setGeometry(QtCore.QRect(0, -20, 1441, 891))
        self.label_bg_astro.setText("")
        self.label_bg_astro.setPixmap(QtGui.QPixmap("./images/astroscope/astroscope_bg.png"))
        self.label_bg_astro.setScaledContents(True)
        self.label_bg_astro.setObjectName("label_bg_astro")



        self.groupBox_compatibility = QtWidgets.QGroupBox(self.centralwidget_astroscope)
        self.groupBox_compatibility.setGeometry(QtCore.QRect(1030, 170, 371, 361))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.groupBox_compatibility.setFont(font)
        
        self.groupBox_compatibility.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 140);")
        self.groupBox_compatibility.setObjectName("groupBox_compatibility")
        self.groupBox_compatibility.setStyleSheet("\n"
"QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 50);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 2px 10px;\n"
"    background-color: rgba(0, 0, 0, 0);\n"  # dark background
"    color: white;\n"                          # bright text
"    border-radius: 5px;\n"
"}\n"
"")





        self.groupBox_moon_phase = QtWidgets.QGroupBox(self.centralwidget_astroscope)
        self.groupBox_moon_phase.setGeometry(QtCore.QRect(50, 170, 381, 361))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.groupBox_moon_phase.setFont(font)
        
        self.groupBox_moon_phase.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 140);")
        self.groupBox_moon_phase.setObjectName("groupBox_moon_phase")
        self.groupBox_moon_phase.setStyleSheet("\n"
"QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 50);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 2px 10px;\n"
"    background-color: rgba(0, 0, 0, 0);\n"  # dark background
"    color: white;\n"                          # bright text
"    border-radius: 5px;\n"
"}\n"
"")


        self.textEdit_moon_phase = QtWidgets.QTextEdit(self.groupBox_moon_phase)
        self.textEdit_moon_phase.setGeometry(QtCore.QRect(20, 35, 331, 300))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_moon_phase.setFont(font)
        self.textEdit_moon_phase.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textEdit_moon_phase.setObjectName("textEdit_moon_phase")
        self.textEdit_moon_phase.setReadOnly(True)  # 🔒 make it non-editable
        self.textEdit_moon_phase.setFocusPolicy(Qt.NoFocus)
        self.textEdit_moon_phase.setStyleSheet("\n"
"QTextEdit {\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 0);\n"
"}\n"
"\n"
"QTextEdit::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"}\n"
"")



        self.comboBox_your_zodiac = QtWidgets.QComboBox(self.groupBox_compatibility)
        self.comboBox_your_zodiac.setGeometry(QtCore.QRect(150, 50, 211, 41))
        self.comboBox_your_zodiac.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_your_zodiac.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 133);")
        self.comboBox_your_zodiac.setObjectName("comboBox_your_zodiac")
        self.comboBox_your_zodiac.addItem("")
        self.comboBox_your_zodiac.addItem("")
        self.comboBox_your_zodiac.addItem("")
        self.comboBox_your_zodiac.addItem("")
        self.comboBox_your_zodiac.addItem("")
        self.comboBox_your_zodiac.addItem("")
        self.comboBox_your_zodiac.addItem("")
        self.comboBox_your_zodiac.addItem("")
        self.comboBox_your_zodiac.addItem("")
        self.comboBox_your_zodiac.addItem("")
        self.comboBox_your_zodiac.addItem("")
        self.comboBox_your_zodiac.addItem("")
        self.comboBox_your_zodiac.setStyleSheet("""
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



        self.pushButton_compatibility = QtWidgets.QPushButton(self.groupBox_compatibility)
        self.pushButton_compatibility.setGeometry(QtCore.QRect(70, 160, 231, 41))
        font = QtGui.QFont()
        # font.setFamily("Baskerville")
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton_compatibility.setFont(font)
        self.pushButton_compatibility.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_compatibility.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(104, 104, 104);")
        self.pushButton_compatibility.setObjectName("pushButton_compatibility")
        self.pushButton_compatibility.clicked.connect(self.check_zodiac_compatibility)
        self.pushButton_compatibility.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 232, 241,50);
                color: white;
                border-radius: 15px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgb(255, 232, 241);
                color: black;
            }
            QPushButton:pressed {
                background-color: rgb(255, 102, 87);
            }
        """)



        self.textEdit_compatibility = QtWidgets.QTextEdit(self.groupBox_compatibility)
        self.textEdit_compatibility.setGeometry(QtCore.QRect(20, 210, 331, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_compatibility.setFont(font)
        self.textEdit_compatibility.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textEdit_compatibility.setObjectName("textEdit_compatibility")
        self.textEdit_compatibility.setReadOnly(True)  # 🔒 make it non-editable
        self.textEdit_compatibility.setFocusPolicy(Qt.NoFocus)
        self.textEdit_compatibility.setStyleSheet("\n"
"QTextEdit {\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 0);\n"
"}\n"
"\n"
"QTextEdit::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"}\n"
"")



        self.label_enter_date_time_2 = QtWidgets.QLabel(self.groupBox_compatibility)
        self.label_enter_date_time_2.setGeometry(QtCore.QRect(40, 50, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_enter_date_time_2.setFont(font)
        self.label_enter_date_time_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_enter_date_time_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 140);")
        self.label_enter_date_time_2.setObjectName("label_enter_date_time_2")
        self.label_enter_date_time_2.setStyleSheet("\n"
"QLabel {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 0px;\n"
"    padding: 00px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);\n"
"}\n"
"\n"
"QLabel::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"}\n"
"")



        self.label_enter_date_time_3 = QtWidgets.QLabel(self.groupBox_compatibility)
        self.label_enter_date_time_3.setGeometry(QtCore.QRect(40, 95, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_enter_date_time_3.setFont(font)
        self.label_enter_date_time_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_enter_date_time_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 140);")
        self.label_enter_date_time_3.setObjectName("label_enter_date_time_3")
        self.label_enter_date_time_3.setStyleSheet("\n"
"QLabel {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 0px;\n"
"    padding: 00px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 120);\n"
"}\n"
"\n"
"QLabel::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"}\n"
"")




        self.comboBox_your_zodiac_2 = QtWidgets.QComboBox(self.groupBox_compatibility)
        self.comboBox_your_zodiac_2.setGeometry(QtCore.QRect(150, 100, 211, 41))
        self.comboBox_your_zodiac_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_your_zodiac_2.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 133);")
        self.comboBox_your_zodiac_2.setObjectName("comboBox_your_zodiac_2")
        self.comboBox_your_zodiac_2.addItem("")
        self.comboBox_your_zodiac_2.addItem("")
        self.comboBox_your_zodiac_2.addItem("")
        self.comboBox_your_zodiac_2.addItem("")
        self.comboBox_your_zodiac_2.addItem("")
        self.comboBox_your_zodiac_2.addItem("")
        self.comboBox_your_zodiac_2.addItem("")
        self.comboBox_your_zodiac_2.addItem("")
        self.comboBox_your_zodiac_2.addItem("")
        self.comboBox_your_zodiac_2.addItem("")
        self.comboBox_your_zodiac_2.addItem("")
        self.comboBox_your_zodiac_2.addItem("")
        self.comboBox_your_zodiac_2.setStyleSheet("""
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



        self.groupBox_horoscope = QtWidgets.QGroupBox(self.centralwidget_astroscope)
        self.groupBox_horoscope.setGeometry(QtCore.QRect(1030, 550, 381, 201)) # 50, 540, 381, 201
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.groupBox_horoscope.setFont(font)
        self.groupBox_horoscope.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 140);")
        self.groupBox_horoscope.setObjectName("groupBox_horoscope")
        self.groupBox_horoscope.setStyleSheet("\n"
"QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 50);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 2px 10px;\n"
"    background-color: rgba(0, 0, 0, 0);\n"  # dark background
"    color: white;\n"                          # bright text
"    border-radius: 5px;\n"
"}\n"
"")




        self.textEdit_horoscope = QtWidgets.QTextEdit(self.groupBox_horoscope)
        self.textEdit_horoscope.setGeometry(QtCore.QRect(30, 30, 331, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_horoscope.setFont(font)
        self.textEdit_horoscope.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textEdit_horoscope.setObjectName("textEdit_horoscope")
        self.textEdit_horoscope.setReadOnly(True)  # 🔒 make it non-editable
        self.textEdit_horoscope.setFocusPolicy(Qt.NoFocus)
        self.textEdit_horoscope.setStyleSheet("\n"
"QTextEdit {\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 0);\n"
"}\n"
"\n"
"QTextEdit::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"}\n"
"")



        self.groupBox_gemstone = QtWidgets.QGroupBox(self.centralwidget_astroscope)
        self.groupBox_gemstone.setGeometry(QtCore.QRect(50, 540, 381, 201))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.groupBox_gemstone.setFont(font)
        self.groupBox_gemstone.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 140);")
        self.groupBox_gemstone.setObjectName("groupBox_gemstone")
        self.groupBox_gemstone.setStyleSheet("\n"
"QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 50);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 2px 10px;\n"
"    background-color: rgba(0, 0, 0, 0);\n"  # dark background
"    color: white;\n"                          # bright text
"    border-radius: 5px;\n"
"}\n"
"")


        self.textEdit_gemstone = QtWidgets.QTextEdit(self.groupBox_gemstone)
        self.textEdit_gemstone.setGeometry(QtCore.QRect(20, 40, 331, 131))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.textEdit_gemstone.setFont(font)
        self.textEdit_gemstone.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textEdit_gemstone.setObjectName("textEdit_gemstone")
        self.textEdit_gemstone.setReadOnly(True)  # 🔒 make it non-editable
        self.textEdit_gemstone.setFocusPolicy(Qt.NoFocus)
        self.textEdit_gemstone.setStyleSheet("\n"
"QTextEdit {\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 0);\n"
"}\n"
"\n"
"QTextEdit::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"}\n"
"")



        zodiac1 = self.comboBox_your_zodiac.currentText().strip()
        zodiac2 = self.comboBox_your_zodiac_2.currentText().strip()



        self.label_all_rights_reserved = QtWidgets.QLabel(self.centralwidget_astroscope)
        self.label_all_rights_reserved.setGeometry(QtCore.QRect(560, 770, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_all_rights_reserved.setFont(font)
        self.label_all_rights_reserved.setStyleSheet("color: rgb(255, 255, 255);\n"
"    background-color: rgba(0, 0, 0, 0));")
        self.label_all_rights_reserved.setAttribute(Qt.WA_TranslucentBackground)
        self.label_all_rights_reserved.setObjectName("label_all_rights_reserved")
        self.label_all_rights_reserved.setCursor(QtCore.Qt.PointingHandCursor)


        self.label_enter_date_time = QtWidgets.QLabel(self.centralwidget_astroscope)
        self.label_enter_date_time.setGeometry(QtCore.QRect(500, 170, 451, 51))
        self.label_enter_date_time.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_enter_date_time.setStyleSheet("\n"
"QLabel {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 0px;\n"
"    padding: 00px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 50);\n"
"}\n"
"\n"
"QLabel::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"}\n"
"")
        # self.label_enter_date_time.setObjectName("label_all_rights_reserved")
        self.label_enter_date_time.setObjectName("label_enter_date_time")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_enter_date_time.setFont(font)


        self.pushButton_check_main = QtWidgets.QPushButton(self.centralwidget_astroscope)
        self.pushButton_check_main.setGeometry(QtCore.QRect(500, 290, 450, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        # font.setUnderline(True)
        font.setBold(True)
        self.pushButton_check_main.setFont(font)
        self.pushButton_check_main.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_check_main.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 178, 221);")
        self.pushButton_check_main.setObjectName("pushButton_check_main")
        self.pushButton_check_main.clicked.connect(self.on_calculate_clicked)
        self.pushButton_check_main.clicked.connect(self.calculate_moon_phase)
        self.pushButton_check_main.clicked.connect(self.show_widgets)
        
        self.pushButton_check_main.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 232, 241);
                color: black;
                border-radius: 15px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgb(255, 156, 146);  
            }
            QPushButton:pressed {
                background-color: rgb(255, 102, 87);
            }
        """)



        self.dateEdit_main = QtWidgets.QDateEdit(self.centralwidget_astroscope)
        self.dateEdit_main.setCalendarPopup(True)
        self.dateEdit_main.setDisplayFormat("dd/MM/yyyy")
        self.dateEdit_main.setDate(QtCore.QDate.currentDate())
        self.dateEdit_main.setFocusPolicy(QtCore.Qt.NoFocus)
        # self.dateEdit_main.setGeometry(QtCore.QRect(500, 230, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.dateEdit_main.setFont(font)

        self.dateEdit_main.setMinimumSize(QtCore.QSize(240, 50))
        self.dateEdit_main.setMaximumSize(QtCore.QSize(150, 50))

        self.dateEdit_main.resize(200, 40)
        self.dateEdit_main.move(500, 230)



        self.dateEdit_main.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_main.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 143);\n"
"color: rgb(255, 255, 255);")
        self.dateEdit_main.setObjectName("dateEdit_main")
        self.dateEdit_main.setStyleSheet("""
    QDateEdit {
        font-size: 16px;
        padding-left: 10px;
        color: white;
        background-color: rgba(255, 167, 199, 102);
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
        calendar = self.dateEdit_main.calendarWidget()
        calendar.setFixedWidth(self.dateEdit_main.width())


        self.timeEdit_main = QtWidgets.QTimeEdit(self.centralwidget_astroscope)
        self.timeEdit_main.setDisplayFormat("hh:mm AP")
        self.timeEdit_main.setTime(QtCore.QTime.currentTime())
        self.timeEdit_main.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.timeEdit_main.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.timeEdit_main.setFont(font)

        self.timeEdit_main.setMinimumSize(QtCore.QSize(200, 50))
        self.timeEdit_main.setMaximumSize(QtCore.QSize(150, 50))

        self.timeEdit_main.resize(200, 40)
        self.timeEdit_main.move(750, 230)  # You can adjust Y-axis position as needed

        self.timeEdit_main.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.timeEdit_main.setStyleSheet("""
    QTimeEdit {
        font-size: 16px;
        padding-left: 10px;
        color: white;
        background-color: rgba(255, 167, 199, 102);
        border: 1px solid white;
        border-radius: 5px;
    }

    
""")

        self.timeEdit_main.setObjectName("timeEdit_main")




        self.textEdit_main = QtWidgets.QTextEdit(self.centralwidget_astroscope)
        self.textEdit_main.setGeometry(QtCore.QRect(500, 360, 450, 381)) #500, 300, 451, 381     500, 300, 450, 51)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit_main.setFont(font)
        self.textEdit_main.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textEdit_main.setStyleSheet("background-color: rgba(0, 0, 0, 148);")
        self.textEdit_main.setObjectName("textEdit_main")
        self.textEdit_main.setReadOnly(True)  # 🔒 make it non-editable
        self.textEdit_main.setFocusPolicy(Qt.NoFocus)
        self.textEdit_main.setStyleSheet("\n"
"QTextEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(229, 197, 255, 50);\n"
"}\n"
"\n"
"QTextEdit::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"}\n"
"")






        self.label_bg_astro.raise_()
        self.label_astroscope_logo.raise_()
        self.groupBox_compatibility.raise_()
        self.groupBox_moon_phase.raise_()
        # self.groupBox_kundali.raise_()
        self.groupBox_horoscope.raise_()
        self.groupBox_gemstone.raise_()
        self.label_all_rights_reserved.raise_()
        self.label_enter_date_time.raise_()
        self.pushButton_check_main.raise_()
        self.dateEdit_main.raise_()
        self.timeEdit_main.raise_()
        self.textEdit_main.raise_()


        self.groupBox_compatibility.setVisible(False)
        self.groupBox_gemstone.setVisible(False)
        self.groupBox_moon_phase.setVisible(False)
        self.groupBox_horoscope.setVisible(False)
        self.textEdit_main.setVisible(False)






        # self.label.raise_()
        MainWindow_astroscope.setCentralWidget(self.centralwidget_astroscope)
        self.statusbar_astroscope = QtWidgets.QStatusBar(MainWindow_astroscope)
        self.statusbar_astroscope.setObjectName("statusbar_astroscope")
        MainWindow_astroscope.setStatusBar(self.statusbar_astroscope)

        self.retranslateUi(MainWindow_astroscope)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_astroscope)


    

    



    def retranslateUi(self, MainWindow_astroscope):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_astroscope.setWindowTitle(_translate("MainWindow_astroscope", "MainWindow"))
        # self.label_astroscope_logo.setText(_translate("MainWindow_astroscope", "Astroscope Logo"))
        self.groupBox_compatibility.setTitle(_translate("MainWindow_astroscope", "Compatibility Checker"))
        self.groupBox_moon_phase.setTitle(_translate("MainWindow_astroscope", "Your Birth Moon"))
        self.comboBox_your_zodiac.setItemText(0, _translate("MainWindow_astroscope", "Aries (मेष) ♈"))
        self.comboBox_your_zodiac.setItemText(1, _translate("MainWindow_astroscope", "Taurus (वृषभ) ♉"))
        self.comboBox_your_zodiac.setItemText(2, _translate("MainWindow_astroscope", "Gemini (मिथुन) ♊"))
        self.comboBox_your_zodiac.setItemText(3, _translate("MainWindow_astroscope", "Cancer (कर्क) ♋"))
        self.comboBox_your_zodiac.setItemText(4, _translate("MainWindow_astroscope", "Leo (सिंह) ♌"))
        self.comboBox_your_zodiac.setItemText(5, _translate("MainWindow_astroscope", "Virgo (कन्या) ♍"))
        self.comboBox_your_zodiac.setItemText(6, _translate("MainWindow_astroscope", "Libra (तुला) ♎"))
        self.comboBox_your_zodiac.setItemText(7, _translate("MainWindow_astroscope", "Scorpio (वृश्चिक) ♏"))
        self.comboBox_your_zodiac.setItemText(8, _translate("MainWindow_astroscope", "Sagittarius (धनु) ♐"))
        self.comboBox_your_zodiac.setItemText(9, _translate("MainWindow_astroscope", "Capricorn (मकर) ♑"))
        self.comboBox_your_zodiac.setItemText(10, _translate("MainWindow_astroscope", "Aquarius (कुम्भ)♒"))
        self.comboBox_your_zodiac.setItemText(11, _translate("MainWindow_astroscope", "Pisces (मीन) ♓"))
        self.pushButton_compatibility.setText(_translate("MainWindow_astroscope", "Check your compatibility"))
        self.label_enter_date_time_2.setText(_translate("MainWindow_astroscope", "Zodiac 1"))
        self.label_enter_date_time_3.setText(_translate("MainWindow_astroscope", "Zodiac 2"))
        self.comboBox_your_zodiac_2.setItemText(0, _translate("MainWindow_astroscope", "Aries (मेष) ♈"))
        self.comboBox_your_zodiac_2.setItemText(1, _translate("MainWindow_astroscope", "Taurus (वृषभ) ♉"))
        self.comboBox_your_zodiac_2.setItemText(2, _translate("MainWindow_astroscope", "Gemini (मिथुन) ♊"))
        self.comboBox_your_zodiac_2.setItemText(3, _translate("MainWindow_astroscope", "Cancer (कर्क) ♋"))
        self.comboBox_your_zodiac_2.setItemText(4, _translate("MainWindow_astroscope", "Leo (सिंह) ♌"))
        self.comboBox_your_zodiac_2.setItemText(5, _translate("MainWindow_astroscope", "Virgo (कन्या) ♍"))
        self.comboBox_your_zodiac_2.setItemText(6, _translate("MainWindow_astroscope", "Libra (तुला) ♎"))
        self.comboBox_your_zodiac_2.setItemText(7, _translate("MainWindow_astroscope", "Scorpio (वृश्चिक) ♏"))
        self.comboBox_your_zodiac_2.setItemText(8, _translate("MainWindow_astroscope", "Sagittarius (धनु) ♐"))
        self.comboBox_your_zodiac_2.setItemText(9, _translate("MainWindow_astroscope", "Capricorn (मकर) ♑"))
        self.comboBox_your_zodiac_2.setItemText(10, _translate("MainWindow_astroscope", "Aquarius (कुम्भ)♒"))
        self.comboBox_your_zodiac_2.setItemText(11, _translate("MainWindow_astroscope", "Pisces (मीन) ♓"))
        self.groupBox_horoscope.setTitle(_translate("MainWindow_astroscope", "Today\'s Horoscope"))
        self.groupBox_gemstone.setTitle(_translate("MainWindow_astroscope", "Gemstone Recommendations"))
        self.label_all_rights_reserved.setText(_translate("MainWindow_astroscope", " © Lunascope 2024. All Rights Reserved."))
        self.label_enter_date_time.setText(_translate("MainWindow_astroscope", "  Enter your date and time of birth:"))
        self.pushButton_check_main.setText(_translate("MainWindow_astroscope", "Find my zodiac!"))


    def show_widgets(self):
        widgets = [
            self.groupBox_compatibility,
            self.groupBox_gemstone,
            self.groupBox_moon_phase,
            self.groupBox_horoscope,
            self.textEdit_main
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


    def check_zodiac_compatibility(self):
        zodiac1 = clean_zodiac_name(self.comboBox_your_zodiac.currentText().strip())
        zodiac2 = clean_zodiac_name(self.comboBox_your_zodiac_2.currentText().strip())


        # print(f"DEBUG: Selected Zodiacs => {zodiac1} | {zodiac2}")  # Debug line

        percent, tag = get_compatibility_score(zodiac1, zodiac2)
        result_text = f"Compatibility between {zodiac1} & {zodiac2}:💫\nCompatibility: {percent}%\nTag: {tag}"
        self.textEdit_compatibility.setPlainText(result_text)

    def calculate_moon_phase(self):
        try:
            selected_date = self.dateEdit_main.date()
            year = selected_date.year()
            month = selected_date.month()
            day = selected_date.day()
            lunation = get_phase_on_day(year, month, day)
            phase_name = get_moon_phase_name(lunation)
            user_birthday_date = self.dateEdit_main.date().toPyDate()

            moon_phase = get_moon_phase_name(lunation)  # Use the moon phase here directly from the function
            traits = moon_phase_traits.get(moon_phase, "Traits not found for this moon phase.")
        
        # Display the result in the textEdit widget
            self.textEdit_moon_phase.setText(f"                 🌙{moon_phase}\n\n{traits}")

            
        except ValueError:
            QMessageBox.critical(None, "Error", "Invalid date format. Please enter a date in YYYY-MM-DD format.")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An error occurred: {e}")



# GUI ke andar button click event:
    def on_calculate_clicked(self):
    # 1. Get date & time from QDateEdit and QTimeEdit
        date = self.dateEdit_main.date().toPyDate()
        day = date.day
        month = date.month
        



    # 2. Find zodiac sign
        zodiac = get_zodiac_sign(day, month)

    # 3. Fetch data from dictionary
        data = zodiac_traits.get(zodiac, {})

    # 4. Set text in respective QTextEdits
        self.textEdit_gemstone.setText(f"                            {data.get('gemstone', '')}")
        self.textEdit_horoscope.setText(f"{data.get('horoscope', '')}")

        
        data = zodiac_traits.get(zodiac, {})
        traits = data.get('traits', 'N/A')
        element = data.get('element', 'N/A')
        lucky_number = data.get('lucky_number', 'N/A')
        lucky_color = data.get('lucky_color', 'N/A')

        full_text = (
        f"🌟 Zodiac Sign: {zodiac}\n\n"
    f"🧬 Personality Traits:\n{traits}\n\n"
    f"🔥 Element: {element}\n"
    f"🎯 Lucky Number: {lucky_number}\n"
    f"🎨 Lucky Color: {lucky_color}\n\n"
)

        self.textEdit_main.setText(full_text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_astroscope = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_astroscope()
    ui.setupUi(MainWindow_astroscope)
    MainWindow_astroscope.setWindowTitle("Astroscope")
    MainWindow_astroscope.show()
    sys.exit(app.exec_())
