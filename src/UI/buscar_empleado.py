# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1230, 600)
        MainWindow.setStyleSheet("/* Rectangle 11 */\n"
"\n"
"\n"
"position: absolute;\n"
"left: 0%;\n"
"right: 0%;\n"
"top: 0%;\n"
"bottom: 0%;\n"
"\n"
"background: rgba(221, 221, 219, 0.9);\n"
"border: 1px solid rgba(0, 0, 0, 0.5);\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), inset 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radi")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 0, 351, 41))
        self.label.setStyleSheet("/* Buscando Empleado */\n"
"\n"
"\n"
"width: 381px;\n"
"height: 44px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 36px;\n"
"line-height: 44px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #18191F;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 60, 682, 74))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_2.setStyleSheet("/* Cod. Empleado : */\n"
"\n"
"\n"
"width: 185px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #18191F;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(parent=self.horizontalLayoutWidget)
        self.textEdit.setStyleSheet("/* Input */\n"
"\n"
"\n"
"box-sizing: border-box;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 2px 4px 0px 10px;\n"
"\n"
"width: 237px;\n"
"height: 25px;\n"
"\n"
"background: rgba(44, 174, 208, 0.5);\n"
"border: 1px solid rgba(0, 0, 0, 0.5);\n"
"border-radius: 7px;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setStyleSheet("/* image 27 */\n"
"\n"
"\n"
"width: 23px;\n"
"height: 23px;\n"
"\n"
"background: url(image.png);\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 1;\n"
"flex-grow: 0;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 110, 151, 21))
        self.label_3.setStyleSheet("width: 153px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #18191F;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"\n"
"\n"
"/* Frame 44 */\n"
"\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #5EC3DD;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(130, 100, 821, 41))
        self.line.setStyleSheet("/* Frame 44 */\n"
"\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #5EC3DD;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 110, 91, 21))
        self.label_4.setStyleSheet("/* Frame 44 */\n"
"\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #5EC3DD;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"width: 153px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #18191F;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(540, 110, 111, 21))
        self.label_5.setStyleSheet("/* Frame 44 */\n"
"\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #5EC3DD;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"width: 153px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #18191F;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(710, 110, 121, 21))
        self.label_6.setStyleSheet("/* Frame 44 */\n"
"\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #5EC3DD;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"width: 153px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #18191F;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.label_6.setObjectName("label_6")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(130, 140, 821, 391))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 819, 389))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.line_2 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 821, 41))
        self.line_2.setStyleSheet("box-sizing: border-box;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #000000;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 2;\n"
"flex-grow: 0;")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_3.setGeometry(QtCore.QRect(0, 40, 821, 41))
        self.line_3.setStyleSheet("box-sizing: border-box;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #000000;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 2;\n"
"flex-grow: 0;")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_4.setGeometry(QtCore.QRect(0, 80, 821, 41))
        self.line_4.setStyleSheet("box-sizing: border-box;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #000000;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 2;\n"
"flex-grow: 0;")
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_5.setGeometry(QtCore.QRect(0, 120, 821, 41))
        self.line_5.setStyleSheet("box-sizing: border-box;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #000000;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 2;\n"
"flex-grow: 0;")
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_6.setGeometry(QtCore.QRect(0, 160, 821, 41))
        self.line_6.setStyleSheet("box-sizing: border-box;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #000000;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 2;\n"
"flex-grow: 0;")
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_7.setGeometry(QtCore.QRect(0, 200, 821, 41))
        self.line_7.setStyleSheet("box-sizing: border-box;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #000000;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 2;\n"
"flex-grow: 0;")
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_8.setGeometry(QtCore.QRect(0, 240, 821, 41))
        self.line_8.setStyleSheet("box-sizing: border-box;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #000000;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 2;\n"
"flex-grow: 0;")
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_9.setGeometry(QtCore.QRect(0, 280, 821, 41))
        self.line_9.setStyleSheet("box-sizing: border-box;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #000000;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 2;\n"
"flex-grow: 0;")
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_10.setGeometry(QtCore.QRect(0, 320, 821, 41))
        self.line_10.setStyleSheet("box-sizing: border-box;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #000000;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 2;\n"
"flex-grow: 0;")
        self.line_10.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_11.setGeometry(QtCore.QRect(0, 360, 821, 41))
        self.line_11.setStyleSheet("box-sizing: border-box;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 0px;\n"
"gap: 57px;\n"
"\n"
"width: 917px;\n"
"height: 40px;\n"
"\n"
"background: #FFFFFF;\n"
"border: 1px solid #000000;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 2;\n"
"flex-grow: 0;")
        self.line_11.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_11.setObjectName("line_11")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 191, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_2.setGeometry(QtCore.QRect(190, 0, 191, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_3.setGeometry(QtCore.QRect(380, 0, 191, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_4.setGeometry(QtCore.QRect(570, 0, 191, 41))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 0, 75, 41))
        self.pushButton_2.setStyleSheet("/* Ver */\n"
"\n"
"\n"
"width: 33px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 8px 10px;\n"
"gap: 10px;\n"
"\n"
"width: 53px;\n"
"height: 40px;\n"
"\n"
"background: #18191F;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 12px;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 4;\n"
"flex-grow: 0;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(760, 40, 75, 41))
        self.pushButton_3.setStyleSheet("/* Ver */\n"
"\n"
"\n"
"width: 33px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 8px 10px;\n"
"gap: 10px;\n"
"\n"
"width: 53px;\n"
"height: 40px;\n"
"\n"
"background: #18191F;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 12px;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 4;\n"
"flex-grow: 0;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_5 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_5.setGeometry(QtCore.QRect(0, 40, 191, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_6.setGeometry(QtCore.QRect(190, 40, 191, 41))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_7.setGeometry(QtCore.QRect(570, 40, 191, 41))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_8.setGeometry(QtCore.QRect(380, 40, 191, 41))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(760, 80, 75, 41))
        self.pushButton_4.setStyleSheet("/* Ver */\n"
"\n"
"\n"
"width: 33px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 8px 10px;\n"
"gap: 10px;\n"
"\n"
"width: 53px;\n"
"height: 40px;\n"
"\n"
"background: #18191F;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 12px;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 4;\n"
"flex-grow: 0;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser_9 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_9.setGeometry(QtCore.QRect(0, 80, 191, 41))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_10.setGeometry(QtCore.QRect(190, 80, 191, 41))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_11.setGeometry(QtCore.QRect(570, 80, 191, 41))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_12.setGeometry(QtCore.QRect(380, 80, 191, 41))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(760, 120, 75, 41))
        self.pushButton_5.setStyleSheet("/* Ver */\n"
"\n"
"\n"
"width: 33px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 8px 10px;\n"
"gap: 10px;\n"
"\n"
"width: 53px;\n"
"height: 40px;\n"
"\n"
"background: #18191F;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 12px;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 4;\n"
"flex-grow: 0;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser_13 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_13.setGeometry(QtCore.QRect(0, 120, 191, 41))
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.textBrowser_14 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_14.setGeometry(QtCore.QRect(190, 120, 191, 41))
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.textBrowser_15 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_15.setGeometry(QtCore.QRect(570, 120, 191, 41))
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.textBrowser_16 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_16.setGeometry(QtCore.QRect(380, 120, 191, 41))
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_6.setGeometry(QtCore.QRect(760, 160, 75, 41))
        self.pushButton_6.setStyleSheet("/* Ver */\n"
"\n"
"\n"
"width: 33px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 8px 10px;\n"
"gap: 10px;\n"
"\n"
"width: 53px;\n"
"height: 40px;\n"
"\n"
"background: #18191F;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 12px;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 4;\n"
"flex-grow: 0;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.textBrowser_17 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_17.setGeometry(QtCore.QRect(0, 160, 191, 41))
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.textBrowser_18 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_18.setGeometry(QtCore.QRect(190, 160, 191, 41))
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.textBrowser_19 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_19.setGeometry(QtCore.QRect(570, 160, 191, 41))
        self.textBrowser_19.setObjectName("textBrowser_19")
        self.textBrowser_20 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_20.setGeometry(QtCore.QRect(380, 160, 191, 41))
        self.textBrowser_20.setObjectName("textBrowser_20")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_7.setGeometry(QtCore.QRect(760, 200, 75, 41))
        self.pushButton_7.setStyleSheet("/* Ver */\n"
"\n"
"\n"
"width: 33px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 8px 10px;\n"
"gap: 10px;\n"
"\n"
"width: 53px;\n"
"height: 40px;\n"
"\n"
"background: #18191F;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 12px;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 4;\n"
"flex-grow: 0;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.textBrowser_21 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_21.setGeometry(QtCore.QRect(0, 200, 191, 41))
        self.textBrowser_21.setObjectName("textBrowser_21")
        self.textBrowser_22 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_22.setGeometry(QtCore.QRect(190, 200, 191, 41))
        self.textBrowser_22.setObjectName("textBrowser_22")
        self.textBrowser_23 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_23.setGeometry(QtCore.QRect(570, 200, 191, 41))
        self.textBrowser_23.setObjectName("textBrowser_23")
        self.textBrowser_24 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_24.setGeometry(QtCore.QRect(380, 200, 191, 41))
        self.textBrowser_24.setObjectName("textBrowser_24")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_8.setGeometry(QtCore.QRect(760, 240, 75, 41))
        self.pushButton_8.setStyleSheet("/* Ver */\n"
"\n"
"\n"
"width: 33px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 8px 10px;\n"
"gap: 10px;\n"
"\n"
"width: 53px;\n"
"height: 40px;\n"
"\n"
"background: #18191F;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 12px;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 4;\n"
"flex-grow: 0;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.textBrowser_25 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_25.setGeometry(QtCore.QRect(0, 240, 191, 41))
        self.textBrowser_25.setObjectName("textBrowser_25")
        self.textBrowser_26 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_26.setGeometry(QtCore.QRect(190, 240, 191, 41))
        self.textBrowser_26.setObjectName("textBrowser_26")
        self.textBrowser_27 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_27.setGeometry(QtCore.QRect(570, 240, 191, 41))
        self.textBrowser_27.setObjectName("textBrowser_27")
        self.textBrowser_28 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_28.setGeometry(QtCore.QRect(380, 240, 191, 41))
        self.textBrowser_28.setObjectName("textBrowser_28")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_9.setGeometry(QtCore.QRect(760, 280, 75, 41))
        self.pushButton_9.setStyleSheet("/* Ver */\n"
"\n"
"\n"
"width: 33px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 8px 10px;\n"
"gap: 10px;\n"
"\n"
"width: 53px;\n"
"height: 40px;\n"
"\n"
"background: #18191F;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 12px;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 4;\n"
"flex-grow: 0;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.textBrowser_29 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_29.setGeometry(QtCore.QRect(0, 280, 191, 41))
        self.textBrowser_29.setObjectName("textBrowser_29")
        self.textBrowser_30 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_30.setGeometry(QtCore.QRect(190, 280, 191, 41))
        self.textBrowser_30.setObjectName("textBrowser_30")
        self.textBrowser_31 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_31.setGeometry(QtCore.QRect(570, 280, 191, 41))
        self.textBrowser_31.setObjectName("textBrowser_31")
        self.textBrowser_32 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_32.setGeometry(QtCore.QRect(380, 280, 191, 41))
        self.textBrowser_32.setObjectName("textBrowser_32")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_10.setGeometry(QtCore.QRect(760, 320, 75, 41))
        self.pushButton_10.setStyleSheet("/* Ver */\n"
"\n"
"\n"
"width: 33px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 8px 10px;\n"
"gap: 10px;\n"
"\n"
"width: 53px;\n"
"height: 40px;\n"
"\n"
"background: #18191F;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 12px;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 4;\n"
"flex-grow: 0;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.textBrowser_33 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_33.setGeometry(QtCore.QRect(0, 320, 191, 41))
        self.textBrowser_33.setObjectName("textBrowser_33")
        self.textBrowser_34 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_34.setGeometry(QtCore.QRect(190, 320, 191, 41))
        self.textBrowser_34.setObjectName("textBrowser_34")
        self.textBrowser_35 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_35.setGeometry(QtCore.QRect(570, 320, 191, 41))
        self.textBrowser_35.setObjectName("textBrowser_35")
        self.textBrowser_36 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_36.setGeometry(QtCore.QRect(380, 320, 191, 41))
        self.textBrowser_36.setObjectName("textBrowser_36")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_11.setGeometry(QtCore.QRect(760, 360, 75, 41))
        self.pushButton_11.setStyleSheet("/* Ver */\n"
"\n"
"\n"
"width: 33px;\n"
"height: 24px;\n"
"\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"\n"
"/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"align-items: flex-start;\n"
"padding: 8px 10px;\n"
"gap: 10px;\n"
"\n"
"width: 53px;\n"
"height: 40px;\n"
"\n"
"background: #18191F;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 12px;\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 4;\n"
"flex-grow: 0;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.textBrowser_37 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_37.setGeometry(QtCore.QRect(0, 360, 191, 41))
        self.textBrowser_37.setObjectName("textBrowser_37")
        self.textBrowser_38 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_38.setGeometry(QtCore.QRect(190, 360, 191, 41))
        self.textBrowser_38.setObjectName("textBrowser_38")
        self.textBrowser_39 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_39.setGeometry(QtCore.QRect(570, 360, 191, 41))
        self.textBrowser_39.setObjectName("textBrowser_39")
        self.textBrowser_40 = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser_40.setGeometry(QtCore.QRect(380, 360, 191, 41))
        self.textBrowser_40.setObjectName("textBrowser_40")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalScrollBar = QtWidgets.QScrollBar(parent=self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(950, 140, 16, 391))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(990, 10, 111, 171))
        self.frame.setStyleSheet("image: url(:/image/39c7b1265f1bc1803becb29fdc5c034b.jpg);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.line.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.scrollArea.raise_()
        self.verticalScrollBar.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1230, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Buscando Empleado"))
        self.label_2.setText(_translate("MainWindow", "Cod Empleado:"))
        self.pushButton.setText(_translate("MainWindow", "🔎"))
        self.label_3.setText(_translate("MainWindow", "Cod Empleado"))
        self.label_4.setText(_translate("MainWindow", "Nombres"))
        self.label_5.setText(_translate("MainWindow", "Apellido Pat"))
        self.label_6.setText(_translate("MainWindow", "Apellido Mat"))
        self.pushButton_2.setText(_translate("MainWindow", "Ver"))
        self.pushButton_3.setText(_translate("MainWindow", "Ver"))
        self.pushButton_4.setText(_translate("MainWindow", "Ver"))
        self.pushButton_5.setText(_translate("MainWindow", "Ver"))
        self.pushButton_6.setText(_translate("MainWindow", "Ver"))
        self.pushButton_7.setText(_translate("MainWindow", "Ver"))
        self.pushButton_8.setText(_translate("MainWindow", "Ver"))
        self.pushButton_9.setText(_translate("MainWindow", "Ver"))
        self.pushButton_10.setText(_translate("MainWindow", "Ver"))
        self.pushButton_11.setText(_translate("MainWindow", "Ver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())