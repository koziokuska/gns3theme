# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/GitRepos/gns3theme/gns3-gui-2.1.4/gns3/ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(984, 715)
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QPushButton#uiNewAppliancePushButton{\n"
"border: none;\n"
"}\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 12px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
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
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.uiCentralWidget = QtWidgets.QWidget(MainWindow)
        self.uiCentralWidget.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QPushButton#uiNewAppliancePushButton{\n"
"border: none;\n"
"}\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 12px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
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
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.uiCentralWidget.setObjectName("uiCentralWidget")
        self.gridlayout = QtWidgets.QGridLayout(self.uiCentralWidget)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")
        self.uiGraphicsView = GraphicsView(self.uiCentralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiGraphicsView.sizePolicy().hasHeightForWidth())
        self.uiGraphicsView.setSizePolicy(sizePolicy)
        self.uiGraphicsView.setObjectName("uiGraphicsView")
        self.gridlayout.addWidget(self.uiGraphicsView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.uiCentralWidget)
        self.uiMenuBar = QtWidgets.QMenuBar(MainWindow)
        self.uiMenuBar.setGeometry(QtCore.QRect(0, 0, 984, 27))
        self.uiMenuBar.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QPushButton#uiNewAppliancePushButton{\n"
"border: none;\n"
"}\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 12px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
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
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.uiMenuBar.setObjectName("uiMenuBar")
        self.uiEditMenu = QtWidgets.QMenu(self.uiMenuBar)
        self.uiEditMenu.setObjectName("uiEditMenu")
        self.uiFileMenu = QtWidgets.QMenu(self.uiMenuBar)
        self.uiFileMenu.setObjectName("uiFileMenu")
        self.uiHelpMenu = QtWidgets.QMenu(self.uiMenuBar)
        self.uiHelpMenu.setObjectName("uiHelpMenu")
        self.uiViewMenu = QtWidgets.QMenu(self.uiMenuBar)
        self.uiViewMenu.setObjectName("uiViewMenu")
        self.uiDocksMenu = QtWidgets.QMenu(self.uiViewMenu)
        self.uiDocksMenu.setObjectName("uiDocksMenu")
        self.uiControlMenu = QtWidgets.QMenu(self.uiMenuBar)
        self.uiControlMenu.setObjectName("uiControlMenu")
        self.uiAnnotateMenu = QtWidgets.QMenu(self.uiMenuBar)
        self.uiAnnotateMenu.setObjectName("uiAnnotateMenu")
        self.uiDeviceMenu = QtWidgets.QMenu(self.uiMenuBar)
        self.uiDeviceMenu.setObjectName("uiDeviceMenu")
        self.uiToolsMenu = QtWidgets.QMenu(self.uiMenuBar)
        self.uiToolsMenu.setObjectName("uiToolsMenu")
        MainWindow.setMenuBar(self.uiMenuBar)
        self.uiGeneralToolBar = QtWidgets.QToolBar(MainWindow)
        self.uiGeneralToolBar.setToolTip("")
        self.uiGeneralToolBar.setStatusTip("")
        self.uiGeneralToolBar.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QPushButton#uiNewAppliancePushButton{\n"
"border: none;\n"
"}\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 12px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
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
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.uiGeneralToolBar.setOrientation(QtCore.Qt.Horizontal)
        self.uiGeneralToolBar.setIconSize(QtCore.QSize(32, 32))
        self.uiGeneralToolBar.setObjectName("uiGeneralToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.uiGeneralToolBar)
        self.uiNodesDockWidget = NodesDockWidget(MainWindow)
        self.uiNodesDockWidget.setEnabled(True)
        self.uiNodesDockWidget.setVisible(True)
        self.uiNodesDockWidget.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QPushButton#uiNewAppliancePushButton{\n"
"border: none;\n"
"}\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 12px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
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
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.uiNodesDockWidget.setFloating(False)
        self.uiNodesDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.uiNodesDockWidget.setObjectName("uiNodesDockWidget")
        self.uiNodesDockWidgetContents = QtWidgets.QWidget()
        self.uiNodesDockWidgetContents.setObjectName("uiNodesDockWidgetContents")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.uiNodesDockWidgetContents)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, -1, 5, 5)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiNodesFilterComboBox = QtWidgets.QComboBox(self.uiNodesDockWidgetContents)
        self.uiNodesFilterComboBox.setObjectName("uiNodesFilterComboBox")
        self.uiNodesFilterComboBox.addItem("")
        self.uiNodesFilterComboBox.addItem("")
        self.uiNodesFilterComboBox.addItem("")
        self.uiNodesFilterComboBox.addItem("")
        self.verticalLayout.addWidget(self.uiNodesFilterComboBox)
        self.uiNodesFilterLineEdit = QtWidgets.QLineEdit(self.uiNodesDockWidgetContents)
        self.uiNodesFilterLineEdit.setObjectName("uiNodesFilterLineEdit")
        self.verticalLayout.addWidget(self.uiNodesFilterLineEdit)
        self.vboxlayout.addLayout(self.verticalLayout)
        self.uiNodesView = NodesView(self.uiNodesDockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNodesView.sizePolicy().hasHeightForWidth())
        self.uiNodesView.setSizePolicy(sizePolicy)
        self.uiNodesView.setDragEnabled(False)
        self.uiNodesView.setIconSize(QtCore.QSize(32, 32))
        self.uiNodesView.setRootIsDecorated(False)
        self.uiNodesView.setObjectName("uiNodesView")
        self.uiNodesView.header().setVisible(False)
        self.vboxlayout.addWidget(self.uiNodesView)
        self.uiNewAppliancePushButton = QtWidgets.QPushButton(self.uiNodesDockWidgetContents)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiNewAppliancePushButton.setIcon(icon)
        self.uiNewAppliancePushButton.setAutoDefault(False)
        self.uiNewAppliancePushButton.setFlat(True)
        self.uiNewAppliancePushButton.setObjectName("uiNewAppliancePushButton")
        self.vboxlayout.addWidget(self.uiNewAppliancePushButton)
        self.uiNodesDockWidget.setWidget(self.uiNodesDockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.uiNodesDockWidget)
        self.uiBrowsersToolBar = QtWidgets.QToolBar(MainWindow)
        self.uiBrowsersToolBar.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QPushButton#uiNewAppliancePushButton{\n"
