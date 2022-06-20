from PyQt6.QtWidgets import QApplication, QWidget,  QVBoxLayout, QLabel, QPushButton, QLineEdit
# import PyDictionary
# --use-deprecated=backtrack-on-build-failures


def make_sentence():
    input_text = text.text()
    output_label.setText(input_text.capitalize() + 'RESULT BRO')


app = QApplication([])
window = QWidget()
window.setWindowTitle('This is an APP')
layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton('Search For')
layout.addWidget(btn)
# WHEN CLICKED
btn.clicked.connect(make_sentence)

# O
output_label = QLabel('Result')
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()
