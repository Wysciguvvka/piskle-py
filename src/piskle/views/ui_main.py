from PySide6.QtGui import QPainter, QPaintEvent
from PySide6.QtWidgets import QWidget, QStyleOption, QStyle, QPushButton


class UiMainWindow(QWidget):
    def __init__(self, parent: QWidget | None = None, **kwargs) -> None:
        super(UiMainWindow, self).__init__(parent=parent, **kwargs)
        """Initialize UiMainWindow class instance"""
        self.button = QPushButton(self)
        self.value = 0
        self.button.clicked.connect(lambda: self.update_value())  # type: ignore

    def update_value(self):
        self.value += 1

    def paintEvent(self, event: QPaintEvent) -> None:
        """Re-implement paintEvent method"""
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        painter.end()
