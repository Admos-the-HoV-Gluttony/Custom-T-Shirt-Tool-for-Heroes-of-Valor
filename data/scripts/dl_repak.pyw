import urllib.request
import zipfile
import os
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

url = "https://github.com/trumank/repak/releases/download/v0.2.2/repak_cli-x86_64-pc-windows-msvc.zip"
destination_folder = "data/tools/repak cli v0.2.2"

os.makedirs(destination_folder, exist_ok=True)

zip_path = os.path.join(destination_folder, 'repak_cli-x86_64-pc-windows-msvc.zip')
with urllib.request.urlopen(url) as response:
    with open(zip_path, 'wb') as f:
        f.write(response.read())

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(destination_folder)

os.remove(zip_path)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Example")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        
        label = QLabel("Repak CLI Downloaded and Extracted Successfully!", self)
        layout.addWidget(label)
        
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
