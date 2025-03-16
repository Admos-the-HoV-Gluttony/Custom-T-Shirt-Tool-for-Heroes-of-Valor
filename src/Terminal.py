from PyQt6.QtWidgets import QTextEdit

# Fill out once dark mode hookup works so that colours flip correctly when switching between light and dark
colour_loopup = {
    "dark" : {
        "warn" : "FFC300",
        "error" : "e54141",
        "debug" : "f500ed"
    }
}

line_start_character = ">"

class Terminal:
    terminal_window: QTextEdit
    terminal_theme = "dark"

    def __init__(self):
        self.terminal_window = QTextEdit()
        self.terminal_window.setReadOnly(True)

    def log(self, text: str):
        self.__output(text)

    def warn(self, text: str):
        self.__output("<font color=\"#" + colour_loopup[self.terminal_theme]["warn"] + "\">[WARN]:</font> " + text)

    def error(self, text: str):
        self.__output("<font color=\"#" + colour_loopup[self.terminal_theme]["error"] + "\">[ERROR]:</font> " + text)

    def debug(self, text: str):
        self.__output("<font color=\"#" + colour_loopup[self.terminal_theme]["debug"] + "\">[DEBUG]:</font> " + text)

    def setTheme(self, theme: str):
        self.terminal_theme = theme

    def __output(self, text: str):
        self.terminal_window.append(line_start_character + " " + text)