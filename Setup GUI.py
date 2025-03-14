import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QTextEdit, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QComboBox, QLineEdit, QLabel, QFileDialog
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom T-Shirt Tool GUI")
        self.setGeometry(100, 100, 720, 480) 

        main_layout = QHBoxLayout()

        self.page_selector = QTabWidget()
        self.page_selector.setFixedWidth(300)
        self.create_pages()

        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)

        main_layout.addWidget(self.page_selector)
        main_layout.addWidget(self.terminal)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_pages(self):
        page_names = ["Texture Converter", "Packaging Tools", "Test Environment", "Setup Menu"]
        for name in page_names:
            page = QWidget()
            layout = QVBoxLayout(page)
            
            if name == "Texture Converter":
                button_text = "Inject Texture"
                button = QPushButton(button_text)
                button.clicked.connect(lambda: self.button_clicked(button_text))
                layout.addWidget(button)

                h_layout1 = QHBoxLayout()
                label1 = QLabel("Choose T-Shirt to Overwrite")
                combobox1 = QComboBox()
                combobox1.addItems(["Night Camo", "Green Camo", "Frankenstein", "Dracula", "Wolf", "Banana", "Paytest Axis", "Playtest Allied", "FTW Axis", "FTW Allied"])
                h_layout1.addWidget(label1)
                h_layout1.addWidget(combobox1)
                layout.addLayout(h_layout1)

                h_layout2 = QHBoxLayout()
                label2 = QLabel("Image Filter for Mipmap Generation")
                combobox2 = QComboBox()
                combobox2.addItems(["Cubic", "Linear", "Point", "None"])
                h_layout2.addWidget(label2)
                h_layout2.addWidget(combobox2)
                layout.addLayout(h_layout2)

                h_layout3 = QHBoxLayout()
                label3 = QLabel("Path to new Texture")
                self.texture_path_textbox = QLineEdit()
                file_button = QPushButton(QIcon("data/icons/folder.png"), "")
                file_button.clicked.connect(self.open_file_dialog)
                h_layout3.addWidget(label3)
                h_layout3.addWidget(self.texture_path_textbox)
                h_layout3.addWidget(file_button)
                layout.addLayout(h_layout3)
            elif name == "Packaging Tools":
                button_import = QPushButton("Import Game Files")
                button_import.clicked.connect(lambda: self.button_clicked("Import Game Files"))  
                layout.addWidget(button_import)

                button_unpackage = QPushButton("Unpackage Game Files")
                button_unpackage.clicked.connect(lambda: self.button_clicked("Unpackage Game Files"))
                layout.addWidget(button_unpackage)

                button_repackage = QPushButton("Repackage Game Files")
                button_repackage.clicked.connect(lambda: self.button_clicked("Repackage Game Files"))  
                layout.addWidget(button_repackage)

                button_remove_unpacked = QPushButton("Remove Unpackaged Game Files")
                button_remove_unpacked.clicked.connect(lambda: self.button_clicked("Remove Unpackaged Game Files"))  
                layout.addWidget(button_remove_unpacked)

                button_export = QPushButton("Export Game Files")
                button_export.clicked.connect(lambda: self.button_clicked("Export Game Files"))  
                layout.addWidget(button_export)
            elif name == "Test Environment":
                button_text = "Run Test Environment"
                button = QPushButton(button_text)
                button.clicked.connect(lambda: self.button_clicked(button_text))
                layout.addWidget(button)
            elif name == "Setup Menu":
                
                button1_text = "DL and Extract 'repak v0.2.2'"
                button1 = QPushButton(button1_text)
                button1.clicked.connect(lambda: self.button_clicked(button1_text))  
                layout.addWidget(button1)

                button2_text = "DL, Extract and Fix 'UE4 DDS Tools v0.6.1'"
                button2 = QPushButton(button2_text)
                button2.clicked.connect(lambda: self.button_clicked(button2_text))  
                layout.addWidget(button2)

                button3_text = "Set Path to Game Files"
                button3 = QPushButton(button3_text)
                button3.clicked.connect(lambda: self.button_clicked(button3_text))  
                layout.addWidget(button3)
            else:
                button_text = name
                button = QPushButton(button_text)
                button.clicked.connect(lambda: self.button_clicked(button_text))
                layout.addWidget(button)

            self.page_selector.addTab(page, name)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Texture File", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            self.texture_path_textbox.setText(file_path)

    def button_clicked(self, button_name):
        message = f"Button '{button_name}' clicked. Functionality is still under development."
        self.terminal.append(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
