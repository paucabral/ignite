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
import logging
import threading
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 576)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 576))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 576))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/logo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QScrollBar::horizontal{\n"
"    border: 1px solid;\n"
"    background: #32CC99;\n"
"    height: 15px;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"    background: rgb(46, 52, 54);\n"
"    min-width: 0px;\n"
"    min-height:0px;\n"
"    border-radius: 20px;\n"
"}")
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
        self.netconfigButton.setGeometry(QtCore.QRect(10, 220, 231, 41))
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
        self.sysinfoButton.setGeometry(QtCore.QRect(10, 320, 231, 41))
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
        self.accountcreationButton = QtWidgets.QPushButton(self.sidebar)
        self.accountcreationButton.setGeometry(QtCore.QRect(10, 170, 231, 41))
        self.accountcreationButton.setStyleSheet("QPushButton#accountcreationButton{\n"
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
"QPushButton#accountcreationButton:hover{\n"
"background-color: #1d1c23;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assets/sidebar_buttons/accountcreation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accountcreationButton.setIcon(icon6)
        self.accountcreationButton.setIconSize(QtCore.QSize(18, 18))
        self.accountcreationButton.setObjectName("accountcreationButton")
        self.remotetoolsButton = QtWidgets.QPushButton(self.sidebar)
        self.remotetoolsButton.setGeometry(QtCore.QRect(10, 270, 231, 41))
        self.remotetoolsButton.setStyleSheet("QPushButton#remotetoolsButton{\n"
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
"QPushButton#remotetoolsButton:hover{\n"
"background-color: #1d1c23;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("assets/sidebar_buttons/remotetools.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remotetoolsButton.setIcon(icon7)
        self.remotetoolsButton.setIconSize(QtCore.QSize(18, 18))
        self.remotetoolsButton.setObjectName("remotetoolsButton")
        self.dashboardButton.raise_()
        self.processesButton.raise_()
        self.netconfigButton.raise_()
        self.accountconfigButton.raise_()
        self.sysinfoButton.raise_()
        self.accountcreationButton.raise_()
        self.remotetoolsButton.raise_()
        self.dashboardFrame = QtWidgets.QFrame(self.centralwidget)
        self.dashboardFrame.setGeometry(QtCore.QRect(250, 90, 781, 491))
        self.dashboardFrame.setStyleSheet("background-color: #191a1f")
        self.dashboardFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dashboardFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dashboardFrame.setObjectName("dashboardFrame")
        self.clock = QtWidgets.QFrame(self.dashboardFrame)
        self.clock.setGeometry(QtCore.QRect(20, 20, 421, 171))
        self.clock.setStyleSheet("background-color: #121318")
        self.clock.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.clock.setFrameShadow(QtWidgets.QFrame.Raised)
        self.clock.setObjectName("clock")
        self.date = QtWidgets.QLabel(self.clock)
        self.date.setGeometry(QtCore.QRect(20, 10, 391, 61))
        self.date.setStyleSheet("font: 36pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.date.setObjectName("date")
        self.time = QtWidgets.QLabel(self.clock)
        self.time.setGeometry(QtCore.QRect(50, 80, 331, 61))
        self.time.setStyleSheet("font: 38pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.time.setObjectName("time")
        self.calendar = QtWidgets.QFrame(self.dashboardFrame)
        self.calendar.setGeometry(QtCore.QRect(460, 20, 291, 171))
        self.calendar.setStyleSheet("background-color: #121318")
        self.calendar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calendar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calendar.setObjectName("calendar")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.calendar)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 0, 272, 171))
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
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.killbyNamelabel.setObjectName("killbyNamelabel")
        self.processTable = QtWidgets.QTableWidget(self.processesFrame)
        self.processTable.setGeometry(QtCore.QRect(30, 60, 711, 311))
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
"background-color: #191a1f;\n"
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
        self.uptimeLabel = QtWidgets.QLabel(self.processesFrame)
        self.uptimeLabel.setGeometry(QtCore.QRect(140, 20, 61, 31))
        self.uptimeLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"font-weight: bold;\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.uptimeLabel.setObjectName("uptimeLabel")
        self.uptimeDynamicLabel = QtWidgets.QLabel(self.processesFrame)
        self.uptimeDynamicLabel.setGeometry(QtCore.QRect(210, 30, 441, 21))
        self.uptimeDynamicLabel.setStyleSheet("font: 13pt \"Latin Modern Sans\";\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.uptimeDynamicLabel.setObjectName("uptimeDynamicLabel")
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
        self.staticipFrame.setGeometry(QtCore.QRect(180, 130, 421, 321))
        self.staticipFrame.setStyleSheet("background-color: #121318")
        self.staticipFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.staticipFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.staticipFrame.setObjectName("staticipFrame")
        self.broadcastaddressLine = QtWidgets.QLineEdit(self.staticipFrame)
        self.broadcastaddressLine.setGeometry(QtCore.QRect(180, 170, 201, 24))
        self.broadcastaddressLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.broadcastaddressLine.setText("")
        self.broadcastaddressLine.setObjectName("broadcastaddressLine")
        self.subnetmaskLine = QtWidgets.QLineEdit(self.staticipFrame)
        self.subnetmaskLine.setGeometry(QtCore.QRect(180, 120, 201, 24))
        self.subnetmaskLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.subnetmaskLine.setText("")
        self.subnetmaskLine.setObjectName("subnetmaskLine")
        self.broadcastaddressLabel = QtWidgets.QLabel(self.staticipFrame)
        self.broadcastaddressLabel.setGeometry(QtCore.QRect(30, 160, 141, 21))
        self.broadcastaddressLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(255,255,255)")
        self.broadcastaddressLabel.setObjectName("broadcastaddressLabel")
        self.ipaddressLabel = QtWidgets.QLabel(self.staticipFrame)
        self.ipaddressLabel.setGeometry(QtCore.QRect(90, 70, 81, 21))
        self.ipaddressLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(255,255,255)")
        self.ipaddressLabel.setObjectName("ipaddressLabel")
        self.ipaddressLine = QtWidgets.QLineEdit(self.staticipFrame)
        self.ipaddressLine.setGeometry(QtCore.QRect(180, 70, 201, 24))
        self.ipaddressLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.ipaddressLine.setText("")
        self.ipaddressLine.setObjectName("ipaddressLine")
        self.subnetmaskLabel = QtWidgets.QLabel(self.staticipFrame)
        self.subnetmaskLabel.setGeometry(QtCore.QRect(70, 120, 101, 21))
        self.subnetmaskLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(255,255,255)")
        self.subnetmaskLabel.setObjectName("subnetmaskLabel")
        self.setstaticipButton = QtWidgets.QPushButton(self.staticipFrame)
        self.setstaticipButton.setGeometry(QtCore.QRect(180, 270, 201, 31))
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
        self.defaultgatewayLine.setGeometry(QtCore.QRect(180, 220, 201, 24))
        self.defaultgatewayLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.defaultgatewayLine.setText("")
        self.defaultgatewayLine.setObjectName("defaultgatewayLine")
        self.defaultgatewayLabel = QtWidgets.QLabel(self.staticipFrame)
        self.defaultgatewayLabel.setGeometry(QtCore.QRect(40, 220, 121, 21))
        self.defaultgatewayLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(255,255,255)")
        self.defaultgatewayLabel.setObjectName("defaultgatewayLabel")
        self.sinterfaceLine = QtWidgets.QLineEdit(self.staticipFrame)
        self.sinterfaceLine.setGeometry(QtCore.QRect(180, 20, 201, 24))
        self.sinterfaceLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.sinterfaceLine.setText("")
        self.sinterfaceLine.setObjectName("sinterfaceLine")
        self.sinterfaceLabel = QtWidgets.QLabel(self.staticipFrame)
        self.sinterfaceLabel.setGeometry(QtCore.QRect(100, 20, 71, 21))
        self.sinterfaceLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(255,255,255)")
        self.sinterfaceLabel.setObjectName("sinterfaceLabel")
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
        self.setdhcpButton.setGeometry(QtCore.QRect(530, 60, 151, 31))
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
        self.dinterfaceLabel = QtWidgets.QLabel(self.netconfigFrame)
        self.dinterfaceLabel.setGeometry(QtCore.QRect(260, 60, 71, 31))
        self.dinterfaceLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(255,255,255)")
        self.dinterfaceLabel.setObjectName("dinterfaceLabel")
        self.dinterfaceLine = QtWidgets.QLineEdit(self.netconfigFrame)
        self.dinterfaceLine.setGeometry(QtCore.QRect(340, 60, 161, 31))
        self.dinterfaceLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.dinterfaceLine.setText("")
        self.dinterfaceLine.setObjectName("dinterfaceLine")
        self.sysinfoFrame = QtWidgets.QFrame(self.centralwidget)
        self.sysinfoFrame.setGeometry(QtCore.QRect(250, 90, 1441, 491))
        self.sysinfoFrame.setStyleSheet("background-color: #191a1f")
        self.sysinfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sysinfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sysinfoFrame.setObjectName("sysinfoFrame")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.sysinfoFrame)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 30, 711, 431))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(8, 5, 13);\n"
