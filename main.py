from PySide6.QtWidgets import QApplication, QMainWindow

from views import UiMainWindow

import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)


class UI(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(UI, self).__init__(*args, **kwargs)
        self.setWindowTitle("Piskle")
        # self.setWindowIcon(QIcon("./assets/images/icon.png"))
        size = app.primaryScreen().size() * 0.6
        self.resize(size)
        self.setMinimumSize(620, 344)
        self.ui = UiMainWindow(self)
        self.setCentralWidget(self.ui)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec())
