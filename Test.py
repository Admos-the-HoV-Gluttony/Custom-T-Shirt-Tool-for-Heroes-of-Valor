import sys
import os
import json
import logging  
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QTextEdit, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QLineEdit, QLabel, QFileDialog, QMessageBox
from PyQt6.QtGui import QIcon
import shutil

from src.Globals import Terminal
from src.HelperFunctions import create_QHBox, create_push_button, create_checkbox

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom T-Shirt Tool GUI")
        self.setGeometry(100, 100, 720, 480)

        main_layout = QHBoxLayout()

        self.page_selector = QTabWidget()
        self.page_selector.setFixedWidth(300)
        self.create_pages()
        main_layout.addWidget(self.page_selector)
        main_layout.addWidget(Terminal.setup_window())

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.game_path_textbox.textChanged.connect(self.on_game_path_changed)

    def create_pages(self):
        page_names = ["Texture Converter", "Packaging Tools", "Test Environment", "Setup Menu"]
        for name in page_names:
            page = QWidget()
            layout = QVBoxLayout(page)
            
            if name == "Texture Converter":
                button_text = "Inject Texture"
                layout.addWidget(create_push_button(button_text, lambda: self.button_clicked(button_text)))

                layout.addLayout(create_QHBox("Choose T-Shirt to Overwrite", ["Night Camo", "Green Camo", "Frankenstein", "Dracula", "Wolf", "Banana", "Paytest Axis", "Playtest Allied", "FTW Axis", "FTW Allied"]))
                layout.addLayout(create_QHBox("Image Filter for Mipmap Generation", ["Cubic", "Linear", "Point", "None"]))

                self.skip_mipmap_checkbox = create_checkbox("Skip Mipmap Generation", False)
                layout.addWidget(self.skip_mipmap_checkbox)

                h_layout3 = QHBoxLayout()
                label3 = QLabel("Path to new Texture")
                self.texture_path_textbox = QLineEdit()
                file_button = QPushButton(QIcon("data/icons/folder.png"), "")
                file_button.setFixedHeight(25)
                file_button.clicked.connect(self.open_file_dialog)
                h_layout3.addWidget(label3)
                h_layout3.addWidget(self.texture_path_textbox)
                h_layout3.addWidget(file_button)
                layout.addLayout(h_layout3)
            elif name == "Packaging Tools":
                layout.addWidget(create_push_button("Import Game Files", lambda: self.import_game_files()))
                layout.addWidget(create_push_button("Unpackage Game Files", self.unpackage_game_files))
                layout.addWidget(create_push_button("Repackage Game Files", lambda: self.button_clicked("Repackage Game Files")))
                layout.addWidget(create_push_button("Remove Unpackaged Game Files", self.remove_unpacked_game_files))
                layout.addWidget(create_push_button("Export Game Files", self.export_game_files))
            elif name == "Test Environment":
                layout.addWidget(create_push_button("Run Test Environment", self.run_test_environment))
            elif name == "Setup Menu":
                layout.addWidget(create_push_button("DL and Extract 'repak v0.2.2'", lambda: self.download_and_extract_repak()))
                layout.addWidget(create_push_button("DL, Extract and Fix 'UE4 DDS Tools v0.6.1'", lambda: self.download_and_extract_dds_tools()))

                h_layout_game_path = QHBoxLayout()
                label_game_path = QLabel("Path to Game Files")
                self.game_path_textbox = QLineEdit()  
                game_file_button = QPushButton(QIcon("data/icons/folder.png"), "")
                game_file_button.setFixedHeight(25)
                game_file_button.clicked.connect(self.open_set_path_dialog)  
                h_layout_game_path.addWidget(label_game_path)
                h_layout_game_path.addWidget(self.game_path_textbox)
                h_layout_game_path.addWidget(game_file_button)
                layout.addLayout(h_layout_game_path)

            else:
                layout.addWidget(create_push_button(name, lambda: self.button_clicked(name)))

            self.page_selector.addTab(page, name)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Texture File", "", "Image Files (*.png *.jpg *.bmp *.dds *.hdr *.tga)")
        if file_path:
            self.texture_path_textbox.setText(file_path)

    def open_set_path_dialog(self):  
        dir_path = QFileDialog.getExistingDirectory(self, "Select Game Files Directory")
        if dir_path:
            self.game_path_textbox.setText(dir_path)
            self.save_game_path(dir_path)

    def button_clicked(self, button_name):
        
        if button_name == "Repackage Game Files":
            pak_folder_path = r"data\game_files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor"
            
            if not os.path.exists(pak_folder_path):
                Terminal.error("The directory 'HeroesOfValor-WindowsNoEditor' is missing.")
            else:
                reply = QMessageBox.question(self, 'Confirmation', 
                                             "Do you want to repackage the game files? This may take a while",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                             QMessageBox.StandardButton.No)
                
                if reply == QMessageBox.StandardButton.Yes:
                    repak_executable_path = r"data\tools\repak cli v0.2.2\repak.exe"

                    try:
                        result = subprocess.run(
                            [repak_executable_path, "pack", "--compression", "Zlib", pak_folder_path], 
                            stdout=subprocess.PIPE,  
                            stderr=subprocess.PIPE,  
                            creationflags=subprocess.CREATE_NO_WINDOW 
                        )
                        Terminal.log("The game files have been successfully repackaged.")
                        if result.stderr:
                            Terminal.error(result.stderr.decode())
                        if result.stdout:
                            Terminal.log(result.stdout.decode())
                    except subprocess.CalledProcessError as e:
                        Terminal.error(f"An error occurred while repackaging the file: {e}")
                        if e.stderr:
                            Terminal.error(e.stderr.decode())
                        if e.stdout:
                            Terminal.log(e.stdout.decode())
                else:
                    Terminal.log("Repack operation cancelled by user.")
        elif button_name == "Unpackage Game Files":
            pak_file_path = r"data\game_files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor.pak"
            
            if not os.path.exists(pak_file_path):
                Terminal.error("The file 'HeroesOfValor-WindowsNoEditor.pak' is missing.")
            else:
                reply = QMessageBox.question(self, 'Confirmation', 
                                             "Do you want to unpackage the game files? This may take a while",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                             QMessageBox.StandardButton.No)
                
                if reply == QMessageBox.StandardButton.Yes:
                    repak_executable_path = r"data\tools\repak cli v0.2.2\repak.exe"

                    try:
                        result = subprocess.run(
                            [repak_executable_path, "unpack", pak_file_path], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE, 
                            creationflags=subprocess.CREATE_NO_WINDOW  
                        )
                        Terminal.log("The file has been successfully unpacked.")
                        if result.stderr:
                            Terminal.error(result.stderr.decode())
                        if result.stdout:
                            Terminal.log(result.stdout.decode())
                    except subprocess.CalledProcessError as e:
                        Terminal.error(f"An error occurred while unpacking the file: {e}")
                        if e.stderr:
                            Terminal.error(e.stderr.decode())
                        if e.stdout:
                            Terminal.log(e.stdout.decode())
                else:
                    Terminal.log("Unpack operation cancelled by user.")
        elif button_name == "Remove Unpackaged Game Files":
            pass
        else:
            message = f"Button '{button_name}' clicked. Functionality is still under development."
            Terminal.log(message)

    def unpackage_game_files(self):
        pak_file_path = r"data\game_files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor.pak"
        
        if not os.path.exists(pak_file_path):
            Terminal.error("The file 'HeroesOfValor-WindowsNoEditor.pak' is missing.")
        else:
            reply = QMessageBox.question(self, 'Confirmation', 
                                         "Do you want to unpackage the game files? This may take a while",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            
            if reply == QMessageBox.StandardButton.Yes:
                repak_executable_path = r"data\tools\repak cli v0.2.2\repak.exe"

                try:
                    result = subprocess.run(
                        [repak_executable_path, "unpack", pak_file_path], 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE, 
                        creationflags=subprocess.CREATE_NO_WINDOW 
                    )
                    Terminal.log("The file has been successfully unpacked.")
                    if result.stderr:
                        Terminal.error(result.stderr.decode())
                    if result.stdout:
                        Terminal.log(result.stdout.decode())
                except subprocess.CalledProcessError as e:
                    Terminal.error(f"An error occurred while unpacking the file: {e}")
                    if e.stderr:
                        Terminal.error(e.stderr.decode())
                    if e.stdout:
                        Terminal.log(e.stdout.decode())
            else:
                Terminal.log("Unpack operation cancelled by user.")

    def download_and_extract_repak(self):
        reply = QMessageBox.question(self, 'Confirmation', 
                                     "Do you want to download and extract 'repak v0.2.2'?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                result = subprocess.run(
                    ["python", "data\\scripts\\dl_repak.pyw"],
                    capture_output=True, text=True, check=True
                )
                Terminal.log("Download and extraction of 'repak v0.2.2' completed successfully.")
                if result.stdout:
                    Terminal.log(result.stdout)
            except subprocess.CalledProcessError as e:
                Terminal.error(f"Failed to download and extract 'repak v0.2.2'. Error: {e.stderr}")
                if e.stderr:
                    Terminal.error(e.stderr)

    def download_and_extract_dds_tools(self):
        reply = QMessageBox.question(self, 'Confirmation', 
                                     "Do you want to download and extract 'UE4 DDS Tools v0.6.1'?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                result = subprocess.run(
                    ["python", "data\\scripts\\dl_ue4_dds_tools.pyw"],
                    capture_output=True, text=True, check=True
                )
                Terminal.log("Download and extraction of 'UE4 DDS Tools v0.6.1' completed successfully.")
                if result.stdout:
                    Terminal.log(result.stdout)
            except subprocess.CalledProcessError as e:
                Terminal.error(f"Failed to download and extract 'UE4 DDS Tools v0.6.1'. Error: {e.stderr}")
                if e.stderr:
                    Terminal.error(e.stderr)

    def load_game_path(self):
        config_file = "data/config/path_to_game_files.json"
        if os.path.exists(config_file):
            with open(config_file, "r") as file:
                config_data = json.load(file)
                game_path = config_data.get("game_path")
                if game_path:
                    self.game_path_textbox.setText(game_path)
                    return game_path
        else:
            Terminal.warn("Configuration file not found.")
        return None

    def save_game_path(self, path):
        config_dir = os.path.dirname(config_file := "data/config/path_to_game_files.json")
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)
        
        config_data = {"game_path": path}
        
        with open(config_file, "w") as file:
            json.dump(config_data, file, indent=4)
        
        Terminal.log(f"Path saved to {config_file}")

    def is_valid_path(self, path):
        return os.path.isdir(path)

    def on_game_path_changed(self, new_path):
        stripped_path = new_path.strip('\'"')
        
        if self.is_valid_path(stripped_path):
            self.save_game_path(stripped_path)
        else:
            Terminal.warn("Invalid path provided.")

    def check_game_files(self, game_path):
        exe_subpath = os.path.join("HeroesOfValor.exe")
        pak_subpath = os.path.join("HeroesOfValor", "Content", "Paks", "HeroesOfValor-WindowsNoEditor.pak")

        exe_path = os.path.join(game_path, exe_subpath)
        pak_path = os.path.join(game_path, pak_subpath)

        logging.info(f"Checking for 'HeroesOfValor.exe' at: {exe_path}")
        logging.info(f"Checking for 'HeroesOfValor-WindowsNoEditor.pak' at: {pak_path}")

        if os.path.exists(exe_path) and os.path.exists(pak_path):
            logging.info("Both 'HeroesOfValor.exe' and 'HeroesOfValor-WindowsNoEditor.pak' have been found.")
            return True
        else:
            missing_files = []
            if not os.path.exists(exe_path):
                missing_files.append(f"'{exe_subpath}'")
            if not os.path.exists(pak_path):
                missing_files.append(f"'{pak_subpath}'")
            
            logging.error(f"Missing files: {', '.join(missing_files)}")
            Terminal.error(f"Missing files: {', '.join(missing_files)}")
            return False

    def import_game_files(self):
        config_file_path = "data\\config\\path_to_game_files.json"
        
        if not os.path.exists(config_file_path):
            logging.error(f"The configuration file '{config_file_path}' does not exist.")
            Terminal.error(f"The configuration file '{config_file_path}' does not exist.")
            return

        try:
            with open(config_file_path, 'r') as config_file:
                config_data = json.load(config_file)
                game_path = config_data.get("game_path", "").strip()
            
            if not game_path or not os.path.exists(game_path):
                logging.error(f"The specified game path '{game_path}' does not exist.")
                Terminal.error(f"The specified game path '{game_path}' does not exist.")
                return

            if not self.check_game_files(game_path):
                return
            
            reply = QMessageBox.question(self, 'Confirmation', 
                                         "Do you want to import the game files? This may take a while",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    result = subprocess.run(
                        ["python", "data\\scripts\\import.pyw"],
                        capture_output=True, text=True, check=True
                    )

                    if result.returncode != 0:
                        Terminal.error(f"Failed to import game files. {result.stderr}")
                    else:
                        Terminal.log("Game files imported successfully.")
                
                except subprocess.CalledProcessError as e:
                    Terminal.error(f"Failed to import game files. {e.stderr}")

        except FileNotFoundError:
            logging.error(f"File not found: {config_file_path}")
            Terminal.error(f"File not found: {config_file_path}")
        except PermissionError:
            logging.error(f"Permission denied for reading the file: {config_file_path}")
            Terminal.error(f"Permission denied for reading the file: {config_file_path}")
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON from '{config_file_path}': {e}")
            Terminal.error(f"Failed to decode JSON from '{config_file_path}': {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            Terminal.error(f"An unexpected error occurred: {e}")

    def export_game_files(self):
        config_file_path = "data\\config\\path_to_game_files.json"
        
        if not os.path.exists(config_file_path):
            logging.error(f"The configuration file '{config_file_path}' does not exist.")
            Terminal.error(f"The configuration file '{config_file_path}' does not exist.")
            return

        try:
            with open(config_file_path, 'r') as config_file:
                config_data = json.load(config_file)
                game_path = config_data.get("game_path", "").strip()
            
            if not game_path or not os.path.exists(game_path):
                logging.error(f"The specified game path '{game_path}' does not exist.")
                Terminal.error(f"The specified game path '{game_path}' does not exist.")
                return

            modified_pak_path = "data\\game_files\\HeroesOfValor\\Content\\Paks\\HeroesOfValor-WindowsNoEditor.pak"
            
            if not os.path.exists(modified_pak_path):
                logging.error(f"The modified pak file '{modified_pak_path}' does not exist.")
                Terminal.error(f"The modified pak file '{modified_pak_path}' does not exist.")
                return

            reply = QMessageBox.question(self, 'Confirmation', 
                                         "Are you sure you want to export the modified game files? This will overwrite the current files?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            
            if reply == QMessageBox.StandardButton.Yes:
                target_pak_path = os.path.join(game_path, "HeroesOfValor", "Content", "Paks")

                if not os.path.exists(target_pak_path):
                    os.makedirs(target_pak_path)

                try:
                    shutil.copy2(modified_pak_path, target_pak_path)
                    Terminal.log("Game files exported successfully.")
                except Exception as e:
                    logging.error(f"Failed to export game files: {e}")
                    Terminal.error(f"Failed to export game files: {e}")

        except FileNotFoundError:
            logging.error(f"File not found: {config_file_path}")
            Terminal.error(f"File not found: {config_file_path}")
        except PermissionError:
            logging.error(f"Permission denied for reading the file: {config_file_path}")
            Terminal.error(f"Permission denied for reading the file: {config_file_path}")
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON from '{config_file_path}': {e}")
            Terminal.error(f"Failed to decode JSON from '{config_file_path}': {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            Terminal.error(f"An unexpected error occurred: {e}")

    def run_test_environment(self):
        exe_path = os.path.join("data", "game_files", "HeroesOfValor.exe")
        
        if os.path.exists(exe_path):
            logging.info(f"Running '{exe_path}'...")
            try:
                result = subprocess.run(
                    [exe_path],
                    stdout=subprocess.PIPE,  
                    stderr=subprocess.PIPE, 
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
                Terminal.log("Test environment run successfully.")
                if result.stderr:
                    Terminal.error(result.stderr.decode())
                if result.stdout:
                    Terminal.log(result.stdout.decode())
            except subprocess.CalledProcessError as e:
                Terminal.log(f"Failed to start test environment. Error: {e.stderr}")
                if e.stderr:
                    Terminal.error(e.stderr.decode())
                if e.stdout:
                    Terminal.log(e.stdout.decode())
        else:
            logging.error(f"'{exe_path}' does not exist.")
            Terminal.error(f"'HeroesOfValor.exe' not found at '{exe_path}'. Please check the path and try again.")

    def remove_unpacked_game_files(self):
        pak_folder_path = r"data\game_files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor"
        
        if os.path.exists(pak_folder_path):
            reply = QMessageBox.question(self, 'Confirmation', 
                                         "Do you want to delete the unpacked game files?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    shutil.rmtree(pak_folder_path)
                    Terminal.log("Unpacked game files have been successfully deleted.")
                except Exception as e:
                    logging.error(f"Failed to delete the unpacked game files: {e}")
                    Terminal.error(f"Failed to delete the unpacked game files: {e}")
        else:
            Terminal.error("The directory 'HeroesOfValor-WindowsNoEditor' does not exist.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    window.load_game_path()

    sys.exit(app.exec())
