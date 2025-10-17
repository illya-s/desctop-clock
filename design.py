# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(636, 305)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_txt = QLabel(self.centralwidget)
        self.time_txt.setObjectName(u"time_txt")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_txt.sizePolicy().hasHeightForWidth())
        self.time_txt.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Courier 10 Pitch"])
        font.setPointSize(75)
        font.setWeight(QFont.Black)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        self.time_txt.setFont(font)
        self.time_txt.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.time_txt.setTextFormat(Qt.TextFormat.AutoText)
        self.time_txt.setScaledContents(True)
        self.time_txt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_txt.setWordWrap(False)
        self.time_txt.setMargin(25)

        self.horizontalLayout.addWidget(self.time_txt)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.time_txt.setText(QCoreApplication.translate("MainWindow", u"12:00:00", None))
    # retranslateUi

