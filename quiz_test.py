import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QButtonGroup, QMessageBox
)

class TestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Yechish Interfeysi")
        self.setGeometry(100, 100, 400, 300)
        

        self.questions = [
            {"savol": "2 + 2 nima?", "variantlar": ["3", "4", "5", "6"], "to'g'ri": "4"},
            {"savol": "5 x 3 nima?", "variantlar": ["8", "20", "12", "15"], "to'g'ri": "15"},
            {"savol": "9 - 4 nima?", "variantlar": ["3", "5", "7", "6"], "to'g'ri": "5"},
        ]
        
        self.current_question = 0
        self.score = 0
        
        
        self.question_label = QLabel(self)
        self.radio_group_box = QWidget(self)
        self.radio_group = QButtonGroup(self)
        self.radio_buttons = [QRadioButton(self) for _ in range(4)]
        
        
        vbox = QVBoxLayout()
        for i, rb in enumerate(self.radio_buttons):
            self.radio_group.addButton(rb)
            vbox.addWidget(rb)
        
        self.radio_group_box.setLayout(vbox)
        
        
        self.next_button = QPushButton("Keyingi savol", self)
        self.next_button.clicked.connect(self.check_answer)
        
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.question_label)
        main_layout.addWidget(self.radio_group_box)
        main_layout.addWidget(self.next_button)
        
        self.setLayout(main_layout)
        
        
        self.load_question()
    
    def load_question(self):
        self.radio_group.setExclusive(False)
        for rb in self.radio_buttons:
            rb.setChecked(False)
        self.radio_group.setExclusive(True)
        
        current = self.questions[self.current_question]
        self.question_label.setText(current["savol"])
        
        for i, rb in enumerate(self.radio_buttons):
            rb.setText(current["variantlar"][i])
    
    def check_answer(self):
        selected_button = self.radio_group.checkedButton()
        if selected_button:
            selected_answer = selected_button.text()
            correct_answer = self.questions[self.current_question]["to'g'ri"]
            
            if selected_answer == correct_answer:
                self.score += 1
            
            self.current_question += 1
            
            if self.current_question < len(self.questions):
                self.load_question()
            else:
                self.show_result()
    
    def show_result(self):
        QMessageBox.information(self, "Test yakuni", f"Sizning natijangiz: {self.score}/{len(self.questions)}")
        self.close()

app = QApplication(sys.argv)
window = TestApp()
window.show()
sys.exit(app.exec_())