from PySide6.QtWidgets import QApplication

from piskle.views import UiMainWindow
from piskle.main import UI
from PySide6 import QtCore


def test_exit(qtbot, monkeypatch):
    exit_calls = []
    monkeypatch.setattr(QApplication, "exit", lambda: exit_calls.append(1))
    ui = UI()
    ui.show()
    QApplication.exit()
    assert exit_calls == [1]


def test_focus(qtbot):
    app = UiMainWindow()
    app.show()
    qtbot.mouseClick(app.button, QtCore.Qt.LeftButton)
    qtbot.waitUntil(lambda: app.button.hasFocus())
    assert app.button.hasFocus()