"border: none;\n"
"}\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 12px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
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
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.uiBrowsersToolBar.setIconSize(QtCore.QSize(48, 48))
        self.uiBrowsersToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.uiBrowsersToolBar.setObjectName("uiBrowsersToolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.uiBrowsersToolBar)
        self.uiControlToolBar = QtWidgets.QToolBar(MainWindow)
        self.uiControlToolBar.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QPushButton#uiNewAppliancePushButton{\n"
"border: none;\n"
"}\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 12px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
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
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.uiControlToolBar.setIconSize(QtCore.QSize(32, 32))
        self.uiControlToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.uiControlToolBar.setObjectName("uiControlToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.uiControlToolBar)
        self.uiConsoleDockWidget = QtWidgets.QDockWidget(MainWindow)
        self.uiConsoleDockWidget.setMaximumSize(QtCore.QSize(524287, 524287))
        self.uiConsoleDockWidget.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QPushButton#uiNewAppliancePushButton{\n"
"border: none;\n"
"}\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 12px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
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
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.uiConsoleDockWidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.uiConsoleDockWidget.setObjectName("uiConsoleDockWidget")
        self.uiConsoleDockWidgetContents = QtWidgets.QWidget()
        self.uiConsoleDockWidgetContents.setObjectName("uiConsoleDockWidgetContents")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.uiConsoleDockWidgetContents)
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.uiConsoleTextEdit = ConsoleView(self.uiConsoleDockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiConsoleTextEdit.sizePolicy().hasHeightForWidth())
        self.uiConsoleTextEdit.setSizePolicy(sizePolicy)
        self.uiConsoleTextEdit.setObjectName("uiConsoleTextEdit")
        self.vboxlayout1.addWidget(self.uiConsoleTextEdit)
        self.uiConsoleDockWidget.setWidget(self.uiConsoleDockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.uiConsoleDockWidget)
        self.uiAnnotationToolBar = QtWidgets.QToolBar(MainWindow)
        self.uiAnnotationToolBar.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QPushButton#uiNewAppliancePushButton{\n"
"border: none;\n"
"}\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 12px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
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
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.uiAnnotationToolBar.setIconSize(QtCore.QSize(32, 32))
        self.uiAnnotationToolBar.setObjectName("uiAnnotationToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.uiAnnotationToolBar)
        self.uiTopologySummaryDockWidget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiTopologySummaryDockWidget.sizePolicy().hasHeightForWidth())
        self.uiTopologySummaryDockWidget.setSizePolicy(sizePolicy)
        self.uiTopologySummaryDockWidget.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QPushButton#uiNewAppliancePushButton{\n"
"border: none;\n"
"}\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 12px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
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
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.uiTopologySummaryDockWidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.uiTopologySummaryDockWidget.setObjectName("uiTopologySummaryDockWidget")
        self.uiTopologySummaryDockWidgetContents = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiTopologySummaryDockWidgetContents.sizePolicy().hasHeightForWidth())
        self.uiTopologySummaryDockWidgetContents.setSizePolicy(sizePolicy)
        self.uiTopologySummaryDockWidgetContents.setObjectName("uiTopologySummaryDockWidgetContents")
        self.gridlayout1 = QtWidgets.QGridLayout(self.uiTopologySummaryDockWidgetContents)
        self.gridlayout1.setContentsMargins(0, 0, 0, 0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")
        self.uiTopologySummaryTreeWidget = TopologySummaryView(self.uiTopologySummaryDockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiTopologySummaryTreeWidget.sizePolicy().hasHeightForWidth())
        self.uiTopologySummaryTreeWidget.setSizePolicy(sizePolicy)
        self.uiTopologySummaryTreeWidget.setObjectName("uiTopologySummaryTreeWidget")
        self.uiTopologySummaryTreeWidget.header().setVisible(True)
        self.gridlayout1.addWidget(self.uiTopologySummaryTreeWidget, 0, 0, 1, 1)
        self.uiTopologySummaryDockWidget.setWidget(self.uiTopologySummaryDockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.uiTopologySummaryDockWidget)
        self.uiComputeSummaryDockWidget = QtWidgets.QDockWidget(MainWindow)
        self.uiComputeSummaryDockWidget.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QPushButton#uiNewAppliancePushButton{\n"
"border: none;\n"
"}\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 12px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
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
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.uiComputeSummaryDockWidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.uiComputeSummaryDockWidget.setObjectName("uiComputeSummaryDockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.uiComputeSummaryTreeWidget = ComputeSummaryView(self.dockWidgetContents)
        self.uiComputeSummaryTreeWidget.setObjectName("uiComputeSummaryTreeWidget")
        self.uiComputeSummaryTreeWidget.headerItem().setText(0, "1")
        self.uiComputeSummaryTreeWidget.header().setVisible(False)
        self.gridLayout.addWidget(self.uiComputeSummaryTreeWidget, 0, 0, 1, 1)
        self.uiComputeSummaryDockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.uiComputeSummaryDockWidget)
        self.uiStatusBar = StatusBar(MainWindow)
        self.uiStatusBar.setStyleSheet("QWidget{\n"
"    background-color: #002b36;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: #002b36;\n"
"}\n"
"\n"
"QDockWidget::title{\n"
"    background: #073642;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar{\n"
"    color: #839496;\n"
"    font: bold 14px;\n"
"}\n"
"QTextEdit, QPlainTextEdit, QLineEdit, QSpinBox, QComboBox {\n"
"  background-color: #073642;\n"
"  font: 13px;\n"
"  color: #839496;\n"
"}\n"
"QTextEdit#uiConsoleTextEdit {\n"
"  background-color: #002b36;\n"
"  font: 13px;\n"
"}\n"
"QTabWidget {\n"
"    font: 14px;\n"
"    border-top: 2px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"    background: #073642;\n"
"    color: #839496;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    border-top-right-radius: 6px;\n"
"    border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #8a8a8a;\n"
"    color: #1d2021;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #808080;\n"
"    font: 14px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: #073642;\n"
"    width: 1px;\n"
"    height: 1px;\n"
"}\n"
"QComboBox {\n"
"    selection-background-color: #d75f00;\n"
"    selection-color: #1c1c1c;\n"
"}\n"
"\n"
"QToolBar{\n"
"    background: #073642;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #8a8a8a;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QPushButton#uiNewAppliancePushButton{\n"
"border: none;\n"
"}\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #1d2021;\n"
"    font: 14px;\n"
"}\n"
"QTreeWidget, QListWidget {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"    alternate-background-color: #073642;\n"
"    font: 12px;\n"
"}\n"
"QTreeWidget#uiTreeWidget {\n"
"    background-color: #073642;\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QTreeWidget::item:selected, QTreeWidget::item:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #002b36;\n"
"    color: #839496;\n"
"}\n"
"QLabel {\n"
"    color: #839496;\n"
"    font: 14px;\n"
"}\n"
"QLabel#uiTitleLabel {\n"
"    color: #839496;\n"
"    font: bold 16px;\n"
"}\n"
"QMenu::item:selected,QToolButton::hover,QPushButton::hover,QTabBar::tab:hover {\n"
"    background-color: #d75f00;\n"
"    color: #1c1c1c;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #073642;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #073642;\n"
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
"    background-color: #073642;\n"
"    color: #839496;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #839496;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"\n"
"\n"
"")
        self.uiStatusBar.setObjectName("uiStatusBar")
        MainWindow.setStatusBar(self.uiStatusBar)
        self.uiAboutAction = QtWidgets.QAction(MainWindow)
        self.uiAboutAction.setMenuRole(QtWidgets.QAction.AboutRole)
        self.uiAboutAction.setObjectName("uiAboutAction")
        self.uiQuitAction = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/quit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiQuitAction.setIcon(icon1)
        self.uiQuitAction.setObjectName("uiQuitAction")
        self.uiOpenProjectAction = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiOpenProjectAction.setIcon(icon2)
        self.uiOpenProjectAction.setObjectName("uiOpenProjectAction")
        self.uiOnlineHelpAction = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiOnlineHelpAction.setIcon(icon3)
        self.uiOnlineHelpAction.setObjectName("uiOnlineHelpAction")
        self.uiScreenshotAction = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/camera-photo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icons/camera-photo-hover.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiScreenshotAction.setIcon(icon4)
        self.uiScreenshotAction.setObjectName("uiScreenshotAction")
        self.uiStartAllAction = QtWidgets.QAction(MainWindow)
        self.uiStartAllAction.setEnabled(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/start.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/icons/start-hover.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiStartAllAction.setIcon(icon5)
        self.uiStartAllAction.setObjectName("uiStartAllAction")
        self.uiStopAllAction = QtWidgets.QAction(MainWindow)
        self.uiStopAllAction.setEnabled(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(":/icons/stop-hover.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiStopAllAction.setIcon(icon6)
        self.uiStopAllAction.setObjectName("uiStopAllAction")
        self.uiConsoleAllAction = QtWidgets.QAction(MainWindow)
        self.uiConsoleAllAction.setEnabled(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/console.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiConsoleAllAction.setIcon(icon7)
        self.uiConsoleAllAction.setObjectName("uiConsoleAllAction")
        self.uiAboutQtAction = QtWidgets.QAction(MainWindow)
        self.uiAboutQtAction.setMenuRole(QtWidgets.QAction.AboutQtRole)
        self.uiAboutQtAction.setObjectName("uiAboutQtAction")
        self.uiZoomInAction = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap(":/icons/zoom-in-hover.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiZoomInAction.setIcon(icon8)
        self.uiZoomInAction.setObjectName("uiZoomInAction")
        self.uiZoomOutAction = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap(":/icons/zoom-out-hover.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiZoomOutAction.setIcon(icon9)
        self.uiZoomOutAction.setObjectName("uiZoomOutAction")
        self.uiZoomResetAction = QtWidgets.QAction(MainWindow)
        self.uiZoomResetAction.setObjectName("uiZoomResetAction")
        self.uiSelectAllAction = QtWidgets.QAction(MainWindow)
        self.uiSelectAllAction.setObjectName("uiSelectAllAction")
        self.uiSelectNoneAction = QtWidgets.QAction(MainWindow)
        self.uiSelectNoneAction.setObjectName("uiSelectNoneAction")
        self.uiPreferencesAction = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/applications.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiPreferencesAction.setIcon(icon10)
        self.uiPreferencesAction.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.uiPreferencesAction.setObjectName("uiPreferencesAction")
        self.uiSuspendAllAction = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap(":/icons/pause-hover.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiSuspendAllAction.setIcon(icon11)
        self.uiSuspendAllAction.setObjectName("uiSuspendAllAction")
        self.uiAddNoteAction = QtWidgets.QAction(MainWindow)
        self.uiAddNoteAction.setCheckable(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/add-note.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiAddNoteAction.setIcon(icon12)
        self.uiAddNoteAction.setObjectName("uiAddNoteAction")
        self.uiNewProjectAction = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/new-project.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiNewProjectAction.setIcon(icon13)
        self.uiNewProjectAction.setObjectName("uiNewProjectAction")
        self.uiImportExportConfigsAction = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/import_export_configs.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiImportExportConfigsAction.setIcon(icon14)
        self.uiImportExportConfigsAction.setObjectName("uiImportExportConfigsAction")
        self.uiInsertImageAction = QtWidgets.QAction(MainWindow)
        self.uiInsertImageAction.setCheckable(False)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiInsertImageAction.setIcon(icon15)
        self.uiInsertImageAction.setObjectName("uiInsertImageAction")
        self.uiDrawRectangleAction = QtWidgets.QAction(MainWindow)
        self.uiDrawRectangleAction.setCheckable(True)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/rectangle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon16.addPixmap(QtGui.QPixmap(":/icons/rectangle-hover.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiDrawRectangleAction.setIcon(icon16)
        self.uiDrawRectangleAction.setObjectName("uiDrawRectangleAction")
        self.uiDrawEllipseAction = QtWidgets.QAction(MainWindow)
        self.uiDrawEllipseAction.setCheckable(True)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/ellipse.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon17.addPixmap(QtGui.QPixmap(":/icons/ellipse-hover.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiDrawEllipseAction.setIcon(icon17)
        self.uiDrawEllipseAction.setObjectName("uiDrawEllipseAction")
        self.uiShowPortNamesAction = QtWidgets.QAction(MainWindow)
        self.uiShowPortNamesAction.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/show-interface-names.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiShowPortNamesAction.setIcon(icon18)
        self.uiShowPortNamesAction.setObjectName("uiShowPortNamesAction")
        self.uiSnapshotAction = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/snapshot.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiSnapshotAction.setIcon(icon19)
        self.uiSnapshotAction.setObjectName("uiSnapshotAction")
        self.uiShowLayersAction = QtWidgets.QAction(MainWindow)
        self.uiShowLayersAction.setCheckable(True)
        self.uiShowLayersAction.setObjectName("uiShowLayersAction")
        self.uiSnapToGridAction = QtWidgets.QAction(MainWindow)
        self.uiSnapToGridAction.setCheckable(True)
        self.uiSnapToGridAction.setObjectName("uiSnapToGridAction")
        self.uiSaveProjectAsAction = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/save-as-project.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiSaveProjectAsAction.setIcon(icon20)
        self.uiSaveProjectAsAction.setObjectName("uiSaveProjectAsAction")
        self.uiReloadAllAction = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/reload.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiReloadAllAction.setIcon(icon21)
        self.uiReloadAllAction.setObjectName("uiReloadAllAction")
        self.uiAuxConsoleAllAction = QtWidgets.QAction(MainWindow)
        self.uiAuxConsoleAllAction.setEnabled(True)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icons/aux-console.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiAuxConsoleAllAction.setIcon(icon22)
        self.uiAuxConsoleAllAction.setObjectName("uiAuxConsoleAllAction")
        self.uiResetPortLabelsAction = QtWidgets.QAction(MainWindow)
        self.uiResetPortLabelsAction.setObjectName("uiResetPortLabelsAction")
        self.uiCheckForUpdateAction = QtWidgets.QAction(MainWindow)
        self.uiCheckForUpdateAction.setObjectName("uiCheckForUpdateAction")
        self.uiBrowseRoutersAction = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons/router.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon23.addPixmap(QtGui.QPixmap(":/icons/router-hover.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiBrowseRoutersAction.setIcon(icon23)
        self.uiBrowseRoutersAction.setObjectName("uiBrowseRoutersAction")
        self.uiBrowseSwitchesAction = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/icons/switch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon24.addPixmap(QtGui.QPixmap(":/icons/switch-hover.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiBrowseSwitchesAction.setIcon(icon24)
        self.uiBrowseSwitchesAction.setObjectName("uiBrowseSwitchesAction")
        self.uiBrowseEndDevicesAction = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/icons/PC.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon25.addPixmap(QtGui.QPixmap(":/icons/PC-hover.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiBrowseEndDevicesAction.setIcon(icon25)
        self.uiBrowseEndDevicesAction.setObjectName("uiBrowseEndDevicesAction")
        self.uiBrowseSecurityDevicesAction = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/icons/firewall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon26.addPixmap(QtGui.QPixmap(":/icons/firewall-hover.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiBrowseSecurityDevicesAction.setIcon(icon26)
        self.uiBrowseSecurityDevicesAction.setObjectName("uiBrowseSecurityDevicesAction")
        self.uiBrowseAllDevicesAction = QtWidgets.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/icons/browse-all-icons.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon27.addPixmap(QtGui.QPixmap(":/icons/browse-all-icons-hover.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.uiBrowseAllDevicesAction.setIcon(icon27)
        self.uiBrowseAllDevicesAction.setObjectName("uiBrowseAllDevicesAction")
        self.uiAddLinkAction = QtWidgets.QAction(MainWindow)
        self.uiAddLinkAction.setCheckable(True)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/icons/connection-new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon28.addPixmap(QtGui.QPixmap(":/icons/cancel-connection.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon28.addPixmap(QtGui.QPixmap(":/icons/connection-new-hover.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon28.addPixmap(QtGui.QPixmap(":/icons/cancel-connection.svg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.uiAddLinkAction.setIcon(icon28)
        self.uiAddLinkAction.setObjectName("uiAddLinkAction")
        self.uiFitInViewAction = QtWidgets.QAction(MainWindow)
        self.uiFitInViewAction.setObjectName("uiFitInViewAction")
        self.uiActionFullscreen = QtWidgets.QAction(MainWindow)
        self.uiActionFullscreen.setObjectName("uiActionFullscreen")
        self.uiSetupWizard = QtWidgets.QAction(MainWindow)
        self.uiSetupWizard.setMenuRole(QtWidgets.QAction.NoRole)
        self.uiSetupWizard.setObjectName("uiSetupWizard")
        self.uiOpenApplianceAction = QtWidgets.QAction(MainWindow)
        self.uiOpenApplianceAction.setIcon(icon2)
        self.uiOpenApplianceAction.setObjectName("uiOpenApplianceAction")
        self.uiExportDebugInformationAction = QtWidgets.QAction(MainWindow)
        self.uiExportDebugInformationAction.setObjectName("uiExportDebugInformationAction")
        self.uiDoctorAction = QtWidgets.QAction(MainWindow)
        self.uiDoctorAction.setObjectName("uiDoctorAction")
        self.uiExportProjectAction = QtWidgets.QAction(MainWindow)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/icons/export_config.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiExportProjectAction.setIcon(icon29)
        self.uiExportProjectAction.setObjectName("uiExportProjectAction")
        self.uiImportProjectAction = QtWidgets.QAction(MainWindow)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/icons/import_config.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiImportProjectAction.setIcon(icon30)
        self.uiImportProjectAction.setObjectName("uiImportProjectAction")
        self.uiEditReadmeAction = QtWidgets.QAction(MainWindow)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/icons/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiEditReadmeAction.setIcon(icon31)
        self.uiEditReadmeAction.setObjectName("uiEditReadmeAction")
        self.uiAcademyAction = QtWidgets.QAction(MainWindow)
        self.uiAcademyAction.setObjectName("uiAcademyAction")
        self.uiDeleteProjectAction = QtWidgets.QAction(MainWindow)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/icons/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiDeleteProjectAction.setIcon(icon32)
        self.uiDeleteProjectAction.setObjectName("uiDeleteProjectAction")
        self.uiShowGridAction = QtWidgets.QAction(MainWindow)
        self.uiShowGridAction.setCheckable(True)
        self.uiShowGridAction.setObjectName("uiShowGridAction")
        self.uiEditProjectAction = QtWidgets.QAction(MainWindow)
        self.uiEditProjectAction.setIcon(icon31)
        self.uiEditProjectAction.setObjectName("uiEditProjectAction")
        self.uiWebInterfaceAction = QtWidgets.QAction(MainWindow)
        self.uiWebInterfaceAction.setObjectName("uiWebInterfaceAction")
        self.uiDrawLineAction = QtWidgets.QAction(MainWindow)
        self.uiDrawLineAction.setCheckable(True)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(":/icons/vertically.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiDrawLineAction.setIcon(icon33)
        self.uiDrawLineAction.setObjectName("uiDrawLineAction")
        self.uiEditMenu.addAction(self.uiSelectAllAction)
        self.uiEditMenu.addAction(self.uiSelectNoneAction)
        self.uiEditMenu.addSeparator()
        self.uiEditMenu.addAction(self.uiSnapshotAction)
        self.uiEditMenu.addAction(self.uiPreferencesAction)
        self.uiFileMenu.addAction(self.uiNewProjectAction)
        self.uiFileMenu.addAction(self.uiOpenProjectAction)
        self.uiFileMenu.addAction(self.uiSaveProjectAsAction)
        self.uiFileMenu.addAction(self.uiEditProjectAction)
        self.uiFileMenu.addAction(self.uiDeleteProjectAction)
        self.uiFileMenu.addSeparator()
        self.uiFileMenu.addAction(self.uiExportProjectAction)
        self.uiFileMenu.addAction(self.uiImportProjectAction)
        self.uiFileMenu.addSeparator()
        self.uiFileMenu.addAction(self.uiOpenApplianceAction)
        self.uiFileMenu.addSeparator()
        self.uiFileMenu.addAction(self.uiQuitAction)
        self.uiHelpMenu.addAction(self.uiOnlineHelpAction)
        self.uiHelpMenu.addAction(self.uiCheckForUpdateAction)
        self.uiHelpMenu.addAction(self.uiSetupWizard)
        self.uiHelpMenu.addAction(self.uiAcademyAction)
        self.uiHelpMenu.addAction(self.uiDoctorAction)
        self.uiHelpMenu.addAction(self.uiExportDebugInformationAction)
        self.uiHelpMenu.addAction(self.uiAboutQtAction)
        self.uiHelpMenu.addAction(self.uiAboutAction)
        self.uiViewMenu.addAction(self.uiActionFullscreen)
        self.uiViewMenu.addSeparator()
        self.uiViewMenu.addAction(self.uiZoomInAction)
        self.uiViewMenu.addAction(self.uiZoomOutAction)
        self.uiViewMenu.addAction(self.uiZoomResetAction)
        self.uiViewMenu.addAction(self.uiFitInViewAction)
        self.uiViewMenu.addSeparator()
        self.uiViewMenu.addAction(self.uiShowLayersAction)
        self.uiViewMenu.addAction(self.uiSnapToGridAction)
        self.uiViewMenu.addAction(self.uiShowGridAction)
        self.uiViewMenu.addAction(self.uiResetPortLabelsAction)
        self.uiViewMenu.addAction(self.uiShowPortNamesAction)
        self.uiViewMenu.addSeparator()
        self.uiViewMenu.addAction(self.uiDocksMenu.menuAction())
        self.uiControlMenu.addAction(self.uiStartAllAction)
        self.uiControlMenu.addAction(self.uiSuspendAllAction)
        self.uiControlMenu.addAction(self.uiStopAllAction)
        self.uiControlMenu.addAction(self.uiReloadAllAction)
        self.uiControlMenu.addAction(self.uiAuxConsoleAllAction)
        self.uiControlMenu.addAction(self.uiConsoleAllAction)
        self.uiAnnotateMenu.addAction(self.uiAddNoteAction)
        self.uiAnnotateMenu.addAction(self.uiInsertImageAction)
        self.uiAnnotateMenu.addAction(self.uiDrawRectangleAction)
        self.uiAnnotateMenu.addAction(self.uiDrawEllipseAction)
        self.uiAnnotateMenu.addAction(self.uiDrawLineAction)
        self.uiAnnotateMenu.addAction(self.uiEditReadmeAction)
        self.uiToolsMenu.addAction(self.uiScreenshotAction)
        self.uiToolsMenu.addAction(self.uiImportExportConfigsAction)
        self.uiToolsMenu.addAction(self.uiWebInterfaceAction)
        self.uiMenuBar.addAction(self.uiFileMenu.menuAction())
        self.uiMenuBar.addAction(self.uiEditMenu.menuAction())
        self.uiMenuBar.addAction(self.uiViewMenu.menuAction())
        self.uiMenuBar.addAction(self.uiControlMenu.menuAction())
        self.uiMenuBar.addAction(self.uiDeviceMenu.menuAction())
        self.uiMenuBar.addAction(self.uiAnnotateMenu.menuAction())
        self.uiMenuBar.addAction(self.uiToolsMenu.menuAction())
        self.uiMenuBar.addAction(self.uiHelpMenu.menuAction())
        self.uiGeneralToolBar.addAction(self.uiNewProjectAction)
        self.uiGeneralToolBar.addAction(self.uiOpenProjectAction)
        self.uiBrowsersToolBar.addAction(self.uiBrowseRoutersAction)
        self.uiBrowsersToolBar.addSeparator()
        self.uiBrowsersToolBar.addAction(self.uiBrowseSwitchesAction)
        self.uiBrowsersToolBar.addSeparator()
        self.uiBrowsersToolBar.addAction(self.uiBrowseEndDevicesAction)
        self.uiBrowsersToolBar.addSeparator()
        self.uiBrowsersToolBar.addAction(self.uiBrowseSecurityDevicesAction)
        self.uiBrowsersToolBar.addSeparator()
        self.uiBrowsersToolBar.addAction(self.uiBrowseAllDevicesAction)
        self.uiBrowsersToolBar.addSeparator()
        self.uiBrowsersToolBar.addAction(self.uiAddLinkAction)
        self.uiBrowsersToolBar.addSeparator()
        self.uiControlToolBar.addAction(self.uiSnapshotAction)
        self.uiControlToolBar.addAction(self.uiShowPortNamesAction)
        self.uiControlToolBar.addAction(self.uiConsoleAllAction)
        self.uiControlToolBar.addSeparator()
        self.uiControlToolBar.addAction(self.uiStartAllAction)
        self.uiControlToolBar.addAction(self.uiSuspendAllAction)
        self.uiControlToolBar.addAction(self.uiStopAllAction)
        self.uiControlToolBar.addAction(self.uiReloadAllAction)
        self.uiAnnotationToolBar.addAction(self.uiAddNoteAction)
        self.uiAnnotationToolBar.addAction(self.uiInsertImageAction)
        self.uiAnnotationToolBar.addAction(self.uiDrawRectangleAction)
        self.uiAnnotationToolBar.addAction(self.uiDrawEllipseAction)
        self.uiAnnotationToolBar.addAction(self.uiDrawLineAction)
        self.uiAnnotationToolBar.addAction(self.uiZoomInAction)
        self.uiAnnotationToolBar.addAction(self.uiZoomOutAction)
        self.uiAnnotationToolBar.addAction(self.uiScreenshotAction)

        self.retranslateUi(MainWindow)
        self.uiQuitAction.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.uiGraphicsView, self.uiNodesView)
        MainWindow.setTabOrder(self.uiNodesView, self.uiConsoleTextEdit)
        MainWindow.setTabOrder(self.uiConsoleTextEdit, self.uiTopologySummaryTreeWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.uiEditMenu.setTitle(_translate("MainWindow", "&Edit"))
        self.uiFileMenu.setTitle(_translate("MainWindow", "&File"))
        self.uiHelpMenu.setTitle(_translate("MainWindow", "&Help"))
        self.uiViewMenu.setTitle(_translate("MainWindow", "&View"))
        self.uiDocksMenu.setTitle(_translate("MainWindow", "Docks"))
        self.uiControlMenu.setTitle(_translate("MainWindow", "Control"))
        self.uiAnnotateMenu.setTitle(_translate("MainWindow", "Annotate"))
        self.uiDeviceMenu.setTitle(_translate("MainWindow", "Node"))
        self.uiToolsMenu.setTitle(_translate("MainWindow", "&Tools"))
        self.uiGeneralToolBar.setWindowTitle(_translate("MainWindow", "General"))
        self.uiNodesDockWidget.setWindowTitle(_translate("MainWindow", "All devices"))
        self.uiNodesFilterComboBox.setItemText(0, _translate("MainWindow", "Installed & Available appliances"))
        self.uiNodesFilterComboBox.setItemText(1, _translate("MainWindow", "Installed appliances"))
        self.uiNodesFilterComboBox.setItemText(2, _translate("MainWindow", "Available appliances"))
        self.uiNodesFilterComboBox.setItemText(3, _translate("MainWindow", "Custom appliances"))
        self.uiNodesFilterLineEdit.setPlaceholderText(_translate("MainWindow", "Filter"))
        self.uiNodesView.setToolTip(_translate("MainWindow", "Drag a node to the workspace (Press SHIFT while dragging to add multiple identical nodes)."))
        self.uiNodesView.headerItem().setText(0, _translate("MainWindow", "1"))
        self.uiNewAppliancePushButton.setText(_translate("MainWindow", "New appliance template"))
        self.uiBrowsersToolBar.setWindowTitle(_translate("MainWindow", "Devices"))
        self.uiControlToolBar.setWindowTitle(_translate("MainWindow", "Emulation"))
        self.uiConsoleDockWidget.setWindowTitle(_translate("MainWindow", "Console"))
        self.uiAnnotationToolBar.setWindowTitle(_translate("MainWindow", "Drawing"))
        self.uiTopologySummaryDockWidget.setWindowTitle(_translate("MainWindow", "Topology Summary"))
        self.uiTopologySummaryTreeWidget.headerItem().setText(0, _translate("MainWindow", "Node"))
        self.uiTopologySummaryTreeWidget.headerItem().setText(1, _translate("MainWindow", "Console"))
        self.uiComputeSummaryDockWidget.setWindowTitle(_translate("MainWindow", "Servers Summary"))
        self.uiAboutAction.setText(_translate("MainWindow", "&About"))
        self.uiAboutAction.setStatusTip(_translate("MainWindow", "About"))
        self.uiQuitAction.setText(_translate("MainWindow", "&Quit"))
        self.uiQuitAction.setStatusTip(_translate("MainWindow", "Quit"))
        self.uiQuitAction.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.uiOpenProjectAction.setText(_translate("MainWindow", "&Open project"))
        self.uiOpenProjectAction.setToolTip(_translate("MainWindow", "Open project"))
        self.uiOpenProjectAction.setStatusTip(_translate("MainWindow", "Open project"))
        self.uiOpenProjectAction.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.uiOnlineHelpAction.setText(_translate("MainWindow", "&Online help"))
        self.uiOnlineHelpAction.setToolTip(_translate("MainWindow", "Online help"))
        self.uiOnlineHelpAction.setStatusTip(_translate("MainWindow", "Online Help"))
        self.uiScreenshotAction.setText(_translate("MainWindow", "Take a screenshot"))
        self.uiScreenshotAction.setToolTip(_translate("MainWindow", "Take a screenshot"))
        self.uiScreenshotAction.setStatusTip(_translate("MainWindow", "Take a screenshot"))
        self.uiStartAllAction.setText(_translate("MainWindow", "Start/Resume all nodes"))
        self.uiStartAllAction.setToolTip(_translate("MainWindow", "Start/Resume all nodes"))
        self.uiStartAllAction.setStatusTip(_translate("MainWindow", "Start/Resume all devices"))
        self.uiStopAllAction.setText(_translate("MainWindow", "Stop all nodes"))
        self.uiStopAllAction.setToolTip(_translate("MainWindow", "Stop all nodes"))
        self.uiStopAllAction.setStatusTip(_translate("MainWindow", "Stop all devices"))
        self.uiConsoleAllAction.setText(_translate("MainWindow", "Console connect to all nodes"))
        self.uiConsoleAllAction.setToolTip(_translate("MainWindow", "Console connect to all nodes"))
        self.uiConsoleAllAction.setStatusTip(_translate("MainWindow", "Console to all devices"))
        self.uiAboutQtAction.setText(_translate("MainWindow", "About &Qt"))
        self.uiAboutQtAction.setStatusTip(_translate("MainWindow", "About Qt"))
        self.uiZoomInAction.setText(_translate("MainWindow", "Zoom in"))
        self.uiZoomInAction.setToolTip(_translate("MainWindow", "Zoom in"))
        self.uiZoomInAction.setStatusTip(_translate("MainWindow", "Zoom in"))
        self.uiZoomInAction.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.uiZoomOutAction.setText(_translate("MainWindow", "Zoom out"))
        self.uiZoomOutAction.setToolTip(_translate("MainWindow", "Zoom out"))
        self.uiZoomOutAction.setStatusTip(_translate("MainWindow", "Zoom out"))
        self.uiZoomOutAction.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.uiZoomResetAction.setText(_translate("MainWindow", "Zoom reset"))
        self.uiZoomResetAction.setStatusTip(_translate("MainWindow", "Zoom reset"))
        self.uiZoomResetAction.setShortcut(_translate("MainWindow", "Ctrl+0"))
        self.uiSelectAllAction.setText(_translate("MainWindow", "Select &all"))
        self.uiSelectAllAction.setStatusTip(_translate("MainWindow", "Select All"))
        self.uiSelectAllAction.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.uiSelectNoneAction.setText(_translate("MainWindow", "Select &none"))
        self.uiSelectNoneAction.setStatusTip(_translate("MainWindow", "Select None"))
        self.uiSelectNoneAction.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        self.uiPreferencesAction.setText(_translate("MainWindow", "&Preferences..."))
        self.uiPreferencesAction.setStatusTip(_translate("MainWindow", "Preferences"))
        self.uiPreferencesAction.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.uiSuspendAllAction.setText(_translate("MainWindow", "Suspend all nodes"))
        self.uiSuspendAllAction.setToolTip(_translate("MainWindow", "Suspend all nodes"))
        self.uiSuspendAllAction.setStatusTip(_translate("MainWindow", "Suspend all devices"))
        self.uiAddNoteAction.setText(_translate("MainWindow", "Add note"))
        self.uiAddNoteAction.setToolTip(_translate("MainWindow", "Add a note"))
        self.uiAddNoteAction.setStatusTip(_translate("MainWindow", "Add a note"))
        self.uiNewProjectAction.setText(_translate("MainWindow", "&New blank project"))
        self.uiNewProjectAction.setIconText(_translate("MainWindow", "New Project"))
        self.uiNewProjectAction.setToolTip(_translate("MainWindow", "New blank project"))
        self.uiNewProjectAction.setStatusTip(_translate("MainWindow", "New blank project"))
        self.uiNewProjectAction.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.uiImportExportConfigsAction.setText(_translate("MainWindow", "&Import/Export node configs"))
        self.uiImportExportConfigsAction.setToolTip(_translate("MainWindow", "Import/Export node configs"))
        self.uiImportExportConfigsAction.setStatusTip(_translate("MainWindow", "Import/Export device configs"))
        self.uiInsertImageAction.setText(_translate("MainWindow", "Insert picture"))
        self.uiInsertImageAction.setToolTip(_translate("MainWindow", "Insert a picture"))
        self.uiInsertImageAction.setStatusTip(_translate("MainWindow", "Insert a picture"))
        self.uiDrawRectangleAction.setText(_translate("MainWindow", "Draw rectangle"))
        self.uiDrawRectangleAction.setToolTip(_translate("MainWindow", "Draw a rectangle"))
        self.uiDrawRectangleAction.setStatusTip(_translate("MainWindow", "Draw a rectangle"))
        self.uiDrawEllipseAction.setText(_translate("MainWindow", "Draw ellipse"))
        self.uiDrawEllipseAction.setToolTip(_translate("MainWindow", "Draw an ellipse"))
        self.uiDrawEllipseAction.setStatusTip(_translate("MainWindow", "Draw an ellipse"))
        self.uiShowPortNamesAction.setText(_translate("MainWindow", "Show/Hide interface labels"))
        self.uiShowPortNamesAction.setToolTip(_translate("MainWindow", "Show/Hide interface labels"))
        self.uiShowPortNamesAction.setStatusTip(_translate("MainWindow", "Show/Hide interface labels"))
        self.uiSnapshotAction.setText(_translate("MainWindow", "Manage snapshots"))
        self.uiSnapshotAction.setToolTip(_translate("MainWindow", "Manage snapshots"))
        self.uiSnapshotAction.setStatusTip(_translate("MainWindow", "Manage snapshots"))
        self.uiShowLayersAction.setText(_translate("MainWindow", "Show layers"))
        self.uiShowLayersAction.setStatusTip(_translate("MainWindow", "Show layers"))
        self.uiSnapToGridAction.setText(_translate("MainWindow", "Snap to grid"))
        self.uiSnapToGridAction.setStatusTip(_translate("MainWindow", "Snap To Grid"))
        self.uiSaveProjectAsAction.setText(_translate("MainWindow", "&Save project as..."))
        self.uiSaveProjectAsAction.setToolTip(_translate("MainWindow", "Save project as..."))
        self.uiSaveProjectAsAction.setStatusTip(_translate("MainWindow", "Save project as..."))
        self.uiReloadAllAction.setText(_translate("MainWindow", "Reload all nodes"))
        self.uiReloadAllAction.setToolTip(_translate("MainWindow", "Reload all nodes"))
        self.uiReloadAllAction.setStatusTip(_translate("MainWindow", "Reload all devices"))
        self.uiAuxConsoleAllAction.setText(_translate("MainWindow", "Console connect via AUX to all nodes"))
        self.uiAuxConsoleAllAction.setToolTip(_translate("MainWindow", "Console connect via AUX to all nodes"))
        self.uiAuxConsoleAllAction.setStatusTip(_translate("MainWindow", "Console AUX to all devices"))
        self.uiResetPortLabelsAction.setText(_translate("MainWindow", "Reset interface labels"))
        self.uiResetPortLabelsAction.setToolTip(_translate("MainWindow", "Reset interface labels"))
        self.uiResetPortLabelsAction.setStatusTip(_translate("MainWindow", "Reset Interface Labels"))
        self.uiCheckForUpdateAction.setText(_translate("MainWindow", "Check for &Update"))
        self.uiCheckForUpdateAction.setStatusTip(_translate("MainWindow", "Check for Update"))
        self.uiBrowseRoutersAction.setText(_translate("MainWindow", "Browse Routers"))
        self.uiBrowseRoutersAction.setIconText(_translate("MainWindow", "Browse Routers"))
        self.uiBrowseRoutersAction.setToolTip(_translate("MainWindow", "Browse Routers"))
        self.uiBrowseRoutersAction.setStatusTip(_translate("MainWindow", "Browse Routers"))
        self.uiBrowseSwitchesAction.setText(_translate("MainWindow", "Browse Switches"))
        self.uiBrowseSwitchesAction.setIconText(_translate("MainWindow", "Browse Switches"))
        self.uiBrowseSwitchesAction.setToolTip(_translate("MainWindow", "Browse Switches"))
        self.uiBrowseSwitchesAction.setStatusTip(_translate("MainWindow", "Browse Switches"))
        self.uiBrowseEndDevicesAction.setText(_translate("MainWindow", "Browse End Devices"))
        self.uiBrowseEndDevicesAction.setIconText(_translate("MainWindow", "Browse End Devices"))
        self.uiBrowseEndDevicesAction.setToolTip(_translate("MainWindow", "Browse End Devices"))
        self.uiBrowseEndDevicesAction.setStatusTip(_translate("MainWindow", "Browse End Devices"))
        self.uiBrowseSecurityDevicesAction.setText(_translate("MainWindow", "Browse Security Devices"))
        self.uiBrowseSecurityDevicesAction.setIconText(_translate("MainWindow", "Browse Security Devices"))
        self.uiBrowseSecurityDevicesAction.setToolTip(_translate("MainWindow", "Browse Security Devices"))
        self.uiBrowseSecurityDevicesAction.setStatusTip(_translate("MainWindow", "Browse Security Devices"))
        self.uiBrowseAllDevicesAction.setText(_translate("MainWindow", "Browse all devices"))
        self.uiBrowseAllDevicesAction.setToolTip(_translate("MainWindow", "Browse all devices"))
        self.uiBrowseAllDevicesAction.setStatusTip(_translate("MainWindow", "Browse all devices"))
        self.uiAddLinkAction.setText(_translate("MainWindow", "Add a link"))
        self.uiAddLinkAction.setToolTip(_translate("MainWindow", "Add a link"))
        self.uiAddLinkAction.setStatusTip(_translate("MainWindow", "Add a link"))
        self.uiFitInViewAction.setText(_translate("MainWindow", "Fit in view"))
        self.uiActionFullscreen.setText(_translate("MainWindow", "Fullscreen"))
        self.uiActionFullscreen.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.uiSetupWizard.setText(_translate("MainWindow", "&Setup Wizard"))
        self.uiOpenApplianceAction.setText(_translate("MainWindow", "Import appliance"))
        self.uiExportDebugInformationAction.setText(_translate("MainWindow", "Export debug information"))
        self.uiExportDebugInformationAction.setToolTip(_translate("MainWindow", "&Export debug information"))
        self.uiDoctorAction.setText(_translate("MainWindow", "GNS3 &Doctor"))
        self.uiExportProjectAction.setText(_translate("MainWindow", "Export portable project"))
        self.uiImportProjectAction.setText(_translate("MainWindow", "Import portable project"))
        self.uiEditReadmeAction.setText(_translate("MainWindow", "Edit readme"))
        self.uiAcademyAction.setText(_translate("MainWindow", "GNS3 &Academy"))
        self.uiDeleteProjectAction.setText(_translate("MainWindow", "Delete project"))
        self.uiShowGridAction.setText(_translate("MainWindow", "Show the grid"))
        self.uiEditProjectAction.setText(_translate("MainWindow", "Edit project"))
        self.uiWebInterfaceAction.setText(_translate("MainWindow", "Web interface"))
        self.uiDrawLineAction.setText(_translate("MainWindow", "Drawn line"))

from ..compute_summary_view import ComputeSummaryView
from ..console_view import ConsoleView
from ..graphics_view import GraphicsView
from ..nodes_dock_widget import NodesDockWidget
from ..nodes_view import NodesView
from ..status_bar import StatusBar
from ..topology_summary_view import TopologySummaryView
from . import resources_rc