"color: rgb(211, 215, 207);\n"
"font: 10pt \"Courier 10 Pitch\";")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.accountcreationFrame = QtWidgets.QFrame(self.centralwidget)
        self.accountcreationFrame.setGeometry(QtCore.QRect(250, 90, 781, 491))
        self.accountcreationFrame.setStyleSheet("background-color: #191a1f")
        self.accountcreationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accountcreationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accountcreationFrame.setObjectName("accountcreationFrame")
        self.createuseraccountLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.createuseraccountLabel.setGeometry(QtCore.QRect(30, 10, 201, 31))
        self.createuseraccountLabel.setStyleSheet("font: 16pt \"Latin Modern Sans\";\n"
"font-weight: bold;\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.createuseraccountLabel.setObjectName("createuseraccountLabel")
        self.usernameLine = QtWidgets.QLineEdit(self.accountcreationFrame)
        self.usernameLine.setGeometry(QtCore.QRect(120, 40, 221, 31))
        self.usernameLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.usernameLine.setObjectName("usernameLine")
        self.usernameLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.usernameLabel.setGeometry(QtCore.QRect(30, 40, 81, 31))
        self.usernameLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLine = QtWidgets.QLineEdit(self.accountcreationFrame)
        self.passwordLine.setGeometry(QtCore.QRect(120, 80, 221, 31))
        self.passwordLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.passwordLine.setObjectName("passwordLine")
        self.passwordLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.passwordLabel.setGeometry(QtCore.QRect(30, 80, 81, 31))
        self.passwordLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.passwordLabel.setObjectName("passwordLabel")
        self.mprimarygroupLine = QtWidgets.QLineEdit(self.accountcreationFrame)
        self.mprimarygroupLine.setGeometry(QtCore.QRect(170, 220, 171, 31))
        self.mprimarygroupLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.mprimarygroupLine.setObjectName("mprimarygroupLine")
        self.modifyuseraccountLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.modifyuseraccountLabel.setGeometry(QtCore.QRect(30, 150, 201, 31))
        self.modifyuseraccountLabel.setStyleSheet("font: 16pt \"Latin Modern Sans\";\n"
"font-weight: bold;\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.modifyuseraccountLabel.setObjectName("modifyuseraccountLabel")
        self.musernameLine = QtWidgets.QLineEdit(self.accountcreationFrame)
        self.musernameLine.setGeometry(QtCore.QRect(170, 180, 171, 31))
        self.musernameLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.musernameLine.setObjectName("musernameLine")
        self.musernameLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.musernameLabel.setGeometry(QtCore.QRect(30, 180, 81, 31))
        self.musernameLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.musernameLabel.setObjectName("musernameLabel")
        self.mprimarygroupLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.mprimarygroupLabel.setGeometry(QtCore.QRect(30, 220, 111, 31))
        self.mprimarygroupLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.mprimarygroupLabel.setObjectName("mprimarygroupLabel")
        self.msecondarygroupLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.msecondarygroupLabel.setGeometry(QtCore.QRect(30, 260, 131, 31))
        self.msecondarygroupLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.msecondarygroupLabel.setObjectName("msecondarygroupLabel")
        self.msecondarygroupLine = QtWidgets.QLineEdit(self.accountcreationFrame)
        self.msecondarygroupLine.setGeometry(QtCore.QRect(170, 260, 171, 31))
        self.msecondarygroupLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.msecondarygroupLine.setObjectName("msecondarygroupLine")
        self.eusernameLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.eusernameLabel.setGeometry(QtCore.QRect(30, 360, 81, 31))
        self.eusernameLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.eusernameLabel.setObjectName("eusernameLabel")
        self.eusernameLine = QtWidgets.QLineEdit(self.accountcreationFrame)
        self.eusernameLine.setGeometry(QtCore.QRect(170, 360, 171, 31))
        self.eusernameLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.eusernameLine.setObjectName("eusernameLine")
        self.setaccountexpiryLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.setaccountexpiryLabel.setGeometry(QtCore.QRect(30, 330, 201, 31))
        self.setaccountexpiryLabel.setStyleSheet("font: 16pt \"Latin Modern Sans\";\n"
"font-weight: bold;\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.setaccountexpiryLabel.setObjectName("setaccountexpiryLabel")
        self.edateLine = QtWidgets.QLineEdit(self.accountcreationFrame)
        self.edateLine.setGeometry(QtCore.QRect(170, 400, 171, 31))
        self.edateLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.edateLine.setObjectName("edateLine")
        self.edateLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.edateLabel.setGeometry(QtCore.QRect(30, 400, 121, 31))
        self.edateLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.edateLabel.setObjectName("edateLabel")
        self.creategroupLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.creategroupLabel.setGeometry(QtCore.QRect(420, 10, 201, 31))
        self.creategroupLabel.setStyleSheet("font: 16pt \"Latin Modern Sans\";\n"
"font-weight: bold;\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.creategroupLabel.setObjectName("creategroupLabel")
        self.createuseraccountButton = QtWidgets.QPushButton(self.accountcreationFrame)
        self.createuseraccountButton.setGeometry(QtCore.QRect(140, 120, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.createuseraccountButton.setFont(font)
        self.createuseraccountButton.setStyleSheet("QPushButton#createuseraccountButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 10pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#createuseraccountButton:hover{\n"
"background-color: #1483fe;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.createuseraccountButton.setObjectName("createuseraccountButton")
        self.modifyuseraccountButton = QtWidgets.QPushButton(self.accountcreationFrame)
        self.modifyuseraccountButton.setGeometry(QtCore.QRect(140, 300, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.modifyuseraccountButton.setFont(font)
        self.modifyuseraccountButton.setStyleSheet("QPushButton#modifyuseraccountButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 10pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#modifyuseraccountButton:hover{\n"
"background-color: rgb(150, 20, 30);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.modifyuseraccountButton.setObjectName("modifyuseraccountButton")
        self.setexpiryButton = QtWidgets.QPushButton(self.accountcreationFrame)
        self.setexpiryButton.setGeometry(QtCore.QRect(140, 440, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.setexpiryButton.setFont(font)
        self.setexpiryButton.setStyleSheet("QPushButton#setexpiryButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 10pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#setexpiryButton:hover{\n"
"background-color: rgb(117, 80, 123);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.setexpiryButton.setObjectName("setexpiryButton")
        self.groupnameLine = QtWidgets.QLineEdit(self.accountcreationFrame)
        self.groupnameLine.setGeometry(QtCore.QRect(530, 40, 201, 31))
        self.groupnameLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.groupnameLine.setObjectName("groupnameLine")
        self.groupnameLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.groupnameLabel.setGeometry(QtCore.QRect(420, 40, 101, 31))
        self.groupnameLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.groupnameLabel.setObjectName("groupnameLabel")
        self.creategroupButton = QtWidgets.QPushButton(self.accountcreationFrame)
        self.creategroupButton.setGeometry(QtCore.QRect(530, 80, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.creategroupButton.setFont(font)
        self.creategroupButton.setStyleSheet("QPushButton#creategroupButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 10pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#creategroupButton:hover{\n"
"background-color: rgb(78, 154, 6);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.creategroupButton.setObjectName("creategroupButton")
        self.userinfoLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.userinfoLabel.setGeometry(QtCore.QRect(480, 120, 161, 31))
        self.userinfoLabel.setStyleSheet("font: 16pt \"Latin Modern Sans\";\n"
"font-weight: bold;\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.userinfoLabel.setObjectName("userinfoLabel")
        self.iusernameLine = QtWidgets.QLineEdit(self.accountcreationFrame)
        self.iusernameLine.setGeometry(QtCore.QRect(470, 160, 161, 31))
        self.iusernameLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.iusernameLine.setObjectName("iusernameLine")
        self.iusernameLabel = QtWidgets.QLabel(self.accountcreationFrame)
        self.iusernameLabel.setGeometry(QtCore.QRect(380, 160, 81, 31))
        self.iusernameLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #191a1f;\n"
"color: rgb(255,255,255)")
        self.iusernameLabel.setObjectName("iusernameLabel")
        self.userinfoButton = QtWidgets.QPushButton(self.accountcreationFrame)
        self.userinfoButton.setGeometry(QtCore.QRect(650, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.userinfoButton.setFont(font)
        self.userinfoButton.setStyleSheet("QPushButton#userinfoButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 10pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#userinfoButton:hover{\n"
"background-color: #1483fe;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.userinfoButton.setObjectName("userinfoButton")
        self.userinfoTextEdit = QtWidgets.QPlainTextEdit(self.accountcreationFrame)
        self.userinfoTextEdit.setGeometry(QtCore.QRect(380, 200, 361, 261))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.userinfoTextEdit.setFont(font)
        self.userinfoTextEdit.setStyleSheet("background-color: rgb(8, 5, 13);\n"
"color: rgb(211, 215, 207);\n"
"font: 10pt \"Courier 10 Pitch\";")
        self.userinfoTextEdit.setPlainText("")
        self.userinfoTextEdit.setObjectName("userinfoTextEdit")
        self.remotetoolsFrame = QtWidgets.QFrame(self.centralwidget)
        self.remotetoolsFrame.setGeometry(QtCore.QRect(250, 90, 781, 491))
        self.remotetoolsFrame.setStyleSheet("background-color: #191a1f")
        self.remotetoolsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.remotetoolsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.remotetoolsFrame.setObjectName("remotetoolsFrame")
        self.remoteShutdown = QtWidgets.QFrame(self.remotetoolsFrame)
        self.remoteShutdown.setGeometry(QtCore.QRect(20, 210, 361, 191))
        self.remoteShutdown.setStyleSheet("background-color: #121318")
        self.remoteShutdown.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.remoteShutdown.setFrameShadow(QtWidgets.QFrame.Raised)
        self.remoteShutdown.setObjectName("remoteShutdown")
        self.remoteshutdownHeader = QtWidgets.QLabel(self.remoteShutdown)
        self.remoteshutdownHeader.setGeometry(QtCore.QRect(20, 10, 211, 21))
        self.remoteshutdownHeader.setStyleSheet("font: 16pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.remoteshutdownHeader.setObjectName("remoteshutdownHeader")
        self.remoteminutesbsLabel = QtWidgets.QLabel(self.remoteShutdown)
        self.remoteminutesbsLabel.setGeometry(QtCore.QRect(20, 40, 191, 16))
        self.remoteminutesbsLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.remoteminutesbsLabel.setObjectName("remoteminutesbsLabel")
        self.remotenotifmainLabel = QtWidgets.QLabel(self.remoteShutdown)
        self.remotenotifmainLabel.setGeometry(QtCore.QRect(20, 70, 191, 16))
        self.remotenotifmainLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.remotenotifmainLabel.setObjectName("remotenotifmainLabel")
        self.remotenotifdescLabel = QtWidgets.QLabel(self.remoteShutdown)
        self.remotenotifdescLabel.setGeometry(QtCore.QRect(20, 100, 191, 21))
        self.remotenotifdescLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.remotenotifdescLabel.setObjectName("remotenotifdescLabel")
        self.remoteminutesLine = QtWidgets.QLineEdit(self.remoteShutdown)
        self.remoteminutesLine.setGeometry(QtCore.QRect(210, 40, 61, 24))
        self.remoteminutesLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.remoteminutesLine.setObjectName("remoteminutesLine")
        self.remotenotifmainLine = QtWidgets.QLineEdit(self.remoteShutdown)
        self.remotenotifmainLine.setGeometry(QtCore.QRect(210, 70, 131, 24))
        self.remotenotifmainLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.remotenotifmainLine.setObjectName("remotenotifmainLine")
        self.remotenotifdescLine = QtWidgets.QLineEdit(self.remoteShutdown)
        self.remotenotifdescLine.setGeometry(QtCore.QRect(210, 100, 131, 24))
        self.remotenotifdescLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.remotenotifdescLine.setObjectName("remotenotifdescLine")
        self.remoteminutesLabel = QtWidgets.QLabel(self.remoteShutdown)
        self.remoteminutesLabel.setGeometry(QtCore.QRect(280, 40, 61, 16))
        self.remoteminutesLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.remoteminutesLabel.setObjectName("remoteminutesLabel")
        self.remotesetshutdowntimerButton = QtWidgets.QPushButton(self.remoteShutdown)
        self.remotesetshutdowntimerButton.setGeometry(QtCore.QRect(20, 140, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.remotesetshutdowntimerButton.setFont(font)
        self.remotesetshutdowntimerButton.setStyleSheet("QPushButton#remotesetshutdowntimerButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 12pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#remotesetshutdowntimerButton:hover{\n"
"background-color: #c237b6;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.remotesetshutdowntimerButton.setObjectName("remotesetshutdowntimerButton")
        self.remoteHost = QtWidgets.QFrame(self.remotetoolsFrame)
        self.remoteHost.setGeometry(QtCore.QRect(20, 30, 361, 161))
        self.remoteHost.setStyleSheet("background-color: #121318")
        self.remoteHost.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.remoteHost.setFrameShadow(QtWidgets.QFrame.Raised)
        self.remoteHost.setObjectName("remoteHost")
        self.remotehostHeader = QtWidgets.QLabel(self.remoteHost)
        self.remotehostHeader.setGeometry(QtCore.QRect(20, 10, 161, 21))
        self.remotehostHeader.setStyleSheet("font: 16pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.remotehostHeader.setObjectName("remotehostHeader")
        self.remoteaccountLabel = QtWidgets.QLabel(self.remoteHost)
        self.remoteaccountLabel.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.remoteaccountLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.remoteaccountLabel.setObjectName("remoteaccountLabel")
        self.remoteipaddressLabel = QtWidgets.QLabel(self.remoteHost)
        self.remoteipaddressLabel.setGeometry(QtCore.QRect(20, 70, 91, 21))
        self.remoteipaddressLabel.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.remoteipaddressLabel.setObjectName("remoteipaddressLabel")
        self.remoteipaddressLine = QtWidgets.QLineEdit(self.remoteHost)
        self.remoteipaddressLine.setGeometry(QtCore.QRect(120, 70, 221, 24))
        self.remoteipaddressLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.remoteipaddressLine.setObjectName("remoteipaddressLine")
        self.establishsshButton = QtWidgets.QPushButton(self.remoteHost)
        self.establishsshButton.setGeometry(QtCore.QRect(20, 110, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.establishsshButton.setFont(font)
        self.establishsshButton.setStyleSheet("QPushButton#establishsshButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 12pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#establishsshButton:hover{\n"
"background-color: #c237b6;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.establishsshButton.setObjectName("establishsshButton")
        self.remoteaccountLine = QtWidgets.QLineEdit(self.remoteHost)
        self.remoteaccountLine.setGeometry(QtCore.QRect(120, 40, 221, 24))
        self.remoteaccountLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.remoteaccountLine.setObjectName("remoteaccountLine")
        self.remotedeletebackupButton = QtWidgets.QPushButton(self.remotetoolsFrame)
        self.remotedeletebackupButton.setGeometry(QtCore.QRect(280, 420, 101, 31))
        self.remotedeletebackupButton.setStyleSheet("QPushButton#remotedeletebackupButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 7.5pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#remotedeletebackupButton:hover{\n"
"background-color: #e1184d;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.remotedeletebackupButton.setObjectName("remotedeletebackupButton")
        self.remoteextractbackupButton = QtWidgets.QPushButton(self.remotetoolsFrame)
        self.remoteextractbackupButton.setGeometry(QtCore.QRect(150, 420, 101, 31))
        self.remoteextractbackupButton.setStyleSheet("QPushButton#remoteextractbackupButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 7.5pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#remoteextractbackupButton:hover{\n"
"background-color: #2da576;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.remoteextractbackupButton.setObjectName("remoteextractbackupButton")
        self.remoterunbackupButton = QtWidgets.QPushButton(self.remotetoolsFrame)
        self.remoterunbackupButton.setGeometry(QtCore.QRect(20, 420, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.remoterunbackupButton.setFont(font)
        self.remoterunbackupButton.setStyleSheet("QPushButton#remoterunbackupButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 7.5pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#remoterunbackupButton:hover{\n"
"background-color: #1483fe;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.remoterunbackupButton.setObjectName("remoterunbackupButton")
        self.availabledevicesHeader = QtWidgets.QLabel(self.remotetoolsFrame)
        self.availabledevicesHeader.setGeometry(QtCore.QRect(400, 10, 161, 31))
        self.availabledevicesHeader.setStyleSheet("font: 16pt \"Latin Modern Sans\";\n"
"color: rgb(211, 215, 207)")
        self.availabledevicesHeader.setObjectName("availabledevicesHeader")
        self.hostsTable = QtWidgets.QTableWidget(self.remotetoolsFrame)
        self.hostsTable.setGeometry(QtCore.QRect(400, 50, 351, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hostsTable.sizePolicy().hasHeightForWidth())
        self.hostsTable.setSizePolicy(sizePolicy)
        self.hostsTable.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: white;\n"
"font: 10pt \"Latin Modern Sans\";")
        self.hostsTable.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.hostsTable.setRowCount(0)
        self.hostsTable.setColumnCount(3)
        self.hostsTable.setObjectName("hostsTable")
        self.hostinformationTextEdit = QtWidgets.QPlainTextEdit(self.remotetoolsFrame)
        self.hostinformationTextEdit.setGeometry(QtCore.QRect(400, 260, 351, 201))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.hostinformationTextEdit.setFont(font)
        self.hostinformationTextEdit.setStyleSheet("background-color: rgb(8, 5, 13);\n"
"color: rgb(211, 215, 207);\n"
"font: 10pt \"Courier 10 Pitch\";")
        self.hostinformationTextEdit.setPlainText("")
        self.hostinformationTextEdit.setObjectName("hostinformationTextEdit")
        self.searchhostsButton = QtWidgets.QPushButton(self.remotetoolsFrame)
        self.searchhostsButton.setGeometry(QtCore.QRect(680, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.searchhostsButton.setFont(font)
        self.searchhostsButton.setStyleSheet("QPushButton#searchhostsButton{\n"
"background-color: rgb(136, 138, 133);\n"
"font: 87 9pt \"Latin Modern Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#searchhostsButton:hover{\n"
"background-color: #c237b6;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.searchhostsButton.setObjectName("searchhostsButton")
        self.interfaceLine = QtWidgets.QLineEdit(self.remotetoolsFrame)
        self.interfaceLine.setGeometry(QtCore.QRect(560, 10, 111, 31))
        self.interfaceLine.setStyleSheet("font: 12pt \"Latin Modern Sans\";\n"
"background-color: #212025;\n"
"color: rgb(255,255,255)")
        self.interfaceLine.setObjectName("interfaceLine")
        self.useraccountsFrame.raise_()
        self.sysinfoFrame.raise_()
        self.sidebar.raise_()
        self.accountcreationFrame.raise_()
        self.processesFrame.raise_()
        self.remotetoolsFrame.raise_()
        self.netconfigFrame.raise_()
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
        self.accountcreationButton.setText(_translate("MainWindow", "  Account Creation"))
        self.remotetoolsButton.setText(_translate("MainWindow", "  Remote Tools"))
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
        self.uptimeLabel.setText(_translate("MainWindow", "Uptime:"))
        self.uptimeDynamicLabel.setText(_translate("MainWindow", "11:34:26 up 24 min,  1 user,  load average: 0.67, 0.99, 0.82"))
        self.accountsButton.setText(_translate("MainWindow", "View and Export Accounts"))
        self.accountsLabel.setText(_translate("MainWindow", "Accounts"))
        self.dhcpRadioButton.setText(_translate("MainWindow", "DHCP"))
        self.broadcastaddressLabel.setText(_translate("MainWindow", "Broadcast Address:"))
        self.ipaddressLabel.setText(_translate("MainWindow", "IP Address:"))
        self.subnetmaskLabel.setText(_translate("MainWindow", "Subnet Mask:"))
        self.setstaticipButton.setText(_translate("MainWindow", "Save Configuration"))
        self.defaultgatewayLabel.setText(_translate("MainWindow", "Default Gateway:"))
        self.sinterfaceLabel.setText(_translate("MainWindow", "Interface:"))
        self.staticipRadioButton.setText(_translate("MainWindow", "Static IP Configuration"))
        self.setdhcpButton.setText(_translate("MainWindow", "Save Configuration"))
        self.dinterfaceLabel.setText(_translate("MainWindow", "Interface:"))
        self.createuseraccountLabel.setText(_translate("MainWindow", "Create User Account"))
        self.usernameLabel.setText(_translate("MainWindow", "Username:"))
        self.passwordLabel.setText(_translate("MainWindow", "Password:"))
        self.modifyuseraccountLabel.setText(_translate("MainWindow", "Modify User Account"))
        self.musernameLabel.setText(_translate("MainWindow", "Username:"))
        self.mprimarygroupLabel.setText(_translate("MainWindow", "Primary Group:"))
        self.msecondarygroupLabel.setText(_translate("MainWindow", "Secondary Group:"))
        self.eusernameLabel.setText(_translate("MainWindow", "Username:"))
        self.setaccountexpiryLabel.setText(_translate("MainWindow", "Set Account Expiry"))
        self.edateLabel.setText(_translate("MainWindow", "Expiration Date:"))
        self.creategroupLabel.setText(_translate("MainWindow", "Create Group"))
        self.createuseraccountButton.setText(_translate("MainWindow", "SAVE"))
        self.modifyuseraccountButton.setText(_translate("MainWindow", "SAVE"))
        self.setexpiryButton.setText(_translate("MainWindow", "SET"))
        self.groupnameLabel.setText(_translate("MainWindow", "Group Name:"))
        self.creategroupButton.setText(_translate("MainWindow", "SAVE"))
        self.userinfoLabel.setText(_translate("MainWindow", "User Information"))
        self.iusernameLabel.setText(_translate("MainWindow", "Username:"))
        self.userinfoButton.setText(_translate("MainWindow", "Search"))
        self.remoteshutdownHeader.setText(_translate("MainWindow", "Set Shutdown Timer"))
        self.remoteminutesbsLabel.setText(_translate("MainWindow", "Minutes before shutdown: "))
        self.remotenotifmainLabel.setText(_translate("MainWindow", "Notification (main text):"))
        self.remotenotifdescLabel.setText(_translate("MainWindow", "Notification (description):"))
        self.remoteminutesLabel.setText(_translate("MainWindow", "minutes"))
        self.remotesetshutdowntimerButton.setText(_translate("MainWindow", "SET"))
        self.remotehostHeader.setText(_translate("MainWindow", "Remote Host"))
        self.remoteaccountLabel.setText(_translate("MainWindow", "Account:"))
        self.remoteipaddressLabel.setText(_translate("MainWindow", "IP Address:"))
        self.establishsshButton.setText(_translate("MainWindow", "ESTABLISH SSH CONNECTION"))
        self.remotedeletebackupButton.setText(_translate("MainWindow", "DELETE BACKUP"))
        self.remoteextractbackupButton.setText(_translate("MainWindow", "EXTRACT BACKUP"))
        self.remoterunbackupButton.setText(_translate("MainWindow", "RUN BACKUP"))
        self.availabledevicesHeader.setText(_translate("MainWindow", "Recogized Hosts"))
        self.searchhostsButton.setText(_translate("MainWindow", "SEARCH"))

#Succedding lines from this point are now manual code. Include all imports from above!
    #sysinfo and accountcreation read only display
        self.plainTextEdit.setReadOnly(True)
        self.userinfoTextEdit.setReadOnly(True)
    #Table headers
        self.processTable.setHorizontalHeaderLabels("USER;PID;PPID;ELAPSED;%CPU;ARGS;COMMAND".split(";"))
        self.accountsTable.setHorizontalHeaderLabels("Username;Password;Last Password Change;Minimum;Maximum;Warn;Inactive;Expire".split(";"))
        self.disksTable.setHorizontalHeaderLabels("Filesystem;Size;Used;Available;Use%;Mounted".split(";"))
        self.hostsTable.setHorizontalHeaderLabels("IP Address;MAC Address;Hostname".split(";"))
    
    #place holder texts
        self.msecondarygroupLine.setPlaceholderText("Grp1,Grp2,Grp3,...")
        self.edateLine.setPlaceholderText("YYYY-MM-DD")
        self.ipaddressLine.setPlaceholderText("0.0.0.0")
        self.subnetmaskLine.setPlaceholderText("0.0.0.0")
        self.defaultgatewayLine.setPlaceholderText("0.0.0.0")
        self.broadcastaddressLine.setPlaceholderText("0.0.0.0")
        self.interfaceLine.setPlaceholderText("Enter interface")

    #connections
        #start sidebar buttons
        self.accountconfigButton.clicked.connect(self.showAccounts)
        self.dashboardButton.clicked.connect(self.showDashboard)
        self.netconfigButton.clicked.connect(self.showNetwork)
        self.processesButton.clicked.connect(self.showProcesses)
        self.sysinfoButton.clicked.connect(self.showSysinfo)
        self.accountcreationButton.clicked.connect(self.showAccountCreation)
        self.remotetoolsButton.clicked.connect(self.showRemoteTools)
        #end sidebar buttons

        #start processes buttons
        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.processes)
        self.refreshprocessButton.clicked.connect(self.processes)
        self.killbypidButton.clicked.connect(self.killByPID)
        self.killbynameButton.clicked.connect(self.killByName)
        self.timer3 = QtCore.QTimer()
        self.timer3.timeout.connect(self.uptime)
        #end processes buttons

        #start accounts button
        self.accountsButton.clicked.connect(self.exportAccounts)
        #end accounts button

        #start dashboard items
        self.deleteduplicateButton.clicked.connect(self.deleteDuplicates)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.currentTime)
        self.setshutdowntimerButton.clicked.connect(self.setShutdown)
        self.runbackupButton.clicked.connect(self.runBackup)
        self.extractbackupButton.clicked.connect(self.extractBackup)
        self.deletebackupButton.clicked.connect(self.deleteBackup)
        #end dashboard items

        #start network items
        self.dhcpRadioButton.clicked.connect(self.dhcpSettings)
        self.staticipRadioButton.clicked.connect(self.staticipSettings)
        self.setdhcpButton.clicked.connect(self.saveDhcp)
        self.setstaticipButton.clicked.connect(self.saveStaticip)
        #end network items

        #start account creation buttons
        self.userinfoButton.clicked.connect(self.userInfo)
        self.createuseraccountButton.clicked.connect(self.createUser)
        self.modifyuseraccountButton.clicked.connect(self.modifyUser)
        self.setexpiryButton.clicked.connect(self.setExpiry)
        self.creategroupButton.clicked.connect(self.createGroup)
        #end account creation buttons

        #start remotetools buttons
        self.searchhostsButton.clicked.connect(self.showHosts)
        self.establishsshButton.clicked.connect(self.establishSSH)
        self.remotesetshutdowntimerButton.clicked.connect(self.remoteShutdownTimer)
        self.remoterunbackupButton.clicked.connect(self.remoteRunBackup)
        self.remoteextractbackupButton.clicked.connect(self.remoteExtractBackup)
        self.remotedeletebackupButton.clicked.connect(self.remoteDeleteBackup)
        #end remotetools buttons 

    #start sidebar button clicks
    def showAccounts(self):
        self.useraccountsFrame.show()
        self.sysinfoFrame.hide()
        self.processesFrame.hide()
        self.netconfigFrame.hide()
        self.dashboardFrame.hide()
        self.accountcreationFrame.hide()
        self.remotetoolsFrame.hide()

    def showDashboard(self):
        self.useraccountsFrame.hide()
        self.sysinfoFrame.hide()
        self.processesFrame.hide()
        self.netconfigFrame.hide()
        self.dashboardFrame.show()
        self.accountcreationFrame.hide()
        self.remotetoolsFrame.hide()

    def showNetwork(self):
        self.useraccountsFrame.hide()
        self.sysinfoFrame.hide()
        self.processesFrame.hide()
        self.netconfigFrame.show()
        self.dashboardFrame.hide()
        self.accountcreationFrame.hide()
        self.remotetoolsFrame.hide()
    
    def showProcesses(self):
        self.useraccountsFrame.hide()
        self.sysinfoFrame.hide()
        self.processesFrame.show()
        self.netconfigFrame.hide()
        self.dashboardFrame.hide()
        self.accountcreationFrame.hide()
        self.accountcreationFrame.hide()
        self.remotetoolsFrame.hide()

    def showSysinfo(self):
        self.useraccountsFrame.hide()
        self.sysinfoFrame.show()
        self.processesFrame.hide()
        self.netconfigFrame.hide()
        self.dashboardFrame.hide()
        self.accountcreationFrame.hide()
        self.remotetoolsFrame.hide()
    
    def showAccountCreation(self):
        self.useraccountsFrame.hide()
        self.sysinfoFrame.hide()
        self.processesFrame.hide()
        self.netconfigFrame.hide()
        self.dashboardFrame.hide()
        self.accountcreationFrame.show()
        self.remotetoolsFrame.hide()

    def showRemoteTools(self):
        self.remotetoolsFrame.show()
        self.useraccountsFrame.hide()
        self.sysinfoFrame.hide()
        self.processesFrame.hide()
        self.netconfigFrame.hide()
        self.dashboardFrame.hide()
        self.accountcreationFrame.hide()
    #end sidebar button clicks

    #start accountcreation button clicks
    def accountNotif(self, msg, username):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Notification")
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.exec()

    def userInfo(self):
        name = self.iusernameLine.text()
        self.cmd = "./scripts/createaccounts/accountinfo.sh {}".format(name)
        subprocess.call(self.cmd, shell=True)
        sysfile = "userinfo.txt"
        with open(sysfile, 'rt') as txtfile:
            systemI = txtfile.read()
            self.userinfoTextEdit.setPlainText(systemI)

    def createUser(self):
        username = self.usernameLine.text()
        password = self.passwordLine.text()
        self.cmd = "./scripts/createaccounts/createaccounts.sh {} {}".format(username, password)
        subprocess.call(self.cmd, shell=True)
        self.usernameLine.setText("")
        self.passwordLine.setText("")
        
        msg = "User account for {} was successfully created.".format(username)
        self.accountNotif(msg, username)

    def modifyUser(self):
        username = self.musernameLine.text()
        pgroup = self.mprimarygroupLine.text()
        sgroup = self.msecondarygroupLine.text()
        self.cmd = "./scripts/createaccounts/modifyaccounts.sh {} {} {}".format(username, pgroup, sgroup)
        subprocess.call(self.cmd, shell=True)
        self.musernameLine.setText("")
        self.mprimarygroupLine.setText("")
        self.msecondarygroupLine.setText("")

        msg = "User account {} was modified successfully.".format(username)
        self.accountNotif(msg, username)
    
    def setExpiry(self):
        username = self.eusernameLine.text()
        date = self.edateLine.text()
        self.cmd = "./scripts/createaccounts/setaccountexpiry.sh {} {}".format(username, date)
        subprocess.call(self.cmd, shell=True)
        self.eusernameLine.setText("")
        self.edateLine.setText("")

        msg = "User account {} will now expire on {}.".format(username, date)
        self.accountNotif(msg, username)

    def createGroup(self):
        groupname = self.groupnameLine.text()
        self.cmd = "./scripts/createaccounts/creategroup.sh {}".format(groupname)
        subprocess.call(self.cmd, shell=True)
        self.groupnameLine.setText("")

        msg = "The group {} was successfully created.".format(groupname)
        self.accountNotif(msg, groupname)
        
    #end accountcreation button clicks

    #start processes button clicks
    def processesNotif(self, msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Notification")
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.exec()

    def processes(self):
        self.timer2.start(1000)
        self.cmd = "./scripts/processes/ps.sh"
        subprocess.call(self.cmd, shell=True)

        csvfile = "ps.txt"

        with open(csvfile, 'rt') as csvfile:
            next(csvfile) #ignore header row
            reader = csv.reader(csvfile, delimiter=',')
            self.processTable.setRowCount(0)
            for row in reader:
                rowPosition = self.processTable.rowCount()
                self.processTable.insertRow(rowPosition)

                for i in range(len(row)):
                    self.processTable.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(row[i]))
        self.processTable.show()
        self.processTable.verticalHeader().hide()

    def uptime(self):
        self.timer3.start(1000)
        self.cmd = "./scripts/processes/uptime.sh"
        subprocess.call(self.cmd, shell=True)
        
        txtfile = "uptime.txt"
        
        with open(txtfile, 'rt') as txtfile:
            updatedUptime = txtfile.readline()
            self.uptimeDynamicLabel.setText(updatedUptime)

    def killByPID(self):
        pid = str(self.killbypidLine.text())
        print(pid)
        self.cmd = "kill -9 {}".format(pid)
        subprocess.call(self.cmd, shell=True)
        self.killbypidLine.setText("")

        msg = "Process ID: {} was successfully terminated".format(pid)
        self.processesNotif(msg)
    
    def killByName(self):
        psname = str(self.killbynameLine.text())
        self.cmd = "killall {}".format(psname)
        subprocess.call(self.cmd, shell=True)
        self.killbynameLine.setText("")

        msg = "{} was successfully terminated".format(psname)
        self.processesNotif(msg)
    #end processes button clicks

    #start accounts button click
    def exportNotif(self, msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Notification")
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.exec()

    def exportAccounts(self):
        self.cmd = "./scripts/useraccounts/user_pass.sh"
        subprocess.call(self.cmd, shell=True)

        csvfile = "user_pass.txt"
        txtfile = "user_pass.txt"

        with open(csvfile, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=':')
            self.accountsTable.setRowCount(0)
            for row in reader:
                rowPosition = self.accountsTable.rowCount()
                self.accountsTable.insertRow(rowPosition)

                for i in range(len(row)):
                    self.accountsTable.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(row[i]))
        self.accountsTable.show()

        msg = "Comma separated values (CSV) text file for accounts list was exported to {}".format(txtfile)
        self.exportNotif(msg)
    #end accounts button click

    #start dashboard items
    def dashboardNotif(self, msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Notification")
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.exec()

    def displayDisks(self):
        self.cmd = "./scripts/dashboard/diskspace.sh"
        subprocess.call(self.cmd, shell=True)

        csvfile = "diskspace.txt"

        with open(csvfile, 'rt') as csvfile:
            next(csvfile)
            reader = csv.reader(csvfile, delimiter=',')
            self.disksTable.setRowCount(0)
            for row in reader:
                rowPosition = self.disksTable.rowCount()
                self.disksTable.insertRow(rowPosition)

                for i in range(len(row)):
                    self.disksTable.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(row[i]))
        self.disksTable.show()

    def deleteDuplicates(self):
        self.cmd = "./scripts/dashboard/duplicates.sh"
        subprocess.call(self.cmd, shell=True)
        
        msg = "Duplicate files from home directory are now being deleted."
        self.dashboardNotif(msg)

    def currentDate(self):
        self.cmd = "./scripts/dashboard/currentdate.sh"
        subprocess.call(self.cmd, shell=True)

        datefile = "date.txt"

        with open(datefile, 'rt') as txtfile:
            updatedDate = txtfile.read()
            self.date.setText(updatedDate)
    
    def currentTime(self):
        self.timer.start(1000)
        self.cmd = "./scripts/dashboard/currenttime.sh"
        subprocess.call(self.cmd, shell=True)

        timefile = "time.txt"

        with open(timefile, 'rt') as txtfile:
            updatedTime = txtfile.read()
            self.time.setText(updatedTime)

    def setShutdown(self):
        minutes = str(self.minutesLine.text())
        main = str(self.notifmainLine.text())
        desc = str(self.notifdescLine.text())

        self.cmd = "./scripts/dashboard/shutdowntimer.sh {} '{}' '{}'".format(minutes, main, desc)
        subprocess.call(self.cmd, shell=True)
        self.minutesLine.setText("")
        self.notifmainLine.setText("")
        self.notifdescLine.setText("")

        msg = "A shutdown timer of {} was set.".format(minutes)
        shutBox = QtWidgets.QMessageBox()
        shutBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        shutBox.setWindowTitle("Alert!")
        shutBox.setText(msg)
        shutBox.setIcon(QtWidgets.QMessageBox.Warning)

        if shutBox.exec_() == QtWidgets.QMessageBox.Cancel:
            self.cmd = "shutdown -c"
            subprocess.call(self.cmd, shell=True)
        else:
            pass
        
    def runBackup(self):
        self.cmd = "./scripts/dashboard/backup.sh 1"
        subprocess.call(self.cmd, shell=True)

        msg = "Backup is now running in the background."
        self.dashboardNotif(msg)
    
    def extractBackup(self):
        self.cmd = "./scripts/dashboard/backup.sh 2"
        subprocess.call(self.cmd, shell=True)

        msg = "Backup archive is being extracted in the background."
        self.dashboardNotif(msg)
    
    def deleteBackup(self):
        self.cmd = "./scripts/dashboard/backup.sh 3"
        subprocess.call(self.cmd, shell=True)

        msg = "Backup archive is now deleted."
        self.dashboardNotif(msg)

    #end dashboard items

    #start sysinfo items
    def sysInfo(self):
        self.cmd = "./scripts/sysinfo/sysinfo.sh"
        subprocess.call(self.cmd, shell=True)
        sysfile = "system.txt"
        with open(sysfile, 'rt') as txtfile:
            systemI = txtfile.read()
            self.plainTextEdit.setPlainText(systemI)
    #end sysinfo items

    #start networkconfig items
    def networkNotif(self, msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Notification")
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.exec()

    def dhcpSettings(self):
        self.staticipFrame.hide()
        self.dinterfaceLine.show()
        self.dinterfaceLabel.show()
        self.setdhcpButton.show()

    def staticipSettings(self):
        self.staticipFrame.show()
        self.setdhcpButton.hide()
        self.dinterfaceLine.hide()
        self.dinterfaceLabel.hide()
    
    def saveDhcp(self):
        dinterface = str(self.dinterfaceLine.text())
        self.cmd = "./scripts/networkconfig/dhcp.sh {}".format(dinterface)
        subprocess.call(self.cmd, shell=True)
        
        msg = "DHCP settings on {} is now configured.".format(dinterface)
        self.networkNotif(msg)
        self.dinterfaceLine.setText("")

    def saveStaticip(self):
        ip = str(self.ipaddressLine.text())
        sm = str(self.subnetmaskLine.text())
        ba = str(self.broadcastaddressLine.text())
        dg = str(self.defaultgatewayLine.text())
        sinterface = str(self.sinterfaceLine.text())
        
        self.cmd = "./scripts/networkconfig/staticipconfig.sh {} {} {} {} {}".format(ip, sm, ba, dg, sinterface)
        subprocess.call(self.cmd, shell=True)

        self.ipaddressLine.setText("")
        self.subnetmaskLine.setText("")
        self.broadcastaddressLine.setText("")
        self.defaultgatewayLine.setText("")
        self.sinterfaceLine.setText("")

        msg = "IP Address: {} was assigned successfuly on {}.".format(ip, sinterface)
        self.networkNotif(msg)

    #end networkconfig items

    #start remotetool items
    def remoteNotif(self, msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Notification")
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.exec()

    def showHosts(self):
        interface = str(self.interfaceLine.text())

        self.cmd = "./scripts/remotetools/recognizedhosts.sh {}".format(interface)
        subprocess.call(self.cmd, shell=True)

        csvfile = "recognized_hosts.txt"

        with open(csvfile, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            self.hostsTable.setRowCount(0)
            for row in reader:
                rowPosition = self.hostsTable.rowCount()
                self.hostsTable.insertRow(rowPosition)

                for i in range(len(row)):
                    self.hostsTable.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(row[i]))
        self.hostsTable.show()
        self.interfaceLine.setText("")

    def establishSSH(self):
        remoteAccount = str(self.remoteaccountLine.text())
        remoteIP = str(self.remoteipaddressLine.text())

        if remoteAccount == "":
            pass

        else:
            self.cmd = "./scripts/remotetools/saveaccount.sh {}".format(remoteAccount)
            subprocess.call(self.cmd, shell=True)
            
            self.cmd = "./scripts/remotetools/saveip.sh {}".format(remoteIP)
            subprocess.call(self.cmd, shell=True)
            
            msg = "SSH settings saved successfully. You may now use the tools below."
            self.remoteNotif(msg)

        self.remoteaccountLine.setText("")
        self.remoteipaddressLine.setText("")

    def remoteShutdownTimer(self):
        try:
            txtfileA = "remoteaccount.txt"
            with open(txtfileA, 'rt') as txtfileA:
                remoteaccount = txtfileA.readline().splitlines()[0]
        
            txtfileB = "remoteip.txt"
            with open(txtfileB, 'rt') as txtfileB:
                remoteip = txtfileB.readline().splitlines()[0]
        
            rminutes = str(self.remoteminutesLine.text())
            rmain = str(self.remotenotifmainLine.text())
            rdesc = str(self.remotenotifdescLine.text())
        

            if rminutes == "" or rmain == "" or rdesc == "":
                pass
            else:
                script = "scripts/remotetools/remoteshutdowntimer.sh {} '{}' '{}'".format(rminutes, rmain, rdesc)

                self.cmd = "ssh {}@{} \'bash -s\' < {}".format(remoteaccount, remoteip, script)
                print(self.cmd)
                subprocess.call(self.cmd, shell=True)

                msg = "A shutdown timer of {} minute was set for {}.".format(rminutes, remoteip)
                shutBox = QtWidgets.QMessageBox()
                shutBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                shutBox.setWindowTitle("Alert!")
                shutBox.setText(msg)
                shutBox.setIcon(QtWidgets.QMessageBox.Warning)

                if shutBox.exec_() == QtWidgets.QMessageBox.Cancel:
                    self.cmd = "ssh {}@{} -t 'shutdown -c'".format(remoteaccount, remoteip)
                    subprocess.call(self.cmd, shell=True)
                else:
                    pass
        except:
            pass
        
        self.remoteminutesLine.setText("")
        self.remotenotifmainLine.setText("")
        self.remotenotifdescLine.setText("")

    def remoteRunBackup(self):
        try:
            txtfileA = "remoteaccount.txt"
            with open(txtfileA, 'rt') as txtfileA:
                remoteaccount = txtfileA.readline().splitlines()[0]
        
            txtfileB = "remoteip.txt"
            with open(txtfileB, 'rt') as txtfileB:
                remoteip = txtfileB.readline().splitlines()[0]
                
            script = "scripts/remotetools/remotebackup.sh 1"
            self.cmd = "ssh {}@{} \'bash -s\' < {}".format(remoteaccount, remoteip, script)
            subprocess.call(self.cmd, shell=True)
                
            msg = "Backup is currently running on {}".format(remoteip)
            self.remoteNotif(msg)

        except:
            pass
        
    def remoteExtractBackup(self):
        try:
            txtfileA = "remoteaccount.txt"
            with open(txtfileA, 'rt') as txtfileA:
                remoteaccount = txtfileA.readline().splitlines()[0]
        
            txtfileB = "remoteip.txt"
            with open(txtfileB, 'rt') as txtfileB:
                remoteip = txtfileB.readline().splitlines()[0]
                
            script = "scripts/remotetools/remotebackup.sh 2"
            self.cmd = "ssh {}@{} \'bash -s\' < {}".format(remoteaccount, remoteip, script)
            subprocess.call(self.cmd, shell=True)
                
            msg = "Backup archive on {} is currently being extracted.".format(remoteip)
            self.remoteNotif(msg)

        except:
            pass

    def remoteDeleteBackup(self):
        try:
            txtfileA = "remoteaccount.txt"
            with open(txtfileA, 'rt') as txtfileA:
                remoteaccount = txtfileA.readline().splitlines()[0]
        
            txtfileB = "remoteip.txt"
            with open(txtfileB, 'rt') as txtfileB:
                remoteip = txtfileB.readline().splitlines()[0]
                
            script = "scripts/remotetools/remotebackup.sh 3"
            self.cmd = "ssh {}@{} \'bash -s\' < {}".format(remoteaccount, remoteip, script)
            subprocess.call(self.cmd, shell=True)
                
            msg = "Backup archived on {} is being deleted".format(remoteip)
            self.remoteNotif(msg)

        except:
            pass

    #end remotetool items


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.processes()
    ui.uptime()
    ui.displayDisks()
    ui.currentDate()
    ui.currentTime()
    ui.sysInfo()
    ui.staticipFrame.hide()
    ui.setdhcpButton.hide()
    ui.dinterfaceLine.hide()
    ui.dinterfaceLabel.hide()
    ui.userinfoTextEdit.setPlainText("")
    
    MainWindow.show()
    sys.exit(app.exec_())
