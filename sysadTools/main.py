# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sysadTools.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess
import os
import csv


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 576)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 576))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 576))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/logo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1024, 576))
        self.centralwidget.setStyleSheet("background-color:  #191AF")
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 1031, 91))
        self.header.setStyleSheet("background-color: #08070b")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.sysnameLabel = QtWidgets.QLabel(self.header)
        self.sysnameLabel.setGeometry(QtCore.QRect(60, 10, 41, 71))
        self.sysnameLabel.setStyleSheet("font: 75 30pt \"Noto Naskh Arabic UI\";\n"
"color: rgb(211, 215, 207)\n"
"")
        self.sysnameLabel.setObjectName("sysnameLabel")
        self.sysnameLabel2 = QtWidgets.QLabel(self.header)
        self.sysnameLabel2.setGeometry(QtCore.QRect(100, 10, 101, 71))
        self.sysnameLabel2.setStyleSheet("font: 75 30pt \"Noto Naskh Arabic UI\";\n"
"font-weight: bold;\n"
"color: rgb(211, 215, 207)")
        self.sysnameLabel2.setObjectName("sysnameLabel2")
        self.pushButton = QtWidgets.QPushButton(self.header)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 31, 51))
        self.pushButton.setStyleSheet("border: none;")
        self.pushButton.setText("")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(35, 35))
        self.pushButton.setObjectName("pushButton")
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(0, 90, 251, 491))
        self.sidebar.setStyleSheet("background-color: #131217")
        self.sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar.setObjectName("sidebar")
        self.dashboardButton = QtWidgets.QPushButton(self.sidebar)
        self.dashboardButton.setGeometry(QtCore.QRect(10, 20, 231, 41))
        self.dashboardButton.setStyleSheet("QPushButton#dashboardButton{\n"
"background-color: #131217;\n"
"font: 75 12pt \"Latin Modern Sans\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 13px;\n"
"text-align: left;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton#dashboardButton:hover{\n"
"background-color: #1d1c23;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/sidebar_buttons/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboardButton.setIcon(icon1)
        self.dashboardButton.setIconSize(QtCore.QSize(18, 18))
        self.dashboardButton.setObjectName("dashboardButton")
        self.processesButton = QtWidgets.QPushButton(self.sidebar)
        self.processesButton.setGeometry(QtCore.QRect(10, 70, 231, 41))
        self.processesButton.setStyleSheet("QPushButton#processesButton{\n"
"background-color: #131217;\n"
"font: 75 12pt \"Latin Modern Sans\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 13px;\n"
"text-align: left;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton#processesButton:hover{\n"
"background-color: #1d1c23;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/sidebar_buttons/processes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.processesButton.setIcon(icon2)
        self.processesButton.setIconSize(QtCore.QSize(18, 18))
        self.processesButton.setObjectName("processesButton")
        self.netconfigButton = QtWidgets.QPushButton(self.sidebar)
        self.netconfigButton.setGeometry(QtCore.QRect(10, 170, 231, 41))
        self.netconfigButton.setStyleSheet("QPushButton#netconfigButton{\n"
"background-color: #131217;\n"
"font: 75 12pt \"Latin Modern Sans\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 13px;\n"
"text-align: left;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton#netconfigButton:hover{\n"
"background-color: #1d1c23;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/sidebar_buttons/networkconfig.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.netconfigButton.setIcon(icon3)
        self.netconfigButton.setIconSize(QtCore.QSize(18, 18))
        self.netconfigButton.setObjectName("netconfigButton")
        self.sysinfoButton = QtWidgets.QPushButton(self.sidebar)
        self.sysinfoButton.setGeometry(QtCore.QRect(10, 220, 231, 41))
        self.sysinfoButton.setStyleSheet("QPushButton#sysinfoButton{\n"
"background-color: #131217;\n"
"font: 75 12pt \"Latin Modern Sans\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 13px;\n"
"text-align: left;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton#sysinfoButton:hover{\n"
"background-color: #1d1c23;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/sidebar_buttons/sysinfo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sysinfoButton.setIcon(icon4)
        self.sysinfoButton.setIconSize(QtCore.QSize(18, 18))
        self.sysinfoButton.setObjectName("sysinfoButton")
        self.accountconfigButton = QtWidgets.QPushButton(self.sidebar)
        self.accountconfigButton.setGeometry(QtCore.QRect(10, 120, 231, 41))
        self.accountconfigButton.setStyleSheet("QPushButton#accountconfigButton{\n"
"background-color: #131217;\n"
"font: 75 12pt \"Latin Modern Sans\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 13px;\n"
"text-align: left;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton#accountconfigButton:hover{\n"
"background-color: #1d1c23;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/sidebar_buttons/useraccounts.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accountconfigButton.setIcon(icon5)
        self.accountconfigButton.setIconSize(QtCore.QSize(18, 18))
        self.accountconfigButton.setObjectName("accountconfigButton")
        self.dashboardButton.raise_()
        self.processesButton.raise_()
        self.netconfigButton.raise_()
        self.accountconfigButton.raise_()
        self.sysinfoButton.raise_()
        self.dashboardFrame = QtWidgets.QFrame(self.centralwidget)
        self.dashboardFrame.setGeometry(QtCore.QRect(250, 90, 781, 491))
        self.dashboardFrame.setStyleSheet("background-color: #191a1f")
        self.dashboardFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dashboardFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dashboardFrame.setObjectName("dashboardFrame")
        self.clock = QtWidgets.QFrame(self.dashboardFrame)
        self.clock.setGeometry(QtCore.QRect(20, 20, 401, 171))
        self.clock.setStyleSheet("background-color: #121318")
        self.clock.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.clock.setFrameShadow(QtWidgets.QFrame.Raised)
        self.clock.setObjectName("clock")
        self.date = QtWidgets.QLabel(self.clock)
        self.date.setGeometry(QtCore.QRect(20, 10, 381, 61))
        self.date.setStyleSheet("font: 36pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.date.setObjectName("date")
        self.time = QtWidgets.QLabel(self.clock)
        self.time.setGeometry(QtCore.QRect(50, 80, 321, 61))
        self.time.setStyleSheet("font: 38pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.time.setObjectName("time")
        self.calendar = QtWidgets.QFrame(self.dashboardFrame)
        self.calendar.setGeometry(QtCore.QRect(440, 20, 311, 171))
        self.calendar.setStyleSheet("background-color: #121318")
        self.calendar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calendar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calendar.setObjectName("calendar")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.calendar)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 0, 272, 171))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(8)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("color: white ;\n"
"selection-background-color: rgb(46, 52, 54); \n"
"selection-color: rgb(211, 215, 207);\n"
"alternate-background-color: rgb(46, 52, 54)")
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.runbackupButton = QtWidgets.QPushButton(self.dashboardFrame)
        self.runbackupButton.setGeometry(QtCore.QRect(30, 210, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.runbackupButton.setFont(font)
        self.runbackupButton.setStyleSheet("QPushButton#runbackupButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 12pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#runbackupButton:hover{\n"
"background-color: #1483fe;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.runbackupButton.setObjectName("runbackupButton")
        self.extractbackupButton = QtWidgets.QPushButton(self.dashboardFrame)
        self.extractbackupButton.setGeometry(QtCore.QRect(280, 210, 211, 41))
        self.extractbackupButton.setStyleSheet("QPushButton#extractbackupButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 12pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#extractbackupButton:hover{\n"
"background-color: #2da576;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.extractbackupButton.setObjectName("extractbackupButton")
        self.deletebackupButton = QtWidgets.QPushButton(self.dashboardFrame)
        self.deletebackupButton.setGeometry(QtCore.QRect(530, 210, 211, 41))
        self.deletebackupButton.setStyleSheet("QPushButton#deletebackupButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 12pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#deletebackupButton:hover{\n"
"background-color: #e1184d;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.deletebackupButton.setObjectName("deletebackupButton")
        self.shutdown = QtWidgets.QFrame(self.dashboardFrame)
        self.shutdown.setGeometry(QtCore.QRect(20, 270, 401, 191))
        self.shutdown.setStyleSheet("background-color: #121318")
        self.shutdown.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shutdown.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shutdown.setObjectName("shutdown")
        self.shutdownHeader = QtWidgets.QLabel(self.shutdown)
        self.shutdownHeader.setGeometry(QtCore.QRect(20, 10, 261, 31))
        self.shutdownHeader.setStyleSheet("font: 20pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.shutdownHeader.setObjectName("shutdownHeader")
        self.minutesbsLabel = QtWidgets.QLabel(self.shutdown)
        self.minutesbsLabel.setGeometry(QtCore.QRect(40, 50, 191, 16))
        self.minutesbsLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.minutesbsLabel.setObjectName("minutesbsLabel")
        self.notifmainLabel = QtWidgets.QLabel(self.shutdown)
        self.notifmainLabel.setGeometry(QtCore.QRect(40, 80, 191, 16))
        self.notifmainLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.notifmainLabel.setObjectName("notifmainLabel")
        self.notifdescLabel = QtWidgets.QLabel(self.shutdown)
        self.notifdescLabel.setGeometry(QtCore.QRect(40, 110, 191, 21))
        self.notifdescLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.notifdescLabel.setObjectName("notifdescLabel")
        self.minutesLine = QtWidgets.QLineEdit(self.shutdown)
        self.minutesLine.setGeometry(QtCore.QRect(230, 50, 61, 24))
        self.minutesLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.minutesLine.setObjectName("minutesLine")
        self.notifmainLine = QtWidgets.QLineEdit(self.shutdown)
        self.notifmainLine.setGeometry(QtCore.QRect(230, 80, 131, 24))
        self.notifmainLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.notifmainLine.setObjectName("notifmainLine")
        self.notifdescLine = QtWidgets.QLineEdit(self.shutdown)
        self.notifdescLine.setGeometry(QtCore.QRect(230, 110, 131, 24))
        self.notifdescLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.notifdescLine.setObjectName("notifdescLine")
        self.minutesLabel = QtWidgets.QLabel(self.shutdown)
        self.minutesLabel.setGeometry(QtCore.QRect(300, 50, 61, 16))
        self.minutesLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.minutesLabel.setObjectName("minutesLabel")
        self.setshutdowntimerButton = QtWidgets.QPushButton(self.shutdown)
        self.setshutdowntimerButton.setGeometry(QtCore.QRect(40, 150, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.setshutdowntimerButton.setFont(font)
        self.setshutdowntimerButton.setStyleSheet("QPushButton#setshutdowntimerButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 12pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#setshutdowntimerButton:hover{\n"
"background-color: #c237b6;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.setshutdowntimerButton.setObjectName("setshutdowntimerButton")
        self.disks = QtWidgets.QFrame(self.dashboardFrame)
        self.disks.setGeometry(QtCore.QRect(440, 270, 311, 191))
        self.disks.setStyleSheet("background-color: #121318")
        self.disks.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.disks.setFrameShadow(QtWidgets.QFrame.Raised)
        self.disks.setObjectName("disks")
        self.disksTable = QtWidgets.QTableWidget(self.disks)
        self.disksTable.setGeometry(QtCore.QRect(10, 10, 291, 131))
        self.disksTable.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: white;\n"
"font: 10pt \"Latin Modern Sans\";")
        self.disksTable.setColumnCount(6)
        self.disksTable.setObjectName("disksTable")
        self.disksTable.setRowCount(0)
        self.deleteduplicateButton = QtWidgets.QPushButton(self.disks)
        self.deleteduplicateButton.setGeometry(QtCore.QRect(20, 150, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.deleteduplicateButton.setFont(font)
        self.deleteduplicateButton.setStyleSheet("QPushButton#deleteduplicateButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 12pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#deleteduplicateButton:hover{\n"
"background-color: #e14849;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.deleteduplicateButton.setObjectName("deleteduplicateButton")
        self.processesFrame = QtWidgets.QFrame(self.centralwidget)
        self.processesFrame.setGeometry(QtCore.QRect(250, 90, 781, 491))
        self.processesFrame.setStyleSheet("background-color: #191a1f")
        self.processesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.processesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.processesFrame.setObjectName("processesFrame")
        self.killbynameButton = QtWidgets.QPushButton(self.processesFrame)
        self.killbynameButton.setGeometry(QtCore.QRect(580, 430, 80, 24))
        self.killbynameButton.setStyleSheet("QPushButton#killbynameButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 10pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton#killbynameButton:hover{\n"
"background-color: #e14849;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.killbynameButton.setObjectName("killbynameButton")
        self.killbyNamelabel = QtWidgets.QLabel(self.processesFrame)
        self.killbyNamelabel.setGeometry(QtCore.QRect(280, 430, 161, 21))
        self.killbyNamelabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.killbyNamelabel.setObjectName("killbyNamelabel")
        self.processTable = QtWidgets.QTableWidget(self.processesFrame)
        self.processTable.setGeometry(QtCore.QRect(30, 20, 711, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processTable.sizePolicy().hasHeightForWidth())
        self.processTable.setSizePolicy(sizePolicy)
        self.processTable.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: white;\n"
"font: 10pt \"Latin Modern Sans\";")
        self.processTable.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.processTable.setRowCount(0)
        self.processTable.setColumnCount(7)
        self.processTable.setObjectName("processTable")
        self.killbynameLine = QtWidgets.QLineEdit(self.processesFrame)
        self.killbynameLine.setGeometry(QtCore.QRect(450, 430, 113, 24))
        self.killbynameLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.killbynameLine.setObjectName("killbynameLine")
        self.killbyPIDlabel = QtWidgets.QLabel(self.processesFrame)
        self.killbyPIDlabel.setGeometry(QtCore.QRect(280, 390, 161, 31))
        self.killbyPIDlabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.killbyPIDlabel.setObjectName("killbyPIDlabel")
        self.killbypidButton = QtWidgets.QPushButton(self.processesFrame)
        self.killbypidButton.setGeometry(QtCore.QRect(580, 390, 80, 24))
        self.killbypidButton.setStyleSheet("QPushButton#killbypidButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 10pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton#killbypidButton:hover{\n"
"background-color: #e14849;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.killbypidButton.setObjectName("killbypidButton")
        self.killbypidLine = QtWidgets.QLineEdit(self.processesFrame)
        self.killbypidLine.setGeometry(QtCore.QRect(450, 390, 113, 24))
        self.killbypidLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.killbypidLine.setObjectName("killbypidLine")
        self.refreshprocessButton = QtWidgets.QPushButton(self.processesFrame)
        self.refreshprocessButton.setGeometry(QtCore.QRect(90, 390, 171, 61))
        self.refreshprocessButton.setStyleSheet("QPushButton#refreshprocessButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 12pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#refreshprocessButton:hover{\n"
"background-color: #2da576;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.refreshprocessButton.setObjectName("refreshprocessButton")
        self.useraccountsFrame = QtWidgets.QFrame(self.centralwidget)
        self.useraccountsFrame.setGeometry(QtCore.QRect(249, 89, 781, 491))
        self.useraccountsFrame.setStyleSheet("background-color: #191a1f")
        self.useraccountsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.useraccountsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.useraccountsFrame.setObjectName("useraccountsFrame")
        self.accountsButton = QtWidgets.QPushButton(self.useraccountsFrame)
        self.accountsButton.setGeometry(QtCore.QRect(270, 400, 221, 31))
        self.accountsButton.setStyleSheet("QPushButton#accountsButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 12pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#accountsButton:hover{\n"
"background-color: #1483fe;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.accountsButton.setObjectName("accountsButton")
        self.accountsTable = QtWidgets.QTableWidget(self.useraccountsFrame)
        self.accountsTable.setGeometry(QtCore.QRect(30, 50, 711, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountsTable.sizePolicy().hasHeightForWidth())
        self.accountsTable.setSizePolicy(sizePolicy)
        self.accountsTable.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: white;\n"
"font: 10pt \"Latin Modern Sans\";")
        self.accountsTable.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.accountsTable.setRowCount(0)
        self.accountsTable.setColumnCount(8)
        self.accountsTable.setObjectName("accountsTable")
        self.accountsLabel = QtWidgets.QLabel(self.useraccountsFrame)
        self.accountsLabel.setGeometry(QtCore.QRect(350, 20, 71, 16))
        self.accountsLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(255,255,255)")
        self.accountsLabel.setObjectName("accountsLabel")
        self.accountsButton.raise_()
        self.accountsLabel.raise_()
        self.accountsTable.raise_()
        self.netconfigFrame = QtWidgets.QFrame(self.centralwidget)
        self.netconfigFrame.setGeometry(QtCore.QRect(249, 90, 781, 491))
        self.netconfigFrame.setStyleSheet("background-color: #191a1f")
        self.netconfigFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.netconfigFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.netconfigFrame.setObjectName("netconfigFrame")
        self.dhcpRadioButton = QtWidgets.QRadioButton(self.netconfigFrame)
        self.dhcpRadioButton.setGeometry(QtCore.QRect(150, 60, 231, 31))
        self.dhcpRadioButton.setStyleSheet("QRadioButton#dhcpRadioButton{\n"
"    font: 15pt \"Latin Modern Sans\";\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QRadioButton#dhcpRadioButton::indicator {\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 7px;\n"
"    background: none;\n"
"}\n"
"\n"
"QRadioButton#dhcpRadioButton::indicator::checked {\n"
"    background-color: rgb(239, 41, 41);\n"
"}\n"
"\n"
"QRadioButton#dhcpRadioButton::checked{\n"
"    color: rgb(239, 41, 41)\n"
"}")
        self.dhcpRadioButton.setIconSize(QtCore.QSize(16, 16))
        self.dhcpRadioButton.setObjectName("dhcpRadioButton")
        self.staticipFrame = QtWidgets.QFrame(self.netconfigFrame)
        self.staticipFrame.setGeometry(QtCore.QRect(180, 140, 421, 291))
        self.staticipFrame.setStyleSheet("background-color: #121318")
        self.staticipFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.staticipFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.staticipFrame.setObjectName("staticipFrame")
        self.broadcastaddressLine = QtWidgets.QLineEdit(self.staticipFrame)
        self.broadcastaddressLine.setGeometry(QtCore.QRect(180, 130, 201, 24))
        self.broadcastaddressLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.broadcastaddressLine.setText("")
        self.broadcastaddressLine.setObjectName("broadcastaddressLine")
        self.subnetmaskLine = QtWidgets.QLineEdit(self.staticipFrame)
        self.subnetmaskLine.setGeometry(QtCore.QRect(180, 80, 201, 24))
        self.subnetmaskLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.subnetmaskLine.setText("")
        self.subnetmaskLine.setObjectName("subnetmaskLine")
        self.broadcastaddressLabel = QtWidgets.QLabel(self.staticipFrame)
        self.broadcastaddressLabel.setGeometry(QtCore.QRect(30, 130, 141, 21))
        self.broadcastaddressLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(255,255,255)")
        self.broadcastaddressLabel.setObjectName("broadcastaddressLabel")
        self.ipaddressLabel = QtWidgets.QLabel(self.staticipFrame)
        self.ipaddressLabel.setGeometry(QtCore.QRect(90, 30, 81, 21))
        self.ipaddressLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(255,255,255)")
        self.ipaddressLabel.setObjectName("ipaddressLabel")
        self.ipaddressLine = QtWidgets.QLineEdit(self.staticipFrame)
        self.ipaddressLine.setGeometry(QtCore.QRect(180, 30, 201, 24))
        self.ipaddressLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.ipaddressLine.setText("")
        self.ipaddressLine.setObjectName("ipaddressLine")
        self.subnetmaskLabel = QtWidgets.QLabel(self.staticipFrame)
        self.subnetmaskLabel.setGeometry(QtCore.QRect(70, 80, 101, 21))
        self.subnetmaskLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(255,255,255)")
        self.subnetmaskLabel.setObjectName("subnetmaskLabel")
        self.setstaticipButton = QtWidgets.QPushButton(self.staticipFrame)
        self.setstaticipButton.setGeometry(QtCore.QRect(180, 230, 201, 31))
        self.setstaticipButton.setStyleSheet("QPushButton#setstaticipButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 12pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton#setstaticipButton:hover{\n"
"background-color: #c237b6;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.setstaticipButton.setObjectName("setstaticipButton")
        self.defaultgatewayLine = QtWidgets.QLineEdit(self.staticipFrame)
        self.defaultgatewayLine.setGeometry(QtCore.QRect(180, 180, 201, 24))
        self.defaultgatewayLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.defaultgatewayLine.setText("")
        self.defaultgatewayLine.setObjectName("defaultgatewayLine")
        self.defaultgatewayLabel = QtWidgets.QLabel(self.staticipFrame)
        self.defaultgatewayLabel.setGeometry(QtCore.QRect(40, 180, 121, 21))
        self.defaultgatewayLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(255,255,255)")
        self.defaultgatewayLabel.setObjectName("defaultgatewayLabel")
        self.staticipRadioButton = QtWidgets.QRadioButton(self.netconfigFrame)
        self.staticipRadioButton.setGeometry(QtCore.QRect(150, 90, 231, 31))
        self.staticipRadioButton.setStyleSheet("QRadioButton#staticipRadioButton{\n"
"    font: 15pt \"Latin Modern Sans\";\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QRadioButton#staticipRadioButton::indicator {\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 7px;\n"
"    background: none;\n"
"}\n"
"\n"
"QRadioButton#staticipRadioButton::indicator::checked {\n"
"    background-color: rgb(52, 101, 164);\n"
"}\n"
"\n"
"QRadioButton#staticipRadioButton::checked{\n"
"    color: rgb(52, 101, 164)\n"
"}")
        self.staticipRadioButton.setObjectName("staticipRadioButton")
        self.setdhcpButton = QtWidgets.QPushButton(self.netconfigFrame)
        self.setdhcpButton.setGeometry(QtCore.QRect(420, 60, 201, 31))
        self.setdhcpButton.setStyleSheet("QPushButton#setdhcpButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 12pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton#setdhcpButton:hover{\n"
"background-color: #5b37c2;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.setdhcpButton.setObjectName("setdhcpButton")
        self.sysinfoFrame = QtWidgets.QFrame(self.centralwidget)
        self.sysinfoFrame.setGeometry(QtCore.QRect(250, 90, 1441, 491))
        self.sysinfoFrame.setStyleSheet("background-color: #191a1f")
        self.sysinfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sysinfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sysinfoFrame.setObjectName("sysinfoFrame")
        self.textBrowser = QtWidgets.QTextBrowser(self.sysinfoFrame)
        self.textBrowser.setGeometry(QtCore.QRect(60, 30, 651, 431))
        self.textBrowser.setStyleSheet("background-color: rgb(8, 5, 13);\n"
"font: 75 10pt \"DejaVu Sans\";\n"
"color: rgb(211, 215, 207);")
        self.textBrowser.setObjectName("textBrowser")
        self.sysinfoFrame.raise_()
        self.sidebar.raise_()
        self.netconfigFrame.raise_()
        self.processesFrame.raise_()
        self.useraccountsFrame.raise_()
        self.dashboardFrame.raise_()
        self.header.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IGNITE"))
        self.sysnameLabel.setText(_translate("MainWindow", "IGNITE"))
        self.sysnameLabel2.setText(_translate("MainWindow", "NITE"))
        self.dashboardButton.setText(_translate("MainWindow", "  Dashboard"))
        self.processesButton.setText(_translate("MainWindow", "  Processes"))
        self.netconfigButton.setText(_translate("MainWindow", "  Network Configuration"))
        self.sysinfoButton.setText(_translate("MainWindow", "  System Information"))
        self.accountconfigButton.setText(_translate("MainWindow", "  User Accounts"))
        self.date.setText(_translate("MainWindow", "Tue Feb 11 2020"))
        self.time.setText(_translate("MainWindow", "00:24:32 PST"))
        self.runbackupButton.setText(_translate("MainWindow", "RUN BACKUP"))
        self.extractbackupButton.setText(_translate("MainWindow", "EXTRACT BACKUP"))
        self.deletebackupButton.setText(_translate("MainWindow", "DELETE BACKUP"))
        self.shutdownHeader.setText(_translate("MainWindow", "Set Shutdown Timer"))
        self.minutesbsLabel.setText(_translate("MainWindow", "Minutes before shutdown: "))
        self.notifmainLabel.setText(_translate("MainWindow", "Notification (main text):"))
        self.notifdescLabel.setText(_translate("MainWindow", "Notification (description):"))
        self.minutesLabel.setText(_translate("MainWindow", "minutes"))
        self.setshutdowntimerButton.setText(_translate("MainWindow", "SET"))
        self.deleteduplicateButton.setText(_translate("MainWindow", "DELETE DUPLICATE FILES"))
        self.killbynameButton.setText(_translate("MainWindow", "Kill Process"))
        self.killbyNamelabel.setText(_translate("MainWindow", "Kill Process by name:"))
        self.killbyPIDlabel.setText(_translate("MainWindow", "Kill Process by PID:"))
        self.killbypidButton.setText(_translate("MainWindow", "Kill PID"))
        self.refreshprocessButton.setText(_translate("MainWindow", "Refresh"))
        self.accountsButton.setText(_translate("MainWindow", "View and Export Accounts"))
        self.accountsLabel.setText(_translate("MainWindow", "Accounts"))
        self.dhcpRadioButton.setText(_translate("MainWindow", "DHCP"))
        self.broadcastaddressLabel.setText(_translate("MainWindow", "Broadcast Address:"))
        self.ipaddressLabel.setText(_translate("MainWindow", "IP Address:"))
        self.subnetmaskLabel.setText(_translate("MainWindow", "Subnet Mask:"))
        self.setstaticipButton.setText(_translate("MainWindow", "Save Configuration"))
        self.defaultgatewayLabel.setText(_translate("MainWindow", "Default Gateway:"))
        self.staticipRadioButton.setText(_translate("MainWindow", "Static IP Configuration"))
        self.setdhcpButton.setText(_translate("MainWindow", "Save Configuration"))
        self.processTable.setHorizontalHeaderLabels("USER;PID;PPID;ELAPSED;%CPU;ARGS;COMMAND".split(";"))
        self.accountsTable.setHorizontalHeaderLabels("Username;Password;Last Password Change;Minimum;Maximum;Warn;Inactive;Expire".split(";"))

    #connections
        #start sidebar buttons
        self.accountconfigButton.clicked.connect(self.showAccounts)
        self.dashboardButton.clicked.connect(self.showDashboard)
        self.netconfigButton.clicked.connect(self.showNetwork)
        self.processesButton.clicked.connect(self.showProcesses)
        self.sysinfoButton.clicked.connect(self.showSysinfo)
        #end sidebar buttons

        #start processes buttons
        self.refreshprocessButton.clicked.connect(self.processes)
        self.killbypidButton.clicked.connect(self.killByPID)
        self.killbynameButton.clicked.connect(self.killByName)
        #end processes buttons

        #start accounts button
        self.accountsButton.clicked.connect(self.exportAccounts)
        #end accounts button

    #start sidebar button clicks
    def showAccounts(self):
        self.useraccountsFrame.show()
        self.sysinfoFrame.hide()
        self.processesFrame.hide()
        self.netconfigFrame.hide()
        self.dashboardFrame.hide()

    def showDashboard(self):
        self.useraccountsFrame.hide()
        self.sysinfoFrame.hide()
        self.processesFrame.hide()
        self.netconfigFrame.hide()
        self.dashboardFrame.show()

    def showNetwork(self):
        self.useraccountsFrame.hide()
        self.sysinfoFrame.hide()
        self.processesFrame.hide()
        self.netconfigFrame.show()
        self.dashboardFrame.hide()
    
    def showProcesses(self):
        self.useraccountsFrame.hide()
        self.sysinfoFrame.hide()
        self.processesFrame.show()
        self.netconfigFrame.hide()
        self.dashboardFrame.hide()

    def showSysinfo(self):
        self.useraccountsFrame.hide()
        self.sysinfoFrame.show()
        self.processesFrame.hide()
        self.netconfigFrame.hide()
        self.dashboardFrame.hide()
    #end sidebar button clicks

    #start processes button clicks
    def processes(self):
        self.cmd = "./scripts/processes/ps.sh"
        subprocess.call(self.cmd, shell=True)

        csvfile = "ps.txt"

        with open(csvfile, 'rt') as csvfile:
            next(csvfile) #ignore header row
            reader = csv.reader(csvfile, delimiter=',')
            self.processTable.setRowCount(0)
            for row in reader:
                print(row)
                rowPosition = self.processTable.rowCount()
                self.processTable.insertRow(rowPosition)

                for i in range(len(row)):
                    self.processTable.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(row[i]))
        self.processTable.show()
        self.processTable.verticalHeader().hide()

    def killByPID(self):
        pid = str(self.killbypidLine.text())
        print(pid)
        self.cmd = "kill -9 {}".format(pid)
        subprocess.call(self.cmd, shell=True)
        self.killbypidLine.setText("")
    
    def killByName(self):
        psname = str(self.killbynameLine.text())
        self.cmd = "killall {}".format(psname)
        subprocess.call(self.cmd, shell=True)
        self.killbynameLine.setText("")
    #end processes button clicks

    #start accounts button click
    def exportAccounts(self):
        self.cmd = "./scripts/useraccounts/user_pass.sh"
        subprocess.call(self.cmd, shell=True)

        csvfile = "user_pass.txt"

        with open(csvfile, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=':')
            self.accountsTable.setRowCount(0)
            for row in reader:
                print(row)
                rowPosition = self.accountsTable.rowCount()
                self.accountsTable.insertRow(rowPosition)

                for i in range(len(row)):
                    self.accountsTable.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(row[i]))
        self.accountsTable.show()
    #end accounts button click

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.processes()
    MainWindow.show()
    sys.exit(app.exec_())
