# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.11.4/gns3/ui/server_preferences_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerPreferencesPageWidget(object):
    def setupUi(self, ServerPreferencesPageWidget):
        ServerPreferencesPageWidget.setObjectName("ServerPreferencesPageWidget")
        ServerPreferencesPageWidget.resize(659, 932)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ServerPreferencesPageWidget.sizePolicy().hasHeightForWidth())
        ServerPreferencesPageWidget.setSizePolicy(sizePolicy)
        ServerPreferencesPageWidget.setMinimumSize(QtCore.QSize(0, 0))
        ServerPreferencesPageWidget.setStyleSheet("QWidget{\n"
"    background-color: #fbf1c7;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #fbf1c7;\n"
"}\n"
"QDockWidget::title{\n"
"    background: #d5c4a1;\n"
"    padding-left: 5px;\n"
"}\n"
"QDockWidget, QMenuBar{\n"
"    color: #282828;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #d5c4a1;\n"
"  font: 13px;\n"
"  color: #282828;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #fbf1c7;\n"
"  color: #282828;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"}\n"
"QTabBar::tab {\n"
"    background: #d5c4a1;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #458588;\n"
"    color: #FFFFFF;\n"
"}\n"
"QGroupBox {\n"
"    color: #076678;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #d5c4a1;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #458588;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #d5c4a1;\n"
"    border: 0px;\n"
"}\n"
" QPushButton {\n"
"    background-color: #d79921;\n"
"    font: 14px;\n"
"}\n"
"QToolButton {\n"
"    /*background-color: transparent; mainwindowonly*/\n"
"    background-color: #d79921;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #fbf1c7;\n"
"    color: #282828;\n"
"    font: 14px;\n"
"    /*font: 12px; for mainwindow*/\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #d5c4a1;\n"
"    color: #282828;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover, QMenu::item:selected,QToolButton::hover,QPushButton::hover {\n"
"    background-color: #458588;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu {\n"
"    background-color: #fbf1c7;\n"
"}\n"
"QLabel {\n"
"    color: #282828;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #282828;\n"
"    font: bold 16px;\n"
"}\n"
"\n"
"QAbstractScrollArea::corner {\n"
"    background: #fbf1c7;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #d5c4a1;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #d5c4a1;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    width: 6px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    height: 6px;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical, QScrollBar::down-arrow:horizontal, QScrollBar::up-arrow:horizontal { \n"
"    border: 0px;\n"
"    height: 0px; \n"
"    width: 0px; \n"
"}\n"
"         \n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none\n"
"}\n"
"QStatusBar {\n"
"    background-color: #d5c4a1;\n"
"    color: #282828;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #282828;\n"
"}\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ServerPreferencesPageWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiServerPreferenceTabWidget = QtWidgets.QTabWidget(ServerPreferencesPageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiServerPreferenceTabWidget.sizePolicy().hasHeightForWidth())
        self.uiServerPreferenceTabWidget.setSizePolicy(sizePolicy)
        self.uiServerPreferenceTabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.uiServerPreferenceTabWidget.setObjectName("uiServerPreferenceTabWidget")
        self.uiLocalTabWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalTabWidget.sizePolicy().hasHeightForWidth())
        self.uiLocalTabWidget.setSizePolicy(sizePolicy)
        self.uiLocalTabWidget.setObjectName("uiLocalTabWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiLocalTabWidget)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiLocalServerAutoStartCheckBox = QtWidgets.QCheckBox(self.uiLocalTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalServerAutoStartCheckBox.sizePolicy().hasHeightForWidth())
        self.uiLocalServerAutoStartCheckBox.setSizePolicy(sizePolicy)
        self.uiLocalServerAutoStartCheckBox.setMinimumSize(QtCore.QSize(0, 0))
        self.uiLocalServerAutoStartCheckBox.setChecked(False)
        self.uiLocalServerAutoStartCheckBox.setObjectName("uiLocalServerAutoStartCheckBox")
        self.verticalLayout_3.addWidget(self.uiLocalServerAutoStartCheckBox)
        self.uiGeneralSettingsGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiGeneralSettingsGroupBox.setObjectName("uiGeneralSettingsGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiGeneralSettingsGroupBox)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.uiLocalServerPathLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPathLabel.setObjectName("uiLocalServerPathLabel")
        self.gridLayout.addWidget(self.uiLocalServerPathLabel, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiLocalServerPathLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPathLineEdit.setObjectName("uiLocalServerPathLineEdit")
        self.horizontalLayout.addWidget(self.uiLocalServerPathLineEdit)
        self.uiLocalServerToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiLocalServerToolButton.setObjectName("uiLocalServerToolButton")
        self.horizontalLayout.addWidget(self.uiLocalServerToolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.uiUbridgePathLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiUbridgePathLabel.setObjectName("uiUbridgePathLabel")
        self.gridLayout.addWidget(self.uiUbridgePathLabel, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiUbridgePathLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsGroupBox)
        self.uiUbridgePathLineEdit.setObjectName("uiUbridgePathLineEdit")
        self.horizontalLayout_5.addWidget(self.uiUbridgePathLineEdit)
        self.uiUbridgeToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsGroupBox)
        self.uiUbridgeToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiUbridgeToolButton.setObjectName("uiUbridgeToolButton")
        self.horizontalLayout_5.addWidget(self.uiUbridgeToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.uiLocalServerHostLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerHostLabel.setObjectName("uiLocalServerHostLabel")
        self.gridLayout.addWidget(self.uiLocalServerHostLabel, 5, 0, 1, 1)
        self.uiLocalServerHostComboBox = QtWidgets.QComboBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerHostComboBox.setObjectName("uiLocalServerHostComboBox")
        self.gridLayout.addWidget(self.uiLocalServerHostComboBox, 6, 0, 1, 1)
        self.uiLocalServerPortLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPortLabel.setObjectName("uiLocalServerPortLabel")
        self.gridLayout.addWidget(self.uiLocalServerPortLabel, 7, 0, 1, 1)
        self.uiLocalServerPortSpinBox = QtWidgets.QSpinBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPortSpinBox.setSuffix(" TCP")
        self.uiLocalServerPortSpinBox.setMaximum(65535)
        self.uiLocalServerPortSpinBox.setProperty("value", 3080)
        self.uiLocalServerPortSpinBox.setObjectName("uiLocalServerPortSpinBox")
        self.gridLayout.addWidget(self.uiLocalServerPortSpinBox, 8, 0, 1, 1)
        self.uiConsoleConnectionsToAnyIPCheckBox = QtWidgets.QCheckBox(self.uiGeneralSettingsGroupBox)
        self.uiConsoleConnectionsToAnyIPCheckBox.setObjectName("uiConsoleConnectionsToAnyIPCheckBox")
        self.gridLayout.addWidget(self.uiConsoleConnectionsToAnyIPCheckBox, 10, 0, 1, 1)
        self.uiLocalServerAuthCheckBox = QtWidgets.QCheckBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerAuthCheckBox.setObjectName("uiLocalServerAuthCheckBox")
        self.gridLayout.addWidget(self.uiLocalServerAuthCheckBox, 9, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.uiGeneralSettingsGroupBox)
        self.uiConsolePortRangeGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiConsolePortRangeGroupBox.setObjectName("uiConsolePortRangeGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiConsolePortRangeGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiConsoleStartPortSpinBox = QtWidgets.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleStartPortSpinBox.setSuffix(" TCP")
        self.uiConsoleStartPortSpinBox.setMaximum(65535)
        self.uiConsoleStartPortSpinBox.setProperty("value", 2000)
        self.uiConsoleStartPortSpinBox.setObjectName("uiConsoleStartPortSpinBox")
        self.gridLayout_4.addWidget(self.uiConsoleStartPortSpinBox, 0, 0, 1, 1)
        self.uiConsolePortRangeLabel = QtWidgets.QLabel(self.uiConsolePortRangeGroupBox)
        self.uiConsolePortRangeLabel.setObjectName("uiConsolePortRangeLabel")
        self.gridLayout_4.addWidget(self.uiConsolePortRangeLabel, 0, 1, 1, 1)
        self.uiConsoleEndPortSpinBox = QtWidgets.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleEndPortSpinBox.setSuffix(" TCP")
        self.uiConsoleEndPortSpinBox.setMaximum(65535)
        self.uiConsoleEndPortSpinBox.setProperty("value", 5000)
        self.uiConsoleEndPortSpinBox.setObjectName("uiConsoleEndPortSpinBox")
        self.gridLayout_4.addWidget(self.uiConsoleEndPortSpinBox, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(225, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.uiConsolePortRangeGroupBox)
        self.uiUDPPortRangeGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiUDPPortRangeGroupBox.setObjectName("uiUDPPortRangeGroupBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.uiUDPPortRangeGroupBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.uiUDPStartPortSpinBox = QtWidgets.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPStartPortSpinBox.setSuffix(" UDP")
        self.uiUDPStartPortSpinBox.setMaximum(65535)
        self.uiUDPStartPortSpinBox.setProperty("value", 10000)
        self.uiUDPStartPortSpinBox.setObjectName("uiUDPStartPortSpinBox")
        self.horizontalLayout_8.addWidget(self.uiUDPStartPortSpinBox)
        self.uiUDPPortRangeLabel = QtWidgets.QLabel(self.uiUDPPortRangeGroupBox)
        self.uiUDPPortRangeLabel.setObjectName("uiUDPPortRangeLabel")
        self.horizontalLayout_8.addWidget(self.uiUDPPortRangeLabel)
        self.uiUDPEndPortSpinBox = QtWidgets.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPEndPortSpinBox.setSuffix(" UDP")
        self.uiUDPEndPortSpinBox.setMaximum(65535)
        self.uiUDPEndPortSpinBox.setProperty("value", 20000)
        self.uiUDPEndPortSpinBox.setObjectName("uiUDPEndPortSpinBox")
        self.horizontalLayout_8.addWidget(self.uiUDPEndPortSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.uiUDPPortRangeGroupBox)
        self.uiRemoteMainServerGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiRemoteMainServerGroupBox.setObjectName("uiRemoteMainServerGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.uiRemoteMainServerGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.uiRemoteMainServerGroupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.uiRemoteMainServerHostLineEdit = QtWidgets.QLineEdit(self.uiRemoteMainServerGroupBox)
        self.uiRemoteMainServerHostLineEdit.setObjectName("uiRemoteMainServerHostLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiRemoteMainServerHostLineEdit)
        self.label_3 = QtWidgets.QLabel(self.uiRemoteMainServerGroupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.uiRemoteMainServerPortSpinBox = QtWidgets.QSpinBox(self.uiRemoteMainServerGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteMainServerPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteMainServerPortSpinBox.setSizePolicy(sizePolicy)
        self.uiRemoteMainServerPortSpinBox.setMaximum(65535)
        self.uiRemoteMainServerPortSpinBox.setProperty("value", 3080)
        self.uiRemoteMainServerPortSpinBox.setObjectName("uiRemoteMainServerPortSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiRemoteMainServerPortSpinBox)
        self.label = QtWidgets.QLabel(self.uiRemoteMainServerGroupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.uiRemoteMainServerAuthCheckBox = QtWidgets.QCheckBox(self.uiRemoteMainServerGroupBox)
        self.uiRemoteMainServerAuthCheckBox.setText("")
        self.uiRemoteMainServerAuthCheckBox.setObjectName("uiRemoteMainServerAuthCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.uiRemoteMainServerAuthCheckBox)
        self.label_4 = QtWidgets.QLabel(self.uiRemoteMainServerGroupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.uiRemoteMainServerUserLineEdit = QtWidgets.QLineEdit(self.uiRemoteMainServerGroupBox)
        self.uiRemoteMainServerUserLineEdit.setObjectName("uiRemoteMainServerUserLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.uiRemoteMainServerUserLineEdit)
        self.label_5 = QtWidgets.QLabel(self.uiRemoteMainServerGroupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.uiRemoteMainServerPasswordLineEdit = QtWidgets.QLineEdit(self.uiRemoteMainServerGroupBox)
        self.uiRemoteMainServerPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uiRemoteMainServerPasswordLineEdit.setObjectName("uiRemoteMainServerPasswordLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.uiRemoteMainServerPasswordLineEdit)
        self.verticalLayout_3.addWidget(self.uiRemoteMainServerGroupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.uiGeneralSettingsGroupBox.raise_()
        self.uiConsolePortRangeGroupBox.raise_()
        self.uiUDPPortRangeGroupBox.raise_()
        self.uiLocalServerAutoStartCheckBox.raise_()
        self.uiRemoteMainServerGroupBox.raise_()
        self.uiServerPreferenceTabWidget.addTab(self.uiLocalTabWidget, "")
        self.uiRemoteTabWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteTabWidget.sizePolicy().hasHeightForWidth())
        self.uiRemoteTabWidget.setSizePolicy(sizePolicy)
        self.uiRemoteTabWidget.setObjectName("uiRemoteTabWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.uiRemoteTabWidget)
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.uiRemoteServersTreeWidget = QtWidgets.QTreeWidget(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersTreeWidget.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersTreeWidget.setSizePolicy(sizePolicy)
        self.uiRemoteServersTreeWidget.setColumnCount(5)
        self.uiRemoteServersTreeWidget.setObjectName("uiRemoteServersTreeWidget")
        self.uiRemoteServersTreeWidget.headerItem().setText(1, "Protocol")
        self.uiRemoteServersTreeWidget.headerItem().setText(2, "Host")
        self.uiRemoteServersTreeWidget.headerItem().setText(3, "Port")
        self.gridLayout_5.addWidget(self.uiRemoteServersTreeWidget, 0, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiAddRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiAddRemoteServerPushButton.setObjectName("uiAddRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiAddRemoteServerPushButton)
        self.uiUpdateRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiUpdateRemoteServerPushButton.setEnabled(False)
        self.uiUpdateRemoteServerPushButton.setObjectName("uiUpdateRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiUpdateRemoteServerPushButton)
        self.uiDeleteRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiDeleteRemoteServerPushButton.setEnabled(False)
        self.uiDeleteRemoteServerPushButton.setObjectName("uiDeleteRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiDeleteRemoteServerPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)
        self.uiRemoteServersTreeWidget.raise_()
        self.label_7.raise_()
        self.uiServerPreferenceTabWidget.addTab(self.uiRemoteTabWidget, "")
        self.verticalLayout_2.addWidget(self.uiServerPreferenceTabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.uiRestoreDefaultsPushButton = QtWidgets.QPushButton(ServerPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName("uiRestoreDefaultsPushButton")
        self.horizontalLayout_2.addWidget(self.uiRestoreDefaultsPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ServerPreferencesPageWidget)
        self.uiServerPreferenceTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ServerPreferencesPageWidget)
        ServerPreferencesPageWidget.setTabOrder(self.uiServerPreferenceTabWidget, self.uiLocalServerAutoStartCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerAutoStartCheckBox, self.uiLocalServerPathLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerPathLineEdit, self.uiLocalServerToolButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerToolButton, self.uiUbridgePathLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiUbridgePathLineEdit, self.uiUbridgeToolButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiUbridgeToolButton, self.uiLocalServerHostComboBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerHostComboBox, self.uiLocalServerPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerPortSpinBox, self.uiLocalServerAuthCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerAuthCheckBox, self.uiConsoleConnectionsToAnyIPCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleConnectionsToAnyIPCheckBox, self.uiConsoleStartPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleStartPortSpinBox, self.uiConsoleEndPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleEndPortSpinBox, self.uiUDPStartPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiUDPStartPortSpinBox, self.uiUDPEndPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiUDPEndPortSpinBox, self.uiRestoreDefaultsPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiRestoreDefaultsPushButton, self.uiRemoteServersTreeWidget)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServersTreeWidget, self.uiAddRemoteServerPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiAddRemoteServerPushButton, self.uiDeleteRemoteServerPushButton)

    def retranslateUi(self, ServerPreferencesPageWidget):
        _translate = QtCore.QCoreApplication.translate
        ServerPreferencesPageWidget.setWindowTitle(_translate("ServerPreferencesPageWidget", "Server"))
        self.uiLocalServerAutoStartCheckBox.setText(_translate("ServerPreferencesPageWidget", "Enable local server"))
        self.uiGeneralSettingsGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "General settings"))
        self.uiLocalServerPathLabel.setText(_translate("ServerPreferencesPageWidget", "Server path:"))
        self.uiLocalServerToolButton.setText(_translate("ServerPreferencesPageWidget", "&Browse..."))
        self.uiUbridgePathLabel.setText(_translate("ServerPreferencesPageWidget", "Ubridge path:"))
        self.uiUbridgeToolButton.setText(_translate("ServerPreferencesPageWidget", "&Browse..."))
        self.uiLocalServerHostLabel.setText(_translate("ServerPreferencesPageWidget", "Host binding:"))
        self.uiLocalServerPortLabel.setText(_translate("ServerPreferencesPageWidget", "Port:"))
        self.uiConsoleConnectionsToAnyIPCheckBox.setText(_translate("ServerPreferencesPageWidget", "Allow console connections to any local IP address"))
        self.uiLocalServerAuthCheckBox.setText(_translate("ServerPreferencesPageWidget", "Protect server with password (recommended)"))
        self.uiConsolePortRangeGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "Console port range (5900 => 6000 is shared with VNC)"))
        self.uiConsolePortRangeLabel.setText(_translate("ServerPreferencesPageWidget", "to"))
        self.uiUDPPortRangeGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "UDP tunneling port range"))
        self.uiUDPPortRangeLabel.setText(_translate("ServerPreferencesPageWidget", "to"))
        self.uiRemoteMainServerGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "Remote main server"))
        self.label_2.setText(_translate("ServerPreferencesPageWidget", "Host:"))
        self.label_3.setText(_translate("ServerPreferencesPageWidget", "Port:"))
        self.uiRemoteMainServerPortSpinBox.setSuffix(_translate("ServerPreferencesPageWidget", " TCP"))
        self.label.setText(_translate("ServerPreferencesPageWidget", "Auth:"))
        self.label_4.setText(_translate("ServerPreferencesPageWidget", "User:"))
        self.label_5.setText(_translate("ServerPreferencesPageWidget", "Password:"))
        self.uiServerPreferenceTabWidget.setTabText(self.uiServerPreferenceTabWidget.indexOf(self.uiLocalTabWidget), _translate("ServerPreferencesPageWidget", "Main server"))
        self.uiRemoteServersTreeWidget.headerItem().setText(0, _translate("ServerPreferencesPageWidget", "Name"))
        self.uiRemoteServersTreeWidget.headerItem().setText(4, _translate("ServerPreferencesPageWidget", "User"))
        self.uiAddRemoteServerPushButton.setText(_translate("ServerPreferencesPageWidget", "&Add"))
        self.uiUpdateRemoteServerPushButton.setText(_translate("ServerPreferencesPageWidget", "Edit"))
        self.uiDeleteRemoteServerPushButton.setText(_translate("ServerPreferencesPageWidget", "&Delete"))
        self.label_7.setText(_translate("ServerPreferencesPageWidget", "Note: Changes are not visible in other part of the settings or application until you apply them."))
        self.uiServerPreferenceTabWidget.setTabText(self.uiServerPreferenceTabWidget.indexOf(self.uiRemoteTabWidget), _translate("ServerPreferencesPageWidget", "Remote servers"))
        self.uiRestoreDefaultsPushButton.setText(_translate("ServerPreferencesPageWidget", "Restore defaults"))

