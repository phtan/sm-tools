# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_trainstop.ui'
#
# Created: Tue May 26 15:37:16 2015
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

class Ui_TrainStop(object):
    def setupUi(self, TrainStop):
        TrainStop.setObjectName(_fromUtf8("TrainStop"))
        TrainStop.resize(511, 357)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        TrainStop.setFont(font)
        self.pushButton = QtGui.QPushButton(TrainStop)
        self.pushButton.setGeometry(QtCore.QRect(350, 310, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.SegmentGroupBox = QtGui.QGroupBox(TrainStop)
        self.SegmentGroupBox.setGeometry(QtCore.QRect(10, 50, 491, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SegmentGroupBox.setFont(font)
        self.SegmentGroupBox.setObjectName(_fromUtf8("SegmentGroupBox"))
        self.segmentIDlabel = QtGui.QLabel(self.SegmentGroupBox)
        self.segmentIDlabel.setGeometry(QtCore.QRect(30, 10, 81, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.segmentIDlabel.setFont(font)
        self.segmentIDlabel.setObjectName(_fromUtf8("segmentIDlabel"))
        self.segmentIDcomboBox = QtGui.QComboBox(self.SegmentGroupBox)
        self.segmentIDcomboBox.setGeometry(QtCore.QRect(120, 20, 361, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.segmentIDcomboBox.setFont(font)
        self.segmentIDcomboBox.setObjectName(_fromUtf8("segmentIDcomboBox"))
        self.label = QtGui.QLabel(self.SegmentGroupBox)
        self.label.setGeometry(QtCore.QRect(30, 55, 71, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.segmentsListLineEdit = QtGui.QLineEdit(self.SegmentGroupBox)
        self.segmentsListLineEdit.setGeometry(QtCore.QRect(120, 59, 361, 21))
        self.segmentsListLineEdit.setObjectName(_fromUtf8("segmentsListLineEdit"))
        self.idLabel = QtGui.QLabel(TrainStop)
        self.idLabel.setGeometry(QtCore.QRect(30, 150, 31, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName(_fromUtf8("idLabel"))
        self.id = QtGui.QLineEdit(TrainStop)
        self.id.setGeometry(QtCore.QRect(70, 150, 161, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.id.setFont(font)
        self.id.setObjectName(_fromUtf8("id"))
        self.platformNamelabel = QtGui.QLabel(TrainStop)
        self.platformNamelabel.setGeometry(QtCore.QRect(30, 190, 101, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.platformNamelabel.setFont(font)
        self.platformNamelabel.setObjectName(_fromUtf8("platformNamelabel"))
        self.stationNamelabel = QtGui.QLabel(TrainStop)
        self.stationNamelabel.setGeometry(QtCore.QRect(250, 190, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.stationNamelabel.setFont(font)
        self.stationNamelabel.setObjectName(_fromUtf8("stationNamelabel"))
        self.typeLabel = QtGui.QLabel(TrainStop)
        self.typeLabel.setGeometry(QtCore.QRect(30, 220, 41, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.typeLabel.setFont(font)
        self.typeLabel.setObjectName(_fromUtf8("typeLabel"))
        self.tagsLabel = QtGui.QLabel(TrainStop)
        self.tagsLabel.setGeometry(QtCore.QRect(250, 220, 61, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.tagsLabel.setFont(font)
        self.tagsLabel.setObjectName(_fromUtf8("tagsLabel"))
        self.platform_name = QtGui.QLineEdit(TrainStop)
        self.platform_name.setGeometry(QtCore.QRect(132, 190, 101, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.platform_name.setFont(font)
        self.platform_name.setObjectName(_fromUtf8("platform_name"))
        self.station_name = QtGui.QLineEdit(TrainStop)
        self.station_name.setGeometry(QtCore.QRect(350, 190, 131, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.station_name.setFont(font)
        self.station_name.setObjectName(_fromUtf8("station_name"))
        self.tags = QtGui.QTextEdit(TrainStop)
        self.tags.setGeometry(QtCore.QRect(300, 230, 181, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.tags.setFont(font)
        self.tags.setObjectName(_fromUtf8("tags"))
        self.type = QtGui.QLineEdit(TrainStop)
        self.type.setGeometry(QtCore.QRect(80, 230, 151, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.type.setFont(font)
        self.type.setObjectName(_fromUtf8("type"))
        self.TrainStoplabel = QtGui.QLabel(TrainStop)
        self.TrainStoplabel.setGeometry(QtCore.QRect(210, 10, 111, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TrainStoplabel.setFont(font)
        self.TrainStoplabel.setObjectName(_fromUtf8("TrainStoplabel"))

        self.retranslateUi(TrainStop)
        QtCore.QMetaObject.connectSlotsByName(TrainStop)

    def retranslateUi(self, TrainStop):
        TrainStop.setWindowTitle(_translate("TrainStop", "Dialog", None))
        self.pushButton.setText(_translate("TrainStop", "ADD", None))
        self.SegmentGroupBox.setTitle(_translate("TrainStop", "Segment", None))
        self.segmentIDlabel.setText(_translate("TrainStop", "SegmentID*", None))
        self.label.setText(_translate("TrainStop", "Segments*", None))
        self.idLabel.setText(_translate("TrainStop", "Id*", None))
        self.platformNamelabel.setText(_translate("TrainStop", "Platform Name*", None))
        self.stationNamelabel.setText(_translate("TrainStop", "Station Name*", None))
        self.typeLabel.setText(_translate("TrainStop", "Type*", None))
        self.tagsLabel.setText(_translate("TrainStop", "Tags", None))
        self.TrainStoplabel.setText(_translate("TrainStop", "TRAIN STOP", None))

