# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.11.4/gns3/ui/general_preferences_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GeneralPreferencesPageWidget(object):
    def setupUi(self, GeneralPreferencesPageWidget):
        GeneralPreferencesPageWidget.setObjectName("GeneralPreferencesPageWidget")
        GeneralPreferencesPageWidget.resize(1028, 661)
        GeneralPreferencesPageWidget.setStyleSheet("QWidget{\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(GeneralPreferencesPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiMiscTabWidget = QtWidgets.QTabWidget(GeneralPreferencesPageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiMiscTabWidget.sizePolicy().hasHeightForWidth())
        self.uiMiscTabWidget.setSizePolicy(sizePolicy)
        self.uiMiscTabWidget.setStyleSheet("QWidget{\n"
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
        self.uiMiscTabWidget.setObjectName("uiMiscTabWidget")
        self.uiGeneralTab = QtWidgets.QWidget()
        self.uiGeneralTab.setObjectName("uiGeneralTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.uiGeneralTab)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.uiLocalPathsGroupBox = QtWidgets.QGroupBox(self.uiGeneralTab)
        self.uiLocalPathsGroupBox.setObjectName("uiLocalPathsGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.uiLocalPathsGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.uiProjectsPathLabel = QtWidgets.QLabel(self.uiLocalPathsGroupBox)
        self.uiProjectsPathLabel.setObjectName("uiProjectsPathLabel")
        self.verticalLayout_5.addWidget(self.uiProjectsPathLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiProjectsPathLineEdit = QtWidgets.QLineEdit(self.uiLocalPathsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiProjectsPathLineEdit.sizePolicy().hasHeightForWidth())
        self.uiProjectsPathLineEdit.setSizePolicy(sizePolicy)
        self.uiProjectsPathLineEdit.setObjectName("uiProjectsPathLineEdit")
        self.horizontalLayout_2.addWidget(self.uiProjectsPathLineEdit)
        self.uiProjectsPathToolButton = QtWidgets.QToolButton(self.uiLocalPathsGroupBox)
        self.uiProjectsPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiProjectsPathToolButton.setObjectName("uiProjectsPathToolButton")
        self.horizontalLayout_2.addWidget(self.uiProjectsPathToolButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(self.uiLocalPathsGroupBox)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiSymbolsPathLineEdit = QtWidgets.QLineEdit(self.uiLocalPathsGroupBox)
        self.uiSymbolsPathLineEdit.setObjectName("uiSymbolsPathLineEdit")
        self.horizontalLayout_3.addWidget(self.uiSymbolsPathLineEdit)
        self.uiSymbolsPathToolButton = QtWidgets.QToolButton(self.uiLocalPathsGroupBox)
        self.uiSymbolsPathToolButton.setObjectName("uiSymbolsPathToolButton")
        self.horizontalLayout_3.addWidget(self.uiSymbolsPathToolButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.uiConfigsPathLabel = QtWidgets.QLabel(self.uiLocalPathsGroupBox)
        self.uiConfigsPathLabel.setObjectName("uiConfigsPathLabel")
        self.verticalLayout_5.addWidget(self.uiConfigsPathLabel)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiConfigsPathLineEdit = QtWidgets.QLineEdit(self.uiLocalPathsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiConfigsPathLineEdit.sizePolicy().hasHeightForWidth())
        self.uiConfigsPathLineEdit.setSizePolicy(sizePolicy)
        self.uiConfigsPathLineEdit.setObjectName("uiConfigsPathLineEdit")
        self.horizontalLayout_7.addWidget(self.uiConfigsPathLineEdit)
        self.uiConfigsPathToolButton = QtWidgets.QToolButton(self.uiLocalPathsGroupBox)
        self.uiConfigsPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiConfigsPathToolButton.setObjectName("uiConfigsPathToolButton")
        self.horizontalLayout_7.addWidget(self.uiConfigsPathToolButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.label_3 = QtWidgets.QLabel(self.uiLocalPathsGroupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.uiAppliancesPathLineEdit = QtWidgets.QLineEdit(self.uiLocalPathsGroupBox)
        self.uiAppliancesPathLineEdit.setObjectName("uiAppliancesPathLineEdit")
        self.horizontalLayout_12.addWidget(self.uiAppliancesPathLineEdit)
        self.uiAppliancesPathToolButton = QtWidgets.QToolButton(self.uiLocalPathsGroupBox)
        self.uiAppliancesPathToolButton.setObjectName("uiAppliancesPathToolButton")
        self.horizontalLayout_12.addWidget(self.uiAppliancesPathToolButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.verticalLayout_4.addWidget(self.uiLocalPathsGroupBox)
        self.uiStyleGroupBox = QtWidgets.QGroupBox(self.uiGeneralTab)
        self.uiStyleGroupBox.setObjectName("uiStyleGroupBox")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.uiStyleGroupBox)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.uiStyleComboBox = QtWidgets.QComboBox(self.uiStyleGroupBox)
        self.uiStyleComboBox.setObjectName("uiStyleComboBox")
        self.horizontalLayout_11.addWidget(self.uiStyleComboBox)
        self.verticalLayout_4.addWidget(self.uiStyleGroupBox)
        self.uiConfigurationFileGroupBox = QtWidgets.QGroupBox(self.uiGeneralTab)
        self.uiConfigurationFileGroupBox.setObjectName("uiConfigurationFileGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiConfigurationFileGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiImportConfigurationFilePushButton = QtWidgets.QPushButton(self.uiConfigurationFileGroupBox)
        self.uiImportConfigurationFilePushButton.setObjectName("uiImportConfigurationFilePushButton")
        self.horizontalLayout.addWidget(self.uiImportConfigurationFilePushButton)
        self.uiExportConfigurationFilePushButton = QtWidgets.QPushButton(self.uiConfigurationFileGroupBox)
        self.uiExportConfigurationFilePushButton.setObjectName("uiExportConfigurationFilePushButton")
        self.horizontalLayout.addWidget(self.uiExportConfigurationFilePushButton)
        self.uiBrowseConfigurationPushButton = QtWidgets.QPushButton(self.uiConfigurationFileGroupBox)
        self.uiBrowseConfigurationPushButton.setObjectName("uiBrowseConfigurationPushButton")
        self.horizontalLayout.addWidget(self.uiBrowseConfigurationPushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.uiConfigurationFileLabel = QtWidgets.QLabel(self.uiConfigurationFileGroupBox)
        self.uiConfigurationFileLabel.setObjectName("uiConfigurationFileLabel")
        self.gridLayout.addWidget(self.uiConfigurationFileLabel, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.uiConfigurationFileGroupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.uiMiscTabWidget.addTab(self.uiGeneralTab, "")
        self.uiImagesTab = QtWidgets.QWidget()
        self.uiImagesTab.setObjectName("uiImagesTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.uiImagesTab)
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.uiLocalBinaryImagePathsGroupBox = QtWidgets.QGroupBox(self.uiImagesTab)
        self.uiLocalBinaryImagePathsGroupBox.setObjectName("uiLocalBinaryImagePathsGroupBox")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.uiLocalBinaryImagePathsGroupBox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.uiImagesPathLabel = QtWidgets.QLabel(self.uiLocalBinaryImagePathsGroupBox)
        self.uiImagesPathLabel.setObjectName("uiImagesPathLabel")
        self.verticalLayout_10.addWidget(self.uiImagesPathLabel)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiImagesPathLineEdit = QtWidgets.QLineEdit(self.uiLocalBinaryImagePathsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiImagesPathLineEdit.sizePolicy().hasHeightForWidth())
        self.uiImagesPathLineEdit.setSizePolicy(sizePolicy)
        self.uiImagesPathLineEdit.setObjectName("uiImagesPathLineEdit")
        self.horizontalLayout_4.addWidget(self.uiImagesPathLineEdit)
        self.uiImagesPathToolButton = QtWidgets.QToolButton(self.uiLocalBinaryImagePathsGroupBox)
        self.uiImagesPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiImagesPathToolButton.setObjectName("uiImagesPathToolButton")
        self.horizontalLayout_4.addWidget(self.uiImagesPathToolButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.uiImageDirectoriesLabel = QtWidgets.QLabel(self.uiLocalBinaryImagePathsGroupBox)
        self.uiImageDirectoriesLabel.setObjectName("uiImageDirectoriesLabel")
        self.verticalLayout_10.addWidget(self.uiImageDirectoriesLabel)
        self.uiImageDirectoriesListWidget = QtWidgets.QListWidget(self.uiLocalBinaryImagePathsGroupBox)
        self.uiImageDirectoriesListWidget.setLineWidth(0)
        self.uiImageDirectoriesListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.uiImageDirectoriesListWidget.setAlternatingRowColors(False)
        self.uiImageDirectoriesListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.uiImageDirectoriesListWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.uiImageDirectoriesListWidget.setProperty("isWrapping", False)
        self.uiImageDirectoriesListWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.uiImageDirectoriesListWidget.setLayoutMode(QtWidgets.QListView.Batched)
        self.uiImageDirectoriesListWidget.setGridSize(QtCore.QSize(0, 18))
        self.uiImageDirectoriesListWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.uiImageDirectoriesListWidget.setUniformItemSizes(False)
        self.uiImageDirectoriesListWidget.setSelectionRectVisible(True)
        self.uiImageDirectoriesListWidget.setObjectName("uiImageDirectoriesListWidget")
        self.verticalLayout_10.addWidget(self.uiImageDirectoriesListWidget)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.uiImageDirectoriesAddPushButton = QtWidgets.QPushButton(self.uiLocalBinaryImagePathsGroupBox)
        self.uiImageDirectoriesAddPushButton.setObjectName("uiImageDirectoriesAddPushButton")
        self.horizontalLayout_13.addWidget(self.uiImageDirectoriesAddPushButton)
        self.uiImageDirectoriesDeletePushButton = QtWidgets.QPushButton(self.uiLocalBinaryImagePathsGroupBox)
        self.uiImageDirectoriesDeletePushButton.setObjectName("uiImageDirectoriesDeletePushButton")
        self.horizontalLayout_13.addWidget(self.uiImageDirectoriesDeletePushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.verticalLayout_7.addWidget(self.uiLocalBinaryImagePathsGroupBox)
        self.uiMiscTabWidget.addTab(self.uiImagesTab, "")
        self.uiConsoleTab = QtWidgets.QWidget()
        self.uiConsoleTab.setObjectName("uiConsoleTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiConsoleTab)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiTelnetConsoleSettingsGroupBox = QtWidgets.QGroupBox(self.uiConsoleTab)
        self.uiTelnetConsoleSettingsGroupBox.setObjectName("uiTelnetConsoleSettingsGroupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.uiTelnetConsoleSettingsGroupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.uiTelnetConsoleCommandLabel = QtWidgets.QLabel(self.uiTelnetConsoleSettingsGroupBox)
        self.uiTelnetConsoleCommandLabel.setObjectName("uiTelnetConsoleCommandLabel")
        self.verticalLayout_9.addWidget(self.uiTelnetConsoleCommandLabel)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.uiTelnetConsoleCommandLineEdit = QtWidgets.QLineEdit(self.uiTelnetConsoleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiTelnetConsoleCommandLineEdit.sizePolicy().hasHeightForWidth())
        self.uiTelnetConsoleCommandLineEdit.setSizePolicy(sizePolicy)
        self.uiTelnetConsoleCommandLineEdit.setReadOnly(True)
        self.uiTelnetConsoleCommandLineEdit.setObjectName("uiTelnetConsoleCommandLineEdit")
        self.horizontalLayout_9.addWidget(self.uiTelnetConsoleCommandLineEdit)
        self.uiTelnetConsolePreconfiguredCommandPushButton = QtWidgets.QPushButton(self.uiTelnetConsoleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiTelnetConsolePreconfiguredCommandPushButton.sizePolicy().hasHeightForWidth())
        self.uiTelnetConsolePreconfiguredCommandPushButton.setSizePolicy(sizePolicy)
        self.uiTelnetConsolePreconfiguredCommandPushButton.setObjectName("uiTelnetConsolePreconfiguredCommandPushButton")
        self.horizontalLayout_9.addWidget(self.uiTelnetConsolePreconfiguredCommandPushButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addWidget(self.uiTelnetConsoleSettingsGroupBox)
        self.uiConsoleMiscGroupBox = QtWidgets.QGroupBox(self.uiConsoleTab)
        self.uiConsoleMiscGroupBox.setObjectName("uiConsoleMiscGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uiConsoleMiscGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.uiDelayConsoleAllSpinBox = QtWidgets.QSpinBox(self.uiConsoleMiscGroupBox)
        self.uiDelayConsoleAllSpinBox.setMaximum(10000)
        self.uiDelayConsoleAllSpinBox.setProperty("value", 500)
        self.uiDelayConsoleAllSpinBox.setObjectName("uiDelayConsoleAllSpinBox")
        self.gridLayout_7.addWidget(self.uiDelayConsoleAllSpinBox, 1, 0, 1, 1)
        self.uiSlowConsoleAllLabel = QtWidgets.QLabel(self.uiConsoleMiscGroupBox)
        self.uiSlowConsoleAllLabel.setObjectName("uiSlowConsoleAllLabel")
        self.gridLayout_7.addWidget(self.uiSlowConsoleAllLabel, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.uiConsoleMiscGroupBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.uiMiscTabWidget.addTab(self.uiConsoleTab, "")
        self.uiVNCTab = QtWidgets.QWidget()
        self.uiVNCTab.setObjectName("uiVNCTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.uiVNCTab)
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.uiVNCConsoleSettingsGroupBox = QtWidgets.QGroupBox(self.uiVNCTab)
        self.uiVNCConsoleSettingsGroupBox.setObjectName("uiVNCConsoleSettingsGroupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.uiVNCConsoleSettingsGroupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.uiVNCConsoleCommandLabel = QtWidgets.QLabel(self.uiVNCConsoleSettingsGroupBox)
        self.uiVNCConsoleCommandLabel.setObjectName("uiVNCConsoleCommandLabel")
        self.verticalLayout_8.addWidget(self.uiVNCConsoleCommandLabel)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.uiVNCConsoleCommandLineEdit = QtWidgets.QLineEdit(self.uiVNCConsoleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVNCConsoleCommandLineEdit.sizePolicy().hasHeightForWidth())
        self.uiVNCConsoleCommandLineEdit.setSizePolicy(sizePolicy)
        self.uiVNCConsoleCommandLineEdit.setReadOnly(True)
        self.uiVNCConsoleCommandLineEdit.setObjectName("uiVNCConsoleCommandLineEdit")
        self.horizontalLayout_8.addWidget(self.uiVNCConsoleCommandLineEdit)
        self.uiVNCConsolePreconfiguredCommandPushButton = QtWidgets.QPushButton(self.uiVNCConsoleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVNCConsolePreconfiguredCommandPushButton.sizePolicy().hasHeightForWidth())
        self.uiVNCConsolePreconfiguredCommandPushButton.setSizePolicy(sizePolicy)
        self.uiVNCConsolePreconfiguredCommandPushButton.setObjectName("uiVNCConsolePreconfiguredCommandPushButton")
        self.horizontalLayout_8.addWidget(self.uiVNCConsolePreconfiguredCommandPushButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.verticalLayout_6.addWidget(self.uiVNCConsoleSettingsGroupBox)
        self.uiMiscTabWidget.addTab(self.uiVNCTab, "")
        self.uiSPICETab = QtWidgets.QWidget()
        self.uiSPICETab.setObjectName("uiSPICETab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiSPICETab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiSPICEConsoleSettingsGroupBox = QtWidgets.QGroupBox(self.uiSPICETab)
        self.uiSPICEConsoleSettingsGroupBox.setObjectName("uiSPICEConsoleSettingsGroupBox")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.uiSPICEConsoleSettingsGroupBox)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.uiSPICEConsoleCommandLabel = QtWidgets.QLabel(self.uiSPICEConsoleSettingsGroupBox)
        self.uiSPICEConsoleCommandLabel.setObjectName("uiSPICEConsoleCommandLabel")
        self.verticalLayout_11.addWidget(self.uiSPICEConsoleCommandLabel)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.uiSPICEConsoleCommandLineEdit = QtWidgets.QLineEdit(self.uiSPICEConsoleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSPICEConsoleCommandLineEdit.sizePolicy().hasHeightForWidth())
        self.uiSPICEConsoleCommandLineEdit.setSizePolicy(sizePolicy)
        self.uiSPICEConsoleCommandLineEdit.setReadOnly(True)
        self.uiSPICEConsoleCommandLineEdit.setObjectName("uiSPICEConsoleCommandLineEdit")
        self.horizontalLayout_10.addWidget(self.uiSPICEConsoleCommandLineEdit)
        self.uiSPICEConsolePreconfiguredCommandPushButton = QtWidgets.QPushButton(self.uiSPICEConsoleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSPICEConsolePreconfiguredCommandPushButton.sizePolicy().hasHeightForWidth())
        self.uiSPICEConsolePreconfiguredCommandPushButton.setSizePolicy(sizePolicy)
        self.uiSPICEConsolePreconfiguredCommandPushButton.setObjectName("uiSPICEConsolePreconfiguredCommandPushButton")
        self.horizontalLayout_10.addWidget(self.uiSPICEConsolePreconfiguredCommandPushButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem5)
        self.gridLayout_2.addWidget(self.uiSPICEConsoleSettingsGroupBox, 0, 0, 1, 1)
        self.uiMiscTabWidget.addTab(self.uiSPICETab, "")
        self.uiSceneTab = QtWidgets.QWidget()
        self.uiSceneTab.setObjectName("uiSceneTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.uiSceneTab)
        self.gridLayout_8.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.uiRectangleSelectedItemCheckBox = QtWidgets.QCheckBox(self.uiSceneTab)
        self.uiRectangleSelectedItemCheckBox.setChecked(True)
        self.uiRectangleSelectedItemCheckBox.setObjectName("uiRectangleSelectedItemCheckBox")
        self.gridLayout_8.addWidget(self.uiRectangleSelectedItemCheckBox, 5, 0, 1, 2)
        self.uiSceneWidthLabel = QtWidgets.QLabel(self.uiSceneTab)
        self.uiSceneWidthLabel.setObjectName("uiSceneWidthLabel")
        self.gridLayout_8.addWidget(self.uiSceneWidthLabel, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiDefaultLabelFontPushButton = QtWidgets.QPushButton(self.uiSceneTab)
        self.uiDefaultLabelFontPushButton.setObjectName("uiDefaultLabelFontPushButton")
        self.horizontalLayout_5.addWidget(self.uiDefaultLabelFontPushButton)
        self.uiDefaultLabelColorPushButton = QtWidgets.QPushButton(self.uiSceneTab)
        self.uiDefaultLabelColorPushButton.setObjectName("uiDefaultLabelColorPushButton")
        self.horizontalLayout_5.addWidget(self.uiDefaultLabelColorPushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 10, 0, 1, 2)
        self.uiSceneHeightLabel = QtWidgets.QLabel(self.uiSceneTab)
        self.uiSceneHeightLabel.setObjectName("uiSceneHeightLabel")
        self.gridLayout_8.addWidget(self.uiSceneHeightLabel, 2, 0, 1, 1)
        self.uiSceneHeightSpinBox = QtWidgets.QSpinBox(self.uiSceneTab)
        self.uiSceneHeightSpinBox.setMinimum(500)
        self.uiSceneHeightSpinBox.setMaximum(1000000)
        self.uiSceneHeightSpinBox.setSingleStep(100)
        self.uiSceneHeightSpinBox.setProperty("value", 1000)
        self.uiSceneHeightSpinBox.setObjectName("uiSceneHeightSpinBox")
        self.gridLayout_8.addWidget(self.uiSceneHeightSpinBox, 3, 0, 1, 2)
        self.uiLabelPreviewLabel = QtWidgets.QLabel(self.uiSceneTab)
        self.uiLabelPreviewLabel.setObjectName("uiLabelPreviewLabel")
        self.gridLayout_8.addWidget(self.uiLabelPreviewLabel, 8, 0, 1, 1)
        self.uiDrawLinkStatusPointsCheckBox = QtWidgets.QCheckBox(self.uiSceneTab)
        self.uiDrawLinkStatusPointsCheckBox.setChecked(True)
        self.uiDrawLinkStatusPointsCheckBox.setObjectName("uiDrawLinkStatusPointsCheckBox")
        self.gridLayout_8.addWidget(self.uiDrawLinkStatusPointsCheckBox, 6, 0, 1, 1)
        self.uiDefaultLabelStylePlainTextEdit = QtWidgets.QPlainTextEdit(self.uiSceneTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiDefaultLabelStylePlainTextEdit.sizePolicy().hasHeightForWidth())
        self.uiDefaultLabelStylePlainTextEdit.setSizePolicy(sizePolicy)
        self.uiDefaultLabelStylePlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.uiDefaultLabelStylePlainTextEdit.setReadOnly(True)
        self.uiDefaultLabelStylePlainTextEdit.setObjectName("uiDefaultLabelStylePlainTextEdit")
        self.gridLayout_8.addWidget(self.uiDefaultLabelStylePlainTextEdit, 9, 0, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem7, 11, 0, 1, 1)
        self.uiSceneWidthSpinBox = QtWidgets.QSpinBox(self.uiSceneTab)
        self.uiSceneWidthSpinBox.setMinimum(500)
        self.uiSceneWidthSpinBox.setMaximum(1000000)
        self.uiSceneWidthSpinBox.setSingleStep(100)
        self.uiSceneWidthSpinBox.setProperty("value", 2000)
        self.uiSceneWidthSpinBox.setObjectName("uiSceneWidthSpinBox")
        self.gridLayout_8.addWidget(self.uiSceneWidthSpinBox, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.uiSceneTab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 4, 0, 1, 1)
        self.uiShowInterfaceLabelsOnNewProject = QtWidgets.QCheckBox(self.uiSceneTab)
        self.uiShowInterfaceLabelsOnNewProject.setObjectName("uiShowInterfaceLabelsOnNewProject")
        self.gridLayout_8.addWidget(self.uiShowInterfaceLabelsOnNewProject, 7, 0, 1, 1)
        self.uiMiscTabWidget.addTab(self.uiSceneTab, "")
        self.uiMiscTab = QtWidgets.QWidget()
        self.uiMiscTab.setObjectName("uiMiscTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiMiscTab)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiCheckForUpdateCheckBox = QtWidgets.QCheckBox(self.uiMiscTab)
        self.uiCheckForUpdateCheckBox.setChecked(True)
        self.uiCheckForUpdateCheckBox.setObjectName("uiCheckForUpdateCheckBox")
        self.verticalLayout_2.addWidget(self.uiCheckForUpdateCheckBox)
        self.uiCrashReportCheckBox = QtWidgets.QCheckBox(self.uiMiscTab)
        self.uiCrashReportCheckBox.setChecked(True)
        self.uiCrashReportCheckBox.setObjectName("uiCrashReportCheckBox")
        self.verticalLayout_2.addWidget(self.uiCrashReportCheckBox)
        self.uiStatsCheckBox = QtWidgets.QCheckBox(self.uiMiscTab)
        self.uiStatsCheckBox.setChecked(True)
        self.uiStatsCheckBox.setObjectName("uiStatsCheckBox")
        self.verticalLayout_2.addWidget(self.uiStatsCheckBox)
        self.uiOverlayNotificationsCheckBox = QtWidgets.QCheckBox(self.uiMiscTab)
        self.uiOverlayNotificationsCheckBox.setObjectName("uiOverlayNotificationsCheckBox")
        self.verticalLayout_2.addWidget(self.uiOverlayNotificationsCheckBox)
        self.uiExperimentalFeaturesCheckBox = QtWidgets.QCheckBox(self.uiMiscTab)
        self.uiExperimentalFeaturesCheckBox.setObjectName("uiExperimentalFeaturesCheckBox")
        self.verticalLayout_2.addWidget(self.uiExperimentalFeaturesCheckBox)
        self.uiHdpiCheckBox = QtWidgets.QCheckBox(self.uiMiscTab)
        self.uiHdpiCheckBox.setObjectName("uiHdpiCheckBox")
        self.verticalLayout_2.addWidget(self.uiHdpiCheckBox)
        self.uiMultiProfilesCheckBox = QtWidgets.QCheckBox(self.uiMiscTab)
        self.uiMultiProfilesCheckBox.setObjectName("uiMultiProfilesCheckBox")
        self.verticalLayout_2.addWidget(self.uiMultiProfilesCheckBox)
        self.uiDirectFileUpload = QtWidgets.QCheckBox(self.uiMiscTab)
        self.uiDirectFileUpload.setObjectName("uiDirectFileUpload")
        self.verticalLayout_2.addWidget(self.uiDirectFileUpload)
        spacerItem8 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.uiMiscTabWidget.addTab(self.uiMiscTab, "")
        self.verticalLayout.addWidget(self.uiMiscTabWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(324, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.uiRestoreDefaultsPushButton = QtWidgets.QPushButton(GeneralPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName("uiRestoreDefaultsPushButton")
        self.horizontalLayout_6.addWidget(self.uiRestoreDefaultsPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(GeneralPreferencesPageWidget)
        self.uiMiscTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GeneralPreferencesPageWidget)

    def retranslateUi(self, GeneralPreferencesPageWidget):
        _translate = QtCore.QCoreApplication.translate
        GeneralPreferencesPageWidget.setWindowTitle(_translate("GeneralPreferencesPageWidget", "General"))
        self.uiLocalPathsGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Local paths"))
        self.uiProjectsPathLabel.setText(_translate("GeneralPreferencesPageWidget", "My projects:"))
        self.uiProjectsPathLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "Directory where your GNS3 projects are stored"))
        self.uiProjectsPathToolButton.setText(_translate("GeneralPreferencesPageWidget", "&Browse..."))
        self.label.setText(_translate("GeneralPreferencesPageWidget", "My symbols:"))
        self.uiSymbolsPathToolButton.setText(_translate("GeneralPreferencesPageWidget", "Browse..."))
        self.uiConfigsPathLabel.setText(_translate("GeneralPreferencesPageWidget", "My configs:"))
        self.uiConfigsPathLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "Directory where your binary images (e.g. IOS) are stored"))
        self.uiConfigsPathToolButton.setText(_translate("GeneralPreferencesPageWidget", "&Browse..."))
        self.label_3.setText(_translate("GeneralPreferencesPageWidget", "My custom appliances:"))
        self.uiAppliancesPathToolButton.setText(_translate("GeneralPreferencesPageWidget", "Browse..."))
        self.uiStyleGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Style"))
        self.uiConfigurationFileGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Configuration file"))
        self.uiImportConfigurationFilePushButton.setText(_translate("GeneralPreferencesPageWidget", "&Import"))
        self.uiExportConfigurationFilePushButton.setText(_translate("GeneralPreferencesPageWidget", "&Export"))
        self.uiBrowseConfigurationPushButton.setText(_translate("GeneralPreferencesPageWidget", "Browse configuration directory"))
        self.uiConfigurationFileLabel.setText(_translate("GeneralPreferencesPageWidget", "Unknown location"))
        self.uiMiscTabWidget.setTabText(self.uiMiscTabWidget.indexOf(self.uiGeneralTab), _translate("GeneralPreferencesPageWidget", "General"))
        self.uiLocalBinaryImagePathsGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Local paths"))
        self.uiImagesPathLabel.setText(_translate("GeneralPreferencesPageWidget", "My binary images:"))
        self.uiImagesPathLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "Directory where your binary images (e.g. IOS) are stored"))
        self.uiImagesPathToolButton.setText(_translate("GeneralPreferencesPageWidget", "&Browse..."))
        self.uiImageDirectoriesLabel.setText(_translate("GeneralPreferencesPageWidget", "Additional search locations for binary images:"))
        self.uiImageDirectoriesAddPushButton.setText(_translate("GeneralPreferencesPageWidget", "Add"))
        self.uiImageDirectoriesDeletePushButton.setText(_translate("GeneralPreferencesPageWidget", "Delete"))
        self.uiMiscTabWidget.setTabText(self.uiMiscTabWidget.indexOf(self.uiImagesTab), _translate("GeneralPreferencesPageWidget", "Binary images"))
        self.uiTelnetConsoleSettingsGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Console settings"))
        self.uiTelnetConsoleCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Console application command for Telnet:"))
        self.uiTelnetConsoleCommandLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "<html><head/><body><p>Command line replacements:</p>\n"
"<ul>\n"
"<li>%h = console IP or hostname</li>\n"
"<li>%p = console port</li>\n"
"<li>%P = VNC display</li>\n"
"<li>%s = path of the serial connection</li>\n"
"<li>%d = title of the console</li>\n"
"<li>%i = project UUID</li>\n"
"<li>%c = server URL</li>\n"
"</ul>\n"
"</body></html>"))
        self.uiTelnetConsolePreconfiguredCommandPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Edit"))
        self.uiConsoleMiscGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Miscellaneous"))
        self.uiDelayConsoleAllSpinBox.setSuffix(_translate("GeneralPreferencesPageWidget", " ms"))
        self.uiSlowConsoleAllLabel.setText(_translate("GeneralPreferencesPageWidget", "Delay between each console launch when consoling to all devices:"))
        self.uiMiscTabWidget.setTabText(self.uiMiscTabWidget.indexOf(self.uiConsoleTab), _translate("GeneralPreferencesPageWidget", "Console applications"))
        self.uiVNCConsoleSettingsGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Settings for VNC connections"))
        self.uiVNCConsoleCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Console application command for VNC:"))
        self.uiVNCConsoleCommandLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "<html><head/><body><p>Command line replacements:</p>\n"
"<ul>\n"
"<li>%h = console IP or hostname</li>\n"
"<li>%p = console port</li>\n"
"<li>%P = VNC display</li>\n"
"<li>%s = path of the serial connection</li>\n"
"<li>%d = title of the console</li>\n"
"<li>%i = project UUID</li>\n"
"<li>%c = server URL</li>\n"
"</ul>\n"
"</body></html>"))
        self.uiVNCConsolePreconfiguredCommandPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Edit"))
        self.uiMiscTabWidget.setTabText(self.uiMiscTabWidget.indexOf(self.uiVNCTab), _translate("GeneralPreferencesPageWidget", "VNC"))
        self.uiSPICEConsoleSettingsGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Settings for SPICE connections"))
        self.uiSPICEConsoleCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Console application command for SPICE:"))
        self.uiSPICEConsoleCommandLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "<html><head/><body><p>Command line replacements:</p>\n"
"<ul>\n"
"<li>%h = console IP or hostname</li>\n"
"<li>%p = console port</li>\n"
"<li>%P = VNC display</li>\n"
"<li>%s = path of the serial connection</li>\n"
"<li>%d = title of the console</li>\n"
"<li>%i = project UUID</li>\n"
"<li>%c = server URL</li>\n"
"</ul>\n"
"</body></html>"))
        self.uiSPICEConsolePreconfiguredCommandPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Edit"))
        self.uiMiscTabWidget.setTabText(self.uiMiscTabWidget.indexOf(self.uiSPICETab), _translate("GeneralPreferencesPageWidget", "SPICE"))
        self.uiRectangleSelectedItemCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Draw a rectangle when an item is selected"))
        self.uiSceneWidthLabel.setText(_translate("GeneralPreferencesPageWidget", "Default width:"))
        self.uiDefaultLabelFontPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Select default font"))
        self.uiDefaultLabelColorPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Select default color"))
        self.uiSceneHeightLabel.setText(_translate("GeneralPreferencesPageWidget", "Default height:"))
        self.uiSceneHeightSpinBox.setSuffix(_translate("GeneralPreferencesPageWidget", " pixels"))
        self.uiLabelPreviewLabel.setText(_translate("GeneralPreferencesPageWidget", "Default label style:"))
        self.uiDrawLinkStatusPointsCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Draw link status points"))
        self.uiDefaultLabelStylePlainTextEdit.setPlainText(_translate("GeneralPreferencesPageWidget", "AaBbYyZz"))
        self.uiSceneWidthSpinBox.setSuffix(_translate("GeneralPreferencesPageWidget", " pixels"))
        self.label_2.setText(_translate("GeneralPreferencesPageWidget", "If you want to change the size of the current project. Via the project menu you can edit it."))
        self.uiShowInterfaceLabelsOnNewProject.setText(_translate("GeneralPreferencesPageWidget", "Show interface labels on new project"))
        self.uiMiscTabWidget.setTabText(self.uiMiscTabWidget.indexOf(self.uiSceneTab), _translate("GeneralPreferencesPageWidget", "Topology view"))
        self.uiCheckForUpdateCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Automatically check for update"))
        self.uiCrashReportCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Send anonymous crash reports"))
        self.uiStatsCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Send anonymous usage statistics"))
        self.uiOverlayNotificationsCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Display error, warning and info in a overlay popup"))
        self.uiExperimentalFeaturesCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Enable experimental features (dangerous, restart required)"))
        self.uiHdpiCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Enable HDPI mode (this may crash the application on Linux, restart required)"))
        self.uiMultiProfilesCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Request for profile settings at application startup  (work profile / home profile)"))
        self.uiDirectFileUpload.setText(_translate("GeneralPreferencesPageWidget", "Upload files directly to computes (experimental, requires computes visibility from GUI network)"))
        self.uiMiscTabWidget.setTabText(self.uiMiscTabWidget.indexOf(self.uiMiscTab), _translate("GeneralPreferencesPageWidget", "Miscellaneous"))
        self.uiRestoreDefaultsPushButton.setText(_translate("GeneralPreferencesPageWidget", "Restore defaults"))

