import sys, os, shutil
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.extensions = [".py", ".ipynb", ".pdf", 'zip', 'dat', 'csv']
        self.year = ["2018", "2019", "2020"]
        self.years = ["2018년", "2019년", "2020년"]
        self.month = ["{0:02}".format(x + 1) for x in range(0, 12)]
        self.months = ["{0:02}월".format(x + 1) for x in range(0, 12)]
        self.model = QStandardItemModel(16, 3)


    def setUi(self, File):
        File.setObjectName("File")
        File.resize(990, 690)
        File.setMinimumSize(QtCore.QSize(1040, 680))
        self.BigWidget = QtWidgets.QWidget(File)                # 왼쪽 위젯
        self.BigWidget.setGeometry(QtCore.QRect(11, 11, 550, 660))
        self.BigWidget.setMinimumSize(QtCore.QSize(550, 660))

        self.widget = QtWidgets.QWidget(self.BigWidget)         
        self.widget.setGeometry(QtCore.QRect(0, 0, 550, 660))

        self.vbox = QtWidgets.QVBoxLayout(self.widget)
        self.vbox.setContentsMargins(0, 0, 0, 0)

        self.Widget = QtWidgets.QWidget(self.widget)
        self.Widget.setMinimumSize(QtCore.QSize(550, 260))
        self.Widget.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.lineEdit1 = QtWidgets.QLineEdit(self.Widget)           # 정리할 폴더 지정 쓰기
        self.lineEdit1.setGeometry(QtCore.QRect(210, 20, 330, 40))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit1.setStyleSheet("font: 63 14pt \"Bookman Old Style\";\n")
        self.lineEdit1.setFrame(True)
        self.lineEdit1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        self.lineEdit2 = QtWidgets.QLineEdit(self.Widget)           # 정리된 분류 폴더 생성 쓰기
        self.lineEdit2.setGeometry(QtCore.QRect(210, 70, 330, 40))
        self.lineEdit2.setFont(font)
        self.lineEdit2.setStyleSheet("font: 63 14pt \"Bookman Old Style\";\n")

        self.label1 = QtWidgets.QLabel(self.Widget)             # 정리할 폴더 생성
        self.label1.setGeometry(QtCore.QRect(10, 20, 200, 40))
        self.label2 = QtWidgets.QLabel(self.Widget)             # 분류 폴더 생성
        self.label2.setGeometry(QtCore.QRect(10, 70, 200, 40))

        self.pushButton = QtWidgets.QPushButton(self.Widget)        # OK 버튼
        self.pushButton.setGeometry(QtCore.QRect(440, 180, 100, 70))
        # self.pushButton.clicked.connect(self.pathClicked())

        self.sWidget = QtWidgets.QWidget(self.Widget)
        self.sWidget.setGeometry(QtCore.QRect(200, 120, 350, 50))

        self.ComBoxWidget = QtWidgets.QLabel(self.sWidget)              # 분류 종류
        self.ComBoxWidget.setGeometry(QtCore.QRect(10, 10, 110, 30))

        self.ComBox = QtWidgets.QComboBox(self.sWidget)             # 분류 종류 박스
        self.ComBox.setGeometry(QtCore.QRect(130, 10, 210, 30))
        self.ComBox.addItem("이름 분류")
        self.ComBox.addItem("확장자 분류")
        self.ComBox.addItem("날짜 분류")

        self.vbox.addWidget(self.Widget)

        self.TextEdit = QtWidgets.QTextEdit(self.widget)            # 왼쪽 아래 위젯
        self.TextEdit.setMinimumSize(QtCore.QSize(550, 380))
        self.TextEdit.setAcceptRichText(True)

        self.vbox.addWidget(self.TextEdit)

        self.TabView = QtWidgets.QTableView(File)               # 오른쪽 테이블 위젯
        self.TabView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(self.years)
        self.model.setVerticalHeaderLabels(self.months)
        self.TabView.setGeometry(QtCore.QRect(570, 10, 450, 660))
        self.TabView.setMinimumSize(QtCore.QSize(450, 660))
        self.TabView.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.TabView.horizontalHeader().setCascadingSectionResizes(False)

        self.widget1 = QtWidgets.QWidget(File)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 2, 2))

        self.hbox = QtWidgets.QHBoxLayout(self.widget1)
        self.hbox.setContentsMargins(0, 0, 0, 0)

        self.label1.setStyleSheet("font: 12pt \"서울남산체 B\";\n"
                                  "background-color: rgb(226, 255, 208);")
        self.label2.setStyleSheet("background-color: rgb(226, 255, 208);\n"
                                  "font: 12pt \"서울남산체 B\";")
        self.pushButton.setStyleSheet("font: 75 20pt \"Berlin Sans FB Demi\";\n"
                                      "background-color: rgb(250, 250, 250);")
        self.sWidget.setStyleSheet("background-color: rgb(220, 255, 183);")
        self.ComBoxWidget.setStyleSheet("background-color: rgb(220, 255, 183);")
        self.ComBox.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.TextEdit.setStyleSheet("gridline-color: rgb(255, 255, 255);")

        self.transUi(File)
        QtCore.QMetaObject.connectSlotsByName(File)

    def transUi(self, File):
        _translate = QtCore.QCoreApplication.translate
        File.setWindowTitle(_translate("File", "Form"))
        self.lineEdit2.setText(_translate("File", "C:\\users"))
        self.label1.setText(_translate("File", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">분류할 폴더 지정 =&gt;</span></p></body></html>"))
        self.lineEdit1.setText(_translate("File", "C:\\\\users\\dd"))
        self.label2.setText(_translate("File", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">정리될 폴더 지정 =&gt;</span></p></body></html>"))
        self.pushButton.setText(_translate("File", "OK"))
        self.ComBoxWidget.setText(_translate("File", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">분류 방법 :</span></p></body></html>"))

        # 여기서부턴 일단 보류 (붙여넣기만 하고 아직 건들지 못함)ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        
    def pathClicked(self):
        self.file_path = self.pathedit.text()
        self.pathedit.clear()
        self.file_list = os.listdir(self.file_path)
        self.pathlbl.setText(f"[{self.file_path}] 폴더 파일을 분류하겠습니다.")
        return

    def setSlot(self):
        keyname = str(self.ComBox.currentText())
        if keyname == "이름 분류":
            pass
        elif keyname == "확장자 분류":
            pass
        elif keyname == "날짜 분류":
            pass
        # self.searchbutton.clicked.connect
        # self.btnClss.clicked.connect(self.classify)
        # self.btnClss2.clicked.connect(self.check_publishtime)
        # self.btnmove.clicked.connect(self.folder_move)
        return

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    File = QtWidgets.QWidget()
    ui = main()
    ui.setUi(File)
    File.show()
    sys.exit(app.exec_())

