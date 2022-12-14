from PySide6.QtWidgets import QApplication, QMainWindow

from piskle.views import UiMainWindow as UiMainWindow

import signal
import sys

signal.signal(signal.SIGINT, signal.SIG_DFL)


class UI(QMainWindow):
    title = "Piskle"

    def __init__(self, *args, **kwargs) -> None:
        super(UI, self).__init__(*args, **kwargs)
        self.setWindowTitle(self.title)
        size = QApplication.primaryScreen().size() * 0.6
        self.resize(size)
        self.setMinimumSize(620, 340)
        self.ui = UiMainWindow(self)
        self.setCentralWidget(self.ui)


if __name__ == "__main__":  # pragma: no cover
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec())
