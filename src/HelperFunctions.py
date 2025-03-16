from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QTextEdit, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QComboBox, QLineEdit, QLabel, QFileDialog, QMessageBox, QCheckBox
from PyQt6.QtGui import QIcon

def create_push_button(label_text, connect_func, height = 50):
    button = QPushButton(label_text)
    button.setFixedHeight(height)
    button.clicked.connect(connect_func)
    return button

def create_push_button_icon(icon_url, connect_func, height = 50):
    button = QPushButton(QIcon(icon_url), "")
    button.setFixedHeight(height)
    button.clicked.connect(connect_func)
    return button

def create_QHBox(label_text, items):
    comboBox = QComboBox()
    comboBox.addItems(items)

    label = QLabel(label_text)

    layout = QHBoxLayout()
    layout.addWidget(label)
    layout.addWidget(comboBox)
    return layout

def create_checkbox(lablel_text, starting_state):
    checkbox = QCheckBox(lablel_text)
    checkbox.setChecked(starting_state)
    return checkbox