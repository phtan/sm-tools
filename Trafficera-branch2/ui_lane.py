# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_lane.ui'
#
# Created: Wed May 27 16:28:42 2015
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

class Ui_Lane(object):
    def setupUi(self, Lane):
        Lane.setObjectName(_fromUtf8("Lane"))
        Lane.setEnabled(True)
        Lane.resize(486, 483)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(13)
        Lane.setFont(font)
        Lane.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Lane.setWindowTitle(_fromUtf8("iSimGis Converter"))
        Lane.setWindowOpacity(4.0)
        Lane.setToolTip(_fromUtf8(""))
        Lane.setStatusTip(_fromUtf8(""))
        Lane.setSizeGripEnabled(False)
        self.tags = QtGui.QTextEdit(Lane)
        self.tags.setGeometry(QtCore.QRect(70, 380, 161, 71))
        self.tags.setObjectName(_fromUtf8("tags"))
        self.titleLabel = QtGui.QLabel(Lane)
        self.titleLabel.setGeometry(QtCore.QRect(230, 10, 45, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.SegmentGroupBox = QtGui.QGroupBox(Lane)
        self.SegmentGroupBox.setGeometry(QtCore.QRect(10, 37, 461, 54))
        self.SegmentGroupBox.setObjectName(_fromUtf8("SegmentGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.SegmentGroupBox)
        self.gridLayout.setMargin(5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.segmentIdLabel = QtGui.QLabel(self.SegmentGroupBox)
        self.segmentIdLabel.setMaximumSize(QtCore.QSize(100, 100))
        self.segmentIdLabel.setObjectName(_fromUtf8("segmentIdLabel"))
        self.gridLayout.addWidget(self.segmentIdLabel, 0, 0, 1, 1)
        self.segmentId = QtGui.QLabel(self.SegmentGroupBox)
        self.segmentId.setText(_fromUtf8(""))
        self.segmentId.setObjectName(_fromUtf8("segmentId"))
        self.gridLayout.addWidget(self.segmentId, 0, 1, 1, 1)
        self.attributeGroup = QtGui.QGroupBox(Lane)
        self.attributeGroup.setGeometry(QtCore.QRect(10, 97, 471, 271))
        self.attributeGroup.setTitle(_fromUtf8(""))
        self.attributeGroup.setObjectName(_fromUtf8("attributeGroup"))
        self.vehicleModelabel = QtGui.QLabel(self.attributeGroup)
        self.vehicleModelabel.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.vehicleModelabel.setObjectName(_fromUtf8("vehicleModelabel"))
        self.width = QtGui.QLabel(self.attributeGroup)
        self.width.setGeometry(QtCore.QRect(441, 7, 16, 21))
        self.width.setText(_fromUtf8(""))
        self.width.setObjectName(_fromUtf8("width"))
        self.layoutWidget = QtGui.QWidget(self.attributeGroup)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 192, 451, 27))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.can_stop = QtGui.QCheckBox(self.layoutWidget)
        self.can_stop.setObjectName(_fromUtf8("can_stop"))
        self.horizontalLayout.addWidget(self.can_stop)
        self.high_occ_veh = QtGui.QCheckBox(self.layoutWidget)
        self.high_occ_veh.setObjectName(_fromUtf8("high_occ_veh"))
        self.horizontalLayout.addWidget(self.high_occ_veh)
        self.layoutWidget1 = QtGui.QWidget(self.attributeGroup)
        self.layoutWidget1.setGeometry(QtCore.QRect(13, 221, 451, 27))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.can_park = QtGui.QCheckBox(self.layoutWidget1)
        self.can_park.setObjectName(_fromUtf8("can_park"))
        self.horizontalLayout_2.addWidget(self.can_park)
        self.has_road_shoulder = QtGui.QCheckBox(self.layoutWidget1)
        self.has_road_shoulder.setObjectName(_fromUtf8("has_road_shoulder"))
        self.horizontalLayout_2.addWidget(self.has_road_shoulder)
        self.layoutWidget2 = QtGui.QWidget(self.attributeGroup)
        self.layoutWidget2.setGeometry(QtCore.QRect(7, 7, 461, 29))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.idLabel = QtGui.QLabel(self.layoutWidget2)
        self.idLabel.setObjectName(_fromUtf8("idLabel"))
        self.horizontalLayout_4.addWidget(self.idLabel)
        self.id = QtGui.QLineEdit(self.layoutWidget2)
        self.id.setObjectName(_fromUtf8("id"))
        self.horizontalLayout_4.addWidget(self.id)
        self.widthLabel = QtGui.QLabel(self.layoutWidget2)
        self.widthLabel.setObjectName(_fromUtf8("widthLabel"))
        self.horizontalLayout_4.addWidget(self.widthLabel)
        self.wlineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.wlineEdit.setObjectName(_fromUtf8("wlineEdit"))
        self.horizontalLayout_4.addWidget(self.wlineEdit)
        self.widget = QtGui.QWidget(self.attributeGroup)
        self.widget.setGeometry(QtCore.QRect(9, 80, 461, 31))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pedestrian = QtGui.QCheckBox(self.widget)
        self.pedestrian.setObjectName(_fromUtf8("pedestrian"))
        self.horizontalLayout_5.addWidget(self.pedestrian)
        self.bicycle = QtGui.QCheckBox(self.widget)
        self.bicycle.setObjectName(_fromUtf8("bicycle"))
        self.horizontalLayout_5.addWidget(self.bicycle)
        self.car = QtGui.QCheckBox(self.widget)
        self.car.setObjectName(_fromUtf8("car"))
        self.horizontalLayout_5.addWidget(self.car)
        self.van = QtGui.QCheckBox(self.widget)
        self.van.setObjectName(_fromUtf8("van"))
        self.horizontalLayout_5.addWidget(self.van)
        self.truck = QtGui.QCheckBox(self.widget)
        self.truck.setObjectName(_fromUtf8("truck"))
        self.horizontalLayout_5.addWidget(self.truck)
        self.bus = QtGui.QCheckBox(self.widget)
        self.bus.setObjectName(_fromUtf8("bus"))
        self.horizontalLayout_5.addWidget(self.bus)
        self.taxi = QtGui.QCheckBox(self.widget)
        self.taxi.setObjectName(_fromUtf8("taxi"))
        self.horizontalLayout_5.addWidget(self.taxi)
        self.widget1 = QtGui.QWidget(self.attributeGroup)
        self.widget1.setGeometry(QtCore.QRect(12, 132, 451, 29))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.busLanelabel = QtGui.QLabel(self.widget1)
        self.busLanelabel.setObjectName(_fromUtf8("busLanelabel"))
        self.horizontalLayout_3.addWidget(self.busLanelabel)
        self.bus_lane = QtGui.QComboBox(self.widget1)
        self.bus_lane.setObjectName(_fromUtf8("bus_lane"))
        self.bus_lane.addItem(_fromUtf8(""))
        self.bus_lane.addItem(_fromUtf8(""))
        self.bus_lane.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.bus_lane)
        self.errorMessage = QtGui.QLabel(Lane)
        self.errorMessage.setGeometry(QtCore.QRect(10, 408, 16, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.errorMessage.setFont(font)
        self.errorMessage.setStyleSheet(_fromUtf8("color: rgb(255, 20, 27)"))
        self.errorMessage.setText(_fromUtf8(""))
        self.errorMessage.setObjectName(_fromUtf8("errorMessage"))
        self.tagslabel = QtGui.QLabel(Lane)
        self.tagslabel.setGeometry(QtCore.QRect(20, 370, 61, 41))
        self.tagslabel.setObjectName(_fromUtf8("tagslabel"))
        self.actionButton = QtGui.QPushButton(Lane)
        self.actionButton.setGeometry(QtCore.QRect(320, 400, 100, 29))
        self.actionButton.setMaximumSize(QtCore.QSize(100, 100))
        self.actionButton.setObjectName(_fromUtf8("actionButton"))

        self.retranslateUi(Lane)
        QtCore.QMetaObject.connectSlotsByName(Lane)

    def retranslateUi(self, Lane):
        self.titleLabel.setText(_translate("Lane", "LANE", None))
        self.SegmentGroupBox.setTitle(_translate("Lane", "Segment", None))
        self.segmentIdLabel.setText(_translate("Lane", "SegmentId*", None))
        self.vehicleModelabel.setText(_translate("Lane", "Vehicle Mode", None))
        self.can_stop.setText(_translate("Lane", "Can_Stop", None))
        self.high_occ_veh.setText(_translate("Lane", "High Occupancy Vehicle", None))
        self.can_park.setText(_translate("Lane", "Can_Park", None))
        self.has_road_shoulder.setText(_translate("Lane", "Has Road Shoulder", None))
        self.idLabel.setText(_translate("Lane", "Id*", None))
        self.widthLabel.setText(_translate("Lane", "Width*", None))
        self.pedestrian.setText(_translate("Lane", "Pedestrian", None))
        self.bicycle.setText(_translate("Lane", "Bicycle", None))
        self.car.setText(_translate("Lane", "Car", None))
        self.van.setText(_translate("Lane", "Van", None))
        self.truck.setText(_translate("Lane", "Truck", None))
        self.bus.setText(_translate("Lane", "Bus", None))
        self.taxi.setText(_translate("Lane", "Taxi", None))
        self.busLanelabel.setText(_translate("Lane", "Bus Lane", None))
        self.bus_lane.setItemText(0, _translate("Lane", "Both cars and buses use lane whole day", None))
        self.bus_lane.setItemText(1, _translate("Lane", "Normal Bus Lane", None))
        self.bus_lane.setItemText(2, _translate("Lane", "Full Day Bus Lane", None))
        self.tagslabel.setText(_translate("Lane", "Tags", None))
        self.actionButton.setText(_translate("Lane", "ADD", None))

