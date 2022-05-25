# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 1131)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(300, 0))
        self.widget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 463, 1426))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 2, 1, 1)
        self.toolButtonDataFile = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButtonDataFile.setObjectName("toolButtonDataFile")
        self.gridLayout.addWidget(self.toolButtonDataFile, 3, 2, 1, 1)
        self.lineEditPkPk = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditPkPk.setReadOnly(True)
        self.lineEditPkPk.setObjectName("lineEditPkPk")
        self.gridLayout.addWidget(self.lineEditPkPk, 11, 1, 1, 1)
        self.lineEditSampleSize = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditSampleSize.setReadOnly(True)
        self.lineEditSampleSize.setObjectName("lineEditSampleSize")
        self.gridLayout.addWidget(self.lineEditSampleSize, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 11, 0, 1, 1)
        self.labelSampleSize = QtWidgets.QLabel(self.groupBox_2)
        self.labelSampleSize.setObjectName("labelSampleSize")
        self.gridLayout.addWidget(self.labelSampleSize, 5, 0, 1, 1)
        self.lineEditRMS = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditRMS.setReadOnly(True)
        self.lineEditRMS.setObjectName("lineEditRMS")
        self.gridLayout.addWidget(self.lineEditRMS, 9, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)
        self.labelNyquistFreq = QtWidgets.QLabel(self.groupBox_2)
        self.labelNyquistFreq.setObjectName("labelNyquistFreq")
        self.gridLayout.addWidget(self.labelNyquistFreq, 8, 0, 1, 1)
        self.lineEditSamplingRate = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditSamplingRate.setReadOnly(True)
        self.lineEditSamplingRate.setObjectName("lineEditSamplingRate")
        self.gridLayout.addWidget(self.lineEditSamplingRate, 7, 1, 1, 1)
        self.lineEditNyquist = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditNyquist.setReadOnly(True)
        self.lineEditNyquist.setObjectName("lineEditNyquist")
        self.gridLayout.addWidget(self.lineEditNyquist, 8, 1, 1, 1)
        self.lineEditPeak = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditPeak.setReadOnly(True)
        self.lineEditPeak.setObjectName("lineEditPeak")
        self.gridLayout.addWidget(self.lineEditPeak, 10, 1, 1, 1)
        self.labelSamplingRate = QtWidgets.QLabel(self.groupBox_2)
        self.labelSamplingRate.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelSamplingRate.setObjectName("labelSamplingRate")
        self.gridLayout.addWidget(self.labelSamplingRate, 7, 0, 1, 1)
        self.lineEditDataFile = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditDataFile.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditDataFile.setReadOnly(True)
        self.lineEditDataFile.setObjectName("lineEditDataFile")
        self.gridLayout.addWidget(self.lineEditDataFile, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)
        self.labelFileName = QtWidgets.QLabel(self.groupBox_2)
        self.labelFileName.setObjectName("labelFileName")
        self.gridLayout.addWidget(self.labelFileName, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 6, 0, 1, 1)
        self.lineEditZeroPaddedSize = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditZeroPaddedSize.setObjectName("lineEditZeroPaddedSize")
        self.gridLayout.addWidget(self.lineEditZeroPaddedSize, 6, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_7 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.checkBoxShowWindowFunction = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBoxShowWindowFunction.setChecked(True)
        self.checkBoxShowWindowFunction.setObjectName("checkBoxShowWindowFunction")
        self.gridLayout_7.addWidget(self.checkBoxShowWindowFunction, 0, 2, 1, 1)
        self.checkBoxShowRawData = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBoxShowRawData.setChecked(True)
        self.checkBoxShowRawData.setObjectName("checkBoxShowRawData")
        self.gridLayout_7.addWidget(self.checkBoxShowRawData, 0, 0, 1, 1)
        self.checkBoxShowWindowedData = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBoxShowWindowedData.setChecked(True)
        self.checkBoxShowWindowedData.setObjectName("checkBoxShowWindowedData")
        self.gridLayout_7.addWidget(self.checkBoxShowWindowedData, 1, 0, 1, 1)
        self.checkBoxShowZeroPadding = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBoxShowZeroPadding.setChecked(True)
        self.checkBoxShowZeroPadding.setObjectName("checkBoxShowZeroPadding")
        self.gridLayout_7.addWidget(self.checkBoxShowZeroPadding, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_7)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.doubleSpinBoxEndTime = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBoxEndTime.setProperty("value", 1.0)
        self.doubleSpinBoxEndTime.setObjectName("doubleSpinBoxEndTime")
        self.gridLayout_4.addWidget(self.doubleSpinBoxEndTime, 0, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 3, 1, 1)
        self.doubleSpinBoxStartTime = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBoxStartTime.setObjectName("doubleSpinBoxStartTime")
        self.gridLayout_4.addWidget(self.doubleSpinBoxStartTime, 0, 2, 1, 1)
        self.checkBoxTimeSlice = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBoxTimeSlice.setChecked(True)
        self.checkBoxTimeSlice.setObjectName("checkBoxTimeSlice")
        self.gridLayout_4.addWidget(self.checkBoxTimeSlice, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 5, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.radioButtonNearestPower2 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButtonNearestPower2.setChecked(True)
        self.radioButtonNearestPower2.setObjectName("radioButtonNearestPower2")
        self.gridLayout_6.addWidget(self.radioButtonNearestPower2, 1, 0, 1, 1)
        self.lineEditPower2Preview = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEditPower2Preview.setMaximumSize(QtCore.QSize(125, 16777215))
        self.lineEditPower2Preview.setReadOnly(True)
        self.lineEditPower2Preview.setObjectName("lineEditPower2Preview")
        self.gridLayout_6.addWidget(self.lineEditPower2Preview, 2, 2, 1, 1)
        self.checkBoxPadZeros = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBoxPadZeros.setChecked(True)
        self.checkBoxPadZeros.setObjectName("checkBoxPadZeros")
        self.gridLayout_6.addWidget(self.checkBoxPadZeros, 0, 0, 1, 1)
        self.radioButtonMinPower2 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButtonMinPower2.setObjectName("radioButtonMinPower2")
        self.gridLayout_6.addWidget(self.radioButtonMinPower2, 2, 0, 1, 1)
        self.spinBoxMinPower2 = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBoxMinPower2.setMaximum(64)
        self.spinBoxMinPower2.setProperty("value", 10)
        self.spinBoxMinPower2.setObjectName("spinBoxMinPower2")
        self.gridLayout_6.addWidget(self.spinBoxMinPower2, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_6)
        self.label_16.setObjectName("label_16")
        self.gridLayout_6.addWidget(self.label_16, 2, 3, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_6)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 7, 1, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout_2.addWidget(self.radioButton_7, 3, 0, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout_2.addWidget(self.radioButton_8, 9, 0, 1, 1)
        self.radioButtonKaiser = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonKaiser.setObjectName("radioButtonKaiser")
        self.gridLayout_2.addWidget(self.radioButtonKaiser, 7, 0, 1, 1)
        self.radioButtonHanning = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonHanning.setObjectName("radioButtonHanning")
        self.gridLayout_2.addWidget(self.radioButtonHanning, 6, 0, 1, 1)
        self.radioButtonHamming = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonHamming.setObjectName("radioButtonHamming")
        self.gridLayout_2.addWidget(self.radioButtonHamming, 4, 0, 1, 1)
        self.radioButtonUniform = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonUniform.setChecked(True)
        self.radioButtonUniform.setObjectName("radioButtonUniform")
        self.gridLayout_2.addWidget(self.radioButtonUniform, 1, 0, 1, 1)
        self.radioButtonBlackman = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonBlackman.setObjectName("radioButtonBlackman")
        self.gridLayout_2.addWidget(self.radioButtonBlackman, 2, 0, 1, 1)
        self.lineEditKaiserBeta = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditKaiserBeta.setObjectName("lineEditKaiserBeta")
        self.gridLayout_2.addWidget(self.lineEditKaiserBeta, 7, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 7, 3, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_2.addWidget(self.radioButton_5, 10, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.pushButtonReload = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonReload.setObjectName("pushButtonReload")
        self.verticalLayout_5.addWidget(self.pushButtonReload)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.doubleSpinBoxHideLowMagData = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBoxHideLowMagData.setProperty("value", 0.05)
        self.doubleSpinBoxHideLowMagData.setObjectName("doubleSpinBoxHideLowMagData")
        self.gridLayout_3.addWidget(self.doubleSpinBoxHideLowMagData, 7, 1, 1, 1)
        self.checkBoxPlotFreqRes = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxPlotFreqRes.setObjectName("checkBoxPlotFreqRes")
        self.gridLayout_3.addWidget(self.checkBoxPlotFreqRes, 5, 0, 1, 1)
        self.doubleSpinBoxPlotFreqResolution = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBoxPlotFreqResolution.setMinimum(0.01)
        self.doubleSpinBoxPlotFreqResolution.setMaximum(1000.0)
        self.doubleSpinBoxPlotFreqResolution.setProperty("value", 1.0)
        self.doubleSpinBoxPlotFreqResolution.setObjectName("doubleSpinBoxPlotFreqResolution")
        self.gridLayout_3.addWidget(self.doubleSpinBoxPlotFreqResolution, 5, 1, 1, 1)
        self.pushButtonRecalculate = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonRecalculate.setObjectName("pushButtonRecalculate")
        self.gridLayout_3.addWidget(self.pushButtonRecalculate, 8, 0, 1, 3)
        self.radioButtonChartContinuous = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButtonChartContinuous.setChecked(True)
        self.radioButtonChartContinuous.setObjectName("radioButtonChartContinuous")
        self.gridLayout_3.addWidget(self.radioButtonChartContinuous, 1, 0, 1, 1)
        self.radioButtonHistogram = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButtonHistogram.setObjectName("radioButtonHistogram")
        self.gridLayout_3.addWidget(self.radioButtonHistogram, 1, 1, 1, 1)
        self.checkBoxHideLowMagData = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxHideLowMagData.setObjectName("checkBoxHideLowMagData")
        self.gridLayout_3.addWidget(self.checkBoxHideLowMagData, 7, 0, 1, 1)
        self.spinBoxMaxPlottedPoints = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBoxMaxPlottedPoints.setMaximum(50000)
        self.spinBoxMaxPlottedPoints.setProperty("value", 5000)
        self.spinBoxMaxPlottedPoints.setObjectName("spinBoxMaxPlottedPoints")
        self.gridLayout_3.addWidget(self.spinBoxMaxPlottedPoints, 6, 1, 1, 1)
        self.checkBoxLimitPlottedPoints = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxLimitPlottedPoints.setObjectName("checkBoxLimitPlottedPoints")
        self.gridLayout_3.addWidget(self.checkBoxLimitPlottedPoints, 6, 0, 1, 1)
        self.checkBoxMaxPlotFreq = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxMaxPlotFreq.setObjectName("checkBoxMaxPlotFreq")
        self.gridLayout_3.addWidget(self.checkBoxMaxPlotFreq, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 7, 2, 1, 1)
        self.doubleSpinBoxMaxPlotFreq = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBoxMaxPlotFreq.setMaximum(100000.0)
        self.doubleSpinBoxMaxPlotFreq.setProperty("value", 1000.0)
        self.doubleSpinBoxMaxPlotFreq.setObjectName("doubleSpinBoxMaxPlotFreq")
        self.gridLayout_3.addWidget(self.doubleSpinBoxMaxPlotFreq, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 5, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.groupBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_5.addWidget(self.spinBox, 1, 1, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_5.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_5.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 0, 2, 1, 1)
        self.pushButtonCreateWaterfall = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonCreateWaterfall.setObjectName("pushButtonCreateWaterfall")
        self.gridLayout_5.addWidget(self.pushButtonCreateWaterfall, 2, 0, 1, 3)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.widget)
        self.charterAreaWidget = QtWidgets.QWidget(self.centralwidget)
        self.charterAreaWidget.setObjectName("charterAreaWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.charterAreaWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chartWidget = QtWidgets.QWidget(self.charterAreaWidget)
        self.chartWidget.setObjectName("chartWidget")
        self.horizontalLayout_4.addWidget(self.chartWidget)
        self.fftwidget = QtWidgets.QWidget(self.charterAreaWidget)
        self.fftwidget.setObjectName("fftwidget")
        self.horizontalLayout_4.addWidget(self.fftwidget)
        self.horizontalLayout.addWidget(self.charterAreaWidget)
        self.busyWidget = QtWidgets.QWidget(self.centralwidget)
        self.busyWidget.setObjectName("busyWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.busyWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelBusy = QtWidgets.QLabel(self.busyWidget)
        self.labelBusy.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBusy.setObjectName("labelBusy")
        self.verticalLayout_3.addWidget(self.labelBusy)
        self.horizontalLayout.addWidget(self.busyWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1077, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRecent_Files = QtWidgets.QAction(MainWindow)
        self.actionRecent_Files.setObjectName("actionRecent_Files")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionRefresh_Data = QtWidgets.QAction(MainWindow)
        self.actionRefresh_Data.setObjectName("actionRefresh_Data")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPlot_Toolbar = QtWidgets.QAction(MainWindow)
        self.actionPlot_Toolbar.setCheckable(True)
        self.actionPlot_Toolbar.setObjectName("actionPlot_Toolbar")
        self.actionAbout_FreeFFT = QtWidgets.QAction(MainWindow)
        self.actionAbout_FreeFFT.setObjectName("actionAbout_FreeFFT")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRecent_Files)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionRefresh_Data)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionPlot_Toolbar)
        self.menuAbout.addAction(self.actionAbout_FreeFFT)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditDataFile, self.toolButtonDataFile)
        MainWindow.setTabOrder(self.toolButtonDataFile, self.lineEditSampleSize)
        MainWindow.setTabOrder(self.lineEditSampleSize, self.lineEditSamplingRate)
        MainWindow.setTabOrder(self.lineEditSamplingRate, self.lineEditNyquist)
        MainWindow.setTabOrder(self.lineEditNyquist, self.lineEditRMS)
        MainWindow.setTabOrder(self.lineEditRMS, self.lineEditPeak)
        MainWindow.setTabOrder(self.lineEditPeak, self.lineEditPkPk)
        MainWindow.setTabOrder(self.lineEditPkPk, self.checkBoxTimeSlice)
        MainWindow.setTabOrder(self.checkBoxTimeSlice, self.doubleSpinBoxStartTime)
        MainWindow.setTabOrder(self.doubleSpinBoxStartTime, self.doubleSpinBoxEndTime)
        MainWindow.setTabOrder(self.doubleSpinBoxEndTime, self.pushButtonReload)
        MainWindow.setTabOrder(self.pushButtonReload, self.radioButtonUniform)
        MainWindow.setTabOrder(self.radioButtonUniform, self.radioButtonBlackman)
        MainWindow.setTabOrder(self.radioButtonBlackman, self.radioButton_7)
        MainWindow.setTabOrder(self.radioButton_7, self.radioButtonHamming)
        MainWindow.setTabOrder(self.radioButtonHamming, self.radioButtonHanning)
        MainWindow.setTabOrder(self.radioButtonHanning, self.radioButtonKaiser)
        MainWindow.setTabOrder(self.radioButtonKaiser, self.lineEditKaiserBeta)
        MainWindow.setTabOrder(self.lineEditKaiserBeta, self.radioButton_8)
        MainWindow.setTabOrder(self.radioButton_8, self.radioButton_5)
        MainWindow.setTabOrder(self.radioButton_5, self.radioButtonChartContinuous)
        MainWindow.setTabOrder(self.radioButtonChartContinuous, self.radioButtonHistogram)
        MainWindow.setTabOrder(self.radioButtonHistogram, self.checkBoxMaxPlotFreq)
        MainWindow.setTabOrder(self.checkBoxMaxPlotFreq, self.doubleSpinBoxMaxPlotFreq)
        MainWindow.setTabOrder(self.doubleSpinBoxMaxPlotFreq, self.checkBoxPlotFreqRes)
        MainWindow.setTabOrder(self.checkBoxPlotFreqRes, self.doubleSpinBoxPlotFreqResolution)
        MainWindow.setTabOrder(self.doubleSpinBoxPlotFreqResolution, self.checkBoxLimitPlottedPoints)
        MainWindow.setTabOrder(self.checkBoxLimitPlottedPoints, self.spinBoxMaxPlottedPoints)
        MainWindow.setTabOrder(self.spinBoxMaxPlottedPoints, self.checkBoxHideLowMagData)
        MainWindow.setTabOrder(self.checkBoxHideLowMagData, self.doubleSpinBoxHideLowMagData)
        MainWindow.setTabOrder(self.doubleSpinBoxHideLowMagData, self.pushButtonRecalculate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FreeFFT - FFT Analysis Software"))
        self.groupBox_2.setTitle(_translate("MainWindow", "General Data"))
        self.label_4.setText(_translate("MainWindow", "Hz"))
        self.toolButtonDataFile.setText(_translate("MainWindow", "..."))
        self.label_7.setText(_translate("MainWindow", "Pk-Pk (Calculated)"))
        self.labelSampleSize.setText(_translate("MainWindow", "Sample Size"))
        self.label_3.setText(_translate("MainWindow", "Hz"))
        self.label_2.setText(_translate("MainWindow", "RMS"))
        self.labelNyquistFreq.setText(_translate("MainWindow", "Nyquist Frequency"))
        self.labelSamplingRate.setText(_translate("MainWindow", "Sampling Rate"))
        self.label_6.setText(_translate("MainWindow", "Peak (Calculated)"))
        self.labelFileName.setText(_translate("MainWindow", "Data File"))
        self.label_15.setText(_translate("MainWindow", "Zero Padded Size"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Plot Options"))
        self.checkBoxShowWindowFunction.setText(_translate("MainWindow", "Show Window Function"))
        self.checkBoxShowRawData.setText(_translate("MainWindow", "Show Raw Data"))
        self.checkBoxShowWindowedData.setText(_translate("MainWindow", "Show Windowed Data"))
        self.checkBoxShowZeroPadding.setText(_translate("MainWindow", "Show Zero Padding"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Data Options"))
        self.label_11.setText(_translate("MainWindow", "End"))
        self.checkBoxTimeSlice.setText(_translate("MainWindow", "Time Slice"))
        self.label_10.setText(_translate("MainWindow", "Start"))
        self.label_12.setText(_translate("MainWindow", "sec"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Zero Padding"))
        self.radioButtonNearestPower2.setText(_translate("MainWindow", "Nearest Power of 2"))
        self.lineEditPower2Preview.setText(_translate("MainWindow", "1024"))
        self.checkBoxPadZeros.setText(_translate("MainWindow", "Pad Zeros"))
        self.radioButtonMinPower2.setText(_translate("MainWindow", "Minimum Power of 2"))
        self.label_16.setText(_translate("MainWindow", "Points"))
        self.groupBox.setTitle(_translate("MainWindow", "Windowing Options"))
        self.label.setText(_translate("MainWindow", "β"))
        self.radioButton_7.setText(_translate("MainWindow", "Exponential"))
        self.radioButton_8.setText(_translate("MainWindow", "Flat Top"))
        self.radioButtonKaiser.setText(_translate("MainWindow", "Kaiser-Bessel"))
        self.radioButtonHanning.setText(_translate("MainWindow", "Hanning"))
        self.radioButtonHamming.setText(_translate("MainWindow", "Hamming"))
        self.radioButtonUniform.setText(_translate("MainWindow", "Uniform"))
        self.radioButtonBlackman.setText(_translate("MainWindow", "Blackman"))
        self.lineEditKaiserBeta.setText(_translate("MainWindow", "15"))
        self.radioButton_5.setText(_translate("MainWindow", "Force"))
        self.pushButtonReload.setText(_translate("MainWindow", "Reload Data"))
        self.groupBox_3.setTitle(_translate("MainWindow", "FFT Options"))
        self.checkBoxPlotFreqRes.setText(_translate("MainWindow", "Plot Frequency Resolution"))
        self.pushButtonRecalculate.setText(_translate("MainWindow", "Recalculate FFT"))
        self.radioButtonChartContinuous.setText(_translate("MainWindow", "Continuous"))
        self.radioButtonHistogram.setText(_translate("MainWindow", "Histogram"))
        self.checkBoxHideLowMagData.setText(_translate("MainWindow", "Hide Low Magnitude Data"))
        self.checkBoxLimitPlottedPoints.setText(_translate("MainWindow", "Limit Plotted Data Points (Randomized)"))
        self.checkBoxMaxPlotFreq.setText(_translate("MainWindow", "Maximum FFT Frequency"))
        self.label_8.setText(_translate("MainWindow", "% Decimal"))
        self.label_9.setText(_translate("MainWindow", "Hz"))
        self.label_5.setText(_translate("MainWindow", "Hz"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Waterfall Plot"))
        self.checkBox.setText(_translate("MainWindow", "Section by Time"))
        self.checkBox_2.setText(_translate("MainWindow", "Section by Data  Point Count"))
        self.label_14.setText(_translate("MainWindow", "points"))
        self.label_13.setText(_translate("MainWindow", "sec"))
        self.pushButtonCreateWaterfall.setText(_translate("MainWindow", "Create Waterfall Plot"))
        self.labelBusy.setText(_translate("MainWindow", "<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600;\">Busy Label</span></h1></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Edit"))
        self.menuView.setTitle(_translate("MainWindow", "&View"))
        self.menuSettings.setTitle(_translate("MainWindow", "&Settings"))
        self.menuWindow.setTitle(_translate("MainWindow", "&Window"))
        self.menuAbout.setTitle(_translate("MainWindow", "&Help"))
        self.actionOpen.setText(_translate("MainWindow", "&Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionRecent_Files.setText(_translate("MainWindow", "&Recent Files"))
        self.actionClose.setText(_translate("MainWindow", "&Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionRefresh_Data.setText(_translate("MainWindow", "Refresh Data"))
        self.actionExport.setText(_translate("MainWindow", "&Export"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPlot_Toolbar.setText(_translate("MainWindow", "Plot Toolbar"))
        self.actionAbout_FreeFFT.setText(_translate("MainWindow", "&About FreeFFT"))
import resources_rc
