# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainscreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 697)
        MainWindow.setMinimumSize(QtCore.QSize(1088, 697))
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topBar = QtWidgets.QFrame(self.centralwidget)
        self.topBar.setMinimumSize(QtCore.QSize(0, 100))
        self.topBar.setMaximumSize(QtCore.QSize(16777, 100))
        self.topBar.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.topBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topBar.setObjectName("topBar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.topBar)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menuTitle = QtWidgets.QFrame(self.topBar)
        self.menuTitle.setMinimumSize(QtCore.QSize(800, 30))
        self.menuTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        self.menuTitle.setStyleSheet("background-color: rgb(220, 20, 60);")
        self.menuTitle.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.menuTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuTitle.setObjectName("menuTitle")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.menuTitle)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frameMenu = QtWidgets.QFrame(self.menuTitle)
        self.frameMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMenu.setObjectName("frameMenu")
        self.titleMenu = QtWidgets.QLabel(self.frameMenu)
        self.titleMenu.setGeometry(QtCore.QRect(10, 10, 161, 19))
        self.titleMenu.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleMenu.setObjectName("titleMenu")
        self.horizontalLayout_5.addWidget(self.frameMenu)
        self.frameSection = QtWidgets.QFrame(self.menuTitle)
        self.frameSection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSection.setObjectName("frameSection")
        self.titleSection = QtWidgets.QLabel(self.frameSection)
        self.titleSection.setGeometry(QtCore.QRect(10, 10, 171, 19))
        self.titleSection.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleSection.setObjectName("titleSection")
        self.horizontalLayout_5.addWidget(self.frameSection)
        self.frameTime = QtWidgets.QFrame(self.menuTitle)
        self.frameTime.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTime.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTime.setObjectName("frameTime")
        self.titleTime = QtWidgets.QLabel(self.frameTime)
        self.titleTime.setGeometry(QtCore.QRect(10, 10, 171, 19))
        self.titleTime.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleTime.setObjectName("titleTime")
        self.horizontalLayout_5.addWidget(self.frameTime)
        self.verticalLayout_2.addWidget(self.menuTitle)
        self.Info = QtWidgets.QFrame(self.topBar)
        self.Info.setMinimumSize(QtCore.QSize(800, 60))
        self.Info.setMaximumSize(QtCore.QSize(16777215, 60))
        self.Info.setStyleSheet("background-color: rgb(254, 56, 96);")
        self.Info.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info.setObjectName("Info")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Info)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frameCount = QtWidgets.QFrame(self.Info)
        self.frameCount.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCount.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCount.setObjectName("frameCount")
        self.titleCount = QtWidgets.QLabel(self.frameCount)
        self.titleCount.setGeometry(QtCore.QRect(60, -1, 74, 31))
        self.titleCount.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleCount.setAlignment(QtCore.Qt.AlignCenter)
        self.titleCount.setObjectName("titleCount")
        self.numCount = QtWidgets.QLabel(self.frameCount)
        self.numCount.setGeometry(QtCore.QRect(60, 30, 74, 19))
        self.numCount.setStyleSheet("color: rgb(255, 255, 255);")
        self.numCount.setAlignment(QtCore.Qt.AlignCenter)
        self.numCount.setObjectName("numCount")
        self.horizontalLayout_4.addWidget(self.frameCount)
        self.frameDowntime = QtWidgets.QFrame(self.Info)
        self.frameDowntime.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDowntime.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDowntime.setObjectName("frameDowntime")
        self.titleDowntime = QtWidgets.QLabel(self.frameDowntime)
        self.titleDowntime.setGeometry(QtCore.QRect(30, -1, 141, 31))
        self.titleDowntime.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleDowntime.setAlignment(QtCore.Qt.AlignCenter)
        self.titleDowntime.setObjectName("titleDowntime")
        self.numDowntime = QtWidgets.QLabel(self.frameDowntime)
        self.numDowntime.setGeometry(QtCore.QRect(60, 30, 74, 19))
        self.numDowntime.setStyleSheet("color: rgb(255, 255, 255);")
        self.numDowntime.setAlignment(QtCore.Qt.AlignCenter)
        self.numDowntime.setObjectName("numDowntime")
        self.horizontalLayout_4.addWidget(self.frameDowntime)
        self.frameTarget = QtWidgets.QFrame(self.Info)
        self.frameTarget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTarget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTarget.setObjectName("frameTarget")
        self.titleTarget = QtWidgets.QLabel(self.frameTarget)
        self.titleTarget.setGeometry(QtCore.QRect(40, -2, 121, 31))
        self.titleTarget.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleTarget.setAlignment(QtCore.Qt.AlignCenter)
        self.titleTarget.setObjectName("titleTarget")
        self.numTarget = QtWidgets.QLabel(self.frameTarget)
        self.numTarget.setGeometry(QtCore.QRect(60, 30, 74, 19))
        self.numTarget.setStyleSheet("color: rgb(255, 255, 255);")
        self.numTarget.setAlignment(QtCore.Qt.AlignCenter)
        self.numTarget.setObjectName("numTarget")
        self.horizontalLayout_4.addWidget(self.frameTarget)
        self.frameSystem = QtWidgets.QFrame(self.Info)
        self.frameSystem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSystem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSystem.setObjectName("frameSystem")
        self.titleSystem = QtWidgets.QLabel(self.frameSystem)
        self.titleSystem.setGeometry(QtCore.QRect(20, -1, 171, 31))
        self.titleSystem.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleSystem.setAlignment(QtCore.Qt.AlignCenter)
        self.titleSystem.setObjectName("titleSystem")
        self.numSystem = QtWidgets.QLabel(self.frameSystem)
        self.numSystem.setGeometry(QtCore.QRect(70, 30, 74, 19))
        self.numSystem.setStyleSheet("color: rgb(255, 255, 255);")
        self.numSystem.setAlignment(QtCore.Qt.AlignCenter)
        self.numSystem.setObjectName("numSystem")
        self.horizontalLayout_4.addWidget(self.frameSystem)
        self.frameOEE = QtWidgets.QFrame(self.Info)
        self.frameOEE.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameOEE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameOEE.setObjectName("frameOEE")
        self.titleOEE = QtWidgets.QLabel(self.frameOEE)
        self.titleOEE.setGeometry(QtCore.QRect(70, 0, 74, 31))
        self.titleOEE.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleOEE.setAlignment(QtCore.Qt.AlignCenter)
        self.titleOEE.setObjectName("titleOEE")
        self.numOEE = QtWidgets.QLabel(self.frameOEE)
        self.numOEE.setGeometry(QtCore.QRect(70, 30, 74, 19))
        self.numOEE.setStyleSheet("color: rgb(255, 255, 255);")
        self.numOEE.setAlignment(QtCore.Qt.AlignCenter)
        self.numOEE.setObjectName("numOEE")
        self.horizontalLayout_4.addWidget(self.frameOEE)
        self.verticalLayout_2.addWidget(self.Info)
        self.verticalLayout.addWidget(self.topBar)
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sideBar = QtWidgets.QFrame(self.body)
        self.sideBar.setMinimumSize(QtCore.QSize(40, 402))
        self.sideBar.setMaximumSize(QtCore.QSize(40, 16777215))
        self.sideBar.setStyleSheet("background-color: rgb(220, 20, 60);")
        self.sideBar.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.sideBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideBar.setObjectName("sideBar")
        self.horizontalLayout.addWidget(self.sideBar)
        self.content = QtWidgets.QFrame(self.body)
        self.content.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackContentMain = QtWidgets.QStackedWidget(self.content)
        self.stackContentMain.setMinimumSize(QtCore.QSize(992, 568))
        self.stackContentMain.setObjectName("stackContentMain")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Home)
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.layoutRunning = QtWidgets.QFrame(self.Home)
        self.layoutRunning.setMinimumSize(QtCore.QSize(543, 568))
        self.layoutRunning.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.layoutRunning.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.layoutRunning.setFrameShadow(QtWidgets.QFrame.Raised)
        self.layoutRunning.setObjectName("layoutRunning")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutRunning)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frameProducts = QtWidgets.QFrame(self.layoutRunning)
        self.frameProducts.setMinimumSize(QtCore.QSize(541, 256))
        self.frameProducts.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frameProducts.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frameProducts.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameProducts.setObjectName("frameProducts")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frameProducts)
        self.horizontalLayout_6.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.stackProducts = QtWidgets.QStackedWidget(self.frameProducts)
        self.stackProducts.setMinimumSize(QtCore.QSize(537, 247))
        self.stackProducts.setObjectName("stackProducts")
        self.productPage1 = QtWidgets.QWidget()
        self.productPage1.setObjectName("productPage1")
        self.progressBar = QtWidgets.QProgressBar(self.productPage1)
        self.progressBar.setGeometry(QtCore.QRect(10, 160, 511, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.label_9 = QtWidgets.QLabel(self.productPage1)
        self.label_9.setGeometry(QtCore.QRect(10, 90, 131, 19))
        self.label_9.setStyleSheet("font: 75 12pt \"Monospace\";")
        self.label_9.setObjectName("label_9")
        self.labelRemainTime = QtWidgets.QLabel(self.productPage1)
        self.labelRemainTime.setGeometry(QtCore.QRect(380, 90, 141, 20))
        self.labelRemainTime.setStyleSheet("font: 75 12pt \"Monospace\";")
        self.labelRemainTime.setObjectName("labelRemainTime")
        self.numElapsedTime = QtWidgets.QLabel(self.productPage1)
        self.numElapsedTime.setGeometry(QtCore.QRect(10, 120, 74, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.numElapsedTime.setFont(font)
        self.numElapsedTime.setObjectName("numElapsedTime")
        self.labelTargetTime = QtWidgets.QLabel(self.productPage1)
        self.labelTargetTime.setGeometry(QtCore.QRect(380, 210, 131, 20))
        self.labelTargetTime.setObjectName("labelTargetTime")
        self.labelJobNum = QtWidgets.QLabel(self.productPage1)
        self.labelJobNum.setGeometry(QtCore.QRect(10, 0, 74, 19))
        self.labelJobNum.setObjectName("labelJobNum")
        self.labelProductName = QtWidgets.QLabel(self.productPage1)
        self.labelProductName.setGeometry(QtCore.QRect(10, 30, 74, 19))
        self.labelProductName.setObjectName("labelProductName")
        self.numRemainTime = QtWidgets.QLabel(self.productPage1)
        self.numRemainTime.setGeometry(QtCore.QRect(380, 120, 74, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.numRemainTime.setFont(font)
        self.numRemainTime.setObjectName("numRemainTime")
        self.labelCount = QtWidgets.QLabel(self.productPage1)
        self.labelCount.setGeometry(QtCore.QRect(10, 210, 111, 19))
        self.labelCount.setObjectName("labelCount")
        self.labelExtraTime = QtWidgets.QLabel(self.productPage1)
        self.labelExtraTime.setGeometry(QtCore.QRect(380, 20, 121, 20))
        self.labelExtraTime.setStyleSheet("color: rgb(204, 0, 0);\n"
"font: 75 14pt \"Monospace\";")
        self.labelExtraTime.setObjectName("labelExtraTime")
        self.numExtraTime = QtWidgets.QLabel(self.productPage1)
        self.numExtraTime.setGeometry(QtCore.QRect(380, 50, 74, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.numExtraTime.setFont(font)
        self.numExtraTime.setStyleSheet("color: rgb(204, 0, 0);\n"
"font: 75 24pt \"Monospace\";")
        self.numExtraTime.setObjectName("numExtraTime")
        self.stackProducts.addWidget(self.productPage1)
        self.pageProduct2 = QtWidgets.QWidget()
        self.pageProduct2.setObjectName("pageProduct2")
        self.stackProducts.addWidget(self.pageProduct2)
        self.horizontalLayout_6.addWidget(self.stackProducts)
        self.verticalLayout_3.addWidget(self.frameProducts)
        self.frameBroadcast = QtWidgets.QFrame(self.layoutRunning)
        self.frameBroadcast.setMinimumSize(QtCore.QSize(541, 305))
        self.frameBroadcast.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frameBroadcast.setAutoFillBackground(False)
        self.frameBroadcast.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frameBroadcast.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frameBroadcast.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBroadcast.setObjectName("frameBroadcast")
        self.titleBroadcast = QtWidgets.QLabel(self.frameBroadcast)
        self.titleBroadcast.setGeometry(QtCore.QRect(140, 10, 221, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titleBroadcast.setFont(font)
        self.titleBroadcast.setStyleSheet("background-color: rgb(194, 105, 105);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px\n"
"")
        self.titleBroadcast.setScaledContents(False)
        self.titleBroadcast.setAlignment(QtCore.Qt.AlignCenter)
        self.titleBroadcast.setWordWrap(True)
        self.titleBroadcast.setObjectName("titleBroadcast")
        self.prductSub_3 = QtWidgets.QPushButton(self.frameBroadcast)
        self.prductSub_3.setGeometry(QtCore.QRect(380, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.prductSub_3.setFont(font)
        self.prductSub_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 171, 247);\n"
"    border-radius:15px;\n"
"    border: none;\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-left: 1 px solid rgb(32, 74, 135);\n"
"    border-right: 1px solid rgb(32, 74, 135);\n"
"    border-bottom: 1px solid rgb(32, 74, 135);\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(90, 210, 255);\n"
"    border-left: 1 px solid rgb(32, 74, 135);\n"
"    border-right: 1px solid rgb(32, 74, 135);\n"
"    border-bottom: 1px solid rgb(32, 74, 135);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"\n"
"    background-color: rgb(52, 101, 164);\n"
"    border-left: 1 px solid rgb(32, 74, 135);\n"
"    border-right: 1px solid rgb(32, 74, 135);\n"
"    border-top: 1px solid rgb(32, 74, 135);\n"
"}")
        self.prductSub_3.setObjectName("prductSub_3")
        self.treeParts = QtWidgets.QTreeWidget(self.frameBroadcast)
        self.treeParts.setGeometry(QtCore.QRect(20, 100, 461, 191))
        self.treeParts.setObjectName("treeParts")
        self.treeParts.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.treeParts.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeParts)
        self.lineInfo = QtWidgets.QLineEdit(self.frameBroadcast)
        self.lineInfo.setGeometry(QtCore.QRect(50, 50, 311, 31))
        self.lineInfo.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"border-radius: 15px;")
        self.lineInfo.setText("")
        self.lineInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lineInfo.setObjectName("lineInfo")
        self.verticalLayout_3.addWidget(self.frameBroadcast)
        self.horizontalLayout_3.addWidget(self.layoutRunning)
        self.layoutActions = QtWidgets.QFrame(self.Home)
        self.layoutActions.setMinimumSize(QtCore.QSize(475, 516))
        self.layoutActions.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.layoutActions.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.layoutActions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.layoutActions.setObjectName("layoutActions")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutActions)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frameInfo = QtWidgets.QFrame(self.layoutActions)
        self.frameInfo.setMinimumSize(QtCore.QSize(0, 310))
        self.frameInfo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frameInfo.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frameInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInfo.setObjectName("frameInfo")
        self.lineProductName = QtWidgets.QLineEdit(self.frameInfo)
        self.lineProductName.setGeometry(QtCore.QRect(40, 50, 311, 31))
        self.lineProductName.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"border-radius: 15px;")
        self.lineProductName.setText("")
        self.lineProductName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineProductName.setObjectName("lineProductName")
        self.lineUnits = QtWidgets.QLineEdit(self.frameInfo)
        self.lineUnits.setGeometry(QtCore.QRect(40, 110, 311, 31))
        self.lineUnits.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"border-radius: 15px;")
        self.lineUnits.setText("")
        self.lineUnits.setAlignment(QtCore.Qt.AlignCenter)
        self.lineUnits.setObjectName("lineUnits")
        self.btnProductSub = QtWidgets.QPushButton(self.frameInfo)
        self.btnProductSub.setGeometry(QtCore.QRect(360, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnProductSub.setFont(font)
        self.btnProductSub.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 171, 247);\n"
"    border-radius:15px;\n"
"    border: none;\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-left: 1 px solid rgb(32, 74, 135);\n"
"    border-right: 1px solid rgb(32, 74, 135);\n"
"    border-bottom: 1px solid rgb(32, 74, 135);\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(90, 210, 255);\n"
"    border-left: 1 px solid rgb(32, 74, 135);\n"
"    border-right: 1px solid rgb(32, 74, 135);\n"
"    border-bottom: 1px solid rgb(32, 74, 135);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"\n"
"    background-color: rgb(52, 101, 164);\n"
"    border-left-color: 1 px solid rgb(32, 74, 135);\n"
"    border-right-color: 1px solid rgb(32, 74, 135);\n"
"    border-top: 1px solid rgb(32, 74, 135);\n"
"}")
        self.btnProductSub.setObjectName("btnProductSub")
        self.btnUnitsSub = QtWidgets.QPushButton(self.frameInfo)
        self.btnUnitsSub.setGeometry(QtCore.QRect(360, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnUnitsSub.setFont(font)
        self.btnUnitsSub.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 171, 247);\n"
"    border-radius:15px;\n"
"    border: none;\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-left: 1 px solid rgb(32, 74, 135);\n"
"    border-right: 1px solid rgb(32, 74, 135);\n"
"    border-bottom: 1px solid rgb(32, 74, 135);\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(90, 210, 255);\n"
"    border-left: 1 px solid rgb(32, 74, 135);\n"
"    border-right: 1px solid rgb(32, 74, 135);\n"
"    border-bottom: 1px solid rgb(32, 74, 135);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"\n"
"    background-color: rgb(52, 101, 164);\n"
"    border-left-color: 1 px solid rgb(32, 74, 135);\n"
"    border-right-color: 1px solid rgb(32, 74, 135);\n"
"    border-top: 1px solid rgb(32, 74, 135);\n"
"}")
        self.btnUnitsSub.setObjectName("btnUnitsSub")
        self.labelInfoTopic = QtWidgets.QLabel(self.frameInfo)
        self.labelInfoTopic.setGeometry(QtCore.QRect(110, 10, 251, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelInfoTopic.setFont(font)
        self.labelInfoTopic.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(194, 105, 105);\n"
"border-radius: 5px;")
        self.labelInfoTopic.setScaledContents(False)
        self.labelInfoTopic.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfoTopic.setWordWrap(True)
        self.labelInfoTopic.setObjectName("labelInfoTopic")
        self.labelBarcode = QtWidgets.QLabel(self.frameInfo)
        self.labelBarcode.setGeometry(QtCore.QRect(40, 230, 311, 41))
        self.labelBarcode.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"border: 1px solid rgb(239, 41, 41);\n"
"border-radius: 15px;")
        self.labelBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBarcode.setObjectName("labelBarcode")
        self.lineTime = QtWidgets.QLineEdit(self.frameInfo)
        self.lineTime.setGeometry(QtCore.QRect(40, 170, 311, 31))
        self.lineTime.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"border-radius: 15px;")
        self.lineTime.setText("")
        self.lineTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lineTime.setObjectName("lineTime")
        self.btnTime = QtWidgets.QPushButton(self.frameInfo)
        self.btnTime.setGeometry(QtCore.QRect(360, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnTime.setFont(font)
        self.btnTime.setStyleSheet("QPushButton{\n"
"    background-color: rgb(38, 171, 247);\n"
"    border-radius:15px;\n"
"    border: none;\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-left: 1 px solid rgb(32, 74, 135);\n"
"    border-right: 1px solid rgb(32, 74, 135);\n"
"    border-bottom: 1px solid rgb(32, 74, 135);\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(90, 210, 255);\n"
"    border-left: 1 px solid rgb(32, 74, 135);\n"
"    border-right: 1px solid rgb(32, 74, 135);\n"
"    border-bottom: 1px solid rgb(32, 74, 135);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"\n"
"    background-color: rgb(52, 101, 163);\n"
"    border-left-color: 1 px solid rgb(32, 74, 135);\n"
"    border-right-color: 1px solid rgb(32, 74, 135);\n"
"    border-top: 1px solid rgb(32, 74, 135);\n"
"}")
        self.btnTime.setObjectName("btnTime")
        self.verticalLayout_4.addWidget(self.frameInfo)
        self.frameAction = QtWidgets.QFrame(self.layoutActions)
        self.frameAction.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frameAction.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frameAction.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAction.setObjectName("frameAction")
        self.titleAction = QtWidgets.QLabel(self.frameAction)
        self.titleAction.setGeometry(QtCore.QRect(120, 10, 221, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titleAction.setFont(font)
        self.titleAction.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(194, 105, 105);\n"
"border-radius: 5px;")
        self.titleAction.setScaledContents(False)
        self.titleAction.setAlignment(QtCore.Qt.AlignCenter)
        self.titleAction.setWordWrap(True)
        self.titleAction.setObjectName("titleAction")
        self.btnStart = QtWidgets.QPushButton(self.frameAction)
        self.btnStart.setGeometry(QtCore.QRect(240, 100, 221, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(14)
        self.btnStart.setFont(font)
        self.btnStart.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(181, 205, 77);\n"
"    border-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(252, 175, 62);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color: rgb(206, 92, 0);\n"
"}")
        self.btnStart.setObjectName("btnStart")
        self.btnHold = QtWidgets.QPushButton(self.frameAction)
        self.btnHold.setGeometry(QtCore.QRect(40, 180, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(14)
        self.btnHold.setFont(font)
        self.btnHold.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(237, 212, 0);\n"
"    border-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    \n"
"    background-color: rgb(252, 233, 79);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    \n"
"    background-color: rgb(196, 160, 0);\n"
"}")
        self.btnHold.setObjectName("btnHold")
        self.btnStop = QtWidgets.QPushButton(self.frameAction)
        self.btnStop.setGeometry(QtCore.QRect(270, 180, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(14)
        self.btnStop.setFont(font)
        self.btnStop.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    background-color: rgb(239, 41, 41);\n"
"    border-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    \n"
"    background-color: rgb(194, 105, 105);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    \n"
"    background-color: rgb(164, 0, 0);\n"
"}")
        self.btnStop.setObjectName("btnStop")
        self.btnCon = QtWidgets.QPushButton(self.frameAction)
        self.btnCon.setGeometry(QtCore.QRect(10, 100, 221, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCon.sizePolicy().hasHeightForWidth())
        self.btnCon.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(14)
        self.btnCon.setFont(font)
        self.btnCon.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(181, 205, 77);\n"
"    border-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(252, 175, 62);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color: rgb(206, 92, 0);\n"
"}")
        self.btnCon.setFlat(False)
        self.btnCon.setObjectName("btnCon")
        self.verticalLayout_4.addWidget(self.frameAction)
        self.horizontalLayout_3.addWidget(self.layoutActions)
        self.stackContentMain.addWidget(self.Home)
        self.pageProducts = QtWidgets.QWidget()
        self.pageProducts.setObjectName("pageProducts")
        self.tableWidget = QtWidgets.QTableWidget(self.pageProducts)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 600, 300))
        self.tableWidget.setMinimumSize(QtCore.QSize(600, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.stackContentMain.addWidget(self.pageProducts)
        self.horizontalLayout_2.addWidget(self.stackContentMain, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.content)
        self.verticalLayout.addWidget(self.body)
        self.bottomBar = QtWidgets.QFrame(self.centralwidget)
        self.bottomBar.setMinimumSize(QtCore.QSize(0, 15))
        self.bottomBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bottomBar.setStyleSheet("background-color: rgb(220, 20, 60);")
        self.bottomBar.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.bottomBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomBar.setObjectName("bottomBar")
        self.verticalLayout.addWidget(self.bottomBar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackContentMain.setCurrentIndex(0)
        self.stackProducts.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleMenu.setText(_translate("MainWindow", "Page: TSSC Home"))
        self.titleSection.setText(_translate("MainWindow", "Section: Mid Assembly"))
        self.titleTime.setText(_translate("MainWindow", "Date and Time"))
        self.titleCount.setText(_translate("MainWindow", "Count"))
        self.numCount.setText(_translate("MainWindow", "0"))
        self.titleDowntime.setText(_translate("MainWindow", "Total Downtime"))
        self.numDowntime.setText(_translate("MainWindow", "0m"))
        self.titleTarget.setText(_translate("MainWindow", "Target Units"))
        self.numTarget.setText(_translate("MainWindow", "0"))
        self.titleSystem.setText(_translate("MainWindow", "System Utilization"))
        self.numSystem.setText(_translate("MainWindow", "0%"))
        self.titleOEE.setText(_translate("MainWindow", "OEE"))
        self.numOEE.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Elapsed Time"))
        self.labelRemainTime.setText(_translate("MainWindow", "Remaining Time"))
        self.numElapsedTime.setText(_translate("MainWindow", "0m"))
        self.labelTargetTime.setText(_translate("MainWindow", "Target Time : 0m"))
        self.labelJobNum.setText(_translate("MainWindow", "Job No. :"))
        self.labelProductName.setText(_translate("MainWindow", "Product: "))
        self.numRemainTime.setText(_translate("MainWindow", "0m"))
        self.labelCount.setText(_translate("MainWindow", "Unit Count: "))
        self.labelExtraTime.setText(_translate("MainWindow", "Extra Time"))
        self.numExtraTime.setText(_translate("MainWindow", "0m"))
        self.titleBroadcast.setText(_translate("MainWindow", "Broadcast Section"))
        self.prductSub_3.setText(_translate("MainWindow", "Submit"))
        self.treeParts.headerItem().setText(0, _translate("MainWindow", "Parts"))
        self.treeParts.headerItem().setText(1, _translate("MainWindow", "No. of Units"))
        __sortingEnabled = self.treeParts.isSortingEnabled()
        self.treeParts.setSortingEnabled(False)
        self.treeParts.topLevelItem(0).setText(0, _translate("MainWindow", "Compressor"))
        self.treeParts.topLevelItem(0).setText(1, _translate("MainWindow", "10"))
        self.treeParts.setSortingEnabled(__sortingEnabled)
        self.lineInfo.setPlaceholderText(_translate("MainWindow", "Add Information"))
        self.lineProductName.setPlaceholderText(_translate("MainWindow", "Enter Product Name"))
        self.lineUnits.setPlaceholderText(_translate("MainWindow", "Enter Target Units"))
        self.btnProductSub.setText(_translate("MainWindow", "Submit"))
        self.btnUnitsSub.setText(_translate("MainWindow", "Submit"))
        self.labelInfoTopic.setText(_translate("MainWindow", "Add Information Section"))
        self.labelBarcode.setText(_translate("MainWindow", "Barcode not detected"))
        self.lineTime.setPlaceholderText(_translate("MainWindow", "Enter Target Time"))
        self.btnTime.setText(_translate("MainWindow", "Submit"))
        self.titleAction.setText(_translate("MainWindow", "Action Section"))
        self.btnStart.setText(_translate("MainWindow", "Start Production"))
        self.btnHold.setText(_translate("MainWindow", "Hold"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.btnCon.setText(_translate("MainWindow", "Continue"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Job No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Units"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Barcode"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
