# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 880, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(620, 110, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_show = QtWidgets.QLabel(self.centralwidget)
        self.label_show.setGeometry(QtCore.QRect(400, 760, 400, 80))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_show.setFont(font)
        self.label_show.setStyleSheet("")
        self.label_show.setText("")
        self.label_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show.setOpenExternalLinks(False)
        self.label_show.setObjectName("label_show")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 71, 31))
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(120, 160, 1051, 31))
        self.groupBox.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.rb_1 = QtWidgets.QRadioButton(self.groupBox)
        self.rb_1.setGeometry(QtCore.QRect(10, 10, 201, 19))
        self.rb_1.setObjectName("rb_1")
        self.rb_2 = QtWidgets.QRadioButton(self.groupBox)
        self.rb_2.setGeometry(QtCore.QRect(240, 10, 131, 19))
        self.rb_2.setObjectName("rb_2")
        self.rb_3 = QtWidgets.QRadioButton(self.groupBox)
        self.rb_3.setGeometry(QtCore.QRect(400, 10, 115, 19))
        self.rb_3.setObjectName("rb_3")
        self.rb_4 = QtWidgets.QRadioButton(self.groupBox)
        self.rb_4.setGeometry(QtCore.QRect(520, 10, 181, 19))
        self.rb_4.setObjectName("rb_4")
        self.rb_5 = QtWidgets.QRadioButton(self.groupBox)
        self.rb_5.setGeometry(QtCore.QRect(720, 10, 111, 19))
        self.rb_5.setObjectName("rb_5")
        self.rb_6 = QtWidgets.QRadioButton(self.groupBox)
        self.rb_6.setGeometry(QtCore.QRect(860, 10, 171, 19))
        self.rb_6.setObjectName("rb_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 210, 321, 31))
        self.groupBox_2.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.rb_7 = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_7.setGeometry(QtCore.QRect(10, 10, 121, 19))
        self.rb_7.setObjectName("rb_7")
        self.rb_9 = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_9.setGeometry(QtCore.QRect(240, 10, 61, 19))
        self.rb_9.setObjectName("rb_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 71, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 110, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(415, 20, 370, 60))
        self.textBrowser.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 269, 71, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 269, 71, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 279, 21, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(480, 279, 21, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(360, 269, 71, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(590, 269, 71, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(710, 269, 21, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 330, 71, 21))
        self.label_12.setObjectName("label_12")
        self.cb_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_1.setGeometry(QtCore.QRect(130, 330, 21, 19))
        self.cb_1.setText("")
        self.cb_1.setChecked(False)
        self.cb_1.setObjectName("cb_1")
        self.cb_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_2.setGeometry(QtCore.QRect(150, 330, 131, 19))
        self.cb_2.setChecked(False)
        self.cb_2.setObjectName("cb_2")
        self.cb_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_4.setGeometry(QtCore.QRect(320, 330, 61, 19))
        self.cb_4.setChecked(False)
        self.cb_4.setObjectName("cb_4")
        self.cb_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_3.setGeometry(QtCore.QRect(300, 330, 21, 19))
        self.cb_3.setText("")
        self.cb_3.setChecked(False)
        self.cb_3.setObjectName("cb_3")
        self.cb_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_5.setGeometry(QtCore.QRect(440, 330, 21, 19))
        self.cb_5.setText("")
        self.cb_5.setChecked(False)
        self.cb_5.setObjectName("cb_5")
        self.cb_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_6.setGeometry(QtCore.QRect(460, 330, 161, 19))
        self.cb_6.setChecked(False)
        self.cb_6.setObjectName("cb_6")
        self.cb_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_7.setGeometry(QtCore.QRect(620, 330, 21, 19))
        self.cb_7.setText("")
        self.cb_7.setChecked(False)
        self.cb_7.setObjectName("cb_7")
        self.cb_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_8.setGeometry(QtCore.QRect(640, 330, 161, 19))
        self.cb_8.setChecked(False)
        self.cb_8.setObjectName("cb_8")
        self.cb_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_10.setGeometry(QtCore.QRect(150, 370, 131, 19))
        self.cb_10.setChecked(False)
        self.cb_10.setObjectName("cb_10")
        self.cb_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_9.setGeometry(QtCore.QRect(130, 370, 21, 19))
        self.cb_9.setText("")
        self.cb_9.setChecked(False)
        self.cb_9.setObjectName("cb_9")
        self.cb_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_11.setGeometry(QtCore.QRect(300, 370, 21, 19))
        self.cb_11.setText("")
        self.cb_11.setChecked(False)
        self.cb_11.setObjectName("cb_11")
        self.cb_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_12.setGeometry(QtCore.QRect(320, 370, 91, 19))
        self.cb_12.setChecked(False)
        self.cb_12.setObjectName("cb_12")
        self.cb_14 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_14.setGeometry(QtCore.QRect(460, 370, 91, 19))
        self.cb_14.setChecked(False)
        self.cb_14.setObjectName("cb_14")
        self.cb_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_13.setGeometry(QtCore.QRect(440, 370, 21, 19))
        self.cb_13.setText("")
        self.cb_13.setChecked(False)
        self.cb_13.setObjectName("cb_13")
        self.cb_15 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_15.setGeometry(QtCore.QRect(620, 370, 21, 19))
        self.cb_15.setText("")
        self.cb_15.setChecked(False)
        self.cb_15.setObjectName("cb_15")
        self.cb_16 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_16.setGeometry(QtCore.QRect(640, 370, 91, 19))
        self.cb_16.setChecked(False)
        self.cb_16.setObjectName("cb_16")
        self.cb_17 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_17.setGeometry(QtCore.QRect(130, 410, 21, 19))
        self.cb_17.setText("")
        self.cb_17.setChecked(False)
        self.cb_17.setObjectName("cb_17")
        self.cb_18 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_18.setGeometry(QtCore.QRect(150, 410, 101, 19))
        self.cb_18.setChecked(False)
        self.cb_18.setObjectName("cb_18")
        self.cb_20 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_20.setGeometry(QtCore.QRect(320, 410, 71, 19))
        self.cb_20.setChecked(False)
        self.cb_20.setObjectName("cb_20")
        self.cb_19 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_19.setGeometry(QtCore.QRect(300, 410, 21, 19))
        self.cb_19.setText("")
        self.cb_19.setChecked(False)
        self.cb_19.setObjectName("cb_19")
        self.cb_21 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_21.setGeometry(QtCore.QRect(440, 410, 21, 19))
        self.cb_21.setText("")
        self.cb_21.setChecked(False)
        self.cb_21.setObjectName("cb_21")
        self.cb_22 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_22.setGeometry(QtCore.QRect(460, 410, 71, 19))
        self.cb_22.setChecked(False)
        self.cb_22.setObjectName("cb_22")
        self.cb_23 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_23.setGeometry(QtCore.QRect(620, 410, 21, 19))
        self.cb_23.setText("")
        self.cb_23.setChecked(False)
        self.cb_23.setObjectName("cb_23")
        self.cb_24 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_24.setGeometry(QtCore.QRect(640, 410, 151, 19))
        self.cb_24.setChecked(False)
        self.cb_24.setObjectName("cb_24")
        self.cb_25 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_25.setGeometry(QtCore.QRect(820, 410, 21, 19))
        self.cb_25.setText("")
        self.cb_25.setChecked(False)
        self.cb_25.setObjectName("cb_25")
        self.cb_26 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_26.setGeometry(QtCore.QRect(840, 410, 151, 19))
        self.cb_26.setChecked(False)
        self.cb_26.setObjectName("cb_26")
        self.cb_27 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_27.setGeometry(QtCore.QRect(130, 450, 21, 19))
        self.cb_27.setText("")
        self.cb_27.setChecked(False)
        self.cb_27.setObjectName("cb_27")
        self.cb_28 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_28.setGeometry(QtCore.QRect(150, 450, 101, 19))
        self.cb_28.setChecked(False)
        self.cb_28.setObjectName("cb_28")
        self.cb_29 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_29.setGeometry(QtCore.QRect(300, 450, 21, 19))
        self.cb_29.setText("")
        self.cb_29.setChecked(False)
        self.cb_29.setObjectName("cb_29")
        self.cb_30 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_30.setGeometry(QtCore.QRect(320, 450, 101, 19))
        self.cb_30.setChecked(False)
        self.cb_30.setObjectName("cb_30")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 510, 71, 21))
        self.label_13.setObjectName("label_13")
        self.cb_31 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_31.setGeometry(QtCore.QRect(130, 510, 101, 19))
        self.cb_31.setChecked(False)
        self.cb_31.setObjectName("cb_31")
        self.cb_32 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_32.setGeometry(QtCore.QRect(330, 510, 101, 19))
        self.cb_32.setChecked(False)
        self.cb_32.setObjectName("cb_32")
        self.cb_37 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_37.setGeometry(QtCore.QRect(790, 550, 131, 19))
        self.cb_37.setChecked(False)
        self.cb_37.setObjectName("cb_37")
        self.cb_33 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_33.setGeometry(QtCore.QRect(560, 510, 141, 19))
        self.cb_33.setChecked(False)
        self.cb_33.setObjectName("cb_33")
        self.cb_34 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_34.setGeometry(QtCore.QRect(790, 510, 141, 19))
        self.cb_34.setChecked(False)
        self.cb_34.setObjectName("cb_34")
        self.cb_35 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_35.setGeometry(QtCore.QRect(130, 550, 171, 19))
        self.cb_35.setChecked(False)
        self.cb_35.setObjectName("cb_35")
        self.cb_36 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_36.setGeometry(QtCore.QRect(330, 550, 211, 19))
        self.cb_36.setChecked(False)
        self.cb_36.setObjectName("cb_36")
        self.cb_38 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_38.setGeometry(QtCore.QRect(130, 590, 241, 19))
        self.cb_38.setChecked(False)
        self.cb_38.setObjectName("cb_38")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(440, 590, 151, 21))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.rb_12 = QtWidgets.QRadioButton(self.groupBox_3)
        self.rb_12.setGeometry(QtCore.QRect(10, 0, 61, 19))
        self.rb_12.setChecked(True)
        self.rb_12.setObjectName("rb_12")
        self.rb_13 = QtWidgets.QRadioButton(self.groupBox_3)
        self.rb_13.setGeometry(QtCore.QRect(80, 0, 61, 19))
        self.rb_13.setObjectName("rb_13")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(690, 590, 241, 21))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.rb_14 = QtWidgets.QRadioButton(self.groupBox_4)
        self.rb_14.setGeometry(QtCore.QRect(10, 0, 101, 19))
        self.rb_14.setChecked(True)
        self.rb_14.setObjectName("rb_14")
        self.rb_15 = QtWidgets.QRadioButton(self.groupBox_4)
        self.rb_15.setGeometry(QtCore.QRect(140, 0, 91, 19))
        self.rb_15.setObjectName("rb_15")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 650, 71, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 700, 101, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(270, 700, 21, 31))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(180, 700, 41, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(510, 700, 21, 31))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(350, 700, 111, 31))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(600, 700, 111, 31))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(750, 700, 21, 31))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(30, 750, 91, 31))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(260, 750, 21, 31))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(260, 800, 21, 31))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(30, 800, 91, 31))
        self.label_25.setObjectName("label_25")
        self.sb_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_3.setGeometry(QtCore.QRect(200, 270, 41, 31))
        self.sb_3.setObjectName("sb_3")
        self.sb_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_4.setGeometry(QtCore.QRect(430, 270, 41, 31))
        self.sb_4.setObjectName("sb_4")
        self.sb_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_5.setGeometry(QtCore.QRect(660, 270, 41, 31))
        self.sb_5.setObjectName("sb_5")
        self.sb_6 = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_6.setGeometry(QtCore.QRect(220, 700, 41, 31))
        self.sb_6.setObjectName("sb_6")
        self.sb_7 = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_7.setGeometry(QtCore.QRect(460, 700, 41, 31))
        self.sb_7.setObjectName("sb_7")
        self.sb_8 = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_8.setGeometry(QtCore.QRect(700, 700, 41, 31))
        self.sb_8.setObjectName("sb_8")
        self.sb_9 = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_9.setGeometry(QtCore.QRect(180, 750, 71, 31))
        self.sb_9.setObjectName("sb_9")
        self.sb_10 = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_10.setGeometry(QtCore.QRect(180, 800, 71, 31))
        self.sb_10.setObjectName("sb_10")
        self.sb_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_1.setGeometry(QtCore.QRect(760, 110, 211, 31))
        self.sb_1.setMaximum(9999)
        self.sb_1.setObjectName("sb_1")
        self.sb_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_2.setGeometry(QtCore.QRect(240, 160, 41, 31))
        self.sb_2.setMinimum(1)
        self.sb_2.setProperty("value", 1)
        self.sb_2.setObjectName("sb_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(120, 640, 1051, 31))
        self.groupBox_5.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.rb_16 = QtWidgets.QRadioButton(self.groupBox_5)
        self.rb_16.setGeometry(QtCore.QRect(10, 10, 101, 19))
        self.rb_16.setObjectName("rb_16")
        self.rb_17 = QtWidgets.QRadioButton(self.groupBox_5)
        self.rb_17.setGeometry(QtCore.QRect(210, 10, 131, 19))
        self.rb_17.setObjectName("rb_17")
        self.rb_18 = QtWidgets.QRadioButton(self.groupBox_5)
        self.rb_18.setGeometry(QtCore.QRect(440, 10, 131, 19))
        self.rb_18.setObjectName("rb_18")
        self.rb_19 = QtWidgets.QRadioButton(self.groupBox_5)
        self.rb_19.setGeometry(QtCore.QRect(670, 10, 131, 19))
        self.rb_19.setObjectName("rb_19")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(630, 210, 351, 31))
        self.groupBox_6.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.rb_10 = QtWidgets.QRadioButton(self.groupBox_6)
        self.rb_10.setGeometry(QtCore.QRect(10, 10, 71, 19))
        self.rb_10.setObjectName("rb_10")
        self.rb_11 = QtWidgets.QRadioButton(self.groupBox_6)
        self.rb_11.setGeometry(QtCore.QRect(210, 10, 61, 19))
        self.rb_11.setObjectName("rb_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.calculate) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "第二届眉笔杯分数计算器"))
        self.pushButton.setText(_translate("MainWindow", "计算分数"))
        self.label.setText(_translate("MainWindow", "游戏内结算得分"))
        self.label_2.setText(_translate("MainWindow", "开局分队"))
        self.label_3.setText(_translate("MainWindow", "结局"))
        self.rb_1.setText(_translate("MainWindow", "以人为本 第      次使用"))
        self.rb_2.setText(_translate("MainWindow", "物尽其用(骰子)"))
        self.rb_3.setText(_translate("MainWindow", "心胜于物"))
        self.rb_4.setText(_translate("MainWindow", "狙医/术特/近锋/重辅"))
        self.rb_5.setText(_translate("MainWindow", "高规格/矛头"))
        self.rb_6.setText(_translate("MainWindow", "指挥/集群/后勤/研究"))
        self.rb_7.setText(_translate("MainWindow", "未通关/海沫"))
        self.rb_9.setText(_translate("MainWindow", "骑士"))
        self.label_4.setText(_translate("MainWindow", "选手名字"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">第二届眉笔杯分数计算器</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">by：董杭杭</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "临时招募"))
        self.label_6.setText(_translate("MainWindow", "六星干员"))
        self.label_7.setText(_translate("MainWindow", "人"))
        self.label_8.setText(_translate("MainWindow", "人"))
        self.label_9.setText(_translate("MainWindow", "五星干员"))
        self.label_10.setText(_translate("MainWindow", "四星干员"))
        self.label_11.setText(_translate("MainWindow", "人"))
        self.label_12.setText(_translate("MainWindow", "紧急关卡"))
        self.cb_2.setText(_translate("MainWindow", "大君遗脉 无漏"))
        self.cb_4.setText(_translate("MainWindow", "巢穴"))
        self.cb_6.setText(_translate("MainWindow", "瞻前顾后(漏怪)"))
        self.cb_8.setText(_translate("MainWindow", "瞻前顾后(无漏)"))
        self.cb_10.setText(_translate("MainWindow", "溟痕乐园 无漏"))
        self.cb_12.setText(_translate("MainWindow", "领地意识"))
        self.cb_14.setText(_translate("MainWindow", "狩猎场"))
        self.cb_16.setText(_translate("MainWindow", "铳与秩序"))
        self.cb_18.setText(_translate("MainWindow", "好梦在何方"))
        self.cb_20.setText(_translate("MainWindow", "失控"))
        self.cb_22.setText(_translate("MainWindow", "育生池"))
        self.cb_24.setText(_translate("MainWindow", "(左飞机)机械之灾"))
        self.cb_26.setText(_translate("MainWindow", "(右飞机)机械之灾"))
        self.cb_28.setText(_translate("MainWindow", "水火相容"))
        self.cb_30.setText(_translate("MainWindow", "深度认知"))
        self.label_13.setText(_translate("MainWindow", "隐藏关卡"))
        self.cb_31.setText(_translate("MainWindow", "真相(漏怪)"))
        self.cb_32.setText(_translate("MainWindow", "真相(无漏)"))
        self.cb_37.setText(_translate("MainWindow", "狂信如火 无漏"))
        self.cb_33.setText(_translate("MainWindow", "鸭本运作(漏怪)"))
        self.cb_34.setText(_translate("MainWindow", "鸭本运作(无漏)"))
        self.cb_35.setText(_translate("MainWindow", "监工现场(击杀鸭爵)"))
        self.cb_36.setText(_translate("MainWindow", "监工现场(击杀鸭爵且无漏)"))
        self.cb_38.setText(_translate("MainWindow", "“喜”从箱来 (我喜欢跳舞！)"))
        self.rb_12.setText(_translate("MainWindow", "漏怪"))
        self.rb_13.setText(_translate("MainWindow", "无漏"))
        self.rb_14.setText(_translate("MainWindow", "宝箱未全收"))
        self.rb_15.setText(_translate("MainWindow", "宝箱全收"))
        self.label_14.setText(_translate("MainWindow", "奇境BOSS"))
        self.label_15.setText(_translate("MainWindow", "击杀鸭/狗/熊"))
        self.label_16.setText(_translate("MainWindow", "只"))
        self.label_17.setText(_translate("MainWindow", "鸭爵"))
        self.label_18.setText(_translate("MainWindow", "只"))
        self.label_19.setText(_translate("MainWindow", "狗头(流泪小子)"))
        self.label_20.setText(_translate("MainWindow", "熊(高普尼克)"))
        self.label_21.setText(_translate("MainWindow", "只"))
        self.label_22.setText(_translate("MainWindow", "收藏品数量"))
        self.label_23.setText(_translate("MainWindow", "个"))
        self.label_24.setText(_translate("MainWindow", "个"))
        self.label_25.setText(_translate("MainWindow", "启示数量"))
        self.rb_16.setText(_translate("MainWindow", "未进入奇境"))
        self.rb_17.setText(_translate("MainWindow", "绣锤(荒地群猎)"))
        self.rb_18.setText(_translate("MainWindow", "寒灾(寒灾之咒)"))
        self.rb_19.setText(_translate("MainWindow", "墓碑(险路勿近)"))
        self.rb_10.setText(_translate("MainWindow", "大蒂"))
        self.rb_11.setText(_translate("MainWindow", "水月"))
