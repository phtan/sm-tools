# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_linkmanager.ui'
#
# Created: Tue May 26 15:36:43 2015
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

class Ui_LinkManager(object):
    def setupUi(self, LinkManager):
        LinkManager.setObjectName(_fromUtf8("LinkManager"))
        LinkManager.setEnabled(True)
        LinkManager.resize(438, 462)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(13)
        LinkManager.setFont(font)
        LinkManager.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        LinkManager.setWindowTitle(_fromUtf8("iSimGis Converter"))
        LinkManager.setWindowOpacity(4.0)
        LinkManager.setToolTip(_fromUtf8(""))
        LinkManager.setStatusTip(_fromUtf8(""))
        LinkManager.setSizeGripEnabled(False)
        self.attributeGroup = QtGui.QGroupBox(LinkManager)
        self.attributeGroup.setGeometry(QtCore.QRect(10, 153, 411, 301))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.attributeGroup.setFont(font)
        self.attributeGroup.setTitle(_fromUtf8(""))
        self.attributeGroup.setObjectName(_fromUtf8("attributeGroup"))
        self.actionButton = QtGui.QPushButton(self.attributeGroup)
        self.actionButton.setGeometry(QtCore.QRect(290, 264, 91, 31))
        self.actionButton.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.actionButton.setFont(font)
        self.actionButton.setObjectName(_fromUtf8("actionButton"))
        self.categorylabel = QtGui.QLabel(self.attributeGroup)
        self.categorylabel.setGeometry(QtCore.QRect(0, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.categorylabel.setFont(font)
        self.categorylabel.setObjectName(_fromUtf8("categorylabel"))
        self.category = QtGui.QComboBox(self.attributeGroup)
        self.category.setGeometry(QtCore.QRect(80, 120, 321, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.category.setFont(font)
        self.category.setObjectName(_fromUtf8("category"))
        self.category.addItem(_fromUtf8(""))
        self.category.addItem(_fromUtf8(""))
        self.category.addItem(_fromUtf8(""))
        self.tagslabel = QtGui.QLabel(self.attributeGroup)
        self.tagslabel.setGeometry(QtCore.QRect(10, 160, 51, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.tagslabel.setFont(font)
        self.tagslabel.setObjectName(_fromUtf8("tagslabel"))
        self.tagsLink = QtGui.QTextEdit(self.attributeGroup)
        self.tagsLink.setGeometry(QtCore.QRect(80, 160, 321, 71))
        self.tagsLink.setObjectName(_fromUtf8("tagsLink"))
        self.startNodeLabel = QtGui.QLabel(self.attributeGroup)
        self.startNodeLabel.setGeometry(QtCore.QRect(7, 28, 67, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.startNodeLabel.setFont(font)
        self.startNodeLabel.setObjectName(_fromUtf8("startNodeLabel"))
        self.endNodeLabel = QtGui.QLabel(self.attributeGroup)
        self.endNodeLabel.setGeometry(QtCore.QRect(210, 40, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.endNodeLabel.setFont(font)
        self.endNodeLabel.setObjectName(_fromUtf8("endNodeLabel"))
        self.id = QtGui.QLineEdit(self.attributeGroup)
        self.id.setGeometry(QtCore.QRect(80, 10, 111, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.id.setFont(font)
        self.id.setObjectName(_fromUtf8("id"))
        self.idLabel = QtGui.QLabel(self.attributeGroup)
        self.idLabel.setGeometry(QtCore.QRect(0, 0, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName(_fromUtf8("idLabel"))
        self.roadNameLabel = QtGui.QLabel(self.attributeGroup)
        self.roadNameLabel.setGeometry(QtCore.QRect(200, 0, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.roadNameLabel.setFont(font)
        self.roadNameLabel.setObjectName(_fromUtf8("roadNameLabel"))
        self.roadName = QtGui.QLineEdit(self.attributeGroup)
        self.roadName.setGeometry(QtCore.QRect(283, 7, 121, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.roadName.setFont(font)
        self.roadName.setObjectName(_fromUtf8("roadName"))
        self.roadTypeLabel = QtGui.QLabel(self.attributeGroup)
        self.roadTypeLabel.setGeometry(QtCore.QRect(0, 70, 81, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.roadTypeLabel.setFont(font)
        self.roadTypeLabel.setObjectName(_fromUtf8("roadTypeLabel"))
        self.roadType = QtGui.QComboBox(self.attributeGroup)
        self.roadType.setGeometry(QtCore.QRect(80, 80, 321, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.roadType.setFont(font)
        self.roadType.setObjectName(_fromUtf8("roadType"))
        self.roadType.addItem(_fromUtf8(""))
        self.roadType.addItem(_fromUtf8(""))
        self.roadType.addItem(_fromUtf8(""))
        self.roadType.addItem(_fromUtf8(""))
        self.roadType.addItem(_fromUtf8(""))
        self.roadType.addItem(_fromUtf8(""))
        self.startNode = QtGui.QComboBox(self.attributeGroup)
        self.startNode.setGeometry(QtCore.QRect(80, 40, 111, 22))
        self.startNode.setObjectName(_fromUtf8("startNode"))
        self.endNode = QtGui.QComboBox(self.attributeGroup)
        self.endNode.setGeometry(QtCore.QRect(280, 40, 121, 22))
        self.endNode.setObjectName(_fromUtf8("endNode"))
        self.titleLabel = QtGui.QLabel(LinkManager)
        self.titleLabel.setGeometry(QtCore.QRect(160, 20, 123, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.linkGroupBox = QtGui.QGroupBox(LinkManager)
        self.linkGroupBox.setGeometry(QtCore.QRect(10, 56, 411, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.linkGroupBox.setFont(font)
        self.linkGroupBox.setObjectName(_fromUtf8("linkGroupBox"))
        self.linkIdLabel = QtGui.QLabel(self.linkGroupBox)
        self.linkIdLabel.setGeometry(QtCore.QRect(20, 28, 51, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.linkIdLabel.setFont(font)
        self.linkIdLabel.setObjectName(_fromUtf8("linkIdLabel"))
        self.linkIdComboBox = QtGui.QComboBox(self.linkGroupBox)
        self.linkIdComboBox.setGeometry(QtCore.QRect(80, 30, 321, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.linkIdComboBox.setFont(font)
        self.linkIdComboBox.setObjectName(_fromUtf8("linkIdComboBox"))
        self.errorMessage = QtGui.QLabel(LinkManager)
        self.errorMessage.setGeometry(QtCore.QRect(10, 217, 16, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setItalic(True)
        self.errorMessage.setFont(font)
        self.errorMessage.setStyleSheet(_fromUtf8("color: rgb(255, 20, 27)"))
        self.errorMessage.setText(_fromUtf8(""))
        self.errorMessage.setObjectName(_fromUtf8("errorMessage"))

        self.retranslateUi(LinkManager)
        QtCore.QMetaObject.connectSlotsByName(LinkManager)

    def retranslateUi(self, LinkManager):
        self.actionButton.setText(_translate("LinkManager", "ADD", None))
        self.categorylabel.setText(_translate("LinkManager", "Category*", None))
        self.category.setItemText(0, _translate("LinkManager", "1", None))
        self.category.setItemText(1, _translate("LinkManager", "2", None))
        self.category.setItemText(2, _translate("LinkManager", "3", None))
        self.tagslabel.setText(_translate("LinkManager", "Tags", None))
        self.startNodeLabel.setText(_translate("LinkManager", "StartNode*", None))
        self.endNodeLabel.setText(_translate("LinkManager", "EndNode*", None))
        self.idLabel.setText(_translate("LinkManager", "New LinkId*", None))
        self.roadNameLabel.setText(_translate("LinkManager", "Road Name*", None))
        self.roadTypeLabel.setText(_translate("LinkManager", "Road Type*", None))
        self.roadType.setItemText(0, _translate("LinkManager", "Default", None))
        self.roadType.setItemText(1, _translate("LinkManager", "Expressway", None))
        self.roadType.setItemText(2, _translate("LinkManager", "Urban", None))
        self.roadType.setItemText(3, _translate("LinkManager", "Ramp", None))
        self.roadType.setItemText(4, _translate("LinkManager", "Roundabout", None))
        self.roadType.setItemText(5, _translate("LinkManager", "Access", None))
        self.titleLabel.setText(_translate("LinkManager", "LINK MANAGER", None))
        self.linkGroupBox.setTitle(_translate("LinkManager", "Links", None))
        self.linkIdLabel.setText(_translate("LinkManager", "LinkId*", None))
