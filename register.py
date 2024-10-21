from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QPushButton, QLineEdit, QRadioButton, QComboBox
from PyQt5.QtGui import QFont
import sys

# Asosiy Register oynasi
class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.setFixedSize(480, 480)

        # Register uchun ma'lumotlar
        self.information = QLabel("Information Register", self)
        self.font(self.information, 90, 10)
        self.information.setFixedSize(300, 50)
        self.information.setStyleSheet("background: black;color: yellow;")

        self.fullname = QLineEdit(self)
        self.fullname.setPlaceholderText("First Name...")
        self.font(self.fullname, 135, 80)
        self.fullname.setFixedSize(200, 50)
        self.fullname.setStyleSheet("background: black;color: red;")

        self.lastname = QLineEdit(self)
        self.lastname.setPlaceholderText("Last Name")
        self.font(self.lastname, 135, 150)
        self.lastname.setFixedSize(200, 50)
        self.lastname.setStyleSheet("background: black;color: yellow;")

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("User Name")
        self.font(self.username, 135, 220)
        self.username.setFixedSize(200, 50)
        self.username.setStyleSheet("background: black;color: #2d98da;")

        self.next_button = QPushButton("Next", self)
        self.next_button.setFixedSize(200, 50)
        self.font(self.next_button, 135, 300)
        self.next_button.clicked.connect(self.goto_info)

        self.setStyleSheet(self.style())

    def font(self, obj, x, y):
        obj.setFont(QFont("Comic Sans MS", 12))
        obj.move(x, y)

    def style(self):
        return """
            QWidget {
                background-color: #a5b1c2;
                color: #213D44;
            }
            QPushButton {
                background-color: black;  
                color: #fa8231;               
                border: 4px solid black;  
                border-radius: 10px;      
            }
            QLineEdit {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
            QLabel {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
        """

    def goto_info(self):
        # Agar maydonlar to'ldirilmasa xato ko'rsatamiz
        if not self.fullname.text().strip() or not self.lastname.text().strip() or not self.username.text().strip():
            QMessageBox.warning(self, "Error", "All fields must be filled out!")
        else:
            # Keyingi oynaga o'tish
            self.info_window = Info(self.fullname.text(), self.lastname.text(), self.username.text())
            self.info_window.show()
            self.close()


# Info oynasi
class Info(QWidget):
    def __init__(self, fullname, lastname, username):
        super().__init__()
        self.setWindowTitle("Info")
        self.setFixedSize(480, 480)

        self.fullname = fullname
        self.lastname = lastname
        self.username = username

        self.information = QLabel("Information Data", self)
        self.font(self.information, 90, 10)
        self.information.setFixedSize(300, 50)
        self.setStyleSheet("background:#d1d8e0")

        self.month = QComboBox(self)
        self.month.addItems(["Month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        self.font(self.month, 20, 100)
        self.month.setFixedSize(130, 50)
        self.month.setStyleSheet("background:#8854d0;color:yellow")

        self.day = QLineEdit(self)
        self.day.setPlaceholderText("Day")
        self.font(self.day, 170, 100)
        self.day.setFixedSize(130, 50)
        self.day.setStyleSheet("background:#45aaf2;color:black;border: 3px solid border")

        self.year = QLineEdit(self)
        self.year.setPlaceholderText("Year")
        self.font(self.year, 320, 100)
        self.year.setFixedSize(130, 50)
        self.year.setStyleSheet("background:#778ca3;color:black;border: 3px border")

        self.gender_male = QRadioButton("Male", self)
        self.font(self.gender_male, 90, 180)
        self.gender_male.setFixedSize(130, 50)

        self.gender_female = QRadioButton("Female", self)
        self.font(self.gender_female, 240, 180)
        self.gender_female.setFixedSize(130, 50)

        self.next_button = QPushButton("Next", self)
        self.next_button.setFixedSize(200, 50)
        self.font(self.next_button, 135, 250)
        self.next_button.clicked.connect(self.goto_email)

        self.setStyleSheet(self.style())

    def font(self, obj, x, y):
        obj.setFont(QFont("Comic Sans MS", 12))
        obj.move(x, y)

    def style(self):
        return """
            QWidget {
                background-color: white;
                color: #213D44;
            }
            QPushButton {
                background-color: white;  
                color: #213D44;               
                border: 4px solid black;  
                border-radius: 10px;      
            }
            QLineEdit {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
            QLabel {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
            QComboBox {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
            QRadioButton {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
        """

    def goto_email(self):
        # Email oynasiga o'tish
        gender = "Male" if self.gender_male.isChecked() else "Female"
        self.email_window = Email(self.fullname, self.lastname, self.username, self.day.text(), self.month.currentText(), self.year.text(), gender)
        self.email_window.show()
        self.close()


# Email oynasi
class Email(QWidget):
    def __init__(self, fullname, lastname, username, day, month, year, gender):
        super().__init__()

        self.fullname = fullname
        self.lastname = lastname
        self.username = username
        self.day = day
        self.month = month
        self.year = year
        self.gender = gender

        self.setWindowTitle("Email")
        self.setFixedSize(480, 480)

        self.information = QLabel("Create Email", self)
        self.font(self.information, 90, 10)
        self.information.setFixedSize(300, 50)

        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Email")
        self.font(self.email, 135, 80)
        self.email.setFixedSize(200, 50)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.font(self.password, 135, 150)
        self.password.setFixedSize(200, 50)

        self.register_button = QPushButton("Register", self)
        self.register_button.setFixedSize(200, 50)
        self.font(self.register_button, 135, 220)
        self.register_button.clicked.connect(self.goto_loginwindow)

        self.setStyleSheet(self.style())

    def font(self, obj, x, y):
        obj.setFont(QFont("Comic Sans MS", 12))
        obj.move(x, y)

    def goto_loginwindow(self):
        # Email va parolni to'g'ri kiritilganligini tekshiramiz
        email = self.email.text().strip()
        password = self.password.text().strip()

        # Email formati @gmail.com yoki @ru.com bilan tugaganligini tekshirish
        if not email or not (email.endswith('@gmail.com') or email.endswith('@ru.com')) or not password:
            QMessageBox.warning(self, "Error", "All fields must be filled out correctly!")
        else:
            # Keyingi oynaga o'tish va to'plangan ma'lumotlarni o'tkazish
            self.login_window = LoginWindow(self.fullname, self.lastname, self.username, self.day, self.month, self.year, self.gender, email, password)
            self.login_window.show()
            self.close()

    def style(self):
        return """
            QWidget {
                background-color: white;
                color: #213D44;
            }
            QPushButton {
                background-color: white;  
                color: #213D44;               
                border: 4px solid black;  
                border-radius: 10px;      
            }
            QLineEdit {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
            QLabel {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
        """


# LoginWindow
class LoginWindow(QWidget):
    def __init__(self, fullname, lastname, username, day, month, year, gender, email, password):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(480, 480)

        self.information = QLabel(f"Welcome, {fullname} {lastname}!", self)
        self.font(self.information, 100, 50)
        self.information.setFixedSize(300, 50)

        self.details = QLabel(f"Username: {username}\nBirthday: {day}/{month}/{year}\nGender: {gender}\nEmail: {email}", self)
        self.font(self.details, 50, 120)
        self.details.setFixedSize(400, 200)

        self.setStyleSheet(self.style())

    def font(self, obj, x, y):
        obj.setFont(QFont("Comic Sans MS", 12))
        obj.move(x, y)

    def style(self):
        return """
            QWidget {
                background-color: white;
                color: #213D44;
            }
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec_())
