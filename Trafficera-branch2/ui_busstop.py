# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_busstop.ui'
#
# Created: Tue May 26 15:37:05 2015
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Busstop(object):
    def setupUi(self, Busstop):
        Busstop.setObjectName(_fromUtf8("Busstop"))
        Busstop.setEnabled(True)
        Busstop.resize(477, 336)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(13)
        Busstop.setFont(font)
        Busstop.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Busstop.setWindowTitle(_fromUtf8("iSimGis Converter"))
        Busstop.setWindowOpacity(4.0)
        Busstop.setToolTip(_fromUtf8(""))
        Busstop.setStatusTip(_fromUtf8(""))
        Busstop.setSizeGripEnabled(False)
        self.SegmentGroupBox = QtGui.QGroupBox(Busstop)
        self.SegmentGroupBox.setGeometry(QtCore.QRect(0, 30, 481, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.SegmentGroupBox.setFont(font)
        self.SegmentGroupBox.setObjectName(_fromUtf8("SegmentGroupBox"))
        self.segmentIdlabel = QtGui.QLabel(self.SegmentGroupBox)
        self.segmentIdlabel.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.segmentIdlabel.setObjectName(_fromUtf8("segmentIdlabel"))
        self.segmentIDcomboBox = QtGui.QComboBox(self.SegmentGroupBox)
        self.segmentIDcomboBox.setGeometry(QtCore.QRect(120, 20, 341, 22))
        self.segmentIDcomboBox.setObjectName(_fromUtf8("segmentIDcomboBox"))
        self.titleLabel = QtGui.QLabel(Busstop)
        self.titleLabel.setGeometry(QtCore.QRect(10, 10, 451, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.attributeGroup = QtGui.QGroupBox(Busstop)
        self.attributeGroup.setGeometry(QtCore.QRect(0, 100, 481, 231))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.attributeGroup.setFont(font)
        self.attributeGroup.setTitle(_fromUtf8(""))
        self.attributeGroup.setObjectName(_fromUtf8("attributeGroup"))
        self.hasShelter = QtGui.QCheckBox(self.attributeGroup)
        self.hasShelter.setGeometry(QtCore.QRect(30, 140, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.hasShelter.setFont(font)
        self.hasShelter.setObjectName(_fromUtf8("hasShelter"))
        self.label_2 = QtGui.QLabel(self.attributeGroup)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 81, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.attributeGroup)
        self.label_3.setGeometry(QtCore.QRect(260, 80, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.length = QtGui.QLineEdit(self.attributeGroup)
        self.length.setGeometry(QtCore.QRect(100, 80, 121, 21))
        self.length.setObjectName(_fromUtf8("length"))
        self.busstoptags = QtGui.QTextEdit(self.attributeGroup)
        self.busstoptags.setGeometry(QtCore.QRect(310, 80, 151, 81))
        self.busstoptags.setObjectName(_fromUtf8("busstoptags"))
        self.isTerminal = QtGui.QCheckBox(self.attributeGroup)
        self.isTerminal.setGeometry(QtCore.QRect(30, 110, 83, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.isTerminal.setFont(font)
        self.isTerminal.setObjectName(_fromUtf8("isTerminal"))
        self.isBay = QtGui.QCheckBox(self.attributeGroup)
        self.isBay.setGeometry(QtCore.QRect(130, 110, 71, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.isBay.setFont(font)
        self.isBay.setObjectName(_fromUtf8("isBay"))
        self.actionButton = QtGui.QPushButton(self.attributeGroup)
        self.actionButton.setGeometry(QtCore.QRect(350, 190, 91, 27))
        self.actionButton.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.actionButton.setFont(font)
        self.actionButton.setObjectName(_fromUtf8("actionButton"))
        self.idLabel = QtGui.QLabel(self.attributeGroup)
        self.idLabel.setGeometry(QtCore.QRect(12, 1, 22, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName(_fromUtf8("idLabel"))
        self.id = QtGui.QLineEdit(self.attributeGroup)
        self.id.setGeometry(QtCore.QRect(40, 1, 167, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.id.setFont(font)
        self.id.setObjectName(_fromUtf8("id"))
        self.OffsetLabel = QtGui.QLabel(self.attributeGroup)
        self.OffsetLabel.setGeometry(QtCore.QRect(230, 0, 53, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.OffsetLabel.setFont(font)
        self.OffsetLabel.setObjectName(_fromUtf8("OffsetLabel"))
        self.offset = QtGui.QLabel(self.attributeGroup)
        self.offset.setGeometry(QtCore.QRect(324, 1, 131, 20))
        self.offset.setText(_fromUtf8(""))
        self.offset.setObjectName(_fromUtf8("offset"))
        self.widget = QtGui.QWidget(self.attributeGroup)
        self.widget.setGeometry(QtCore.QRect(7, 40, 451, 27))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.busCapacityLabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.busCapacityLabel.setFont(font)
        self.busCapacityLabel.setObjectName(_fromUtf8("busCapacityLabel"))
        self.horizontalLayout_2.addWidget(self.busCapacityLabel)
        self.name = QtGui.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.name.setFont(font)
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout_2.addWidget(self.name)
        self.busstopNoLabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.busstopNoLabel.setFont(font)
        self.busstopNoLabel.setObjectName(_fromUtf8("busstopNoLabel"))
        self.horizontalLayout_2.addWidget(self.busstopNoLabel)
        self.busstopCode = QtGui.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        self.busstopCode.setFont(font)
        self.busstopCode.setObjectName(_fromUtf8("busstopCode"))
        self.horizontalLayout_2.addWidget(self.busstopCode)

        self.retranslateUi(Busstop)
        QtCore.QMetaObject.connectSlotsByName(Busstop)

    def retranslateUi(self, Busstop):
        self.SegmentGroupBox.setTitle(_translate("Busstop", "Segment", None))
        self.segmentIdlabel.setText(_translate("Busstop", "SegmentID", None))
        self.titleLabel.setText(_translate("Busstop", "BUS STOP", None))
        self.hasShelter.setText(_translate("Busstop", "Has Shelter", None))
        self.label_2.setText(_translate("Busstop", "Length*(m)", None))
        self.label_3.setText(_translate("Busstop", "Tags", None))
        self.isTerminal.setText(_translate("Busstop", "Terminal", None))
        self.isBay.setText(_translate("Busstop", "Bay", None))
        self.actionButton.setText(_translate("Busstop", "ADD", None))
        self.idLabel.setText(_translate("Busstop", "Id*", None))
        self.OffsetLabel.setText(_translate("Busstop", "Offset*", None))
        self.busCapacityLabel.setText(_translate("Busstop", "Name*", None))
        self.busstopNoLabel.setText(_translate("Busstop", "BusStopCode*", None))

