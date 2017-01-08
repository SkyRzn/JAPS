# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(205, 419)
        self.verticalLayout = QtGui.QVBoxLayout(Settings)
        self.verticalLayout.setMargin(4)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.settings = QtGui.QTabWidget(Settings)
        self.settings.setObjectName(_fromUtf8("settings"))
        self.mapTab = QtGui.QWidget()
        self.mapTab.setObjectName(_fromUtf8("mapTab"))
        self.gridLayout = QtGui.QGridLayout(self.mapTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lightnessSlider = QtGui.QSlider(self.mapTab)
        self.lightnessSlider.setMinimum(-100)
        self.lightnessSlider.setMaximum(100)
        self.lightnessSlider.setProperty("value", 0)
        self.lightnessSlider.setSliderPosition(0)
        self.lightnessSlider.setTracking(True)
        self.lightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.lightnessSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.lightnessSlider.setObjectName(_fromUtf8("lightnessSlider"))
        self.gridLayout.addWidget(self.lightnessSlider, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.mapTab)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(100, 245, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 2)
        self.label = QtGui.QLabel(self.mapTab)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.mapTab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.homeAltitude = QtGui.QDoubleSpinBox(self.groupBox)
        self.homeAltitude.setMinimum(-90.0)
        self.homeAltitude.setMaximum(90.0)
        self.homeAltitude.setObjectName(_fromUtf8("homeAltitude"))
        self.gridLayout_5.addWidget(self.homeAltitude, 0, 1, 1, 1)
        self.homeLongitude = QtGui.QDoubleSpinBox(self.groupBox)
        self.homeLongitude.setMinimum(-180.0)
        self.homeLongitude.setMaximum(180.0)
        self.homeLongitude.setObjectName(_fromUtf8("homeLongitude"))
        self.gridLayout_5.addWidget(self.homeLongitude, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_5.addWidget(self.label_7, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 2)
        self.saturationSlider = QtGui.QSlider(self.mapTab)
        self.saturationSlider.setMinimum(-100)
        self.saturationSlider.setMaximum(100)
        self.saturationSlider.setProperty("value", 0)
        self.saturationSlider.setSliderPosition(0)
        self.saturationSlider.setTracking(True)
        self.saturationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.saturationSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.saturationSlider.setObjectName(_fromUtf8("saturationSlider"))
        self.gridLayout.addWidget(self.saturationSlider, 2, 1, 1, 1)
        self.mapApply = QtGui.QPushButton(self.mapTab)
        self.mapApply.setObjectName(_fromUtf8("mapApply"))
        self.gridLayout.addWidget(self.mapApply, 5, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.settings.addTab(self.mapTab, _fromUtf8(""))
        self.planeTab = QtGui.QWidget()
        self.planeTab.setObjectName(_fromUtf8("planeTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.planeTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.trackGroupBox = QtGui.QGroupBox(self.planeTab)
        self.trackGroupBox.setCheckable(False)
        self.trackGroupBox.setObjectName(_fromUtf8("trackGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.trackGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.trackRainbowRadio = QtGui.QRadioButton(self.trackGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trackRainbowRadio.sizePolicy().hasHeightForWidth())
        self.trackRainbowRadio.setSizePolicy(sizePolicy)
        self.trackRainbowRadio.setChecked(True)
        self.trackRainbowRadio.setObjectName(_fromUtf8("trackRainbowRadio"))
        self.gridLayout_2.addWidget(self.trackRainbowRadio, 1, 0, 1, 2)
        self.label_5 = QtGui.QLabel(self.trackGroupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(172, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 2)
        self.trackWidthSpinBox = QtGui.QSpinBox(self.trackGroupBox)
        self.trackWidthSpinBox.setProperty("value", 2)
        self.trackWidthSpinBox.setObjectName(_fromUtf8("trackWidthSpinBox"))
        self.gridLayout_2.addWidget(self.trackWidthSpinBox, 0, 1, 1, 1)
        self.trackColorButton = QtGui.QToolButton(self.trackGroupBox)
        self.trackColorButton.setEnabled(False)
        self.trackColorButton.setAutoFillBackground(True)
        self.trackColorButton.setText(_fromUtf8(""))
        self.trackColorButton.setObjectName(_fromUtf8("trackColorButton"))
        self.gridLayout_2.addWidget(self.trackColorButton, 2, 3, 1, 1)
        self.trackSingleColorRadio = QtGui.QRadioButton(self.trackGroupBox)
        self.trackSingleColorRadio.setObjectName(_fromUtf8("trackSingleColorRadio"))
        self.gridLayout_2.addWidget(self.trackSingleColorRadio, 2, 0, 1, 3)
        self.gridLayout_3.addWidget(self.trackGroupBox, 1, 0, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(100, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(282, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 3, 0, 1, 1)
        self.planeApply = QtGui.QPushButton(self.planeTab)
        self.planeApply.setObjectName(_fromUtf8("planeApply"))
        self.gridLayout_3.addWidget(self.planeApply, 3, 1, 1, 1)
        self.iconGroupBox = QtGui.QGroupBox(self.planeTab)
        self.iconGroupBox.setObjectName(_fromUtf8("iconGroupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.iconGroupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_3 = QtGui.QLabel(self.iconGroupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.planeIconSizeSpinBox = QtGui.QSpinBox(self.iconGroupBox)
        self.planeIconSizeSpinBox.setProperty("value", 32)
        self.planeIconSizeSpinBox.setObjectName(_fromUtf8("planeIconSizeSpinBox"))
        self.gridLayout_4.addWidget(self.planeIconSizeSpinBox, 0, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(44, 68, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 2, 2, 1)
        self.label_4 = QtGui.QLabel(self.iconGroupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.planeIconColorButton = QtGui.QToolButton(self.iconGroupBox)
        self.planeIconColorButton.setAutoFillBackground(True)
        self.planeIconColorButton.setText(_fromUtf8(""))
        self.planeIconColorButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.planeIconColorButton.setObjectName(_fromUtf8("planeIconColorButton"))
        self.gridLayout_4.addWidget(self.planeIconColorButton, 1, 1, 1, 1)
        self.label_3.raise_()
        self.planeIconSizeSpinBox.raise_()
        self.label_4.raise_()
        self.planeIconColorButton.raise_()
        self.gridLayout_3.addWidget(self.iconGroupBox, 0, 0, 1, 2)
        self.settings.addTab(self.planeTab, _fromUtf8(""))
        self.polarTab = QtGui.QWidget()
        self.polarTab.setObjectName(_fromUtf8("polarTab"))
        self.settings.addTab(self.polarTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.settings)

        self.retranslateUi(Settings)
        self.settings.setCurrentIndex(0)
        QtCore.QObject.connect(self.trackSingleColorRadio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.trackColorButton.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(_translate("Settings", "Form", None))
        self.label_2.setText(_translate("Settings", "Saturation", None))
        self.label.setText(_translate("Settings", "Lightness", None))
        self.groupBox.setTitle(_translate("Settings", "Home", None))
        self.label_6.setText(_translate("Settings", "Altitude", None))
        self.label_7.setText(_translate("Settings", "Longitude", None))
        self.mapApply.setText(_translate("Settings", "PushButton", None))
        self.settings.setTabText(self.settings.indexOf(self.mapTab), _translate("Settings", "Map", None))
        self.trackGroupBox.setTitle(_translate("Settings", "Track", None))
        self.trackRainbowRadio.setText(_translate("Settings", "Rainbow", None))
        self.label_5.setText(_translate("Settings", "Width", None))
        self.trackSingleColorRadio.setText(_translate("Settings", "Single color", None))
        self.planeApply.setText(_translate("Settings", "Apply", None))
        self.iconGroupBox.setTitle(_translate("Settings", "Icon", None))
        self.label_3.setText(_translate("Settings", "Size", None))
        self.label_4.setText(_translate("Settings", "Color", None))
        self.settings.setTabText(self.settings.indexOf(self.planeTab), _translate("Settings", "Plane", None))
        self.settings.setTabText(self.settings.indexOf(self.polarTab), _translate("Settings", "Polar", None))

