# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.11.4/gns3/ui/snapshots_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SnapshotsDialog(object):
    def setupUi(self, SnapshotsDialog):
        SnapshotsDialog.setObjectName("SnapshotsDialog")
        SnapshotsDialog.setWindowModality(QtCore.Qt.WindowModal)
        SnapshotsDialog.resize(496, 288)
        SnapshotsDialog.setStyleSheet("QWidget{\n"
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
        self.gridLayout = QtWidgets.QGridLayout(SnapshotsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.uiSnapshotsList = QtWidgets.QListWidget(SnapshotsDialog)
        self.uiSnapshotsList.setObjectName("uiSnapshotsList")
        self.gridLayout.addWidget(self.uiSnapshotsList, 0, 0, 1, 4)
        self.uiCreatePushButton = QtWidgets.QPushButton(SnapshotsDialog)
        self.uiCreatePushButton.setObjectName("uiCreatePushButton")
        self.gridLayout.addWidget(self.uiCreatePushButton, 1, 0, 1, 1)
        self.uiRestorePushButton = QtWidgets.QPushButton(SnapshotsDialog)
        self.uiRestorePushButton.setEnabled(False)
        self.uiRestorePushButton.setObjectName("uiRestorePushButton")
        self.gridLayout.addWidget(self.uiRestorePushButton, 1, 2, 1, 1)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(SnapshotsDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.gridLayout.addWidget(self.uiButtonBox, 1, 3, 1, 1)
        self.uiDeletePushButton = QtWidgets.QPushButton(SnapshotsDialog)
        self.uiDeletePushButton.setEnabled(False)
        self.uiDeletePushButton.setObjectName("uiDeletePushButton")
        self.gridLayout.addWidget(self.uiDeletePushButton, 1, 1, 1, 1)

        self.retranslateUi(SnapshotsDialog)
        self.uiButtonBox.accepted.connect(SnapshotsDialog.accept)
        self.uiButtonBox.rejected.connect(SnapshotsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SnapshotsDialog)

    def retranslateUi(self, SnapshotsDialog):
        _translate = QtCore.QCoreApplication.translate
        SnapshotsDialog.setWindowTitle(_translate("SnapshotsDialog", "Snapshots"))
        self.uiCreatePushButton.setText(_translate("SnapshotsDialog", "&Create"))
        self.uiRestorePushButton.setText(_translate("SnapshotsDialog", "&Restore"))
        self.uiDeletePushButton.setText(_translate("SnapshotsDialog", "&Delete"))

