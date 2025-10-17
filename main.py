import datetime
import os
import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QApplication, QMenu, QSystemTrayIcon
from PySide6.QtGui import QAction, QIcon, QFontMetrics


def UiClass(path):
    formClass, widgetClass = loadUiType(path)
    name = os.path.basename(path).replace(".", "_")

    def __init__(self, parent=None):
        widgetClass.__init__(self, parent)
        formClass.setupUi(self, self)

    return type(name, (widgetClass, formClass), {"__init__": __init__})


class TransparentWidget(UiClass("design.ui")):
    def __init__(self):
        super().__init__()

        self._old_pos = None

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(
            QIcon(os.path.join(os.path.dirname(__file__), "assets/school.png"))
        )

        self.tray_menu = QMenu()

        open_action = QAction("Развернуть", self)
        exit_action = QAction("Выход", self)

        self.tray_menu.addAction(open_action)
        self.tray_menu.addAction(exit_action)

        open_action.triggered.connect(self.show_window)
        exit_action.triggered.connect(QApplication.quit)

        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.activated.connect(self.on_tray_activated)
        self.tray_icon.show()

        self.time_txt.setText(datetime.datetime.now().time().strftime("%H:%M:%S"))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)
        self.timer.start(1000)

    # --- Остальной код ---
    def update_info(self):
        self.time_txt.setText(datetime.datetime.now().time().strftime("%H:%M:%S"))

    def hide_to_tray(self):
        """Скрыть окно и показать иконку в трее"""
        self.hide()
        self.tray_icon.show()
        self.tray_icon.showMessage(
            "Свернуто в трей",
            "Приложение продолжает работать.",
            QSystemTrayIcon.Information,
            2000,
        )

    def show_window(self):
        self.show()
        self.raise_()
        self.activateWindow()

    def closeEvent(self, event):
        """Переопределяем закрытие — сворачиваем вместо выхода"""
        event.ignore()
        self.hide_to_tray()

    def on_tray_activated(self, reason):
        """Двойной клик по иконке — показать"""
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_window()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TransparentWidget()
    widget.show()
    sys.exit(app.exec())
