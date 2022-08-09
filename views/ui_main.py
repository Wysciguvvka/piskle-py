import logging

from PySide6.QtCore import QObject
from PySide6.QtGui import QPainter, QPaintEvent
from PySide6.QtWidgets import QWidget, QStyleOption, QStyle


class UiMainWindow(QWidget):
    def __init__(self, parent: QObject = None, **kwargs) -> None:
        super(UiMainWindow, self).__init__(parent=parent, **kwargs)
        """Initialize UiMainWindow class instance"""
    def paintEvent(self, event: QPaintEvent) -> None:
        """Re-implement paintEvent method"""
        try:
            opt = QStyleOption()
            opt.initFrom(self)
            painter = QPainter(self)
            self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
            painter.end()
        except KeyboardInterrupt:
            return
