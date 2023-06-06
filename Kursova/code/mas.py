# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mas.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QEasingCurve, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QShowEvent, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow, QPushButton,QMessageBox,QFileDialog,QVBoxLayout, QDialog,
    QTextEdit, QWidget, QLabel)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(450, 355)  # Set fixed size here
        #MainWindow.resize(450, 355)

        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 0, 124, 255), stop:1 rgba(0, 26, 171, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.NumEdit = QTextEdit(self.centralwidget)
        self.NumEdit.setObjectName(u"NumEdit")
        self.NumEdit.setGeometry(QRect(280, 70, 61, 31))
        font = QFont()
        font.setPointSize(10)
        self.NumEdit.setFont(font)
        self.NumEdit.setStyleSheet(u"QTextEdit {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:30px;\n"
"height:20px; \n"
"}\n"
"")
        self.MinEdit = QTextEdit(self.centralwidget)
        self.MinEdit.setObjectName(u"NumEdit")
        self.MinEdit.setGeometry(QRect(250, 30, 50, 27))
        font = QFont()
        font.setPointSize(10)
        self.MinEdit.setFont(font)
        self.MinEdit.setStyleSheet(u"QTextEdit {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:30px;\n"
"height:20px; \n"
"}\n"
"")
        self.MaxEdit = QTextEdit(self.centralwidget)
        self.MaxEdit.setObjectName(u"NumEdit")
        self.MaxEdit.setGeometry(QRect(350, 30, 55, 27))
        font = QFont()
        font.setPointSize(10)
        self.MaxEdit.setFont(font)
        self.MaxEdit.setStyleSheet(u"QTextEdit {\n"       
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:30px;\n"
"height:20px; \n"
"}\n"
"")
        self.MinLabel = QLabel(self.centralwidget)
        self.MinLabel.setObjectName(u"MinLabel")
        self.MinLabel.setGeometry(QRect(225, 30, 25, 27))
        font = QFont()
        font.setPointSize(10)
        self.MinLabel.setFont(font)
        self.MinLabel.setStyleSheet(u"QLabel {\n"       
"color: white;\n"
"background-color: rgba(255,255,255,0);\n"
"border:0px solid rgba(255,255,255,40);\n"
"width:30px;\n"
"height:20px; \n"
"}\n"
"")

        self.MaxLabel = QLabel(self.centralwidget)
        self.MaxLabel.setObjectName(u"MaxLabel")
        self.MaxLabel.setGeometry(QRect(315, 30, 35, 27))
        font = QFont()
        font.setPointSize(10)
        self.MaxLabel.setFont(font)
        self.MaxLabel.setStyleSheet(u"QLabel {\n"       
"color: white;\n"
"background-color: rgba(255,255,255,0);\n"
"border:px solid rgba(255,255,255,40);\n"
"width:30px;\n"
"height:20px; \n"
"}\n"
"")

        self.ComboSort = QComboBox(self.centralwidget)
        self.ComboSort.addItem("")
        self.ComboSort.addItem("")
        self.ComboSort.addItem("")
        self.ComboSort.setObjectName(u"ComboSort")
        self.ComboSort.setGeometry(QRect(20, 70, 201, 31))
        self.ComboSort.setStyleSheet(u"QComboBox {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:30px;\n"
"height:20px; \n"
"}\n"
"QComboBox QAbstractItemView{\n"
"color: white\n"
"}\n"                               
"")
        self.Generate = QPushButton(self.centralwidget)
        self.Generate.setObjectName(u"Generate")
        self.Generate.setGeometry(QRect(350, 70, 91, 31))
        font1 = QFont()
        font1.setBold(True)
        self.Generate.setFont(font1)
        self.Generate.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:30px;\n"
"height:20px; \n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70)\n"
"}\n"
"")
        #self.Generate.clicked.connect(self.generate_numbers)

        self.Sort = QPushButton(self.centralwidget)
        self.Sort.setObjectName(u"Sort")
        self.Sort.setGeometry(QRect(140, 200, 151, 61))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.Sort.setFont(font2)
        self.Sort.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:30px;\n"
"height:20px; \n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70)\n"
"}\n"
"")
        #self.Sort.clicked.connect(self.show_message)  # Connect the button to the function


        self.Animation = QPushButton(self.centralwidget)
        self.Animation.setObjectName(u"Animation")
        self.Animation.setGeometry(QRect(320, 330, 121, 21))
        self.Animation.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:60px;\n"
"height:20px; \n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70)\n"
"}\n"
"")
        self.Graph = QPushButton(self.centralwidget)
        self.Graph.setObjectName(u"Graph")
        self.Graph.setGeometry(QRect(10, 330, 121, 21))
        self.Graph.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:10px;\n"
"height:20px; \n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70)\n"
"}\n"
"")
        self.Save = QPushButton(self.centralwidget)
        self.Save.setObjectName(u"Save")
        self.Save.setGeometry(QRect(140, 330, 171, 21))
        self.Save.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:50px;\n"
"height:20px; \n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70)\n"
"}\n"
"")
        self.Clear = QPushButton(self.centralwidget)
        self.Clear.setObjectName(u"Clear")
        self.Clear.setGeometry(QRect(355, 110, 80, 30))
        self.Clear.setStyleSheet(u"QPushButton {\n"
 "color: white;\n"
 "background-color: rgba(255,255,255,30);\n"
 "border:1px solid rgba(255,255,255,40);\n"
 "border-radius: 7px;\n"
 "width:10px;\n"
 "height:20px; \n"
 "}\n"
 "QPushButton:hover{\n"
 "background-color: rgba(255,255,255,40)\n"
 "}\n"
 "QPushButton:pressed{\n"
 "background-color: rgba(255,255,255,70)\n"
 "}\n"
 "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0443\u0432\u0430\u043d\u043d\u044f \u043c\u0430\u0441\u0438\u0432\u0456\u0432", None))
        self.ComboSort.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0411\u043b\u043e\u0447\u043d\u0435 \u0441\u043e\u0440\u0442\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.ComboSort.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0443\u0432\u0430\u043d\u043d\u044f \u043f\u0456\u0434\u0440\u0430\u0445\u0443\u043d\u043a\u043e\u043c", None))
        self.ComboSort.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u043e\u0437\u0440\u044f\u0434\u043d\u0435 \u0441\u043e\u0440\u0442\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.MinLabel.setText(QCoreApplication.translate("MainWindow", u"Мін:", None))
        self.MaxLabel.setText(QCoreApplication.translate("MainWindow", u"Макс:", None))

        self.Generate.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0433\u0435\u043d\u0435\u0440\u0443\u0432\u0430\u0442\u0438", None))
        self.Sort.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0443\u0432\u0430\u0442\u0438", None))
        self.Animation.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0456\u043c\u0430\u0446\u0456\u044f", None))
        self.Graph.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0456\u043a", None))
        self.Save.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0431\u0435\u0440\u0435\u0436\u0435\u043d\u043d\u044f \u0432 \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u0438\u0439 \u0444\u0430\u0439\u043b", None))
        self.Clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u0438", None))
    # retranslateUi

